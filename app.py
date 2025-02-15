from flask import Flask
from flask import send_file
from flask import request
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader
import json
import os

load_dotenv()

YOUR_API_KEY = os.getenv("PERPLEXITYKEY")

client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.perplexity.ai")

def generateResumeJson(resume):
    reader = PdfReader(r"C:\Users\cammc\Downloads\Copy of Technical Resume Template.pdf")

    resume = ""

    for page in reader.pages:
        resume += page.extract_text()
        
    messages = [
        {
            "role": "system",
            "content": (
                '{"name" : "data here","email": "data here","mobile_number" : "data here","skills" : ["data here"],"education" : [{"name" : "data here","degree" : "data here","designation" : "data here","year" : "data here"}],"experience" : [{"name" :"data here","skills_used" : "data here","date" : "data here","description" : "data here"}],"references" : [{"name" :"data here","contact_info" : "data here","comment" : "data here"}]}'
            ),
        },
        {   
            "role": "user",
            "content": (
                '{"name" : "data here","email": "data here","mobile_number" : "data here","skills" : ["data here"],"education" : [{"name" : "data here","degree" : "data here","designation" : "data here","year" : "data here"}],"experience" : [{"name" :"data here","skills_used" : "data here","date" : "data here","description" : "data here"}],"references" : [{"name" :"data here","contact_info" : "data here","comment" : "data here"}]}'
                "Again ensure that there is NO OTHER TEXT other than the json file"
                "Here is my resume:"
                "%s" % resume
            ),
        },
    ]


    # chat completion without streaming
    response = client.chat.completions.create(
        model="sonar",
        messages=messages,
    )
    
    thing = [choice.message.content for choice in response.choices]

    formatted_thing = "<br>".join(thing)

    formatted_thing = formatted_thing.strip("`")
    
    return formatted_thing

app = Flask(__name__)

infoforjob = job_info = "This is a job at a tech company looking for a software engineer with experience in Python and machine learning."

def send_json_to_perplexity(json_data, job_info, model="sonar", system_prompt="You are a helpful assistant. Can you write me a cover letter from this JSON data?"):
    try:
    
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
                        "Please do not show your analysis and JUST write the cover letter"
                        "AGAIN NOTHING BUT THE COVER LETTER"
                        "NO \"HERE'S YOU'RE COVER LETTER:\""
                        "NO \"SURE THING\""
                        "JUST THE COVER LETTER"
                    ),
                },
            ],
        )

        # Collect all messages from the response
        messages = [choice.message.content for choice in response.choices]
        
        messages = "<br>".join(messages)

        messages = messages.replace("\n", "<br>")

        # Return all messages
        return messages

    except Exception as e:
        return f"Error: {e}"


@app.route("/")
def hello_world():
    return send_file("homepage.html")

@app.route("/generatecoverletter", methods=["post"])
def resumePage():
    resumePath = request.form['resume']
    jobDescription = request.form['job-description']
    return "<p>%s</p" % send_json_to_perplexity(generateResumeJson(resumePath), jobDescription)