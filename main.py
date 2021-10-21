from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def meni():
    return render_template("meni.html")

@app.route("/meni2")
def meni2():
    return render_template("meni2.html")

@app.route("/meni_eng")
def meni_eng():
    return render_template("meni_eng.html")

if __name__ == '__main__':
    app.run()
