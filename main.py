from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact')
def index2():
    return render_template('contact.html')


@app.route('/recomendation')
def index3():
    return render_template('recomendation.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
