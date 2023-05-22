def load(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

def get_slides_from_names(slide_names, globals=globals()):
    if slide_names is None:
        return None
    return [globals[name.strip()]() for name in slide_names.split(",")]
