# 💬 AI Customer Support Chatbot with Memory

An AI-powered customer support chatbot that answers customer questions based on a business's FAQ knowledge base, while maintaining conversation context across multiple turns.

## Features
- **Contextual Memory**: Remembers earlier parts of the conversation to answer follow-up questions accurately (e.g., understands "how long does *that* take?" refers to a topic mentioned earlier).
- **FAQ-Grounded Responses**: Answers are based strictly on the provided business knowledge base, reducing hallucination.
- **Graceful Fallback**: When a question falls outside the knowledge base, the bot politely redirects the customer to human support instead of guessing.
- **Clean Chat UI**: Built with Streamlit for a simple, responsive chat interface.

## Tech Stack
- Python
- Google Gemini API (`google-generativeai`)
- Streamlit (UI)
- python-dotenv (environment variable management)

## How It Works
1. User sends a message through the chat interface.
2. The message, along with the full conversation history, is sent to the Gemini model.
3. The model responds using the business FAQ context provided as a system instruction.
4. The response is stored in session memory, allowing the bot to reference it in future turns.

## Setup & Run Locally
\`\`\`bash
git clone https://github.com/maruf-agent-dev-1/customer-support-chatbot.git
cd customer-support-chatbot
pip install -r requirements.txt
echo "GOOGLE_API_KEY=your_api_key_here" > .env
streamlit run app.py
\`\`\`

## Demo
<img width="1366" height="768" alt="Screenshot 2026-08-17 020256" src="https://github.com/user-attachments/assets/f8d87fa6-12e1-461f-af98-7f3259b28abb" />
<img width="1366" height="768" alt="Screenshot 2026-08-17 020355" src="https://github.com/user-attachments/assets/a9b3c16e-701a-42e3-bef8-e3814981ae22" />



## Use Case
This project demonstrates how businesses can automate first-line customer support — reducing response time for common questions like shipping, returns, and payment policies — while maintaining natural, context-aware conversations.

