from openai import OpenAI

from .prompts import (
    SYSTEM_PROMPT,
    QUESTION_PROMPT,
    SUMMARY_PROMPT,
    REWRITE_PROMPT,
    EXTRACT_JSON_PROMPT,
)


class TextAssistant:

    def __init__(self, client: OpenAI):
        self.client = client
        self.model = "gemini-3.6-flash"

    def _generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

    def answer_question(self, question: str) -> str:
        prompt = QUESTION_PROMPT.format(user_input=question)
        return self._generate(prompt)

    def summarize(self, text: str) -> str:
        prompt = SUMMARY_PROMPT.format(user_input=text)
        return self._generate(prompt)

    def rewrite(self, text: str) -> str:
        prompt = REWRITE_PROMPT.format(user_input=text)
        return self._generate(prompt)

    def extract_entities(self, text: str) -> str:
        prompt = EXTRACT_JSON_PROMPT.format(user_input=text)
        # Using standard generation; the prompt heavily coerces JSON format.
        return self._generate(prompt)