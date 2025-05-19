def greet(name: str) -> str:
    return f"Hello, {name}!"

def multiplicacion_dos_numeros(a:int,b:int):
    return a*b

def main():
    name = input("Enter your name: ")
    print(greet(name))

if __name__ == "__main__":
    main()
