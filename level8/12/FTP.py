from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def main():
    # Instantiate a dummy authorizer for managing 'virtual' users
    authorizer = DummyAuthorizer()

    # Define a new user having full r/w permissions and a read-only
    # anonymous user
    authorizer.add_user('secure_user', 'mutineers', '/opt', perm='lr')

    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer

    # Define a customized banner (string returned when client connects)
    handler.banner = "pyftpdlib based ftpd ready."

    # Specify a masquerade address and the range of ports to use for
    # passive connections.  Decomment in case you're behind a NAT.
    handler.masquerade_address = '3.249.74.244'
    handler.passive_ports = range(60000, 60009)

    # Instantiate FTP server class and listen on 0.0.0.0:2121
    address = ("0.0.0.0", 2121)
    server = FTPServer(address, handler)

    # set a limit for connections
    server.max_cons = 2048
    server.max_cons_per_ip = 20

    # start ftp server
    server.serve_forever()

if __name__ == '__main__':
    main()

