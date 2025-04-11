from flask import Flask 
# inicialização
app = Flask(__name__) ## Apenas para o flask se organizar

# rotas
@app.route("/") # criação da rota principal, por padrão ela vem com método 

def ola_mundo(): # função que aparece ao entrar na página
    return 'tudo bão?'

# execução
app.run(debug = True) ## Para o Flask entender que estamos no modo de desenvolvedor; a porta padrão irá ser a 5000