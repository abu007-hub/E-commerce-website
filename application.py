from flask import Flask, render_template

application = Flask(__name__)

@application.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

@application.route("/products", methods=["POST", "GET"])
def products():
    return render_template("products.html")

@application.route("/about", methods=["POST", "GET"])
def about():
    return render_template("about.html")

@application.route("/contact", methods=["POST", "GET"])
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    application.run(debug=True)
