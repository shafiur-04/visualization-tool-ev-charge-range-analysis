from flask import Flask, render_template, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-key-change-in-production'

# Tableau embed configurations - UPDATED dashboard ID
TABLEAU_CONFIG = {
    'dashboard': {
        'id': 'viz1772730065683',  # Updated dashboard ID
        'name': 'ElectricCarAnalytics_17727194068140/Dashboard1',
        'static_image': 'https://public.tableau.com/static/images/El/ElectricCarAnalytics_17727194068140/Dashboard1/1.png',
        'width': '1230px',
        'height': '2727px'
    },
    'story': {
        'id': 'viz1772725294967',
        'name': 'ElectricCarandChargingStationinIndia/StoryofElectricCarinIndia',
        'static_image': 'https://public.tableau.com/static/images/El/ElectricCarandChargingStationinIndia/StoryofElectricCarinIndia/1.png',
        'width': '1016px',
        'height': '727px'
    }
}

@app.route('/')
def index():
    return render_template('index.html', tableau_config=TABLEAU_CONFIG)

@app.route('/api/tableau-config')
def get_tableau_config():
    return jsonify(TABLEAU_CONFIG)

if __name__ == '__main__':
    print("=" * 50)
    print("E-CarStart Flask App Starting...")
    print("Access the app at: http://localhost:5000")
    print("=" * 50)
    app.run(debug=True, host='127.0.0.1', port=5000)