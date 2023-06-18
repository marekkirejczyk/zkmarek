from typing import List
from zkmarek.video.slides.common.slide_base import SlideBase

def into_groups(arr, n):
    return [arr[i:i + n] for i in range(0, len(arr), n)]

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
