from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")cd 
def index():
    return render_template("index.html")
    
@app.route("/scrape", methods=['POST'])        
def scrape():
    # Collect data from index_html file se site se 
    site = request.form['site']
    data = scrape_site(site)
    return render_template('results.html', data=data)

def scrape_site(site):
    data = {}
    if site=='youtube':
        url = "https://www.youtube.com/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        data['Title'] = soup.title.string
    elif site == 'amazon':
        url = "https://www.amazon.in/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        data['Title'] = soup.title.string
    elif site == 'Netflix':
        url ="https://www.netflix.com/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        data['Title'] = soup.title.string
    
    else:
        data['error'] = "Site not Supported."
    return data
    

#'''Jab aap soup = BeautifulSoup(response.text, 'html.parser') likhte
# hain, to aap basically website se li gayi HTML ko BeautifulSoup ke 
# through parse kar rahe hain aur usko soup variable mein store kar 
# rahe hain taaki aap asaani se us HTML se data nikaal sakein.'''


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    
    