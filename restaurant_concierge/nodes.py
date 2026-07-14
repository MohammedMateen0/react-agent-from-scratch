print("Loading nodes.py")
from langchain_ollama import ChatOllama
print("Imported ChatOllama")
import json
print("Imported json")
from tools import RestaurantTool
from utils import extract_json,count_tokens
from config import MAX_TOKEN_BUDGET

llm=ChatOllama(
    model="llama3.2",
    temperature=0
)

def parser_node(state):
    question=state["question"]
    prompt=f'''
You are an information extraction system.

Extract restaurant search parameters.

Return ONLY valid JSON.

Schema:

{{
    "cuisine": "",
    "budget": null,
    "area": ""
}}

Rules:

- If budget is absent use null.
- If cuisine is absent use "".
- If area is absent use "".

Question:

{question}
'''
    response=llm.invoke(prompt)
    used=count_tokens(prompt)
    used+=count_tokens(response.content)
    print('\nLLM OUTPUT\n')
    print(response.content)
    data=extract_json(response.content)
    return {
        "cuisine":data["cuisine"],
        "budget":data["budget"],
        "area":data["area"],
        "total_tokens":state["total_tokens"]+used
    }


tool=RestaurantTool()


def search_node(state):
    results=tool.search(
        cuisine=state["cuisine"] or None,
        budget=state["budget"],
        area=state["area"] or None
    )

    return {
        "tool_result":results
    }

def retry_node(state):
    print("\n Retrying search...\n")
    return {
        "iterations":state["iterations"]+1
    }

def answer_node(state):
     restaurants=state["tool_result"]["restaurants"]
     text=''
     for r in restaurants:
         text+=(
             f"{r['name']}"
             f"{r['area']}"
             f"₹{r['budget']}\n"
         )
     return {
             "answer":text
         }

MAX_ITERATIONS=3

def route(state):
    if state["tool_result"]["success"]:
        return "answer"
    if state["iterations"]>=MAX_ITERATIONS:
        return "stop"
    return "retry"

def budget_node(state):
    print(
        f"\n Token Used: {state['total_tokens']}"
    )
    return {}
def budget_route(state):
    if state["total_tokens"]>=MAX_TOKEN_BUDGET:
        return "stop"
    return "search"