import ollama
import json
from tools import calculator,search

TOOLS={
    "calculator":calculator,
    "search":search
}
SYSTEM_PROMPT='''
You are a ReAct-style tool-calling agent.

You have access to these tools:

1. search(query)
   Use for factual lookup.
   

2. calculator(expression)
   Use for arithmetic calculations only.

   
search(query)

This is NOT a web search engine.

It is a small database.

Available facts:

leader of zentoria
alice birthplace
lumina country
capital of india
capital of usa
largest population country

Use these exact concepts.
Do not search for alternative phrasings.
Do not assume internet access.


IMPORTANT RULES:

- Return EXACTLY ONE valid JSON object.
- Never return explanations.
- Never return markdown.
- Never return multiple JSON objects.
- Never return text before or after JSON.
- Never answer from memory if a tool can provide the information.
- Think step-by-step.
- If information is missing, use a tool.
- If a tool result is insufficient, reformulate the query and call another tool.
- Do not guess.
- Do not hallucinate.
- Do not invent tool names.
- Use only the provided tools.
- Use calculator ONLY for mathematical expressions.
- Never use calculator for factual questions.

For a tool call return:

{
  "thought": "reasoning for next step",
  "tool": "tool_name",
  "input": "tool_input"
}

For a final answer return:

{
  "final_answer": "answer"
}

Before returning final_answer:

Verify that all entities in the reasoning chain have been resolved.

Example:

leader -> person
person -> birthplace
birthplace -> country

Do not stop until the chain is complete.

Before returning final_answer ask yourself:

Do I have every intermediate fact required?

If an observation contains a person,
and the question asks about birthplace,
search for birthplace.

If an observation contains a city,
and the question asks about country,
search for country.

Only return final_answer when all entities have been resolved.

Examples:

Question:
What is 25 * 17?

Response:
{
  "thought": "Need arithmetic calculation",
  "tool": "calculator",
  "input": "25*17"
}

Question:
What is the capital of India?

Response:
{
  "thought": "Need factual lookup",
  "tool": "search",
  "input": "capital of india"
}

Question:
Observation: New Delhi

Response:
{
  "final_answer": "New Delhi"
}

Question:
Observation: No result found

Response:
{
  "thought": "Need a better search query",
  "tool": "search",
  "input": "reformulated query"
}

Remember:

Return ONLY ONE JSON object.
Nothing else.
'''
class Agent:
    def __init__(self):
        self.max_steps=5
    def call_llm(self,messages):
        response=ollama.chat(
            model="llama3.2",
            messages=messages,
            options={
                "temperature": 0,
                "top_p": 0.1
            }
        )
        return response['message']["content"]
    def run(
            self,
            query
    ):
        messages=[
            {
                "role":"system",
                "content":SYSTEM_PROMPT
            },
            {
                "role":"user",
                "content":f"""
Question:

{query}

Available tools:

search(query)
calculator(expression)

Return exactly one JSON object.
"""
            }
        ]
        for step in range(self.max_steps):
            print(f"\nSTEP {step+1}")
            response=self.call_llm(
                messages
            )
            print(f"\nLLM: {response}")

            try:
                data=json.loads(response)
            except:
                return response
            if ("final_answer" in data):
                return data["final_answer"]
            tool_name=data["tool"]
            tool_input=data["input"]
            print("\nRAW RESPONSE")
            print(response)
            print(
                "ACTION: ",
                tool_name
            )
            observation=TOOLS[
                tool_name
            ](tool_input)
            print("OBSERVATION: ",observation)
            messages.append(
                {
                    "role":"assistant",
                    "content":response
                }
            )
            messages.append(
                {
                    "role":"user",
                    "content":
                    f"Observation: {observation}"
                }
            )
        return (
            "Maximum steps reached"
        )