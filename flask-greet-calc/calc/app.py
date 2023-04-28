from flask import Flask, request, render_template
from operations import add, sub, mult, div

app = Flask(__name__)

"""
    Simple Calculator    
    http://localhost:5000/add?a=10&b=20 
"""

@app.route("/add")
def init():
    """Add"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)

@app.route("/sub")
def sub_init():
    """Subtract"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)

    return str(result)

@app.route("/mult")
def mult_init():
    """Multiply"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)

    return str(result)

@app.route("/div")
def div_init():
    """Divide"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)

    return str(result)

### PART TWO

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def math_init(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)




##EXTRA
@app.route("/")
def home():
    """Display the calculator form"""
    return render_template("calculator.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    """Calculate the result of the operation"""
    oper = request.form["oper"]
    a = int(request.form["a"])
    b = int(request.form["b"])
    result = operators[oper](a, b)
    return render_template("result.html", result=result)