from flask import Flask, request, render_template
from sklearn import linear_model
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn import svm


app = Flask(__name__, static_url_path='')

input_map = [[10, 0, 1, 8], [10, 0, 2, 9], [10, 1, 1, 13], [5, 0, 1, 15], [5, 1, 5, 16], [5, 1, 6, 18]]
output_status = [8, 7, 5, 6, 9, 9]

linear = linear_model.LinearRegression()
poly = make_pipeline(PolynomialFeatures(2), linear)
# clf = svm.SVC(gamma=0.001, C=100.)

@app.route('/')
def root():
    return render_template('index.html')



@app.route('/train', methods=['GET'])
def train():

    global input_map
    global output_status

    roadid = int(request.args.get('roadid'))
    direction = int(request.args.get('direction'))
    day = int(request.args.get('day'))
    time = int(request.args.get('time'))
    status = int(request.args.get('status'))

    input = [roadid, direction, day, time]
    output = status

    input_map.append(input)
    output_status.append(output)

    print input_map
    print output_status

    poly.fit(input_map, output_status)

    return render_template('index.html')

@app.route('/predict')
def predict():

    roadid = int(request.args.get('roadid'))
    direction = int(request.args.get('direction'))
    day = int(request.args.get('day'))
    time = int(request.args.get('time'))


    return str(poly.predict([ [roadid, direction, day, time] ]))

if __name__ == '__main__':
	app.run(host='0.0.0.0')
