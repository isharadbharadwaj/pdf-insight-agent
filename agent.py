# agent.py
from agents import Agent, FileSearchTool, ModelSettings
from pydantic import BaseModel
from typing import List

# -------------------------
# Pydantic Output Schema
# -------------------------
class Insight(BaseModel):
    theme: str
    summary_point: str
    tone: str
    key_challenge: str
    main_takeaway: str


class InsightSummary(BaseModel):
    insights: List[Insight]


# -------------------------
# INSTRUCTIONS FOR AGENT
# -------------------------
INSTRUCTIONS = """
You are an AI Insight Summarizer Agent.

Your goal:
Read the uploaded PDF content and produce exactly **5 structured insight points**
that capture the most important ideas.

Follow these rules strictly:

1. Analyze the document holistically (not line-by-line).
2. Each insight must include:
   - "theme": short title of the section/topic (2–6 words)
   - "summary_point": concise main idea (1–2 sentences)
   - "tone": e.g., analytical, persuasive, informative, critical, or reflective
   - "key_challenge": main difficulty or problem discussed
   - "main_takeaway": a short, clear learning or recommendation

3. Keep the language simple and precise.
4. Avoid repeating points.
5. If the document has technical terms, include them contextually.

Output must strictly follow JSON schema provided (no markdown, no text outside JSON).
"""


# -------------------------
# Factory function
# -------------------------
def create_agent(vector_store_id: str):
    """
    Creates and returns the Insight Summarizer Agent configured with vector store.
    """
    return Agent(
        name="PDF Insight Summarizer",
        instructions=INSTRUCTIONS,
        tools=[
            FileSearchTool(
                max_num_results=8,
                vector_store_ids=[vector_store_id],
                include_search_results=True,
            )
        ],
        model_settings=ModelSettings(temperature=0.7),
        output_type=InsightSummary,
    )
