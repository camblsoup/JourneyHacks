import json
from openai import OpenAI

PERPLEX_API_KEY = "INSERTKEYHERE"

# Initialize the Perplexity API client
client = OpenAI(api_key=PERPLEX_API_KEY, base_url="https://api.perplexity.ai")

def send_json_to_perplexity(file_path, job_info, model="sonar-pro", system_prompt="You are a helpful assistant. Can you write me a cover letter from this JSON data?"):
    try:
        # Read JSON file
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)

        # Convert JSON data to string format
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

# Example usage
file_path = "data.json"  # Replace with your actual JSON file path
job_info = "This is a job at a tech company looking for a software engineer with experience in Python and machine learning."
job_info_two = "We are looking for a dedicated individual to join our team as a General Laborer. Responsibilities include manual labor tasks such as lifting, carrying, and moving materials, cleaning and maintaining work areas, and assisting with various tasks as needed. No prior experience is required, but a strong work ethic and the ability to follow instructions are essential. This is a physically demanding job that requires stamina and the ability to work in various weather conditions."

response = send_json_to_perplexity(file_path, job_info_two)

# Print the response messages
for message in response:
    print(message)
