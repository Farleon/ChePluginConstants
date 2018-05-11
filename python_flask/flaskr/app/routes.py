from app import app

@app.route('/')
@app.route('/index')

@app.route('/')
def hello_world():
    return 'Hello, World!'
