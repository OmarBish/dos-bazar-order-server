from flask import redirect,request,jsonify
import requests


# local imports
from app import app

#TODO: redirct all unwanted routes to root dir
# index route, redirect to api dcumentation url
@app.route('/')
def index():
    return redirect('https://bazar2.docs.apiary.io')

#TODO: redirct all unwanted routes to root dir
# index route, redirect to api dcumentation url
@app.route('/operation/buy',methods=['POST'])
def buy():
    data = request.get_json()
    amount = data['amount']
    book_id = data['id']
    if(amount == 0):
        return jsonify() ,410
    
    newAmount = amount - 1
    sql_update_query = "UPDATE books SET amount = "+ str(newAmount) +" WHERE id = "+ str(book_id)

    req = {
        'sqlite_query':sql_update_query,
        'id':data['id']
    }
    result = requests.post('https://dos-bazar-catalog-master.herokuapp.com/query',json=req)
    # result = requests.post('http://127.0.0.1:5000/query',json=req)
    if result.status_code == 201:
        data['amount'] = newAmount
        return jsonify(data) ,200
    else:
        return jsonify() ,500

    

    
    