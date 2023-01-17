from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route('/')
@make_bold
@make_emphasis
@make_underlined
def hello():
    return 'Hello, World!'

@app.route('/<name>')
def greet(name):
    return f'<h1 style ="text-align: center; margin: 250px">Unholy {name}!</h1>' \
           "<p style ='text-align: center'> mommy don\'t know daddy\'s getting hot</p>"

if __name__ == "__main__":
    app.run(debug=True)