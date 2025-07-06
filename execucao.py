import os
        
def executar_comando(entrada):

    if '>>' in entrada:
        partes = entrada.split('>>')

        if len(partes) != 2 :
            os.write(1, b"Erro de sintaxe! Verifique a escrita e tente novamente!\n")
            return
        
        comando = partes[0].strip()
        arquivo = partes[1].strip()
        argumentos = comando.split()

        if not argumentos:
            os.write(1, "Comando inválido!\n".encode())
            return

        try:
            pid = os.fork()
            if pid == 0:
                saida = os.open(arquivo, os.O_WRONLY | os.O_APPEND | os.O_CREAT, 0o644)
                os.dup2(saida, 1)
                os.execvp(argumentos[0], argumentos)                
            else:
                os.wait()
        except Exception as e:
            os.write(1,f"Erro: {str(e)}\n".encode())

    elif '>' in entrada:
        partes = entrada.split('>')
        if len(partes) != 2 :
            os.write(1, b"Erro de sintaxe! Verifique a escrita e tente novamente!\n")
            return
        comando = partes[0].strip()
        arquivo = partes[1].strip()
        argumentos = comando.split()

        if not argumentos:
            os.write(1, "Comando inválido!\n".encode())
            return

        try:
            pid = os.fork()
            if pid == 0 :
                saida = os.open(arquivo, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
                os.dup2(saida, 1)
                os.execvp(argumentos[0], argumentos)
            else:
                os.wait()
        except Exception as e:
            os.write(1,f"Erro: {str(e)}\n".encode())

    else:
        argumentos = entrada.split()
        if not argumentos:
            os.write(1, "Comando inválido!\n".encode())
            return

        try:
            pid = os.fork() #criando um processo filho

            if pid == 0: #o sistema ja sabe que o processo filho ganha o pid = 0 
                try:
                    os.execvp(argumentos[0], argumentos)
                except FileNotFoundError:
                    os.write(1, f"Esse comando não foi encontrado: {argumentos[0]}".encode());
                    os._exit(1);
            else:
                os.wait();
        except OSError as e:
            os.write(1, f"Erro ao criar o processo: {e}\n".encode());
