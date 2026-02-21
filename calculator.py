print("Calculadora")
print("----------------")

while True:
    print("\nOpciones:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    print("5. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 + num2
        print(f"La suma es {resultado}")
    elif opcion == "2":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 - num2
        print(f"La resta es {resultado}")
    elif opcion == "3":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 * num2
        print(f"El producto es {resultado}")
    elif opcion == "4":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        if num2 != 0:
            resultado = num1 / num2
            print(f"La división es {resultado}")
        else:
            print("Error: No se puede dividir entre cero")
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")
