from flask import jsonify, request,Blueprint,session, redirect
import requests
from . import api
from models import Todo, db, Myuser


@api.route('/todos', methods=['GET','POST','DELETE','PUT'])
def todos():
    userid = session.get('userid')
    data = request.get_json()
    
    if request.method == 'POST':   #POST - 할일을 생성할때의 메서드
        todo=Todo()
        todo.title = data.get('title')
        myuser = Myuser.query.filter_by(userid=userid).first()
        todo.myuser_id = myuser.id
        todo.due = data.get('due')
        todo.status = 0
        db.session.add(todo)
        
        
    # elif request.method == 'GET':
    #     todo = Todo.query.filter_by(myuser_id=userid)
    #     return jsonify([t.serialize for t in todos])

    elif request.method == 'DELETE':
        todo_id = data.get('todo_id')
        todo = Todo.query.filter_by(id=todo_id).first()
        db.session.delete(todo)
        
        return jsonify(), 203


    elif request.method == 'PUT':
        userid = session.get('userid',None)
        data = request.get_json()
        todo_id = data.get('todo_id')
        todo = Todo.query.filter_by(id=todo_id).first()
        myuser = Myuser.query.filter_by(userid=userid).first()
        todo.status = 1
        db.session.commit()

        return jsonify()



    db.session.commit()
    return jsonify(data)

