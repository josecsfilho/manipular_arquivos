import shutil
import datetime
import time

nome_do_arquivo = "teste.exe"

caminho_origem = 'C:/Users/josefilho/Documents/arquivo-origem'
caminho_destino = 'C:/Users/josefilho/Documents/arquivo-destino'

contador = 1  # inicio do contador

while True:
    try:
        data_hora_atual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nome_do_arquivo_novo = f"{contador:03d}_{nome_do_arquivo}_{data_hora_atual}"# "03d" significa que comando vai iniciar com 3 digitos
        caminho_arquivo_origem = f"{caminho_origem}/{nome_do_arquivo}"
        caminho_arquivo_destino = f"{caminho_destino}/{nome_do_arquivo_novo}"
        shutil.move(caminho_arquivo_origem, caminho_arquivo_destino)
        contador += 1  # Incrementa contador
    except:
        print(f"O arquivo {nome_do_arquivo} foi copiado para {caminho_destino} com o novo nome {nome_do_arquivo_novo}")
    time.sleep(10)





















