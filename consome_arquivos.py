from pronunciamento import Pronunciamento
import os


def main():
    arquivos = os.listdir("./arquivos_brutos/ClementAttlee")
    for i, arquivo in enumerate(arquivos, 1):
        print(f"""Arquivo: {arquivo}""")
        url = f".//arquivos_brutos//ClementAttlee//{arquivo}"
        p = Pronunciamento(url)
        p.limpa_pronunciamentos()


if __name__ == '__main__':
    main()
