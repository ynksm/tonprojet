from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

@app.route("/", methods=["GET", "POST"])
def home():
    password = ""
    if request.method == "POST":
        length = int(request.form["length"])
        password = generate_password(length)
    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(host="192.168.0.16", port=5000, debug=True)