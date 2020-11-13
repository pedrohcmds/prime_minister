# Projeto de Coleta de Pronunciamento dos primeiros

Serão coletados nesse projeto os os pronunciamentos dos primeiros ministros do Reino Unido do período de 28/05/1937 a 26/07/1955

## Primeira parte

Coleta dos links que das páginas que contem os pronunciamentos dos primeiros lista_de_primeiros_ministros_ordem_cronologica

Script Responsável: main.py

Tecnologias Utilizadas: Selenium, BeautifulSoup, Requests

Breve Explicação:

O script é responsável por realizar a coleta dos links a partir do Selenium que é uma forma de emular o comportamento humano em páginas web. Os links são coletados e os arquivos são baixados na página de arquivos brutos, separados por primeiro ministros

## Segunda parte

Limpeza dos arquivos brutos em uma tabela CSV e os pronunciamentos em arquivos de texto

Tecnologias Utilizadas: python, copia_links_para_arquivo

Breve Explicação:

Os scripts realizam a limpeza dos arquivos brutos separando as informações relevantes:
Nome do Arquivo (ano-mes-dia/nome_do_primeiro_ministro_/local_de_fala/falante)
Data
Nome do Falante
Tema da Discussão (título do pronunciamento)
Contagem de palavras
Pronunciamento


## Terceira parte

Ajustes nas tabelas

Realizado pelo script resume tabela, condensa as informações de um falante numa única linha do csv
