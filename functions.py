import json
from PyPDF2 import PdfReader
import openai
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Set up OpenAI API key
PERPLEX_API_KEY = os.getenv("PERPLEX_API_KEY")

client = OpenAI(api_key=PERPLEX_API_KEY, base_url="https://api.perplexity.ai")




def send_json_to_perplexity(json_string, job_info, model="sonar", system_prompt="You are a helpful assistant. Can you write me a cover letter from this JSON data?"):
    try:
        # Parse JSON from the string
        json_data = json.loads(json_string)

        # Convert JSON data to string format with indentation
        json_text = json.dumps(json_data, indent=2)


        # Send the JSON data and job info to Perplexity
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": (
                        f"Here is my JSON data:\n{json_text}\n\n"
                        f"Here is the job information:\n{job_info}\n\n"
                        "Can you analyze it and help me write a cover letter?"
                    ),
                },
            ],
        )

        # Collect all messages from the response
        messages = [choice.message.content for choice in response.choices]

        # Return all messages
        return messages

    except Exception as e:
        return f"Error: {e}"
    

sample_json = """

        {
    "name": "John Doe",
    "contact": {
        "email": "john.doe@example.com",
        "phone": "+1234567890",
        "address": "123 Main St, Anytown, USA"
    },
    "summary": "Experienced software developer with a strong background in developing scalable web applications and working with cross-functional teams.",
    "experience": [
        {
            "job_title": "Senior Software Developer",
            "company": "Tech Solutions Inc.",
            "location": "San Francisco, CA",
            "start_date": "January 2020",
            "end_date": "Present",
            "responsibilities": [
                "Lead a team of developers to build and maintain web applications.",
                "Collaborate with product managers to define project requirements and timelines.",
                "Implement best practices for code quality and performance optimization."
            ]
        },
        {
            "job_title": "Software Developer",
            "company": "Web Innovations LLC",
            "location": "New York, NY",
            "start_date": "June 2016",
            "end_date": "December 2019",
            "responsibilities": [
                "Developed and maintained web applications using JavaScript, HTML, and CSS.",
                "Worked closely with designers to create user-friendly interfaces.",
                "Participated in code reviews and contributed to team knowledge sharing."
            ]
        }
    ],
    "education": [
        {
            "degree": "Bachelor of Science in Computer Science",
            "institution": "State University",
            "location": "Anytown, USA",
            "graduation_year": 2016
        }
    ],
    "skills": [
        "JavaScript",
        "React",
        "Node.js",
        "HTML",
        "CSS",
        "Git",
        "Agile methodologies"
    ],
    "certifications": [
        {
            "name": "Certified JavaScript Developer",
            "issuing_organization": "Tech Certification Board",
            "issue_date": "March 2018"
        }
    ]
}
    
"""

job_info = "This is a job at a tech company looking for a software engineer with experience in Python and machine learning."
job_info_two = "We are looking for a dedicated individual to join our team as a General Laborer. Responsibilities include manual labor tasks such as lifting, carrying, and moving materials, cleaning and maintaining work areas, and assisting with various tasks as needed. No prior experience is required, but a strong work ethic and the ability to follow instructions are essential. This is a physically demanding job that requires stamina and the ability to work in various weather conditions."

response = send_json_to_perplexity(sample_json, job_info_two)

# Print the response messages
for message in response:
    print(message)
