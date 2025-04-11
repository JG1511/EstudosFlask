from flask import Flask 
# inicialização
app = Flask(__name__) ## Apenas para o flask se organizar

# rotas
@app.route("/") # criação da rota principal, por padrão ela vem com método 

def ola_mundo(): # função que aparece ao entrar na página
    return 'tudo bão?'
@app.route("/sobre")

def sobre_o_criador():
    return 'Meu nome é João Guilherme e eu tenho 19 anos'

# execução
app.run(debug = True) ## Para o Flask entender que estamos no modo de desenvolvedor; a porta padrão irá ser a 5000