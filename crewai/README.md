# Day 3 — CrewAI Fundamentals

This module introduces **CrewAI**, a framework for building collaborative AI systems where multiple role-based agents work together to solve complex tasks. Unlike LangGraph, which focuses on explicit graph execution, CrewAI abstracts orchestration through **Agents**, **Tasks**, and **Crews**, enabling rapid development of multi-agent workflows.

---

## Learning Objectives

By the end of this module, you will understand:

- Creating AI Agents with specialized roles
- Assigning Tasks to agents
- Building and executing a Crew
- Sequential multi-agent workflows
- Automatic and explicit context passing
- Hierarchical manager-worker execution
- Differences between CrewAI and LangGraph
- Running CrewAI locally with Ollama (Llama 3.2)

---

# Programs

## Program 1 — Creating an Agent

### Concepts

- Agent
- Role
- Goal
- Backstory
- LLM Configuration

### What was implemented

Created a Restaurant Researcher agent using CrewAI.

```python
researcher = Agent(
    role="Restaurant Researcher",
    goal="Find the best restaurants in Hyderabad",
    backstory="Expert food researcher.",
    llm=llm,
    verbose=True
)
```

### Learned

- An Agent is not another LLM.
- It is a role-specific prompt wrapped around an LLM.
- Agents define specialization.

---

## Program 2 — Creating Tasks

### Concepts

- Task
- Description
- Expected Output
- Agent Assignment

### What was implemented

```python
research_task = Task(
    description="Research the best restaurants in Hyderabad.",
    expected_output="Top 5 restaurants",
    agent=researcher
)
```

### Learned

Tasks represent work assigned to agents.

An Agent without a Task performs no execution.

---

## Program 3 — Creating a Crew

### Concepts

- Crew
- kickoff()
- Execution Pipeline

### What was implemented

```python
crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    llm=llm,
    verbose=True
)

result = crew.kickoff()
```

### Learned

Execution begins only after calling

```python
crew.kickoff()
```

CrewAI automatically

- Builds prompts
- Executes the assigned agent
- Collects outputs
- Returns the final response

---

## Program 4 — Sequential Multi-Agent Workflow

Three specialized agents collaborate.

```
Researcher
      │
      ▼
Analyst
      │
      ▼
Writer
```

### Agents

- Restaurant Researcher
- Food Analyst
- Food Writer

### Execution

```python
process=Process.sequential
```

### Learned

Sequential execution follows a predefined order.

Task outputs automatically become inputs for the next task.

---

## Program 5 — Context Passing

Instead of relying only on sequential execution,

CrewAI allows explicit task dependencies.

```python
analysis_task = Task(
    ...
    context=[research_task]
)
```

Writer receives

```python
context=[
    research_task,
    analysis_task
]
```

### Learned

- Explicit context passing
- Task dependency management
- Multi-input prompt composition

---

## Program 6 — Hierarchical Process

Instead of a fixed workflow,

a manager agent delegates work.

```
              Manager
             /   |   \
            ▼    ▼    ▼
      Research Analyst Writer
```

### Execution

```python
process=Process.hierarchical
```

Manager

```python
allow_delegation=True
```

### Learned

- Dynamic delegation
- Manager-worker architecture
- Multi-agent coordination
- Higher flexibility
- Higher token cost

---

# CrewAI Architecture

```
                Crew
                  │
        ┌─────────┴─────────┐
        │                   │
     Agents              Tasks
        │                   │
        └─────────┬─────────┘
                  │
             Crew Orchestrator
                  │
                  ▼
                 LLM
                  │
                  ▼
              Final Output
```

---

# Sequential Workflow

```
Researcher

↓

Research Task

↓

Analyst

↓

Analysis Task

↓

Writer

↓

Report
```

---

# Hierarchical Workflow

```
              Manager
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
 Researcher   Analyst    Writer
```

Manager dynamically decides which specialist should execute the next task.

---

# CrewAI vs LangGraph

| CrewAI | LangGraph |
|---------|-----------|
| High-level abstraction | Low-level orchestration |
| Agent-based | State-based |
| Fast prototyping | Production workflows |
| Automatic context passing | Explicit state management |
| Role semantics | Graph semantics |
| Easier to start | Greater control |

---

# CrewAI vs ReAct

| ReAct | CrewAI |
|--------|---------|
| Single agent | Multiple agents |
| Manual reasoning loop | Automatic orchestration |
| Manual tool execution | Task abstraction |
| Tool-centric | Role-centric |

---

# Key Concepts

## Agent

Defines

- Role
- Goal
- Backstory
- Tools (optional)

---

## Task

Defines

- Description
- Expected Output
- Assigned Agent

---

## Crew

Coordinates

- Agents
- Tasks
- Execution

---

## Sequential Process

```
Task1

↓

Task2

↓

Task3
```

Simple and predictable.

---

## Context Passing

Explicitly specify previous task outputs.

```python
context=[research_task]
```

---

## Hierarchical Process

Manager agent dynamically delegates work.

```
Manager

↓

Specialists
```

---

# Challenges Encountered

- Configuring CrewAI with Ollama instead of the default OpenAI provider
- Understanding CrewAI's LLM configuration
- Resolving task assignment validation errors
- Fixing hierarchical delegation issues
- Understanding implicit vs explicit context passing

---

# Technologies Used

- Python
- CrewAI
- Ollama
- Llama 3.2
- Local LLM Inference

---

# Skills Gained

- Agent-based AI design
- Multi-agent orchestration
- Task management
- Context propagation
- Sequential workflows
- Hierarchical workflows
- Local LLM integration
- CrewAI architecture

---

# Repository Structure

```
crewai/
│
├── basic_agent.py
├── task.py
├── crew.py
├── multi_agents.py
├── context_passing.py
├── hierarchical_process.py
├── README.md
```

---

# Key Takeaways

- Agents encapsulate specialized roles and objectives.
- Tasks define work assigned to agents.
- Crews orchestrate execution across agents.
- Sequential workflows are simple and efficient.
- Context passing enables task dependencies.
- Hierarchical workflows introduce manager-driven delegation.
- CrewAI is well suited for rapid multi-agent prototyping.
- LangGraph remains the preferred choice for production systems requiring explicit state management, checkpointing, and complex routing.

---

**Day 3 Status:** ✅ Completed

**Next Module:** Day 4 — Single-Agent vs Multi-Agent (The 80% Rule)