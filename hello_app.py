import os
from flask import Flask
import random
import urllib2

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def hello():
    return get_random_thing()

def get_random_thing() :
    adjs = adjs = urllib2.urlopen("https://raw.githubusercontent.com/bellcodo/potential-octo-chainsaw/master/adjectives.lst").read()
    adjs = adjs.split()
    
    random_selection = random.choice(adjs)
    
    return random_selection

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
