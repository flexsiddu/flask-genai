from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

@app.route('/about')
def about():
    return "i admit it another hoe got me finished, broke my heart oh no you didn't, fuck sippin imma down a whole bottle hard liquor hard truth can't swallow need a bartender put me out my sorrow wake up the next day in a monte carlo with a new women she said she from colorado and she love women and she'll be gone by tomorrow am i kidding all this jealousy and agony that i sit in, im a jealous boy realy feel like john linen"

@app.route('/template')
def template():
    name = "juice wrld"
    items = ["item1", "item2", "item3"]
    dic = {"juicewrld": "dagoat", "sanholo": "also dagoat"}
    classrooms = [
        {"name": "Classroom A", "yearlevel": "1", "capacity": 30},
        {"name": "Classroom B", "yearlevel": "2", "capacity": 25},
        {"name": "Classroom C", "yearlevel": "3", "capacity": 20}
    ]
    return render_template("index.html", name=name, items=items, dic=dic, classrooms=classrooms)

@app.route('/bootstrap')
def bootstrap():
    return render_template("base.html")

app.run()