from base import app


@app.route('/')
def home():
    return "hello world"
