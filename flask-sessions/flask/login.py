from flask import Flask, render_template, request


app = Flask(__name__)

employees= [
    {"empid":1001,"name":"Alice","dept":"Finance"},
     {"empid":1002,"name":"Bob","dept":"Operations"},
     {"empid":1003,"name":"Charlie","dept":"Operations"},
      {"empid":1004,"name":"David","dept":"Quality"},
       {"empid":1005,"name":"Eiffel","dept":"Finance"}

]

@app.route("/display")
def display():
    return render_template("display.html", employees =employees)

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/save", methods=['POST'])
def saveEmployee():
    emp = request.get_json()
    employees.append(emp)
    return "Success"
    


@app.route("/validate")
def validate():
    username = request.args.get('lid')
    password = request.args.get('pwd')
    if username == "admin" and password == "12345":
        return render_template('success.html', username=username)
    else:
        return render_template("fail.html", username=username)


if __name__ == '__main__':
    app.run(debug=True)