# Step 1: Create a Virtual Environment
py -3 -m venv .venv

# Step 2: Activate the Virtual Environment
# For Windows PowerShell
.\.venv\Scripts\Activate

# Step 3: Install Dependencies
# Install the required dependencies from a requirements file (you can create this file from the code's dependencies or install manually)
# Example: You may want to add the following to a `requirements.txt` file:
# Flask==2.0.1
# openai==0.11.0
# python-dotenv==0.19.2
# pypdf==3.0.0

# You can create requirements.txt manually or install the packages directly:
pip install flask openai python-dotenv pypdf

# Step 4: Run the Flask Application
flask --app app run  # This assumes your file is named app.py and contains your Flask app