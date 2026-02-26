from openai import OpenAI
from config import OPENAI_API, MODEL_NAME
from prompts import SYSTEM_PROMPT, build_user_prompt
import json

client = OpenAI(api_key=OPENAI_API)

def generate_advisory(env_data):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=0.2,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_user_prompt(env_data)}
        ]
    )

    return json.loads(response.choices[0].message.content)
    