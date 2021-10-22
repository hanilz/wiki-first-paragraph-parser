# Assignment from Max of LoudN'Clear to Hanil Zarbailov
# Make a Wikipedia first paragraph parser using Python and HTML

from flask import Flask, redirect, url_for, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/",methods=["POST", "GET"]) 
def home(): # main page
	if request.method== "POST": # if requested search
		name = request.form["search"] # get search input
		url = "https://wikipedia.org/wiki/" + name # get requested URL

		r = requests.get(url)

		soup = BeautifulSoup(r.content, 'html5lib') # get all HTML of URL

		# get all HTML of <div id='mw-content-text'>
		paragraph = soup.find('div', attrs = {'id':'mw-content-text'}) 

		# for finding first paragraph
		p=paragraph.find("p", attrs={'class': None}) 
		return  render_template("index.html", content = p.get_text('\n'))
	else: # first call to index
		return render_template("index.html", content = "")

if __name__ == "__main__":
	app.run()