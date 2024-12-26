import os
import shutil
import time
import logging

DIRETORIO_ORIGEM = "/home/valcann/backupsFrom"
DIRETORIO_DESTINO = "/home/valcann/backupsTo"
LOG_ORIGEM = "/home/valcann/backupsFrom.log"
LOG_DESTINO = "/home/valcann/backupsTo.log"
LIMITE_TRES_DIAS = time.time() - 3 * 86400

def validar_diretorio(diretorio):
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

def listar_arquivos(diretorio):
    arquivos = []
    for root, dirs, files in os.walk(diretorio):
        for file in files:
            arquivos.append(os.path.join(root, file))
    return arquivos

def filtrar_arquivos_por_data(arquivos, limite_tempo):
    arquivos_para_copiar = []
    arquivos_para_remover = []
    for arquivo in arquivos:
        tempo_criacao = os.stat(arquivo).st_ctime
        if tempo_criacao <= limite_tempo:
            arquivos_para_copiar.append(arquivo)
        else:
            arquivos_para_remover.append(arquivo)
    return arquivos_para_copiar, arquivos_para_remover

def remover_arquivos(arquivos):
    for arquivo in arquivos:
        try:
            os.remove(arquivo)
            logging.info(f"Removido: {arquivo}")
        except Exception as e:
            logging.error(f"Erro ao remover {arquivo}: {e}")
    
def copiar_arquivos(arquivos, destino):
    for arquivo in arquivos:
        try:
            shutil.copy2(arquivo, destino)
            logging.info(f"Copiado: {arquivo} => {destino}")
        except Exception as e:
            logging.error(f"Erro ao copiar {arquivo} para {destino}: {e}")

def inicializar_logger(caminho_log):
    logging.basicConfig(
        filename=caminho_log,
        filemode='a',  
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def main():
    validar_diretorio(DIRETORIO_ORIGEM), validar_diretorio(DIRETORIO_DESTINO)

    if not os.listdir(DIRETORIO_ORIGEM):
        print("Nenhum arquivo encontrado no diretório de origem.")
        return

    inicializar_logger(LOG_ORIGEM)

    arquivos = listar_arquivos(DIRETORIO_ORIGEM)
    for arquivo in arquivos:
        stats = os.stat(arquivo)
        logging.info(f"Encontrado: {arquivo}, {stats.st_size}, "
                     f"{time.ctime(stats.st_ctime)}, {time.ctime(stats.st_mtime)}")

    arquivos_para_copiar, arquivos_para_remover = filtrar_arquivos_por_data(arquivos, LIMITE_TRES_DIAS)

    if not arquivos_para_copiar and not arquivos_para_remover:
        print("Nenhum arquivo atende aos critérios para remoção ou cópia.")
        return

    remover_arquivos(arquivos_para_remover)

    inicializar_logger(LOG_DESTINO)
    copiar_arquivos(arquivos_para_copiar, DIRETORIO_DESTINO)

if __name__ == "__main__":
    main()
