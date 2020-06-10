from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    user_logged = False
    list_a = ["Hydrogen", "Helium", "Lithium"]
    return render_template('basic_template_flow.html', list_a = list_a, user_logged = user_logged, framework="flask")

if __name__ == "__main__":
    app.run(debug=True)