from flask import Flask, request, render_template, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SECRET_KEY'] = 'benji'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config['SQLALCHEMY_ECHO'] = False
app.app_context().push()

connect_db(app)


@app.route('/api/cupcakes')
def get_all_cupcakes():
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)

@app.route('/api/cupcakes/<int:cupcake_id>')
def get_one_cupcake(cupcake_id):
    selected_cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake = selected_cupcake.serialize())

@app.route('/api/cupcakes', methods = {'POST'})
def create_cupcake():
    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json.get('image', 'https://tinyurl.com/demo-cupcake')
    new_cupcake = Cupcake(flavor= flavor, size = size, rating = rating, image = image)
    db.session.add(new_cupcake)
    db.session.commit()
    response = jsonify(cupcake= new_cupcake.serialize())
    return (response, 201)

@app.route('/api/cupcakes/<int:cupcake_id>', methods = ['PATCH'])
def update_cupcake(cupcake_id):
    selected_cupcake = Cupcake.query.get_or_404(cupcake_id)
    flavor = request.json.get('flavor', selected_cupcake.flavor)
    size = request.json.get('size', selected_cupcake.size)
    rating = request.json.get('rating', selected_cupcake.rating )
    image = request.json.get('image', selected_cupcake.image)
    selected_cupcake.flavor = flavor
    selected_cupcake.size = size
    selected_cupcake.rating = rating
    selected_cupcake.image = image
    db.session.commit()
    response = jsonify(cupcake= selected_cupcake.serialize())
    return response

@app.route('/api/cupcakes/<int:cupcake_id>', methods= ['DELETE'])
def delete_cupcake(cupcake_id):
    Cupcake.query.filter_by(id=cupcake_id).delete()
    db.session.commit()
    return jsonify({"message": "Deleted"})


@app.route('/')
def homepage():
    return render_template('index.html')