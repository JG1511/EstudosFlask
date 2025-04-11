from flask import Flask, url_for, render_template
# o url_for serve para montar urls internas do nosso servidor 
# render_template serve para buscar um arquivo para o html ou até mesmo para comunicação do back e o front

# inicialização
app = Flask(__name__) ## Apenas para o flask se organizar

# rotas
@app.route("/") # criação da rota principal, por padrão ela vem com método 

def ola_mundo(): # função que aparece ao entrar na página
    titulo = "Gestão de Usuários"
    usuarios = [
        {"nome":"João", "membro_ativo": True},
        {"nome":"Lucas", "membro_ativo": False},
        {"nome":"Jorge", "membro_ativo": False}
    ]
    return render_template('index.html')

@app.route("/sobre")

def sobre_o_criador():
    return 'Meu nome é João Guilherme e eu tenho 19 anos'

# execução
app.run(debug = True) ## Para o Flask entender que estamos no modo de desenvolvedor; a porta padrão irá ser a 5000