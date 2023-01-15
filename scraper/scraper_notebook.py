from .scraper_base import ScraperBase
from playwright.sync_api import sync_playwright


class ScraperNotebook(ScraperBase):
    def __init__(self):
        self.list_notebooks = []
        self.url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'

    def run(self):
        with sync_playwright() as p:
            self.create_navegador(p)
            self.create_page()
            self.go_to_page(self.url)
            self.itens = self.seleciona_itens('div.thumbnail')
            self.captura_dados()
            self.ordenar_itens('preco')
    
    def seleciona_itens(self, seletor):
        return self.page.query_selector_all(seletor)
    
    def captura_dados(self):
        for item in self.itens:
            preco = item.query_selector('div.caption .price').inner_text()
            descricao = item.query_selector('p.description').inner_text()
            reviews = item.query_selector('div.ratings p.pull-right').inner_text()
            rating = item.query_selector('div.ratings p[data-rating]').get_attribute('data-rating')
            
            dict_item = {
                "preco": self.corrige_valor_notebook(preco),
                "descricao": descricao,
                "reviews": self.corrige_valor_reviews(reviews),
                "rating": rating
            }
            self.list_notebooks.append(dict_item)

    def ordenar_itens(self, chave_ordenacao):
        self.list_notebooks = sorted(self.list_notebooks, key = lambda obj: obj[chave_ordenacao])

    def corrige_valor_notebook(self, valor_string):
        from decimal import Decimal
        valor = valor_string[valor_string.find('$') + 1 :]
        return Decimal(valor)

    def corrige_valor_reviews(self, valor_reviews):
        valor_reviews = valor_reviews[ : valor_reviews.find(' ')]
        return int(valor_reviews)

