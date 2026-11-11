from strands import Agent, tool
from strands.vended_tools import web_fetch


@tool
def letter_counter(word: str, letter: str) -> int:
    """
    Count occurrences of a specific letter in a word.

    Args:
        word (str): The input word to search in
        letter (str): The specific letter to count

    Returns:
        int: The number of occurrences of the letter in the word
    """
    if len(letter) != 1:
        raise ValueError("The 'letter' parameter must be a single character")

    return word.lower().count(letter.lower())
agent = Agent(tools=[web_fetch, letter_counter])
agent("What are the pricing options here https://skillbuilder.aws/subscriptions . How many letters are in the cheapest plan's name?")