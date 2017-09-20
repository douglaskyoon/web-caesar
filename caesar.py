

def alphabet_position(letter):
    return ord(letter.upper()) - 65

def rotate_character(char, rot):
    if 64 < ord(char) < 90:
        return chr((((ord(char) - 64) + rot) % 26) + 64)
    elif 96 < ord(char) < 122:
        return chr((((ord(char) - 96) + rot) % 26) + 96)
    else:
        return char

def encrypt(text, rot):
    new_txt = []
    for char in text:
        new_txt.append(rotate_character(char, rot))
    return "".join(new_txt)

def main():
    from sys import argv
    text = input("Type a message:")
    rot = int(argv[1])
    print(encrypt(text, rot))

if __name__ == "__main__":
    main()