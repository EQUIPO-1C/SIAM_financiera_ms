from flask import Flask, request , jsonify, Response
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
import db

app= Flask(__name__)

@app.route('/')
def flask_mongodb_atlas():
    return "flask mongodb atlas!"

#test to insert data to the data base
@app.route("/test")
def test():
    db.db.recibos_col.insert_one({"name": "John"})
    return "Connected to the data base!"


@app.route("/financiera",methods=["POST"])
def create_recibo_pago():
    id_estudiante = request.json["id_estudiante"]
    semestre=  request.json["semestre"]
    valor_semestre=request.json["valor_semestre"]
    fecha_pago_oportuno=request.json["fecha_pago_oportuno"]
    estado_recibo= request.json ["estado_recibo"]
    programa=request.json["programa"]

    
    if id_estudiante and semestre and valor_semestre and fecha_pago_oportuno and estado_recibo and programa:
        id =  db.db.recibos_col.insert_one({
                "id_estudiante": id_estudiante,"semestre": semestre, "valor_semestre": valor_semestre, "fecha_pago_oportuno":fecha_pago_oportuno, "estado_recibo": estado_recibo, "programa":programa
            })
        response ={
            "id":str(id),
            "id_estudiante": id_estudiante,
            "semestre": semestre, 
            "valor_semestre": valor_semestre, 
            "fecha_pago_oportuno":fecha_pago_oportuno, 
            "estado_recibo": estado_recibo, 
            "programa":programa
        }
        return response
    else:
        return not_found()

    return{"message":"received"}

#Get all 
@app.route("/financiera", methods=["GET"])
def get_recibo_pago():
    Financiera =  db.db.recibos_col.find()
    response = json_util.dumps(Financiera)
    return Response(response, mimetype="application/json")

#Get all recibos with Specified ID
@app.route('/financiera/<id>', methods=['GET'])
def get_user(id):
    print(id)
    financiera2 =  db.db.recibos_col.find({ 'id_estudiante': id })
    response = json_util.dumps(financiera2)
    return Response(response, mimetype="application/json")

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404
    }
    response = jsonify(message)
    response.status_code = 404
    return response

#Delete with specified ID
@app.route('/financiera/<id>', methods=['DELETE'])
def delete_user(id):
    db.db.recibos_col.delete_one({'_id': ObjectId(id)})
    response = jsonify({'message': 'User' + id + ' Deleted Successfully'})
    response.status_code = 200
    return response

#Update with specified ID
@app.route('/financiera/<id>', methods=['PUT'])
def update_user(id):
    id_estudiante = request.json["id_estudiante"]
    semestre=  request.json["semestre"]
    valor_semestre=request.json["valor_semestre"]
    fecha_pago_oportuno=request.json["fecha_pago_oportuno"]
    estado_recibo= request.json ["estado_recibo"]
    programa=request.json["programa"]

    if id_estudiante and semestre and valor_semestre and fecha_pago_oportuno and estado_recibo and programa:
        db.db.recibos_col.update_one(
            {'_id': ObjectId(id['$oid']) if '$oid' in id else ObjectId(id)}, {'$set': {"id_estudiante": id_estudiante,"semestre": semestre, "valor_semestre": valor_semestre, "fecha_pago_oportuno":fecha_pago_oportuno, "estado_recibo": estado_recibo, "programa":programa}})
        response = jsonify({'message': 'User' + id + 'Updated Successfuly'})
        response.status_code = 200
        return response
    else:
      return not_found()


if __name__ == '__main__':
    app.run(port=8000, debug = true)
