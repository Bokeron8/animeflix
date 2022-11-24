from core import app

@app.route('/')
def say_hello():
    return "Hello World!"