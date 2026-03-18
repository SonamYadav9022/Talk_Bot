import pyautogui
import time
import pyperclip
import google.generativeai as genai

# Configure Google Gemini API
GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")


# Function to check if last message is from specific sender
def is_last_message_from_sender(chat_log, sender_name="Rohan Das"):
    lines = chat_log.strip().split("\n")
    if not lines:
        return False
    
    last_message = lines[-1]
    return sender_name in last_message


# Function to get reply from Gemini
def ask_gemini(chat_log):
    prompt = f"""
You are a person named Naruto who speaks Hindi and English.
You are from India and you are a coder.
You analyze chat history and roast people in a funny way.

Chat history:
{chat_log}

Reply with ONLY the next message. Do not include timestamp or name.
"""

    response = model.generate_content(prompt)
    return response.text.strip()


# Main loop
while True:
    time.sleep(5)

    # Select chat area
    pyautogui.moveTo(972, 202)
    pyautogui.dragTo(2213, 1278, duration=1.5, button='left')

    # Copy selected text
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)

    # Click somewhere safe to remove selection
    pyautogui.click(1994, 281)

    # Get chat history from clipboard
    chat_history = pyperclip.paste()

    print("\nChat History:\n", chat_history)

    # Check sender
    if is_last_message_from_sender(chat_history, "Rohan Das"):

        print("Last message from Rohan Das. Generating reply...")

        reply = ask_gemini(chat_history)

        print("Reply:", reply)

        # Copy reply to clipboard
        pyperclip.copy(reply)

        # Click message input box
        pyautogui.click(1808, 1328)
        time.sleep(1)

        # Paste reply
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        # Press Enter
        pyautogui.press('enter')

        print("Reply sent.")

    else:
        print("Last message not from Rohan Das.")
