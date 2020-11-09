from selenium import webdriver
from time import sleep
import sh
import selenium


def baixa_todos_arquivos_sem_repeticao():
    # Funções que importam comandos linux
    sh.cd("./arquivos_brutos/NevilleChamberlain")
    sh.wget("-N", "-i", "../links.txt")


def coleta_links_da_pagina(driver, links):
    resultados = driver.find_elements_by_xpath("//a[@class='no-underline']")
    print(f"{len(resultados)} resultados nesta página")
    for result in resultados:
        link = result.get_attribute('href')
        print(link)
        links.append(link)


def copia_links_para_arquivo(links):
    with open('./links_ClementAttlee.txt', 'a') as f:
        for link in links:
            f.write(f'{link} \n')


def dicionario_de_links_periodizados():
    return {
        "Chamberlain": "https://hansard.parliament.uk/search/Contributions?startDate=1937-05-28&endDate=1955-07-26&searchTerm=spokenby%3AChamberlain&partial=False",
        "Churchill": "https://hansard.parliament.uk/search/Contributions?startDate=1937-05-28&endDate=1955-07-26&searchTerm=spokenby%3AChurchill&partial=False",
        "Attlee": "https://hansard.parliament.uk/search/Contributions?startDate=1937-05-28&endDate=1955-07-26&searchTerm=spokenby%3AAttlee&partial=False",
    }


def lista_de_primeiros_ministros_ordem_cronologica():
    return ["Neville Chamberlain", "Winston Churchill", "Clement Attlee", "Winston Churchill"]


def inicio_e_fim_da_pesquisa():
    return "28/05/1937", "26/07/1955"


def main():
    existe_proxima_pagina = True
    links = []
    driver = webdriver.Firefox()
    url = "https://hansard.parliament.uk/search/Contributions?startDate=1937-05-28&endDate=1955-07-26&searchTerm=spokenby%3AChurchill&partial=False"
    driver.get(url)
    sleep(6)
    botao_ajuda_inicial = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[3]/button")
    botao_ajuda_inicial.click()
    sleep(6)
    coleta_links_da_pagina(driver, links)
    sleep(6)
    while existe_proxima_pagina:
        driver.execute_script('window.scroll(0, 200)')
        botao_proxima_pagina = driver.find_element_by_xpath("//a[@title='Go to next page']")
        try:
            botao_proxima_pagina.click()
        except selenium.common.exceptions.NoSuchElementException:
            existe_proxima_pagina = False
        sleep(6)
        coleta_links_da_pagina(driver, links)
        sleep(3)
        copia_links_para_arquivo(links)
        if not existe_proxima_pagina:
            break
    # driver.quit()

    copia_links_para_arquivo(links)
    # sleep(3)
    # baixa_todos_arquivos_sem_repeticao()


if __name__ == '__main__':
    main()
