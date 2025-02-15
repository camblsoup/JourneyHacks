from flask import Flask, render_template, request
from functions import *


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


app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/action1', methods=['POST'])
def action1():
    formatted_response = "<br>".join(response)  # Adds line breaks between responses
    return f"<p>{formatted_response}</p>"

@app.route('/action2', methods=['POST'])
def action2():
    return "<h2>Action 2 executed!</h2><p>Running Python Code 2...</p>"

@app.route('/action3', methods=['POST'])
def action3():
    return "<h2>Action 3 executed!</h2><p>Running Python Code 3...</p>"

if __name__ == '__main__':
    app.run(debug=True)
