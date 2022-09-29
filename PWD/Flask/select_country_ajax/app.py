from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def load_login():
    return render_template("home.html")


@app.route('/validate_login')
def validate_login():
    country_id = request.args.get('countryId')
    print(country_id)

    country = []
    if country_id == "1":
        country_list = [
            {
                "stateId": 1,
                "stateName": 'Guj'
            },
            {
                "stateId": 2,
                "stateName": 'Kol',
            },
        ]
        country.extend(country_list)
    if country_id == "2":
        country_list = [
            {
                "stateId": 1,
                "stateName": 'Loss'
            },
            {
                "stateId": 2,
                "stateName": 'Cup',
            },
        ]
        country.extend(country_list)
    print(country)
    return jsonify(country)


if __name__ == '__main__':
    app.run(debug=True)
