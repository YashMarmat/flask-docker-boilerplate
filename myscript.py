from flask import Flask
# from dotenv import load_dotenv

# to read .env files
# load_dotenv()

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Welcome to Flask.'

if __name__ == '__main__':
    # app.run(debug=True, port=8001)
    app.run(debug=True)