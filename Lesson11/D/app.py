from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/<filename>", methods=["GET"])
def get_file(filename: str):
    return app.send_static_file(filename)


@app.route("/convert_celsius_to_fahrenheit")
def convert_celsius_to_fahrenheit():
    celsius = str(request.args.get("celsius"))

    # --- Validate a number ---
    if not re.match(r"^\d+$", celsius) and not re.match(r"^\d+.\d+$", celsius):
        return {"celsius": "NOT A NUMBER", "fahrenheit": "ERROR"}

    # --- Convert C to F ---
    fahrenheit = float(celsius) * 9/5 + 32
    return {"celsius": celsius, "fahrenheit": f"{fahrenheit:.2f}"}


@app.route("/", methods=["GET"])
def main():
    return render_template("index.html", title="L11 Exercise D")

app.run(debug=True, host="0.0.0.0", port=8080)
