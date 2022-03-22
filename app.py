from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from forms import SignUpVal

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def SignUp():
    form = SignUpVal()
    if request.method == 'POST' and form.validate():
        # do stuff
        return jsonify({"success": True})

    return render_template('signup.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)
    