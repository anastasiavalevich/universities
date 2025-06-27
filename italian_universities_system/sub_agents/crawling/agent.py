from google.adk import Agent
from . import prompt

MODEL = "gemini-2.5-pro"


crawling_agent = Agent(
    model=MODEL,
    name="crawling_agent",
    description=(
        "Crawls university websites and "
        "extracts structured, relevant content."
    ),
    instruction=prompt.CRAWLING_AGENT_PROMPT,
    output_key="crawled_pages",
)
