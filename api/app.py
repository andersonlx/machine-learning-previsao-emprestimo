import pickle
import numpy as np
import os

from flask import Flask, request, render_template, make_response

from sklearn import preprocessing
from sklearn.preprocessing import binarize, LabelEncoder, MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn import linear_model

#from sklearn.utils.deprecation import deprecated

app = Flask(__name__, static_url_path='/static')
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

#arquivo = "model/modelo.pkl"
#with open(arquivo, "rb") as f:
#    model = pickle.load(f)

model = pickle.load(open("model/modelo.pkl", "rb"))


@app.route("/")
def display_gui():
    return render_template("template.html")


@app.route("/verificar", methods=["POST"])
def verificar():
    sexo = request.form['gridRadiosSexo']
    dependentes = request.form['dependentes']
    casado = request.form['gridRadiosCasado']
    trabalho_conta_propria = request.form['gridRadiosTrabalhoProprio']
    rendimento = request.form['rendimento']
    educacao = request.form['educacao']
    valoremprestimo = request.form['valoremprestimo']
    teste = np.array([[
        sexo, casado, dependentes, educacao, trabalho_conta_propria,
        rendimento, valoremprestimo
    ]])

    print(":::::: Dados de Teste ::::::")
    print("Sexo: {}".format(sexo))
    print("Numero de Dependentes: {}".format(dependentes))
    print("Casado: {}".format(casado))
    print("Educacao: {}".format(educacao))
    print("Trabalha por conta propria: {}".format(trabalho_conta_propria))
    print("Rendimento: {}".format(rendimento))
    print("Valor do emprestimo: {}".format(valoremprestimo))
    print("\n")

    classe = model.predict(teste)[0]
    print("Classe Predita: {}".format(str(classe)))

    return render_template('template.html', classe=str(classe))


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)