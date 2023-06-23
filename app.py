from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Engineer',
        'location': 'Bengaluru',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 3,
        'title': 'Data Infrastructure Manager',
        'location': 'Bengaluru'
    },
    {
        'id': 4,
        'title': 'Senior Data Analyst',
        'location': 'Bengaluru',
        'salary': 'Rs. 10,00,000'
    }
]

@app.route('/')
def hello_world():
    return render_template('test.html', jobs=JOBS)

@app.route('/jobs')
def json_response():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
