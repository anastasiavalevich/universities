# Italian Universities AI Extractor

This project is a Python-based, fully autonomous multi-agent system that discovers and crawls official Italian university websites. It extracts structured academic content using LLMs (Google Gemini via google-adk) — all without manually specifying any URLs.

## Objective

- Discover accredited Italian universities automatically using web search.
- Crawl their official websites and extract meaningful content.
- Save the results as individual JSON files for each university, including:
  - Clean Markdown-formatted content
  - Metadata (URL, page titles)
  - LLM-generated summaries

## Project Structure

italian_universities_system/

- agent.py – Main coordinator agent
- prompt.py – Prompt for coordinator agent
- .env – API keys (not tracked by Git)
- sub_agents/
  - crawling/
    - agent.py – Crawling agent logic
    - prompt.py – Crawling prompt
  - university_discovery/ - agent.py – Discovery agent logic - prompt.py – Discovery prompt
    output/
  - One JSON file per university

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Create a `.env` file in the project root with your API key:
   GOOGLE_API_KEY=your_api_key_here
   GOOGLE_GENAI_USE_VERTEXAI=FALSE

3. Start the ADK web interface:

```
adk web
```

4. Save the output manually or extend the script to write one JSON file per university.

## Example Output

Each JSON file contains something like this:

```
{
  "name": "Università degli Studi di Bologna",
  "url": "https://www.unibo.it",
  "pages": [
    {
      "title": "Admissions for International Students",
      "url": "https://www.unibo.it/en/admissions",
      "content_markdown": "## Welcome to Admissions\nHere you’ll find information..."
    }
  ],
  "summary": "The university offers a wide range of international programs...",
  "metadata": {
    "domain": "unibo.it",
    "pages_scraped": 8
  }
}
```

## Dependencies

- google-adk – Multi-agent framework provided by Google
- python-dotenv – Load environment variables from .env file
