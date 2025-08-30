
from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '<h1>We are home</h1>'

# Adding routes after home page
@app.route('/about')
def about():
    return '<h1>About Page</h1>'

if __name__ == '__main__':
    app.run(debug=True)


