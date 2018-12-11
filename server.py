from flask import Flask, request, jsonify

# https://stackoverflow.com/questions/10434599/how-to-get-data-received-in-flask-request
# http://flask.pocoo.org/docs/1.0/quickstart/#about-responses

app = Flask(__name__)
ret = {}


@app.route('/get', methods=['GET'])
def doget(): # This is called view function
    print(request.method)
    for k,v in request.args.items():
        print(k,v)
    name = request.args['name']
    ret['name'] = 'Received_via_get' + name
    return jsonify(ret)

@app.route('/get', methods=['POST'])
def dopost():
    print(request.method)
    for k,v in request.args.items():
        print(k,v)
    name = request.args['name']
    ret['name'] = 'Received_via_post' + name
    return jsonify(ret)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

