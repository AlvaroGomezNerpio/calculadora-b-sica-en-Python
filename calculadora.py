def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def main():
    print("Selecciona la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    while True:
        opcion = input("Ingresa tu opción (1/2/3/4): ")

        if opcion in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Error: Por favor ingresa un número válido.")
                continue

            if opcion == '1':
                print(f"{num1} + {num2} = {sumar(num1, num2)}")
            elif opcion == '2':
                print(f"{num1} - {num2} = {restar(num1, num2)}")
            elif opcion == '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
            elif opcion == '4':
                print(f"{num1} / {num2} = {dividir(num1, num2)}")
            
            # Opción para salir del bucle
            siguiente = input("¿Quieres realizar otra operación? (si/no): ").strip().lower()
            if siguiente != 'si':
                break
        else:
            print("Opción no válida. Por favor selecciona una opción entre 1 y 4.")

if __name__ == "__main__":
    main()
