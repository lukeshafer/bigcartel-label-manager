from flask import Flask, request, abort, send_from_directory, render_template
from printLetter import printLetter

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    #return "hi"
    return render_template('index.html')


@app.route('/print/', methods=['POST'])
def print_labels():
    #if not request.form or not 'name' in request.form:
        #abort(400)

    if request.method == 'POST':
        print(request)
        #print(printLetter(request.form))
        return "hello world"
        #return send_from_directory(directory='./', filename='sample.pdf',mimetype='application/pdf')


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
