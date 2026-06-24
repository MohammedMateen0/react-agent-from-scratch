# Day 1 - ReAct Agent From Scratch

Part of Week 15 - AI Agents 

## Overview

This project implements a simple ReAct-style AI agent from scratch using Python and Llama 3.2 through Ollama.

The goal was not to use LangGraph, CrewAI, or any agent framework, but to understand the fundamental mechanics behind all modern AI agents.

The agent follows the ReAct pattern:

Thought → Action → Observation → Repeat

and uses external tools to gather information before producing a final answer.

---

## Learning Objectives

- Understand what makes an AI agent different from a chain
- Implement the ReAct loop manually
- Learn tool calling mechanics
- Build a tool registry
- Handle observations
- Implement termination conditions
- Add guardrails against infinite loops
- Debug common agent failures

---

## Project Structure

```text
llm_tool_calling_agent/
│
├── tools.py
├── agent.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Tools

### Search Tool

A simple knowledge-base lookup tool.

```python
def search(query):
```

Used for factual retrieval.

Example knowledge:

```python
knowledge = {
    "largest population country":"India",
    "capital of india":"New Delhi",
    "capital of usa":"Washington DC",
    "largest planet":"Jupiter",

    "leader of zentoria":"Alice",
    "alice birthplace":"Lumina",
    "lumina country":"Novaland"
}
```

---

### Calculator Tool

```python
def calculator(expression):
```

Used for arithmetic calculations.

Example:

```text
25 * 17
```

Output:

```text
425
```

---

## Tool Registry

Tools are registered in a dictionary.

```python
TOOLS = {
    "search": search,
    "calculator": calculator
}
```

The agent selects a tool dynamically and executes it during runtime.

---

## ReAct Loop

The agent follows:

```text
Question
    ↓
Thought
    ↓
Action
    ↓
Tool Execution
    ↓
Observation
    ↓
Repeat
```

Pseudo-code:

```python
while not done:

    response = llm(context)

    if tool_call:
        execute_tool()

    elif final_answer:
        stop()
```

---

## Example

Question:

```text
What is the capital of the country with the largest population?
```

Execution:

```text
STEP 1

Tool:
search

Input:
country with the largest population

Observation:
India

STEP 2

Final Answer:
New Delhi
```

---

## LLM

Model:

```text
Llama 3.2
```

Runtime:

```text
Ollama
```

Generation settings:

```python
temperature=0
top_p=0.1
```

---

## Agent Architecture

```text
User
 │
 ▼
Llama 3.2
 │
 ▼
JSON Tool Call
 │
 ▼
Python Agent
 │
 ▼
Tool Execution
 │
 ▼
Observation
 │
 ▼
Llama 3.2
 │
 ▼
Final Answer
```

---

## Challenges Encountered

### Tool Misuse

The model occasionally called the calculator for factual questions.

Example:

```text
Question:
What is the country with the largest population?

Tool:
calculator()
```

Reason:

The model was confused after receiving unsuccessful observations.

---

### Retrieval Failure

Initial search implementation relied on exact string matching.

Example:

```text
country with the largest population
```

did not match:

```text
largest population country
```

Solution:

Implemented keyword-overlap retrieval.

---

### Premature Termination

The model often produced a final answer before completing all required reasoning steps.

Example:

```text
Alice
↓
Lumina
↓
STOP
```

instead of:

```text
Alice
↓
Lumina
↓
Novaland
```

This highlighted one of the major challenges in agent design.

---

### Tool Description Problem

The model interpreted the search tool as a web search engine rather than a small knowledge-base lookup tool.

Improved tool descriptions significantly improved performance.

---

## Key Concepts Learned

### Agent

```text
LLM
+
Tools
+
Decision Loop
```

---

### Tool Calling

The model does not execute code.

It generates JSON.

Example:

```json
{
  "tool":"search",
  "input":"capital of india"
}
```

Python executes the tool.

---

### Observation Injection

Tool outputs are converted back into text and appended to the conversation history.

Example:

```text
Observation:
New Delhi
```

The model then reasons using the updated context.

---

### ReAct

```text
Reason
Act
Observe
Repeat
```

The foundation of most modern agent frameworks.

---

### Agent vs Chain

Chain:

```text
Fixed Workflow
```

Agent:

```text
Dynamic Workflow
```

The agent chooses the next step based on observations.

---

## Results

Successfully implemented:

* Tool Registry
* Tool Calling
* Observation Injection
* ReAct Loop
* Structured JSON Outputs
* Retry Logic
* Max-Step Guardrails
* Llama 3.2 Integration

---

## Technologies Used

* Python
* Ollama
* Llama 3.2

---

## Next Steps

Day 2:

* LangGraph
* StateGraph
* State Management
* Nodes
* Edges
* Conditional Routing
* Checkpointing
* Human-in-the-Loop (HITL)

---

````

# End of Day 1 Summary

### What you built

A complete ReAct-style agent from scratch without any framework.

### What worked

- LLM-generated tool calls
- JSON parsing
- Tool execution
- Observation injection
- Iterative reasoning loop
- Guardrails with `max_steps`

### What failed (and why)

- Multi-hop reasoning was inconsistent.
- The model often terminated early.
- Tool descriptions strongly influenced behavior.
- Retrieval quality directly impacted agent performance.

### Most Important Lesson

An agent is **not** the model.

The model only predicts text.

The agent is:

```text
Prompt
+
Tools
+
Loop
+
State
+
Guardrails
````

Understanding that distinction is the primary objective of Day 1 and the foundation for everything in LangGraph, CrewAI, and production agent systems.
