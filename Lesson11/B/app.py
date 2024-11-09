from flask import Flask, render_template, request
import requests


app = Flask(__name__)


@app.route("/", methods=["GET"])
def main():
    return render_template("index.html", title="L11 Exercise B")


@app.route("/check_tld")
def check_tld():
    url = request.args.get('url')
    tld = url.split(".")[-1]
    try:
        resp = requests.get(url = "https://data.iana.org/TLD/tlds-alpha-by-domain.txt", timeout=3)
        if resp.status_code != 200:
            raise requests.exceptions.RequestException
        tlds = resp.text.splitlines()
        if tld.upper() not in tlds:
            return {"valid": "INVALID URL FORMAT"}
    except requests.exceptions.RequestException:
        return {"valid": "INVALID URL FORMAT"}
    return {"valid": "VALID"}

@app.route("/check_url")
def get_url():
    url = request.args.get('url')
    try:
        resp = requests.get(f"http://{url.strip('http://')}", timeout=1)
        if resp.status_code == 200:
            return {"status": "Alive"}
    except requests.exceptions.RequestException:
        return {"status": "Unreachable"}


@app.route("/<filename>", methods=["GET"])
def get_file(filename: str):
    return app.send_static_file(filename)


app.run(host="0.0.0.0", debug=True, port=8080)
