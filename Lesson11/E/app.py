from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/<filename>", methods=["GET"])
def get_file(filename: str):
    return app.send_static_file(filename)


@app.route("/calculate")
def calculate():
    calc_option = str(request.args.get("operation", None))
    num_one = request.args.get("num1", None)
    num_two = request.args.get("num2", None)

    if not calc_option:
        return {"result": "Error: MissingOperator"}
    if not num_one:
        return {"result": "Error: MissingFirstNumber"}
    if not num_two:
        return {"result": "Error: MissingSecondNumber"}

    if calc_option == "Add":
        result = float(str(f"{float(num_one) + float(num_two):.3f}"))
    elif calc_option == "Subtract":
        result = float(str(f"{float(num_one) - float(num_two):.3f}"))
    elif calc_option == "Divide":
        try:
            result = float(str(f"{float(num_one) / float(num_two):.3f}"))
        except ZeroDivisionError:
            return {"result": "ErrorDividedByZero"}
    elif calc_option == "Multiply":
        result = float(str(f"{float(num_one) * float(num_two):.3f}"))
    else:
        result = "Error: NoSuchOperator"
    return {"result": result}


@app.route("/", methods=["GET"])
def main():
    return render_template("index.html", title="L11 Exercise E")

app.run(debug=True, host="0.0.0.0", port=8080)
