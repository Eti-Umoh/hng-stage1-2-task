import os
from flask import Flask,jsonify,request
from enum import Enum
import openai 

app = Flask(__name__)

#THIS IS THE STAGE 1 TASK
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






#THIS IS THE STAGE 2 TASK ON THE SAME SERVER
class Operators(Enum):
    addition = '+'
    subtraction = '-'
    multiplication = '*'

@app.route('/returnresponse',methods=['POST'])
def return_response():

    body = request.json
    x = body.get('x')
    y = body.get('y')
    operation_type = body.get('operation_type')

    if operation_type == Operators.addition.name:
        result = x+y
        operation_type_value =  Operators.addition.value

    elif operation_type == Operators.subtraction.name:
        result = x-y
        operation_type_value =  Operators.subtraction.value

    elif operation_type == Operators.multiplication.name:
        result = x*y
        operation_type_value =  Operators.multiplication.value

    else:
        openai.api_key = ("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")

        response = openai.Completion.create(engine = "text-davinci-002",prompt = operation_type,
                    temperature = 0,max_tokens = 200,top_p = 1,frequency_penalty = 0,presence_penalty = 0
                    )
        result = (response.choices[0].text)
        response2 = openai.Completion.create(engine = "text-davinci-002",prompt = f"Only tell me the operation type carried out in this mathematical operation, Do not tell me the answer/n/n{operation_type}",
                    temperature = 0,max_tokens = 200,top_p = 1,frequency_penalty = 0,presence_penalty = 0
                    )
        operation_type_value = (response2.choices[0].text)
    
    data = {"slackUsername":"MrMorale",
        "operation_type":operation_type_value,
        "result":result
        }

    return jsonify(data)

if __name__=="__main__":
    app.run(debug=True)