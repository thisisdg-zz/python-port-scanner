import socket
import platform

def detectSystemIP():
    return socket.gethostbyname(socket.gethostname())

def detectSystemMAC():
    if platform.system() == "Windows":
        from uuid import getnode as get_mac
        return (hex(get_mac()))
    elif platform.system() == "Linux":
        #import module for Linux systems and return the mac address
        return "Linux"