from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

# ---------- HOME ----------
@app.route('/')
def home():

    # If no secret code exists
    if not os.path.exists("secret.txt") or os.path.getsize("secret.txt") == 0:
        return redirect('/setup')

    return render_template('index.html')


# ---------- SETUP SECRET CODE ----------
@app.route('/setup', methods=['GET', 'POST'])
def setup():

    if request.method == 'POST':

        secret_code = request.form['secret_code']

        with open("secret.txt", "w") as file:
            file.write(secret_code)

        return redirect('/')

    return render_template('setup.html')


# ---------- CHECK CALCULATOR INPUT ----------
@app.route('/check_code', methods=['POST'])
def check_code():

    entered_code = request.form['code']

    with open("secret.txt", "r") as file:
        saved_code = file.read()

    if entered_code == saved_code:
        return "vault"

    try:
        result = eval(entered_code)
        return str(result)

    except:
        return "Error"


# ---------- VAULT ----------
@app.route('/vault')
def vault():

    notes = ""

    if os.path.exists("notes.txt"):
        with open("notes.txt", "r") as file:
            notes = file.read()

    return render_template('vault.html', notes=notes)


# ---------- SAVE NOTES ----------
@app.route('/save_notes', methods=['POST'])
def save_notes():

    notes = request.form['notes']

    with open("notes.txt", "w") as file:
        file.write(notes)

    return redirect('/vault')


if __name__ == '__main__':
    app.run(debug=True)
