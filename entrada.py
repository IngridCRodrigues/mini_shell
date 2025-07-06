import os 


def mostrar_prompt():
    os.write(1, b'> ')


def ler_entrada():
    buffer = os.read(0,1024)
    return buffer.decode().strip() #pega o que o usuario digitou e converte para string e também tira os espaços