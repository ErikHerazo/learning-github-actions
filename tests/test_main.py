from app.main import greet, multiplicacion_dos_numeros

def test_greet():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("") == "Hello, !"

def test_multiplicacion_dos_numeros():
    assert multiplicacion_dos_numeros(2, 3) == 6
    assert multiplicacion_dos_numeros(-1, 5) == -5
    