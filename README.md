# Book Search Agent

A beginner-friendly AI Agent built using Python and OpenRouter Function Calling.

The agent can search for books using the Google Books API (or Open Library API) and answer user queries through tool calling.

---

## Features

- LLM-powered AI Agent
- Function Calling (Tool Calling)
- Book Search Tool
- Conversation Memory
- System Prompt
- Multi-step Agent Loop
- External API Integration

---

## Project Structure

```
book-search-agent/
│
├── main.py
├── tools.py
├── memory.py
├── prompts.py
├── memory.json
├── .env
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/book-search-agent.git

cd book-search-agent
```

### 2. Create a virtual environment

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

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## API Key

Create a `.env` file.

```env
OPENROUTER_API_KEY=your_api_key_here
```

Get your API key from:

https://openrouter.ai/

---

## Run

```bash
python main.py
```

---

## Example

```
You:
Tell me about Atomic Habits

Agent:

Title: Atomic Habits
Author: James Clear
Published: 2018

Description:
...
```

---

## Technologies Used

- Python 3
- OpenRouter API
- Function Calling
- Requests
- python-dotenv
- JSON Memory

---

## Future Improvements

- Cover Images
- ISBN Search
- Book Recommendations
- Author Search
- Multiple Tools
- GUI using Streamlit
- Voice Assistant

---

## Author

Your Name
