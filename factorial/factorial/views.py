#предел факториала и приветственная и прощальная страничка
from flask import render_template, request
from factorial import app

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Number must be non-negative")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    n = None

    if request.method == "POST":
        try:
            n = int(request.form["n"])
            result = factorial(n)
        except ValueError:
            error = "Please enter a valid non-negative integer"

    return render_template(
        "index.html",
        title="Factorial Calculator",
        result=result,
        n=n,
        error=error
    )