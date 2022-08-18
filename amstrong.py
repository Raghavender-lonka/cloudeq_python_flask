from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")

def hello_world():
    return "Ashish choudhry"


@app.route("/Amstrong/<string:num>")

def armstrong(num):
    number = int(num)
    cube = 0
    for i in range(len(num)):
        cube1 = number % 10
        cube += cube1*cube1*cube1
        number = int(number/10)
        continue

    if int(num) == cube:
        data1={
            "username":"Ashish choudhry",
            "server id":"123.145.12.6",
            "number": cube,
            "Armstrong":True
        }
        return jsonify(data1)
    else:
        data1={
            "username":"Atul Bhist",
            "server id":"123.145.12.6",
            "number": cube,
            "Armstrong":False
        }
        return jsonify(data1)

if __name__=="__main__":

    app.run(debug=True)