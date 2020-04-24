def decompress(data):
    decompressed = ""
    for i in range(0, len(data), 3):
        final = int(data[i]+data[i+1])*data[i+2]
        decompressed += final
    return decompressed
############################################################################
def enter_rle():
    decompressed = "\n"
    art = open("art.txt", "a+")
    lines = int(input("""
---------------ENTER-RLE---------------------
Input number of lines you would like
to decompress to ASCII-art format:
    (P.S: You are only allowed max: 2 lines): """))
    while lines > 2: lines = int(input("You have more than 2 lines, try again: "))
    for i in range(lines):
        decomp = decompress(input("Input your line of rle: \n"))
        art.write(decomp)
        decompressed+=decomp + "\n"
    return decompressed
############################################################################
def display_ASCII_art():
    filename = input("Input the name of the file\n(p.s don't forget .txt): ")
    print(open(filename, "r").read())
############################################################################
def convert_ASCII_art():
    filename = input("Input the name of the file\n(p.s don't forget .txt): ")
    with open(filename, "r") as f:
        t = f.readlines()
    with open(filename, "w+") as f:
        for line in t:
            new_line = decompress(line.strip("\n"))
            f.write(new_line+"\n")
        print(f.read())
        f.close()
#############################################################################
def display_menu():
    print("""
Welcome to my project. Here you can do many things like:
    *Make your own ASCII_art by entering compressed version
of your lines in RLE format
    *Convert your file with RLE to ASCII-art

----------------------MAIN-MENU---------------------------
    A.	Enter RLE
    B.	Display ASCII art
    C.	Convert to ASCII art
    D.	Quit.
\Enter your choice (A, B, C, D)
""")
