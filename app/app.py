from flask import Flask, flash, redirect, render_template, request, session
import requests


app = Flask(__name__)

# Auto reload les templates
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def hello_world():
    url = "https://www.googleapis.com/books/v1/volumes?q=goriot"
    response = requests.get(url)
    print(response)
    res = response.json()
    info = res['items']
    print(info)
    print('yes')
    return render_template("layout.html")

if __name__ == "__main__":
    app.run(debug=True)
