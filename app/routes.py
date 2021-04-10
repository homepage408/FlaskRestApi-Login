from app import app
from flask import request
from app.controller import userController


@app.route('/')
def index():
    return 'Hello Flask App API'


@app.route('/creatadmin', methods=['POST'])
def admins():
    return userController.buatAdmin()


@app.route('/login', methods=['POST'])
def login():
    return userController.login()