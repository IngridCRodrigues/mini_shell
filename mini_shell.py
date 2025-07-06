import os 

from entrada import mostrar_prompt, ler_entrada
from execucao import executar_comando
    
def loop_shell():
    while True:
        mostrar_prompt()
        entrada = ler_entrada()
        if entrada.lower() == "exit":
            break
        elif entrada == "":
            continue
        else:
            executar_comando(entrada)


if __name__ == "__main__":
    loop_shell()