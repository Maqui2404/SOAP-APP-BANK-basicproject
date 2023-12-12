from zeep import Client

# URL del servicio SOAP
url = 'http://localhost:8000/?wsdl'

while True:
    try:
        # Crear cliente SOAP
        client = Client(url)

        # Autenticar usuario
        response = client.service.authenticate('usuario1', 'contraseña1')

        print(response)  # Imprimir mensaje de autenticación

        # Mostrar menú de opciones
        print("Menú:")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Salir")

        choice = input("Seleccione una opción: ")

        if choice == '1':
            # Realizar un depósito
            amount = int(input("Ingrese la cantidad a depositar: "))
            response_deposit = client.service.deposit('usuario1', amount)
            print(response_deposit)  # Imprimir mensaje de depósito exitoso
        elif choice == '2':
            # Realizar un retiro
            amount = int(input("Ingrese la cantidad a retirar: "))
            response_withdraw = client.service.withdraw('usuario1', amount)
            print(response_withdraw)  # Imprimir mensaje de retiro exitoso
        elif choice == '3':
            print("Saliendo...")
            break  # Salir del bucle
        else:
            print("Opción no válida")

    except Exception as e:
        print(f"Error al comunicarse con el servicio SOAP: {e}")
