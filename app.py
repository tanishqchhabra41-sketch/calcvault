from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():

    expression = request.form['expression']

    result = subprocess.run(
        ["./calc"],
        input=expression,
        text=True,
        capture_output=True
    )

    output = result.stdout.strip()

    return output


if __name__ == '__main__':
    app.run(debug=True)
