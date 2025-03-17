from os import environ

from typing import List
from zkmarek.video.slides.common.slide_base import SlideBase


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def load(filename):
    with open(filename, "r") as file:
        data = file.read()
    return data


def get_slide_by_label(slide_id, all_slides, globals) -> SlideBase:
    try:
        return all_slides[int(slide_id.strip()) - 1]
    except ValueError:
        return globals[slide_id.strip()]()


def get_slides_from_names(
    slide_names: List[str], all_slides: List[SlideBase], globals=globals()
) -> List[SlideBase]:
    if slide_names is None:
        return all_slides
    return [
        get_slide_by_label(label, all_slides, globals)
        for label in slide_names.split(",")
    ]


def get_deck_name(default_deck):
    env_name = dict(environ).get("DECK")
    return default_deck if env_name is None else env_name


# code: Code (arg)
#   code: Paragraph
#     lines_text: Text
#       text: str // with some whitespaces removed
#       original_text: str

def extract_text_from_code(code_obj):
    if hasattr(code_obj, "code"):
        return "\n".join(
            "".join(line.text for line in vgroup if hasattr(line, "text"))
            for vgroup in code_obj.code.submobjects
        )
    raise AttributeError("Could not find code text in Code object.")


def find_in_code(code_obj, subject):
    try:
        text = extract_text_from_code(code_obj)
        indices = [i for i in range(len(text)) if text.startswith(subject, i)]
        return indices
    except AttributeError:
        raise AttributeError("Could not extract text from Code object.")
