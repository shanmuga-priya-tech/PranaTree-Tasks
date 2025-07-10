import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Create model and chat session
model = genai.GenerativeModel("models/gemini-1.5-flash")
chat = model.start_chat()

# DSA topic menu
topics = {
    "1": "Arrays",
    "2": "Strings",
    "3": "Linked Lists",
    "4": "Stacks and Queues",
    "5": "Trees",
    "6": "Graphs",
    "7": "Recursion",
    "8": "Dynamic Programming",
    "9": "Searching & Sorting",
    "10": "Hashing"
}

# Display menu
print("📚 Choose a DSA Topic to Learn:")
for number, topic in topics.items():
    print(f"{number}. {topic}")

choice = input("Enter your choice (1-10): ")

# Validate choice
if choice not in topics:
    print("\n ❌ Invalid choice. Exiting.")
    exit()

selected_topic = topics[choice]
print(f"\n ✅ You selected: {selected_topic}")

# Prompt Gemini
prompt = f"""
You are my DSA tutor. Teach me the topic: {selected_topic}
- Explain it clearly for a beginner.
- Exaplain one python problem with line-by-line explanation and different approach to solve it.
- Give 2 related LeetCode problems with links.
- Suggest 2 study material like (blogs, videos, docs).
- make it concise to only 10 lines as bullet points except the code block.
"""

response = chat.send_message(prompt)
print("\n" + response.text)

# Optional: Follow-up loop
while True:
    follow_up = input("💬 Ask a follow-up question (or type 'exit' to quit): ")
    if follow_up.lower() == 'exit':
        print("👋 Goodbye! Happy learning!")
        break
    reply = chat.send_message(follow_up)
    print("\n" + reply.text)
