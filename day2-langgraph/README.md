# Week 15 - Day 2: LangGraph Fundamentals

Part of the **Hyderabad ML Mission 2026**.

This project introduces **LangGraph**, the production framework for building reliable AI agents. Instead of manually implementing the ReAct loop, LangGraph models agent workflows as **stateful directed graphs** where nodes operate on shared state and edges define execution flow.

---

## Learning Objectives

- Understand LangGraph architecture
- Learn StateGraph and shared state
- Build graph-based workflows
- Connect nodes using edges
- Implement conditional routing
- Use reducers to merge conversation history
- Add checkpointing with MemorySaver
- Implement Human-in-the-Loop (HITL)

---

## Project Structure

```text
week15-day2-langgraph/
│
├── README.md
├── requirements.txt
│
├── program1_basic_graph.py
├── program2_multiple_nodes.py
├── program3_conditional_edges.py
├── program4_reducers.py
├── program5_checkpointing.py
└──  program6_human_in_the_loop.py

```

---

# What is LangGraph?

LangGraph is a framework for building stateful AI agents using graphs.

Instead of writing loops manually,

```python
while True:
    ...
```

LangGraph represents execution as a graph.

```text
START
  │
  ▼
Search
  │
  ▼
Summarize
  │
  ▼
END
```

Each node performs one task and updates a shared state.

---

# Concepts Covered

## 1. StateGraph

A directed graph that defines the workflow of an AI agent.

```python
builder = StateGraph(State)
```

---

## 2. State

Shared memory accessible by every node.

Example:

```python
class State(TypedDict):
    question: str
    answer: str
    summary: str
```

The state acts as the single source of truth throughout graph execution.

---

## 3. Nodes

Nodes are Python functions that receive the current state and return partial state updates.

Example:

```python
def search_node(state):
    ...
```

---

## 4. Edges

Edges define transitions between nodes.

```python
builder.add_edge(
    START,
    "search"
)

builder.add_edge(
    "search",
    END
)
```

Execution Flow

```text
START
 │
 ▼
Search
 │
 ▼
END
```

---

## 5. Conditional Edges

Instead of following a fixed path, the graph dynamically decides the next node.

```python
def route(state):

    if state["answer"] == "Unknown":
        return "retry"

    return "summarize"
```

```python
builder.add_conditional_edges(
    "search",
    route,
    {
        "retry": "retry",
        "summarize": "summarize"
    }
)
```

Execution

```text
          Search
         /      \
        /        \
 Retry         Summarize
     │             │
     └──────┬──────┘
            │
           END
```

---

## 6. Reducers

Reducers define how LangGraph merges state updates.

Using `add_messages`, message history grows automatically instead of being overwritten.

```python
messages: Annotated[
    list,
    add_messages
]
```

---

## 7. Checkpointing

Checkpointing saves graph state after node execution.

Development:

```python
MemorySaver()
```

Production:

```python
PostgresSaver()
```

Benefits

- Resume execution
- Recover after failures
- Long-running agents
- Time-travel debugging

---

## 8. Human-in-the-Loop

Execution can pause before critical nodes.

```python
graph = builder.compile(
    checkpointer=memory,
    interrupt_before=["summarize"]
)
```

Execution

```text
START
 │
 ▼
Search
 │
 ▼

PAUSE

 │
 ▼
Summarize
 │
 ▼
END
```

Human approval is required before execution resumes.

---

# Programs

## Program 1 – Basic Graph

Topics

- StateGraph
- TypedDict
- START
- END
- Single Node

Workflow

```text
START
 │
 ▼
Search
 │
 ▼
END
```

---

## Program 2 – Multiple Nodes

Topics

- Shared State
- Multiple Nodes
- State Updates

Workflow

```text
START
 │
 ▼
Search
 │
 ▼
Summarize
 │
 ▼
END
```

---

## Program 3 – Conditional Routing

Topics

- Conditional Edges
- Router Function
- Dynamic Execution

Workflow

```text
             Search
            /      \
           /        \
 Retry          Summarize
     │               │
     └───────┬───────┘
             │
            END
```

---

## Program 4 – Reducers

Topics

- add_messages
- Message History
- Annotated Types

Purpose

Automatically merge conversation history across multiple nodes.

---

## Program 5 – Checkpointing

Topics

- MemorySaver
- thread_id
- Persistent State
- Resume Execution

Purpose

Save workflow progress and recover after interruptions.

---

## Program 6 – Human-in-the-Loop

Topics

- interrupt_before
- Pause Execution
- Resume Execution
- Approval Workflow

Purpose

Allow human approval before executing critical actions.

---

# Key Learnings

- Graph-based workflows replace manual loops.
- State is shared across every node.
- Nodes update only the fields they modify.
- Edges define workflow transitions.
- Conditional edges enable dynamic routing.
- Reducers merge state updates automatically.
- Checkpointing enables recovery and debugging.
- Human-in-the-loop improves safety in production agents.

---

# Technologies Used

- Python
- LangGraph
- LangChain Core

---

# Requirements

```text
langgraph
langchain
langchain-core
```

---

# Next Steps

Week 15 – Day 3

- Advanced LangGraph
- Production Agent Patterns
- Multi-Agent Coordination
- CrewAI
- LangSmith
- Agent Debugging

---

# Conclusion

This project demonstrates the core concepts required to build production-ready AI agents using LangGraph. By implementing graph-based workflows, shared state management, conditional routing, reducers, checkpointing, and human approval, it provides the foundation for developing reliable and scalable agent systems.