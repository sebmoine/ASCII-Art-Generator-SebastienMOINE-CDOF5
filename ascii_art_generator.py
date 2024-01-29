import pyfiglet

def generate_ascii_art(text):
    # Using pyfiglet for ASCII art conversion
    ascii_art = pyfiglet.figlet_format(text)
    return ascii_art

def main():
    user_input = input("Enter text for ASCII art: ")
    art = generate_ascii_art(user_input)
    print(art)

if __name__ == "__main__":
    main()
