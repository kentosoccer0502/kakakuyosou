from flask import Flask, render_template, request, jsonify
from predict_price import predict_price


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

@app.route('/predict', methods=['POST'])
def give_predicted_price():
    if request.method == 'POST':
        terms = request.get_json()
        room_size = terms['roomSize']
        distance = terms['distance']
        years = terms['years']
        area = terms['area']

        predicted_price = predict_price(room_size, distance, years, area)
        predicted_price_json = {'predicted_price': predicted_price}
        
        return jsonify(predicted_price_json)

if __name__ == '__main__':
    app.run(debug=True)