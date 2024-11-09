from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<filename>", methods=["GET"])
def get_file(filename: str):
    return app.send_static_file(filename)


@app.route("/", methods=["GET"])
def main():
    return render_template("index.html", title="L11 Exercise A")

app.run(debug=True, host="0.0.0.0", port=8080)
