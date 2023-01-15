class ScraperBase:
    def __init__(self):
        self.navegador = None
        self.page = None

    def create_navegador(self, playwright):
        self.navegador = playwright.chromium.launch()
        
    def create_page(self):
        self.page = self.navegador.new_page()
    
    def go_to_page(self, url):
        self.page.goto(url)
