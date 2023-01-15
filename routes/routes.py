from app import app
from flask import jsonify

@app.route('/')
def index():
    return 'Index'


@app.route('/scraper/notebook')
def get_notebook():
    from scraper.scraper_notebook import ScraperNotebook
    scraper = ScraperNotebook()
    scraper.run()
    
    return jsonify(scraper.list_notebooks)
