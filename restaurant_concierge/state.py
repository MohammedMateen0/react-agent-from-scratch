from typing import TypedDict

class AgentState(TypedDict):

    question: str

    cuisine:str
    budget:int
    area:str
    
    tool_result:str

    answer:str

    iterations:int

    total_tokens:int

    validation:bool