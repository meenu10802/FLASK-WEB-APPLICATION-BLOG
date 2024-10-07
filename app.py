from flask import Flask, render_template

app = Flask(__name__)
posts=[
    {
        'Author':'Durjoy datta',
        'Background':"PHD Pyhsic",
        "Status":"Married to beautiful wife",
        'Name':"Love trinagle",
        'Content':'About'
    },
    {
        'Title':"Meri section",
        'Author':'Durjoy datta',
        'Background':"PHD Pyhsic",
        "Status":"Married to beautiful wife",
        'Name':"Love trinagle",
        'Content':'About'
    }
]
@app.route("/")
@app.route("/home") #we can have two decorators when both the links takes us to same page
def hello():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title='ABOUT')

if __name__ == "__main__":
    app.run(debug=True)
