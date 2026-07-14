from graph import graph
config = {
    "configurable": {
        "thread_id": "restaurant-user"
    }
    }

while True:
    question=input("\nAsk: ")
    if question.lower()=="exit":
        break
    input_state = {
        "question": question,
        "iterations": 0,
        "total_tokens": 0,
        "history": []
    }

    result = graph.invoke(
       input_state,
       config=config
  )
    print()
    print("\nAssistant:\n")
    print(result["answer"])