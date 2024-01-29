import pyfiglet
from PIL import Image
import numpy as np

def generate_ascii_art_from_text(text, font='standard'):
    ascii_art = pyfiglet.figlet_format(text, font=font)
    return ascii_art

def image_to_ascii(image_path, width=100, threshold=128):
    try:
        image = Image.open(image_path)
        image = image.resize((width, int(width * image.height / image.width)))
        image = image.convert('L')  # convert to grayscale
        pixels = np.array(image)
        chars = np.array([' ', '.', ':', '-', '=', '+', '*', '#', '%', '@'])
        ascii_art = "\n".join("".join(chars[pixels[j, i] // (256 // len(chars))] for i in range(width)) for j in range(image.height))
        return ascii_art
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    choice = input("Type 'text' for text-to-ASCII art or 'image' for image-to-ASCII art: ").lower()
    if choice == 'text':
        fonts = ["slant", "standard", "3-d", "3x5", "5lineoblique"]
        print("Choisissez une police pour votre art ASCII :")
        for i, font in enumerate(fonts, start=1):
            print(f"{i}. {font}")

        choice = input("Entrez le numéro de votre choix de police (par défaut 1): ")
        font_choice = fonts[int(choice) - 1] if choice.isdigit() and 0 < int(choice) <= len(fonts) else "standard"
        user_input = input("Enter text for ASCII art: ")
        print(generate_ascii_art_from_text(user_input, font=font_choice))

    elif choice == 'image':
        image_path = input("Enter path to the image: ")
        width = int(input("Enter width for ASCII art (default 100): ") or 100)
        print(image_to_ascii(image_path, width))
    else:
        print("Invalid choice. Please type 'text' or 'image'.")

if __name__ == "__main__":
    main()