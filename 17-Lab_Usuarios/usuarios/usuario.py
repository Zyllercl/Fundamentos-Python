
class Usuario:
    def __init__(self, id_usuario=None, username=None, password=None):
        # Inicializacion de las variables
        self._id_usuario = id_usuario
        self._username = username
        self._password = password
    
    def __str__(self):
        return (f'ID: {self._id_usuario} | Username: {self._username} | Password: {self._password}')
    
    # Metodo GET
    @property
    def get_id_usuario(self):
        return self._id_usuario
    # Metodo SET
    @get_id_usuario.setter
    def set_id_usuario(self, id_usuario):
        self._id_usuario = id_usuario
    
    # Metodo GET
    @property
    def get_username(self):
        return self._username
    # Metodo SET
    @get_username.setter
    def set_username(self, username):
        self._username = username
    
    # Metodo GET
    @property
    def get_password(self):
        return self._password
    # Metodo SET
    @get_password.setter
    def set_password(self, password):
        self._password = password


# TESTING #
if __name__ == '__main__':
    # Crear un usuario
    usuario = Usuario(1, 'zyller', 'zyller123')
    print(f'[+] Usuario creado con exito: {usuario}')
    
    # Obtener metodo GET de username
    print(f'[+] Nombre de usuario: {usuario.set_username}')
    
    # Obtener metodo SET de username
    usuario.username = 'Mopachino'
    print(f'[-] Nombre modificado: {usuario.set_username}\n')
    
    # Mostrar usuario modificado
    print(f'[+] Usuario modificado con exito: {usuario}')