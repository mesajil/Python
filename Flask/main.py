from client.curso import Curso
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def main():
    blogs = [Curso('Title', 'Description')]
    message = 'My message'
    return render_template("index.html",
        msn=message, blogs=blogs)


if __name__ == '__main__':
    app.run(debug=True)