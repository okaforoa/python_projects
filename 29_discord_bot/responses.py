from difflib import get_close_matches
import json
from typing import Optional


def get_best_match(user_question: str, questions: dict) -> Optional[str]:
    """Compares the user message similarity to the ones in the dictionary"""

    questions_list = [q for q in questions]
    matches = get_close_matches(user_question, questions_list, n=1, cutoff=0.6)

    # Return the first best match, else return None
    if matches:
        return matches[0]
    return None


def get_response(message: str, knowledge: dict) -> str:
    # Finds the best match, otherwise returns None
    best_match: Optional[str] = get_best_match(message, knowledge)

    # Gets the best match from the knowledge base
    if best_match and (answer := knowledge.get(best_match)):
        return answer
    else:
        return 'I don\'t understand... Could you try rephrasing that?'


def load_knowledge(file: str) -> dict:
    with open(file, 'r') as f:
        return json.load(f)
