from flask import Flask, render_template
import requests
import random

app = Flask(__name__)


@app.route('/')
def inicio():
    id_sorteado = random.randint(1,1025)
    url_api = 'https://pokeapi.co/api/v2/pokemon-form/'+str(id_sorteado)
    response = requests.get(url_api)
    dados = response.json()
    print(dados.get("name"))

    sprites = dados.get("sprites", {})
    other = sprites.get("other",{})
    showdown = other.get("showdown",{})
    link_imagem = showdown.get("front_default")


    return render_template('index.html',numero=id_sorteado, nome=dados.get("name") ,imagem=link_imagem)

if __name__== '__main__':
    app.run(debug=True)