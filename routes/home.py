from flask import Blueprint,render_template # o Blueprint serve para o gerenciamento das rotas

home_route = Blueprint('home',__name__) # Criação de uma variável para armazenzar o blueprint/rota

@home_route.route('/') # criação da rota home
def home():
    return render_template('index.html')