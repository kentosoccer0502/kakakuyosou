from flask import Flask, render_template, request, jsonify


class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(
        dict(
            variable_start_string = "%%",
            variable_end_string = "%%",
        )
    )

app = CustomFlask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)