from flask import Flask, render_template, request
import re
app = Flask(__name__)

@app.route("/<filename>", methods=["GET"])
def get_file(filename: str):
    return app.send_static_file(filename)


@app.route("/count_words")
def validate_email():
    text = request.args.get("words")
    if not text:
        return {"status": 0}

    words = re.findall(r"([a-zA-Z]{2,})", text)
    return {"status": len(words)}


@app.route("/", methods=["GET"])
def main():
    return render_template("index.html", title="L11 Exercise J")

app.run(debug=True, host="0.0.0.0", port=8080)
