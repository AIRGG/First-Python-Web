from flask import Flask, render_template

app = Flask(__name__)

@app.route('/apaaja')
def tampil():
    return render_template('index.html')
    # return "Hello World"

app.run(port=8082, debug=True, host='localhost')
