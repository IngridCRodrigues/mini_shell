# Mini Shell 

Esse projeto visa construir um mini interpretador de comandos (mini shell) utilizando a linguagem Python.
O objetivo é simular um terminal Linux bem simples, interpretando comandos digitados pelo usuário e criando processos filhos para executá-los.

## Como executar

**Pré requisitos:**
- Python
- Linux ou WSL 

### Passos:
- Baixe ou clone o projeto
- Abra o terminal e navegue até a pasta onde está o arquivo mini_shel.py
- Execute o arquivo utilizando o comando `python3 mini_shel.py`


## Chamadas de Sistema

Para que o código interaja com o sistema operacional utilizamos chamadas de sistema da biblioteca `os` no python.

As chamadas utilizadas foram:

- `os.fork()` – Cria um processo filho.
- `os.wait()` – Aguarda a finalização do processo filho.
- `os.write()` – Escreve mensagens na saída.
- `os.execvp()` – Executa um comando no processo filho.
- `os.dup2()` – Redireciona descritores de arquivo.
- `os.open()` – Abre arquivos.
- `os.read()` – Lê a entrada do usuário ou conteúdo de arquivos.


## Exemplos de comandos testados

 ```bash
> echo Olá Mundo! 
Olá Mundo!

> ls -l 
(Exibiu total de arquivos locais)

> cat entrada.py
(conteúdo do arquivo)

> echo Primeira Linha > arquivo.txt
(Criou um arquivo com o conteúdo: Primeira Linha de Código)

> echo Primeira Linha > arquivo.txt
(Adicionou ao arquivo o conteúdo: Segunda Linha de Código)

> wc -l < arquivo.txt
(Exibiu a quantidade de linhas do arquivo)

> echo oi >>> arquivo 
Erro de sintaxe! Operadores de redirecionamento inválidos!

 ```

### Demonstração 
Vídeo de demonstração [aqui]

### Limitações conhecidas 
- Espera comandos bem formatados
- Não foi implementado o uso de pipes 
- Não é compatível com multiplos redirecionamentos 