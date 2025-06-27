from google.adk import Agent
from google.adk.tools import google_search
from . import prompt

MODEL = "gemini-2.5-pro"


university_discovery_agent = Agent(
    model=MODEL,
    name="university_discovery_agent",
    description=(
        "Finds official Italian university "
        "websites using Google search."
    ),
    instruction=prompt.UNIVERSITY_DISCOVERY_PROMPT,
    output_key="university_list",
    tools=[google_search],
)