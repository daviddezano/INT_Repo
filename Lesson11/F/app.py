import os.path
import re
import os
from flask import Flask, render_template, request

if not os.path.isfile("feedback.log"):
    open("feedback.log", "a").close()

app = Flask(__name__)

@app.route("/<filename>", methods=["GET"])
def get_file(filename: str):
    return app.send_static_file(filename)


@app.route("/validate_email")
def validate_email():
    email_addr = request.args.get("email").strip()
    email_regex = r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z]{2,}$' # Very shallow validation. to tld validation.
    valid_not_valid = "VALID" if re.match(email_regex, email_addr) is not None else "NOT VALID"
    return {"status": f"Email is {valid_not_valid}"}


@app.route("/log_feedback")
def log_feedback():
    user_name = request.args.get("user")
    email = request.args.get("email")
    feedback = request.args.get("feedback")

    if feedback.strip():
        with open("feedback.log", "a") as f:
            f.write(f"[{user_name}] [{email}]:  [{feedback}]\n")
    return {"status": "Ok"}


@app.route("/", methods=["GET"])
def main():
    return render_template("index.html", title="L11 Exercise E")

app.run(debug=True, host="0.0.0.0", port=8080)
