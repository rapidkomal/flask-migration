from config import db


class NewStdData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    department = db.Column(db.String(255), nullable=False)
    std_id = db.Column(db.String(255), nullable=False)
    std_id_test = db.Column(db.String(255), nullable=False)
    def __repr__(self):
        return f'<Std: {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'department': self.department
        }

class NewStdData2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    department = db.Column(db.String(255), nullable=False)
    def __repr__(self):
        return f'<Std: {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'department': self.department
        }