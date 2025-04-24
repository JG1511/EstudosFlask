from flask import Blueprint, render_template
from database.cliente import CLIENTE

cliente_route = Blueprint('cliente',__name__)

"""
Base para criação das rotas de cliente

- /clientes/ (POST) - inserir o cliente no servidor
- /clientes/new (GET) - renderizar o formulario para criar um cliente
- /clientes/<id> (GET) - obter os dados do cliente
- /clientes/<id>/edit (GET) - renderizar o formulario para editar o cliente
- /clientes/<id>/update (PUT) - autualizar os dados do cliente
- /clientes/<id>/delete (DELETE) - deleta o registro do cliente



"""

@cliente_route.route('/')
def lista_clientes():
    return render_template('lista_cliente', clientes = CLIENTE)


@cliente_route.route('/', methods = ['POST'])
def inserir_clientes():
    pass

@cliente_route.route('/new')
def form_clientes():
    pass

@cliente_route.route('/<int:cliente_id>')
def detalhe_clientes():
    pass

@cliente_route.route('/<int:cliente_id>/edit')
def form_editar_clientes():
    pass

@cliente_route.route('/<int:cliente_id>/update', methods = ['PUT'])
def atualizar_clientes():
    pass

@cliente_route.route('/<int:cliente_id>/delete', methods = ['DELETE'])
def deletar_clientes():
    pass