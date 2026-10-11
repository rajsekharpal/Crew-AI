# Blog Generator using CrewAI

## Overview
An AI-powered blog generator built with **CrewAI** that uses multiple AI agents to research topics and generate blog content automatically.

## Features
- Automated blog content generation
- AI agents for research and writing
- Web search using the Serper API
- Google Gemini LLM integration

## Technologies Used
- Python
- CrewAI
- Google Gemini API
- Serper API

## Project Structure

```text
Blog-creator/
├── Blog creator/
│   ├── agents.py
│   ├── crew.py
│   ├── tasks.py
│   └── tools.py
├── agents.py
├── crew.py
├── task.py
├── tools.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository:

   ```bash
   git clone <your-repository-url>
   cd <repository-folder>
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   ```

   Windows:

   ```bash
   venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Environment Variables

Create a `.env` file in the project root and add your API keys:

```env
GOOGLE_API_KEY=your_google_api_key
SERPER_API_KEY=your_serper_api_key
```

Get your keys from:

- Google AI Studio: https://aistudio.google.com/
- Serper: https://serper.dev/

**Security:** Never share your API keys or commit your `.env` file to GitHub.

## Usage

Run the main CrewAI Python script. For example, if `crew.py` contains your entry point:

```bash
python crew.py
```

Adjust the command according to your actual entry-point file.

## How It Works

1. The research agent searches for relevant information using Serper.
2. The writing agent uses the research findings to generate blog content.
3. CrewAI coordinates the agents and their tasks.
4. The generated blog is returned as output.

## Future Improvements
- Add a Streamlit user interface.
- Support multiple blog formats and writing styles.
- Export blogs to Markdown or PDF.

## License
For educational and learning purposes.
