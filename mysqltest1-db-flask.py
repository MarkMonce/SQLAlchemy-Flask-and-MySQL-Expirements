from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Naples727575!!@127.0.0.1:3306/payroll'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



# Define a model corresponding to the 'example_table'
class ExampleTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

# Initialize the database
# @app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    # Query all records from ExampleTable
    results = ExampleTable.query.all()
    return '\n'.join([f'{row.id}: {row.name}' for row in results])

if __name__ == '__main__':
    app.run(debug=True)