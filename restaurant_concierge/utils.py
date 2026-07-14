import json
import re

def extract_json(text):
    match=re.search(
        r"\{.*\}",
        text,
        re.DOTALL
    )
    if not match:
        raise ValueError("No JSON found.")
    return json.loads(match.group())
def count_tokens(text:str):
    return len(text.split())