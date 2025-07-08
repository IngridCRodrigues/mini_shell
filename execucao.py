import os
import re
        
def executar_comando(entrada):

    if re.search(r'>>>+|> {1,}>|<<+|<{1,}<', entrada):
        os.write(1, "Erro de sintaxe! Operadores de redirecionamento inválidos.\n".encode())
        return

    regex_saida = re.match(r'^\s*(.*?)\s*(>>|>|<)\s*(.*?)\s*$', entrada)
    
    if regex_saida:
        comando = regex_saida.group(1)
        operador = regex_saida.group(2)
        arquivo = regex_saida.group(3)

        argumentos = comando.split()

        if not argumentos or not arquivo:
            os.write(1, "Comando inválido!\n".encode()) #indica ao descritor de arquivo o que escrever
            return
        
        try:
            pid = os.fork()
            if pid == 0:
                if operador == '>>': #redireionamento de saida - acrescenta informação
                    r_saida = os.open(arquivo, os.O_WRONLY | os.O_APPEND | os.O_CREAT, 0o644) #o open retorna o a identificao numerica do arquivo
                    os.dup2(r_saida, 1) #ao inves de apontar pra tela, o descritor aponta pro arquivo r_saida
                    os.execvp(argumentos[0], argumentos)      
                elif operador == '>':        
                    r_saida = os.open(arquivo, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644) #subscreve
                    os.dup2(r_saida, 1)
                    os.execvp(argumentos[0], argumentos) 
                elif operador == '<':       #testa redirecionamento de entrada  
                    r_entrada = os.open(arquivo, os.O_RDONLY)# os.O_RDONLY Abre o arquivo somente para leitura.
                    os.dup2(r_entrada, 0)
                    os.execvp(argumentos[0], argumentos) 
            else:
                os.wait() #processo pai espera 
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
                    os.write(1, f"Esse comando não foi encontrado: {argumentos[0]}".encode())
                    os._exit(1)
            else:
                os.wait()
        except OSError as e:
            os.write(1, f"Erro ao criar o processo: {e}\n".encode())