SYSTEM_PROMPT = """
You are a helpful AI text assistant.

Your responsibilities are:
1. Answer questions clearly.
2. Summarize text accurately.
3. Rewrite text while preserving its meaning.
4. Never intentionally invent facts.
5. If you are uncertain, clearly say that you are uncertain.
6. Follow the user's requested task.
"""


QUESTION_PROMPT = """
Answer the following question clearly and accurately.

Question:
{user_input}
"""


SUMMARY_PROMPT = """
Summarize the following text.

Requirements:
- Preserve the main meaning.
- Remove unnecessary repetition.
- Keep important facts.
- Use simple language.

Text:
{user_input}
"""


REWRITE_PROMPT = """
Rewrite the following text so that it is clearer and more professional.

Requirements:
- Preserve the original meaning.
- Improve grammar and clarity.
- Do not add unsupported information.

Text:
{user_input}
"""

EXTRACT_JSON_PROMPT = """
Extract key entities (like names, places, organizations, dates, concepts) from the following text and return the result strictly as a structured JSON object. 

Example JSON format:
{{
  "entities": {{
    "names": ["John Doe"],
    "places": ["New York"],
    "organizations": ["OpenAI"],
    "dates": ["2024"],
    "concepts": ["Generative AI"]
  }}
}}

Text:
{user_input}
"""