from spyne import Application, rpc, ServiceBase, Unicode, Integer, Fault
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

# Simulación de una base de datos de usuarios y sus saldos
users = {
    'usuario1': {'contraseña': 'contraseña1', 'saldo': 1000},
    'usuario2': {'contraseña': 'contraseña2', 'saldo': 1500}
}

class AuthService(ServiceBase):
    @rpc(Unicode, Unicode, _returns=Unicode) # Decorador
    def authenticate(ctx, username, password):
        if username in users and users[username]['contraseña'] == password:
            return f"Bienvenido, {username}!"
        else:
            raise Fault(f"No autorizado: Usuario o contraseña incorrectos")
            # raise Fault ... Este error se utiliza específicamente para informar a un cliente que ha ocurrido un problema durante la ejecución de una operación remota SOAP
    @rpc(Unicode, Integer, _returns=Unicode)
    def deposit(ctx, username, amount):
        if username in users:
            users[username]['saldo'] = int(users[username]['saldo'] + amount)
            return f"Depósito exitoso. Nuevo saldo de {username}: {users[username]['saldo']}"
        else:
            raise Fault("Usuario no encontrado")

    @rpc(Unicode, Integer, _returns=Unicode)
    def withdraw(ctx, username, amount):
        if username in users:
            if users[username]['saldo'] >= amount:
                users[username]['saldo'] = int(users[username]['saldo'] - amount)
                return f"Retiro exitoso. Nuevo saldo de {username}: {users[username]['saldo']}"
            else:
                raise Fault("Fondos insuficientes")
        else:
            raise Fault("Usuario no encontrado")
# Instanciar
application = Application([AuthService], tns='auth.services', in_protocol=Soap11(validator='lxml'), out_protocol=Soap11())

if __name__ == '__main__':
    wsgi_application = WsgiApplication(application)
    server = make_server('0.0.0.0', 8000, wsgi_application)
    print("Servidor SOAP con autenticación iniciado en http://0.0.0.0:8000")
    server.serve_forever()
