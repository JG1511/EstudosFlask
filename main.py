from flask import Flask
from routes.home import home_route
# o url_for serve para montar urls internas do nosso servidor 
# render_template serve para buscar um arquivo para o html ou até mesmo para comunicação do back e o front

# inicialização
app = Flask(__name__) ## Apenas para o flask se organizar

app.register_blueprint(home_route)
# rotas

# execução
app.run(debug = True) ## Para o Flask entender que estamos no modo de desenvolvedor; a porta padrão irá ser a 5000