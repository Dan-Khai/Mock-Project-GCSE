def decompress(data):
    decompressed = ""
    for i in range(0, len(data), 3):
        final = int(data[i]+data[i+1])*data[i+2]
        decompressed += final
    return decompressed
################################
def enter_rle():
    art = open("art.txt", "a")
    lines = int(input("""
---------------ENTER-RLE---------------------
Input number of lines you would like
to decompress to ASCII-art format:
    (P.S: You are only allowed max: 2 lines): """))
    while lines > 2: lines = int(input("You have more than 2 lines, try again: "))
    for i in range(lines):
        art.write(decompress(input("\nInput your line of rle: \n")))
    return art.read()
################################
def display_ASCII_art():
    filename = input("Input the name of the file\n(p.s don't forget .txt): ")
    print(open(filename, "r").read())
#################################
def convert_ASCII_art():
    filename = input("Input the name of the file\n(p.s don't forget .txt): ")
    file = open(filename, "w+")
    compressed = file.read()
    file.write(decompress(compressed))
    print(file.read())
