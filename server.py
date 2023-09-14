from flask import Flask, render_template
app= Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Home page. Please forward slash play, play/x and play/x/color to select a screen.'

@app.route('/play')
def play():
    return render_template("index.html", count = 3, color = "blue")

@app.route('/play/<int:x>')
def play_two(x):
    return render_template("index.html", count = x, color = "lightblue")

@app.route('/play/<int:x>/<string:color>')
def play_three(x, color):
    return render_template("index.html", count = x, color = color)

if __name__=="__main__":
    app.run(debug=True)
