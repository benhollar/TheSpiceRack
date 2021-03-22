from typing import List as _List

from dragnet.extractor import Extractor as _Extractor
from fast_bert.learner_cls import BertLearner as _BertLearner
import requests as _requests


class Recipe:
    title: str = ''
    ingredients: _List[str] = []
    instructions: _List[str] = []

    def __init__(self):
        self.title = ''
        self.ingredients = []
        self.instructions = []

    def __str__(self):
        return (
            "| " + self.title + " |\n" +
            "-" * (len(self.title) + 4) + "\n" +
            "Ingredients\n  " +
            "\n  ".join(self.ingredients) + "\n" +
            "Instructions\n  " +
            "\n  ".join(self.instructions)
        )



def extract_recipe(url: str,
                   extractor: _Extractor,
                   classifier: _BertLearner) -> Recipe:

    # Get the content of the webpage, then use our model to get the recipe.
    raw_html = _requests.get(url).content
    raw_text = extractor.extract(raw_html)

    # As a preprocessing step, break lines into an array (for line-by-line) 
    # classification, and attempt a heuristic to keep related content together.
    raw_text = raw_text.split('\n')
    for index in range(1, len(raw_text)):
        if len(raw_text[index - 1]) > 0 and len(raw_text[index - 1]) < 9:
            raw_text[index - 1] = raw_text[index - 1] + ' ' + raw_text[index]
            raw_text[index] = ''
    raw_text = list(filter(len, raw_text))

    # Now we've got good lines of content, classify each line
    predictions = classifier.predict_batch(raw_text)

    # And now that we have predictions, we can build up a `Recipe`
    recipe = Recipe()
    for tuple in list(zip(raw_text, predictions)):
        best_guess: str = tuple[1][0][0]
        current_line: str = tuple[0]
        if best_guess == 'title' and len(recipe.title) == 0:
            recipe.title = current_line
        elif best_guess == 'ingredient' and len(recipe.instructions) == 0:
            recipe.ingredients.append(current_line)
        elif best_guess == 'instruction':
            separated_steps = current_line.split(".")
            separated_steps = [x.strip() + "." for x in separated_steps]
            separated_steps = list(filter(lambda x: x != ".", separated_steps))
            [recipe.instructions.append(x) for x in separated_steps]

    return recipe
