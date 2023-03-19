import os


def main():
    nombre = os.getenv("USERNAME")
    lenguaje = os.getenv("LANGUAGE")
    print(f"¡Hola, {nombre} desde {lenguaje}!")


if __name__ == "__main__":
    main()
