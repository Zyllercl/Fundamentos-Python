from logger_base import log
from usuario_DAO import UsuarioDAO
from usuario import Usuario

def app():
    # Inicializacion de la APP
    action = True
    
    while action:
        try:
            print('\n####  MENU  ####')
            print('1. Listar usuarios')
            print('2. Agregar usuario')
            print('3. Actualizar usuario')
            print('4. Eliminar usuario')
            print('5. Salir')
            
            option = int(input('\nIngrese una opcion: '))
            
            # Tipos de opciones:
            if option == 1:
                users_list = UsuarioDAO.db_select()
                log.debug(f'[+] Listado de usuarios en la db: ')
                
                for user in users_list:
                    log.debug(user)
            elif option == 2:
                new_username = input('Nombre de usuario: ')
                new_password = input('Contraseña de usuario: ')
                
                new_user = Usuario(username=new_username, password=new_password)
                users_added = UsuarioDAO.db_insert(new_user)
                log.debug(f'[+] Usuarios agregados con exito: {users_added}')
            elif option == 3:
                id_user = int(input('ID usuario a modificar: '))
                update_username = input('Actualizar usuario: ')
                update_password = input('Actualizar password: ')
                
                update_user = Usuario(id_user, update_username, update_password)
                users_updated = UsuarioDAO.db_update(update_user)
                log.debug(f'[+] Usuarios actualizados con exito: {users_updated}')
            elif option == 4:
                id_user = int(input('ID usuario a modificar: '))
                user = Usuario(id_usuario=id_user)
                users_deleted = UsuarioDAO.db_delete(user)
                log.debug(f'[!] Usuarios eliminados: {users_deleted}')
            elif option == 5:
                log.debug(f'[!] Saliendo del programa...')
                break
        except ValueError as e:
            log.warning(f'[!] Solo puede ingresar numeros')
        except Exception as e:
            log.error(f'[!] ERROR: {e}')
            option = False
    else:
        log.error(f'[!] Ocurrio un problema...')

app()