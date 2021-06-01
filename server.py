"""
Here, we will first verify if the input link is from wikipedia or not.
If yes, then we will extract all data from that page, and split on basis of space. Also we will take the line till we we find "]\n". Then that list we will send to the function. Now that list will be also stored in set so we can get unique values. Now we will create 2D list in which we will iterate the set items and find the count from list and store that word and count in the 2D list. And then we sort that list in descending order on basis of second element that is frequency, and return that first 10 elements of the 2D list. 
If link is not correct we will get message as "Please enter correct link"
"""

from flask import Flask, render_template, request
import validators
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
@app.route('/')
def index():
  return render_template('index.html')
def freq(l):
    li=l
    h=[]  
    sets=set(l)
    for i in sets:
        h.append([i,li.count(i)])
    h.sort(key = lambda x: x[1],reverse=True)
    h=h[0:10]
    return h
    
@app.route('/',methods=['POST'])
def my_link():
    text=request.form['u']
    if "en.wikipedia.org/wiki/" in text and validators.url(text)==True:
        url=text
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "lxml")
        txt= soup.find_all('p')
        l=[]       
        for i in txt:
            extracted_text=i.text
            valid_len=extracted_text.find("]\n")
            l+=extracted_text[0:valid_len].split(" ")
        li=freq(l)
        return render_template('index.html', my_list=li)
    else:
        return "Please enter correct link"

if __name__ == '__main__':
  app.run(debug=True)
  