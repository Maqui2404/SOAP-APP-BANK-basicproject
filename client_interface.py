from zeep import Client
from PyInquirer import prompt

# URL del servicio SOAP
url = 'http://localhost:8000/?wsdl'

def authenticate_user(client, username, password):
    try:
        # Autenticar usuario
        response = client.service.authenticate(username, password)
        return response
    except Exception as e:
        return f"Error al autenticar: {e}"

def deposit_amount(client, username, amount):
    try:
        # Realizar un depósito
        response_deposit = client.service.deposit(username, amount)
        return response_deposit
    except Exception as e:
        return f"Error al depositar: {e}"

def withdraw_amount(client, username, amount):
    try:
        # Realizar un retiro
        response_withdraw = client.service.withdraw(username, amount)
        return response_withdraw
    except Exception as e:
        return f"Error al retirar: {e}"

# Crear cliente SOAP
client = Client(url)

# Número máximo de intentos permitidos para la contraseña
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    questions = [
        {
            'type': 'input',
            'name': 'username',
            'message': 'Ingrese su nombre de usuario:'
        },
        {
            'type': 'password',
            'name': 'password',
            'message': 'Ingrese su contraseña:'
        }
    ]

    # Pedir al usuario que ingrese su nombre de usuario y contraseña
    answers = prompt(questions)
    username = answers['username']
    password = answers['password']

    # Autenticar al usuario
    auth_response = authenticate_user(client, username, password)

    if 'éxito' in auth_response:  # Verificar si la autenticación fue exitosa
        print(auth_response)  # Imprimir mensaje de autenticación exitosa
        break
    else:
        print(auth_response)  # Imprimir mensaje de error en la autenticación
        attempts += 1
        if attempts == max_attempts:
            print("Se han agotado los intentos. Saliendo...")
            exit()

while True:
    menu_question = [
        {
            'type': 'list',
            'name': 'choice',
            'message': 'Menú:',
            'choices': [
                'Depositar',
                'Retirar',
                'Salir'
            ]
        }
    ]

    choice = prompt(menu_question)['choice']

    if choice == 'Depositar':
        amount = float(input("Ingrese la cantidad a depositar: "))
        response = deposit_amount(client, username, amount)
        print(response)  # Imprimir mensaje de depósito
    elif choice == 'Retirar':
        amount = float(input("Ingrese la cantidad a retirar: "))
        response = withdraw_amount(client, username, amount)
        print(response)  # Imprimir mensaje de retiro
    elif choice == 'Salir':
        print("Saliendo...")
        break
