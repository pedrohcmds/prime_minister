from bs4 import BeautifulSoup


class Pronunciamento:
    def __init__(self, url, ministro="Churchill"):
        with open(url, encoding="utf8", errors="ignore") as f:
            self.ministro = ministro
            self.soup = BeautifulSoup(f, "lxml")
            self.data = self.get_data()
            self.titulo = self.get_titulo().strip()
            self.pronunciamentos = self.get_pronunciamentos()
            self.camara = self.get_camara()

    def __str__(self):
        return f"Titulo: {self.titulo} \n Camara: {self.camara} \n Data: {self.data} \n falas: {self.pronunciamentos}"

    @staticmethod
    def get_linha():
        num_linhas = 0
        file = open("tabela_Churchill.csv")
        for line in file:
            if line != "\n":
                num_linhas = +1

        return str(num_linhas)

    def get_data(self):
        data = self.soup.find("div", class_="col-xs-12 debate-date")
        data = data.find("strong").get_text()
        dia, mes, ano = data.split()
        meses = {
            "Jan": 1,
            "Feb": 2,
            "Mar": 3,
            "Apr": 4,
            "May": 5,
            "Jun": 6,
            "Jul": 7,
            "Aug": 8,
            "Sep": 9,
            "Oct": 10,
            "Nov": 11,
            "Dec": 12,
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12,
        }
        data_formatada = str(f"{ano}-{meses[mes]}-{dia}")
        return data_formatada

    def get_titulo(self):
        titulo = self.soup.find("div", class_="title")
        titulo = titulo.get_text().strip(" ").strip("  ").strip("\n")
        return titulo

    def get_camara(self):
        camara = self.soup.find("div", class_="house-header").find("span").get_text()

        return camara

    def get_pronunciamentos(self):
        list_pronunciamentos = []
        pronunciamentos = self.soup.find_all("div", class_="content-item")
        for fala in pronunciamentos:
            try:
                fala_autor = fala.find("div", class_="col-md-9 nohighlight member-container").get_text()
                fala_autor = fala_autor.strip("\n").strip()
                fala_texto = fala.find_all("p")
                list_pronunciamentos.append((fala_autor, fala_texto))
            except AttributeError:
                continue
        return list_pronunciamentos

    def limpa_pronunciamentos(self):
        for fala in self.pronunciamentos:
            autor = fala[0]
            texto = fala[1]
            texto = texto[0].get_text()
            if autor == "MR. J. CHAMBERLAIN" or autor == "Mr. Ronald Chamberlain":
                continue
            elif autor in Pronunciamento.lista_autores():
                self.cria_txt(autor, texto)
                self.insere_na_tabela(autor, texto)

    def insere_na_tabela(self, autor, texto):
        nome_arquivo = f"{self.data}-{self.ministro}-{self.camara}-{autor}.txt"
        palavras = len(texto.split())
        local_arquivo = f"/home/labri_pedro/prime_minister/{nome_arquivo}"
        with open("tabela_Churchill.csv", "a") as f:
            f.write(f"{local_arquivo};{nome_arquivo};{self.data};{self.titulo};{autor};{palavras};{texto}\n")

    def cria_txt(self, autor, texto):
        nome_arquivo = f"{self.data}-{self.ministro}-{self.camara}-{self.titulo}-{autor}.txt"
        with open(f".//arquivos_limpos//WinstonChurchill//{nome_arquivo}", "a") as file:
            file.write(texto)
            file.write("\n")

    @staticmethod
    def lista_autores():
        return [
            "Mr. Chamberlain",
            "The Prime Minister (Mr. Chamberlain)",
            "The Prime Minister (Sir Winston Churchill)",
            "The Prime Minister",
            "Mr. Churchill",
            "Mr. Churchill (Woodford)",
            "The Prime Minister (Mr. Churchill)",
            "The First Lord of the Admiralty (Mr. Churchill)",
            "Mr. Attlee",
            "Mr. Attlee (by Private Notice)",
            "Mr. C. R. Attlee",
            "Mr. C. R. Attlee (Walthamstow, West)",
            "The Prime Minister (Mr. Attlee)",
            "The Deputy Prime Minister (Mr. Attlee)",
            "The Lord President of the Council (Mr. Attlee)",
            "The Secretary of State for Dominion Affairs (Mr. Attlee)",
            "The Lord Privy Seal (Mr. Attlee)",
        ]
