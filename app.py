from flask import Flask
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader
import json
import os

load_dotenv()

YOUR_API_KEY = os.getenv("PERPLEXITYKEY")



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

    client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.perplexity.ai")

    # chat completion without streaming
    response = client.chat.completions.create(
        model="sonar",
        messages=messages,
    )

    
    return [choice.message.content for choice in response.choices]

thing = generateResumeJson(r"C:\Users\cammc\Downloads\Copy of Technical Resume Template.pdf")

formatted_thing = "<br>".join(thing)

formatted_thing = formatted_thing.strip("`")

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>%s</p>" % formatted_thing