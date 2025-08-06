from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tipos')
def tipos():
    return render_template('tipos.html')

@app.route('/reciclaje')
def reciclaje():
    return render_template('reciclaje.html')

if __name__ == '__main__':
    app.run(debug=True)