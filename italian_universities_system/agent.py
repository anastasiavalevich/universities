from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.university_discovery import university_discovery_agent
from .sub_agents.crawling import crawling_agent

import os
from dotenv import load_dotenv

load_dotenv()
MODEL = "gemini-2.5-pro"


italian_universities_coordinator = LlmAgent(
    name="italian_universities_coordinator",
    model=MODEL,
    description=(
        "autonomously discovers official Italian "
        "universities and crawls their websites "
        "to extract structured content, metadata, "
        "and summaries using LLM capabilities."
    ),
    instruction=prompt.ITALIAN_UNIVERSITIES_COORDINATOR_PROMPT,
    output_key="university_data",
    tools=[
        AgentTool(agent=university_discovery_agent),
        AgentTool(agent=crawling_agent),
    ],
)

root_agent = italian_universities_coordinator
