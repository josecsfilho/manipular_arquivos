import shutil
import datetime
import socket

# Variaveis
hostname = socket.gethostname()
nome_do_arquivo = "teste.exe"
caminho_origem = 'C:/arquivo-origem'
caminho_destino = 'C:/arquivo-destino'

# Manipulando os arquivos
data_hora_atual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
nome_do_arquivo_novo = f"{nome_do_arquivo}_{data_hora_atual}_{hostname}"
caminho_arquivo_origem = f"{caminho_origem}/{nome_do_arquivo}"
caminho_arquivo_destino = f"{caminho_destino}/{nome_do_arquivo_novo}"
shutil.move(caminho_arquivo_origem, caminho_arquivo_destino)

print(f"O arquivo {nome_do_arquivo} foi copiado para {caminho_destino} "
      f"com o novo nome {nome_do_arquivo_novo}")

