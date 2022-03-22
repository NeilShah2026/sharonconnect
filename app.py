from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')

# run as dev server
if __name__ == '__main__':
    app.run(debug=True)
    