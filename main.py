from input_handlers import get_user_input, get_color_choice
from art_generator import generate_art
from aligner import align_text
from printer import preview_art
from saver import save_art

def main():
    while True:
        shape, width, height, alignment, symbol = get_user_input()
        color_code = get_color_choice()

        art = generate_art(shape, width, height, symbol)
        art = align_text(art, width, alignment)

        preview_art(art, color_code)

        save_art(art)

        restart = input("Бажаєте створити ще один ASCII-арт? (y/n): ")
        if restart.lower() != 'y':
            break

if __name__ == "__main__":
    main()
