from crypt import methods
from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/returnjson',methods=['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        data = {
            "slackUsername":"Eti Umoh",
            "backend":True,
            "age":19,
            "bio":"I am a talented software enthusiast with extensive interest in the full life-cycle of software engineering, development, programming, support and implementation."
        }

        return jsonify(data)

if __name__=="__main__":
    app.run(debug=False)