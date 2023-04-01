from flask import Flask

app = Flask(__name__)


@app.route('/')
def roots():
    return 'Справочник по регионам России'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
