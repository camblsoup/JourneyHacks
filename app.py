from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/action1', methods=['POST'])
def action1():
    text = 1 + 1
    return f"<h2>Action 1 executed!{text} is 1 + 1</h2><p>Running Python Code 1...</p>"

@app.route('/action2', methods=['POST'])
def action2():
    return "<h2>Action 2 executed!</h2><p>Running Python Code 2...</p>"

@app.route('/action3', methods=['POST'])
def action3():
    return "<h2>Action 3 executed!</h2><p>Running Python Code 3...</p>"

if __name__ == '__main__':
    app.run(debug=True)
