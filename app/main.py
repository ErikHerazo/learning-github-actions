def greet(name: str) -> str:
    return f"Hello, {name}!"

def multiplicacion_dos_numeros(a:int,b:int):
    return a*b

def main():
    name = input("Enter your name: ")
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(greet(name))
    print(multiplicacion_dos_numeros(a,b))

if __name__ == "__main__":
    main()
