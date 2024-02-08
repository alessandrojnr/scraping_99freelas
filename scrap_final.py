import requests
from parsel import Selector
from bs4 import BeautifulSoup
import json
import pandas as pd


class Scrap():
    def __init__(self):

        self.lista = []

        headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
                }

        pagina = 1

        while True:

            url = "https://www.99freelas.com.br/projects?categoria=web-mobile-e-software&sub-categorias=desenvolvimento-web&page="+ str(pagina)
            print(url)
            r = requests.get(url = url, headers= headers)
            print(r.status_code)

            if "Nós não encontramos nenhum projeto que corresponde à sua pesquisa. Por favor, modifique a sua pesquisa para ver mais projetos." in r.text:
                break

            else:    
                s = Selector(text=r.text)
                teste = s.xpath('/html/body/div[1]/div/div[3]/ul')

                soup = BeautifulSoup(r.text, "html.parser", )
                ul = soup.find("ul" , class_ = "result-list")

                cabecalho = ul.find_all("li")


                for item in cabecalho:
                    text_information = item.find("p",class_="item-text information").get_text().replace('\n','').replace('\t','').split('|')
                    p = item.find('p',class_="item-text habilidades")
                    
                    stack=[]

                    try:
                        aux = p.find_all('a')
                        
                        for a in aux:
                            stack.append(a.get_text().replace('\n','').replace('\t',''))
                    except:
                        stack = []

                    link = str("https://www.99freelas.com.br" + item.find("a").get('href')), 
                    data = {
                        "title": item.find("h1", class_= "title").get_text().replace('\n','').replace('\t',''),
                        "description": item.find("div", class_= "item-text description formatted-text").get_text().replace('\n','').replace('\t',''),
                        "text_information": text_information[0],
                        "level":text_information[1],
                        "stack": stack,
                        "proposals": [int (s) for s in text_information[4].split() if s.isdigit()][0],
                        "interested": [int (s) for s in text_information[5].split() if s.isdigit()][0],
                        "link": link, 
                        "message": ''.join(link).replace("project/", "project/message/")
                    }
                    self.lista.append(data)
                    
                print(pagina)
                pagina+=1

    def envio_excel(self):
        freelas = pd.DataFrame(self.lista)
        freelas.to_excel("planilha.xlsx")


if __name__== "__main__":
    scrap = Scrap()
    scrap.envio_excel()