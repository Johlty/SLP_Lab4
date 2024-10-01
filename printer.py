def print_art(art, color_code):
    for line in art:
        print(f"{color_code}{line}\033[0m")

def preview_art(art, color_code):
    print("\nПопередній перегляд ASCII-арту:")
    print_art(art, color_code)
