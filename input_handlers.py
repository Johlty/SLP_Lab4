def get_shape_choice(shapes):
    while True:
        print("Виберіть фігуру для створення ASCII-арту:")
        for i, shape in enumerate(shapes, start=1):
            print(f"{i}. {shape}")
        
        try:
            shape_choice = int(input("Введіть номер фігури: ")) - 1
            if 0 <= shape_choice < len(shapes):
                return shape_choice
            else:
                print("Будь ласка, виберіть дійсний номер.")
        except ValueError:
            print("Будь ласка, введіть число.")

def get_integer_input(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Будь ласка, введіть число між {min_value} і {max_value}.")
        except ValueError:
            print("Будь ласка, введіть дійсне число.")

def get_alignment_choice():
    while True:
        alignment = input("Виберіть вирівнювання (ліво, центр, право): ").lower()
        if alignment in ['ліво', 'центр', 'право']:
            return alignment
        else:
            print("Будь ласка, виберіть 'ліво', 'центр' або 'право'.")

def get_symbol_input():
    symbol = input("Введіть символ для малювання фігури: ")
    return symbol

def get_color_choice():
    colors = {
        'червоний': '\033[31m',
        'зелений': '\033[32m',
        'жовтий': '\033[33m',
        'синій': '\033[34m',
        'білий': '\033[37m'
    }

    while True:
        color_choice = input("Виберіть колір (червоний, зелений, жовтий, синій, білий): ").lower()
        if color_choice in colors:
            return colors[color_choice]
        else:
            print("Будь ласка, виберіть дійсний колір.")


def get_user_input():
    shapes = ["Квадрат", "Трикутник", "Ромб", "Колесо"]
    
    shape_choice = get_shape_choice(shapes)
    width = get_integer_input("Введіть ширину (10-80): ", 10, 80)
    height = get_integer_input("Введіть висоту (5-40): ", 5, 40)
    alignment = get_alignment_choice()
    symbol = get_symbol_input()
    
    return shapes[shape_choice], width, height, alignment, symbol
