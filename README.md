# Book Search Agent

An AI-powered Book Search Agent built with **Python**, **Streamlit**, **OpenRouter Function Calling**, and the **Google Books/Open Library API**.

The agent uses an LLM with tool calling to search for books, retrieve book information from an external API, and provide conversational responses.

---

## Features

- Search books by title, author, or subject
- AI-powered responses using OpenRouter
- Function Calling (Tool Calling)
- Conversation memory
- External Book API integration
- Streamlit web interface
- Beginner-friendly project structure

---

## Project Structure

```
book-search-agent/
│
├── app.py              # Streamlit UI
├── main.py             # AI Agent
├── tools.py            # Book Search Tool
├── memory.py           # Conversation Memory
├── prompts.py          # System Prompt
├── memory.json         # Stores conversation history
├── requirements.txt
├── README.md
└── .env
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/book-search-agent.git

cd book-search-agent
```

### Create a virtual environment (Optional)

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project directory.

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

Get your API key from:

https://openrouter.ai/

---

## Run the Streamlit App

```bash
streamlit run app.py
```

The application will open in your browser.

---
## Output

<img width="824" height="416" alt="image" src="https://github.com/user-attachments/assets/7825b715-1fd6-4bf2-bf93-d3ce327b8626" />

## Example

```
You:
Tell me about Atomic Habits

Agent:

Title: Atomic Habits
Author: James Clear
Published: 2018

Description:
Atomic Habits is a practical guide to building good habits,
breaking bad ones, and achieving lasting personal growth...
```

---

## Technologies Used

- Python
- Streamlit
- OpenRouter API
- Function Calling
- Requests
- python-dotenv

---

## Future Improvements

- Book cover images
- Ratings and reviews
- ISBN search
- Author search
- Favorite books
- Download book information
- Voice support

---

## License

This project is intended for learning and educational purposes.

---

## Author

Sandhya M
