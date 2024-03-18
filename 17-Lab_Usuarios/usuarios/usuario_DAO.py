from usuario import Usuario
from logger_base import log
from cursor_db import Cursor


class UsuarioDAO:
    '''
        DAO     -> Data Access Object para la tabla de usuario
        CRUD    -> CREATE | READ | UPDATE | DELETE para la tabla de usuario
    '''
    
    # Variables Privadas sentencia SQL
    _SELECT = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERT = 'INSERT INTO usuario(username, password) VALUES(%s, %s)'
    _UPDATE = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _DELETE = 'DELETE FROM usuario WHERE id_usuario=%s'
    
    
    # Metodos de clases
    @classmethod
    def db_select(cls):
        with Cursor() as cursor: # Obtenemos el cursor
            cursor.execute(cls._SELECT) # Ejecucion de la sentencia SQL
            users = cursor.fetchall() # Obtenemos todos los registros de la db
            
            users_list = [] # Lista Users
            
            for user in users:
                user = Usuario(user[0], user[1], user[2]) # Transformacion a objetos de tipo usuario
                users_list.append(user) # Se agrega a la lista un objeto de tipo usuario
            return users_list # Retornarmos la lista de usuarios
    
    @classmethod
    def db_insert(cls, user):
        with Cursor() as cursor: # Obtenemos el cursor
            values = (user.get_username, user.get_password)
            cursor.execute(cls._INSERT, values) # Ejecucion de la sentencia SQL
            log.debug(f'[+] Usuario agregado: {user}')
            return cursor.rowcount # Retorna el numero de filas afectadas
    
    @classmethod
    def db_update(cls, user):
        with Cursor() as cursor:
            values = (user.set_username, user.set_password, user.set_id_usuario)
            cursor.execute(cls._UPDATE, values) # Ejecucion sentencia SQL
            log.debug(f'[-] Usuario actualizado: {user}')
            return cursor.rowcount # Retorna el numero de filas afectada    
    
    @classmethod
    def db_delete(cls, user):
        with Cursor() as cursor: # Obtenemos el cursor
            values = (user.get_id_usuario,)
            cursor.execute(cls._DELETE, values) # Ejecucion sentencia SQL
            log.debug(f'[!] Usuario eliminado: {user}')
            return cursor.rowcount # Retorna el numero de filas afectadas


# TESTING #
if __name__ == '__main__':
    # TEST de query INSERT
    # user = Usuario(username='Cocox', password='coco123')
    # users_added = UsuarioDAO.db_insert(user) # Ejecucion metodo db_insert
    # log.debug(f'[+] Usuarios insertados: {users_added}')
    
    # TEST de query UPDATE
    # user = Usuario(5, 'palgos', 'palgo123')
    # users_added = UsuarioDAO.db_update(user) # Ejecucion del metodo db_update
    # log.debug(f'[-] Usuarios actualizados: {users_added}')
    
    # TEST de query DELETE
    user = Usuario(id_usuario=4)
    users_deleted = UsuarioDAO.db_delete(user) # Ejecucion del metodo db_delete
    log.debug(f'[!] Usuarios eliminados: {users_deleted}')
    
    # TEST de query SELECT
    users = UsuarioDAO.db_select()
    
    for user in users:
        print('[+] Ejecutando sentencia SQL SELECT')
        log.debug(user)