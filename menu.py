import algorithms
while True:
    rle = open("Logo-rle.txt", "a+")
    art = open("logo-ASCII.txt", "a+")
    algorithms.display_menu()
    choice = input()
    if choice == "A": print("\nHERE IS YOUR IMAGE:\n\n\n", algorithms.enter_rle())
    elif choice == "B": algorithms.display_ASCII_art()
    elif choice == "C": algorithms.convert_ASCII_art()
    else:
        break
