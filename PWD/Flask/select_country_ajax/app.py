from calendar import c
from flask import Flask, render_template, request, jsonify
from pytz import country_names

app = Flask(__name__)


# country_list = {
#     'india': ['guj', 'panjab', 'jammu'],
#     'USA': ['cupartono', 'lossanjalis', 'continatal']
# }


@app.route('/')
def load_login():
    return render_template("home.html")


@app.route('/validate_login')
def validate_login():
    country_id = request.args.get('countryId')
    print(country_id)

    # country_list = [
    #     {
    #         "country_id": 1,
    #         "state_list": ['Guj']
    #     },
    #     {
    #         "country_id": 2,
    #         "state_list": ['Cup', 'Loss']
    #     },
    # ]
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
        print("1 ----------> call")
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
