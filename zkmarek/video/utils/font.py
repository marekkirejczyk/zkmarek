from manimpango import list_fonts, register_font

def get_font_names(file):
    orig_font = list_fonts()
    if not register_font(file):
        print(f"Error registering {file}")
    new_font = list_fonts()
    fonts_names = list(set(new_font) - set(orig_font))
    return fonts_names
