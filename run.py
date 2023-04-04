from config import app, db
from flask import request, jsonify
from app import NewStdData2

@app.route('/student', methods=['POST'])
def create_std():
    name = request.form.get('name')
    age = request.form.get('age')
    department = request.form.get('department')

    new_std = NewStdData2(name=name, age=age, department=department)
    db.session.add(new_std)
    db.session.commit()
    return jsonify({'message': 'Student data created successfully.'}), 201

@app.route('/student/<id>', methods=['PUT'])
def update(id):
    std_to_update = NewStdData2.query.filter_by(id=id).first()   
    if std_to_update:
        if 'name' in request.form.to_dict().keys():
            std_to_update.name = request.form['name']
            
        if 'age' in request.form.to_dict().keys():
            std_to_update.age = request.form['age']
            
        if 'department' in request.form.to_dict().keys():
            std_to_update.department = request.form['department']   
    else :
        return jsonify({'message': 'Student Id not founded.'}), 202
   
    db.session.commit()
    return jsonify({'message': 'Student data updated successfully.'}), 201

@app.route('/student/<id>', methods=['DELETE'])
def delete(id):
    std_to_delete = NewStdData2.query.filter_by(id=id).first()
    db.session.delete(std_to_delete)
    db.session.commit()

    return jsonify({'message': 'Student data delete successfully.'}), 201


@app.route('/student', methods=['GET'])
def get_std():
    # Select all records
    all_stds = NewStdData2.query.all()
    for i in all_stds:
        print(i)
    stds = NewStdData2.query.all()
    std_list = [std.to_dict() for std in stds]
    # Select records with a certain condition
    # stds_with_department = NewStdData2.query.filter_by(department=department).all()

    # Select a single record
    # std = NewStdData2.query.filter_by(id=id).first()

    return jsonify({'message': 'Student data delete successfully.', 'data': std_list}), 201
    

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)