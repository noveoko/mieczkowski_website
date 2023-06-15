import os
import click
import random
from pydantic import BaseModel, Field, ValidationError
from flask import Flask, render_template, flash, redirect, url_for, request, jsonify
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from wtforms import StringField, SelectField, RadioField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from config import Config
from forms.samonosne_form import SamonosneStairsForm
from forms.beton_form import BetonStairsForm
from utils.products import products as image_links
from collections import defaultdict

app = Flask(__name__)


def filter_valid_images(products):
    for category in products:
        for product in products[category]:
            images = [img for img in product["images"] if os.path.isfile(os.path.join(app.root_path, 'static', img))]
            if len(images) >= 1:
                product["images"] = images
    return products


image_links = filter_valid_images(image_links)

app.config.from_object(Config)

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=5)


class UserLogin(BaseModel):
    username: str
    password: str


@app.cli.command("create-user")
@click.argument("username")
@click.argument("password")
def create_user(username, password):
    password_hash = generate_password_hash(password, method='sha256')
    new_user = User(username=username, password=password_hash)

    existing_user = User.query.filter_by(username=username).first()
    if existing_user is None:
        db.session.add(new_user)
        db.session.commit()
        click.echo(f"User {username} has been created successfully.")
    else:
        click.echo(f"User {username} already exists.")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login', methods=['POST'])
def login():
    try:
        login_data = UserLogin(**request.json)
        user = User.query.filter_by(username=login_data.username).first()
        if user and user.check_password(login_data.password):
            login_user(user)
            return redirect(url_for('protected'))
        else:
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))
    except ValidationError as e:
        return jsonify(e.errors()), 400


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged out'


@app.route('/create_user', methods=['POST'])
def create_new_user():
    try:
        user_data = UserCreate(**request.json)
        user = User(username=user_data.username)
        user.set_password(user_data.password)
        db.session.add(user)
        db.session.commit()
        return f'User {user_data.username} created successfully.'
    except ValidationError as e:
        return jsonify(e.errors()), 400


@app.route('/protected')
@login_required
def protected():
    return f'Logged in as: {current_user.username}'


@app.route('/product/<category>/<product_name>')
def product_page(category, product_name):
    product_info = image_links[category][product_name]
    form = None
    if category == 'samonosne':
        form = SamonosneStairsForm()
    elif category == 'beton':
        form = BetonStairsForm()
    return render_template('product.html', category=category, product_name=product_name, product_info=product_info,
                           form=form)


@app.route('/products/<category>')
def category_page(category):
    products = defaultdict(list)
    for prod in image_links[category]:
        products[prod['type']].append(prod)
    return render_template('products.html', products=products, category=category)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
