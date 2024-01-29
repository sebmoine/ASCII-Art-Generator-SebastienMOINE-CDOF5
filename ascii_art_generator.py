import pyfiglet

def generate_ascii_art(text, fontsize=None):
    # Using pyfiglet for ASCII art conversion
    ascii_art = pyfiglet.figlet_format(text, width=fontsize)
    return ascii_art

def main():
    user_input = input("Enter text for ASCII art: ")
    font_size_input = input("Enter font size : ")
    
    art = generate_ascii_art(user_input, int(font_size_input))
    print(art)

if __name__ == "__main__":
    main()
