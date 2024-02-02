import pyfiglet

def generate_ascii_art(text, fontsize=None, font="standard"):
    # Using pyfiglet for ASCII art conversion
    ascii_art = pyfiglet.figlet_format(text, font=font, width=fontsize)
    return ascii_art

def select_font():
    fonts = ["block", "banner", "standard", "avatar", "3d_diagonal"]
    print("Choose a font for your ASCII art:")
    for i, font in enumerate(fonts, start=1):
        print(f"{i}. {font}")

    while True:
        choice = input("Enter the number of your font choice: ")
        if choice.isdigit() and 0 < int(choice) <= len(fonts):
            return fonts[int(choice)]
        else:
            print("Invalid choice. Please enter a valid number.")

def main():
    user_input = input("Enter text for ASCII art: ")
    font_size_input = input("Enter font size: ")
    font_choice = select_font()
    
    art = generate_ascii_art(user_input, int(font_size_input), font_choice)
    print(art)

if __name__ == "__main__":
    main()
