from mcrcon import MCRcon

server_address = "localhost"
server_pass = "minecraft"
server_port = 25575

with MCRcon(server_address, server_pass, server_port) as mcr:
    while True:
        cm = input("command>")
        log = mcr.command(cm)
        print(log)
