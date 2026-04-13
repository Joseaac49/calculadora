def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero.")
    return a / b


def main():
    try:
        num1 = float(input("Ingresá el primer número: "))
        num2 = float(input("Ingresá el segundo número: "))
        operacion = input("Elegí una operación (+, -, *, /): ")

        if operacion == "+":
            resultado = sumar(num1, num2)
        elif operacion == "-":
            resultado = restar(num1, num2)
        elif operacion == "*":
            resultado = multiplicar(num1, num2)
        elif operacion == "/":
            resultado = dividir(num1, num2)
        else:
            print("Operación inválida.")
            return

        print(f"El resultado es: {resultado}")

    except ValueError:
        print("Error: debés ingresar valores numéricos válidos.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")


main()