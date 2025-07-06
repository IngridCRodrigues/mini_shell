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
> echo oi >> arquivo >> echo oi
Erro de sintaxe! Verifique a escrita e tente novamente!

> ls -l 
(Exibiu total de arquivos locais e sua )

> cat test.txt
(conteúdo do arquivo)
 ```

### Demonstração 
Vídeo

### Limitações conhecidas 
- Espera comandos bem formatados
