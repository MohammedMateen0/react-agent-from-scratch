def calculator(expression):
    try:
        return str(eval(expression))
    except Exception as e:
        return str(e)
def search(query):

    query_words = set(
        query.lower().split()
    )

    knowledge = {
        "largest population country":"India",
        "capital of india":"New Delhi",
        "capital of usa":"Washington DC",
        "largest planet":"Jupiter",
        
        "leader of zentoria": "Alice",
        "alice birthplace": "Lumina",
        "lumina country": "Novaland"
}
    

    best_match = None
    best_score = 0

    for key,value in knowledge.items():

        key_words = set(
            key.split()
        )

        score = len(
            query_words & key_words
        )

        if score > best_score:
            best_score = score
            best_match = value

    if best_score >= 2:
        return best_match

    return "No result found"