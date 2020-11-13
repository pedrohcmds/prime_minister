def get_arquivo():
    arquivo = "tabela_Chamberlain.csv"
    return arquivo


def escreve_na_tabela_limpa(local, nome_arquivo, data, titulo, autor, fala):
    lista_fala_limpa = []
    fala_limpa = " ".join(fala)
    print(fala_limpa)
    palavras = len(fala_limpa.split(" "))
    lista_fala_limpa.append(fala_limpa)

    with open("tabela_Chamberlain_limpa.csv", "a") as file:
        file.write(f"{local};{nome_arquivo};{data};{titulo};{autor};{palavras};{lista_fala_limpa}")
        file.write("\n")
    print("Informações inseridas na Tabela")


def limpa_tabela():
    lista_arquivos_limpos = []
    arquivo = get_arquivo()
    arquivo = open(arquivo, "r")
    for i, linha in enumerate(arquivo):
        conteudo_linha = linha.split(";")
        local = conteudo_linha[0]
        nome_arquivo = conteudo_linha[1]
        data = conteudo_linha[2]
        titulo = conteudo_linha[3]
        autor = conteudo_linha[4]
        fala = conteudo_linha[6:]
        # print(f"Linha i: {i}")
        if nome_arquivo in lista_arquivos_limpos:
            continue
        arquivo_j = open("tabela_Chamberlain_j.csv")
        for j, linha_j in enumerate(arquivo_j):
            conteudo_linhaj = linha_j.split(";")
            nome_arquivo_atual = conteudo_linhaj[1]
            data_atual = conteudo_linhaj[2]
            titulo_atual = conteudo_linhaj[3]
            autor_atual = conteudo_linhaj[4]
            fala_atual = conteudo_linhaj[6:]

            # print(f"Linha i: {i}")

            if data == data_atual and titulo == titulo_atual and autor == autor_atual and i != j:
                fala += fala_atual
        lista_arquivos_limpos.append(nome_arquivo)

        escreve_na_tabela_limpa(local, nome_arquivo, data, titulo, autor, fala)


if __name__ == '__main__':
    limpa_tabela()
