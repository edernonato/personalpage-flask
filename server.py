from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("cv/index.html")


@app.route('/index.html')
def en_us():
    return render_template("cv/index.html")


@app.route('/pt-br.html')
def pt_br():
    return render_template("cv/pt-br.html")


if __name__ == "__main__":
    app.run(debug=True)
