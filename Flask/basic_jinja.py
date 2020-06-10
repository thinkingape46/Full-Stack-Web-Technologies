from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    reader_name = "Jose"
    list_name = list(reader_name)
    return render_template('basic_jinja.html', reader_name = reader_name, list_name = list_name)

if __name__ == "__main__":
    app.run(debug=True)