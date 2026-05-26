from flask import Flask, render_template, request, redirect
import subprocess
import os

app = Flask(__name__)


# HOME PAGE
@app.route('/')
def home():

    return render_template('index.html')


# SECRET VAULT PAGE
@app.route('/vault')
def vault():

    notes = ""

    if os.path.exists("notes.txt"):

        with open("notes.txt", "r") as file:

            notes = file.read()

    return render_template('vault.html', notes=notes)


# SAVE NOTES
@app.route('/save_notes', methods=['POST'])
def save_notes():

    notes = request.form['notes']

    with open("notes.txt", "w") as file:

        file.write(notes)

    return redirect('/vault')


# SET SECRET CODE
@app.route('/set_code', methods=['POST'])
def set_code():

    code = request.form['secret_code']

    with open("secret.txt", "w") as file:

        file.write(code)

    return redirect('/')


# CALCULATOR + SECRET CODE CHECK
@app.route('/calculate', methods=['POST'])
def calculate():

    expression = request.form['expression']

    # READ SAVED SECRET CODE
    saved_code = ""

    if os.path.exists("secret.txt"):

        with open("secret.txt", "r") as file:

            saved_code = file.read().strip()

    # CHECK SECRET CODE
    if expression == saved_code:

        return "VAULT"

    # NORMAL CALCULATION USING C
    result = subprocess.run(

        ["./calc"],

        input=expression,

        text=True,

        capture_output=True
    )

    output = result.stdout.strip()

    return output


# RUN APP
if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
