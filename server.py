from flask import Flask, request, jsonify

# https://stackoverflow.com/questions/10434599/how-to-get-data-received-in-flask-request
# http://flask.pocoo.org/docs/1.0/quickstart/#about-responses
# http://docs.python-requests.org/en/master/user/quickstart/

app = Flask(__name__)
ret = {}

def printit(msg,dict):
    if dict is not None:
        for k,v in dict.items():
            print(msg,k,v)

@app.route('/get', methods=['GET','POST'])
def doget(): # This is called view function

    print(request.method)
    printit('request.args',request.args)
    printit('request.form',request.form)
    printit('request.values',request.values) # values = args union form, if duplicate,args gets precedence
    printit('request.json',request.json) # values = args union form, if duplicate,args gets precedence

    if request.content_type == 'application/json':
        k = request.json
    else:
        k = request.values

    name = k['name']
    ret['name'] = f'{request.method} :' + name
    return jsonify(ret)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

