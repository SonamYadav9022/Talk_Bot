import google.generativeai as genai

# Paste your Google API key here
GOOGLE_API_KEY = "AIzaSyDk8bdqB4J0jU7TZmeQx7Oj8qd2L77ALNI"

# Configure the API
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the model (Gemini)
model = genai.GenerativeModel("gemini-1.5-flash")

# Send a message to the bot brain
response = model.generate_content("Hello, how are you?")

# Print bot response
print(response.text)