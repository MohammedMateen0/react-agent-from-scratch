from graph import graph

while True:
    question=input("\nAsk: ")
    if question.lower()=="exit":
        break
    result=graph.invoke(
        {
            "question":question,
            "iterations":0
        }
    )
    print()
    print(result["tool_result"])