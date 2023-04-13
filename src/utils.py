def load(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data
