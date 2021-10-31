from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def oof():
    return render_template('test.html')

@app.route('/<x>')
def var_x(x=0):
    x= int(x)

    return render_template('varriable_x.html', x=x)

@app.route('/<x>/<y>')
def var_x_y(x=0,y=0):
    x=int(x)
    y=int(y)
    return render_template('varriable_x_y.html',x=x,y=y)

if __name__ == "__main__":
    app.run(debug=True)