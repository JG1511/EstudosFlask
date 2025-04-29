from flask import Blueprint, render_template, request
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
    return render_template('lista_cliente.html', clientes = CLIENTE)


@cliente_route.route('/', methods = ['POST'])
def inserir_clientes():
    
    data = request.json ## vai receber a requisição do front-end

    novo_cliente = {
        "id" : len(CLIENTE) + 1, # nesse caso, irá pegar o tamanho da lista/ID e adicionar + 1
        "nome" : data['nome'],
        "email" : data['email']
    }

    CLIENTE.append(novo_cliente)# Adiciona o novo cliente na lista

    return render_template('item_cliente.html', cliente = novo_cliente)

@cliente_route.route('/new')
def form_clientes():
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_clientes(cliente_id):
    pass

@cliente_route.route('/<int:cliente_id>/edit')
def form_editar_clientes(cliente_id):
    pass

@cliente_route.route('/<int:cliente_id>/update', methods = ['PUT'])
def atualizar_clientes(cliente_id):
    pass

@cliente_route.route('/<int:cliente_id>/delete', methods = ['DELETE'])
def deletar_clientes(cliente_id):
    global CLIENTE # para poder modificar 
    CLIENTE = [ cliente for cliente in CLIENTE if cliente['id'] != cliente_id]