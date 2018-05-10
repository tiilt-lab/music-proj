from flask import Flask, render_template, json, request
from lyric_scraper import scrape
from lyric_scraper import compute
from model import InputForm
import sys




app = Flask(__name__, template_folder=".")

@app.route('/handle_data/', methods=['POST', 'GET'])
def handle_data():
    info = request.form['data']
    # song_name = request.form['Song'].lower()
    
    return render_template("page.html")


    # your code
    # return a response

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      value = result['expression']

      url = "https://genius.com/"
      for word in value.split(' '):
      	url+= word+"-"
      url += "lyrics"
      print(url)
      scraped = scrape(url)

      return render_template('page.html',result=scraped)


@app.route("/", methods=['GET', 'POST'])
def init():
  form = InputForm(request.form)
  if request.method == 'POST' and form.validate():
    result = compute(form.Artist.data, form.Song.data)
  else:
    result = None

  return render_template('example.html', form=form, result=result)

if __name__ == "__main__":
    app.run(debug=True)
