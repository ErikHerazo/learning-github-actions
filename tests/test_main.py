from app.main import greet

def test_greet():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("") == "Hello, !"

def test_multiplicacion_dos_numeros():
    assert multiplicacion_dos_numeros(2, 3) == 6
    assert multiplicacion_dos_numeros(-1, 5) == -5
    assert multiplicacion_dos_numeros(0, 10) == 0
    assert multiplicacion_dos_numeros(5, 0) == 0
    assert multiplicacion_dos_numeros(1, 1) == 1
    assert multiplicacion_dos_numeros(-2, -3) == 10