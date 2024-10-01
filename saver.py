def save_art(art):
    user_input = input("Бажаєте зберегти ASCII-арт у файл? (y/n): ")
    if user_input.lower() == 'y':
        with open("ascii_art.txt", "w", encoding="utf-8") as file:
            for line in art:
                file.write(line + "\n")
        print("ASCII-арт збережено у файл ascii_art.txt")
    else:
        print("ASCII-арт не збережено.")
