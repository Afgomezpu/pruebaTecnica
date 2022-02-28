from conects import conect
from flask import Flask, jsonify,request,Response,render_template,Blueprint
from bson import json_util
from bson.json_util import loads, dumps
from bson.objectid import ObjectId
from flask_cors import CORS, cross_origin
from sqlalchemy import create_engine
from ..models.user  import User

#Metodo para identificar si un numero ingresado es primo
def number_prime(number):
    number_mod = 0
    for n in range(1,number):
        if number % n == 0:
            number_mod += 1
    if number_mod==0 or number_mod==1:
        return True
    return False

blueprint = Blueprint('views', __name__)

#Ruta para ingresar en la base de datos prostgres un usuario 
@blueprint.route('/set-data', methods=['PUT'])
def set_data():
    # try:
        user = request.json['user']
        pw = request.json['pw']
        object_user = User(username=user,pw_hash=pw)
        conect.session.add(object_user)
        conect.session.commit()
        return jsonify({"user": "Usuario ingresado"})
    # except:
    #     return jsonify({"Error": "El usuario no fue ingresado"})


#Devuelve las lista de los numeros primos hasta el numero ingresado
@blueprint.route('/get-prime-numbers', methods=['GET'])
def numeros():
    try: 
        number_str = request.json['numero']
        number_whole = int(number_str)
        list_number_primes=[]
        for number in range(1,number_whole+1):
            is_prime = number_prime(number)
            if is_prime:
                list_number_primes.append(number)
        return jsonify({"Numeros primos": list_number_primes})
    except:
        return jsonify({"Error": "Ingrese un numero correcto"})

#Convierte la altura en pulgadas en metros
@blueprint.route('/convert-height', methods=['POST'])
def convert_height():
    try:
        name = request.json['name']
        height = round((int(request.json['height'].split(" ")[0])) * 0.0254,2)
        return jsonify({ "name": name ,"height" : str(height) + " metros"})
    except:
        return jsonify({ "Error" : "No se puede convertir la altura"})
    

