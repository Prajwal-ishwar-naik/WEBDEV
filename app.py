from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/loly")
def lolypop():
    return render_template("lolypop.htm")

@app.route("/order")
def order_page():
    return render_template("order.html")

@app.route("/place-order", methods=["POST"])
def place_order():
    name = request.form["name"]
    item = request.form["item"]
    return f"<h1 style='color:green'>🍭 Order placed by <b>{name}</b> for <b>{item}</b>!</h1><br><a href='/'>Back to Home</a>"

if __name__ == "__main__":
    app.run(debug=True)
