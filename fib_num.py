from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/fibnum/<string:num>")

def fibnum(num):
    n = int(num)
    a = 0
    b = 1
    while a <= n:
        if n ==a:
            data = {
                "number": n,
                "isFibnum": True,
                "username": "John"
            }
            return jsonify(data)
        a, b = b, a + b
    data2 = {
        "number": n,
        "isFibnum": False,
        "username": "Smith"
    }
    return jsonify(data2)

if __name__ == "__main__":
    app.run(debug=True)
