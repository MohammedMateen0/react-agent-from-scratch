def calculator(expression):
    try:
        return eval(expression)
    except Exception as e:
        return str(e)

def search(query):
    knowledge={
        "capital of india":"New Delhi",
        "capital of usa":"Washington DC",
        "largest planet":"Jupiter"
    }
    return knowledge.get(
        query.lower(),
        "No result found"
    )