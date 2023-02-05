from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("chatpage.html")
@app.route("/result", methods = ['POST', "GET"])
def result():
    output = request.form.to_dict()
    name = output["name"]

    return render_template("chatpage.html", name = name)

    
if __name__ == '__main__':
    app.run(debug = True, port = 5001)