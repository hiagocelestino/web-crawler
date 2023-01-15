from playwright.sync_api import sync_playwright

list_item = []
with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")
    itens = pagina.query_selector_all('div.thumbnail')
    
    for item in itens:
        preco = item.query_selector('div.caption .price').inner_text()
        descricao = item.query_selector('p.description').inner_text()
        reviews = item.query_selector('div.ratings p.pull-right').inner_text()
        rating = item.query_selector('div.ratings p[data-rating]').get_attribute('data-rating')
        
        dict_item = {
            "preco": preco,
            "descricao": descricao,
            "reviews": reviews,
            "rating": rating
        }
        list_item.append(dict_item)
