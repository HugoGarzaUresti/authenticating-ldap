from ldap3 import Server, Connection, ALL

def authenticate(username, password):
    server = Server('ldap://your-ldap-server', get_info=ALL)
    conn = Connection(server, f'uid={username},ou=users,dc=example,dc=com', password)
    if conn.bind():
        print('Authenticated successfully')
        conn.unbind()
        return True
    else:
        print('Authentication failed')
        return False
