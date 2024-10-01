def generate_art(shape, width, height, symbol):
    art = []
    for y in range(height):
        line = ""
        for x in range(width):
            if shape == "Квадрат":
                line += symbol
            elif shape == "Трикутник":
                line += symbol if x <= (y * (width // height)) else " "
            elif shape == "Ромб":
                line += symbol if abs(width // 2 - x) + abs(height // 2 - y) <= height // 2 else " "
            elif shape == "Колесо":
                line += symbol if (x - width // 2) ** 2 + (y - height // 2) ** 2 <= (height // 2) ** 2 else " "
        art.append(line)

    max_length = max(len(line) for line in art)
    art = [line.ljust(max_length) for line in art]
    
    return art
