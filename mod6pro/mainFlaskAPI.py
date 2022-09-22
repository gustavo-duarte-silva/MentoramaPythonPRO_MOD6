from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def main_menu():
    return "<h2> Calculadora Modulo 6<h2>"

@app.route("/<operacao>/<int:valor1>/<int:valor2>")
def operacao_matematica(operacao, valor1, valor2):
    if operacao.lower() in ['div', 'divisao', 'divisão']:
        return f"A divisão entre {valor1} e {valor2} : {valor1/valor2}"
    if operacao.lower() in ['sum', 'soma']:
        return f"A Soma entre {valor1} e {valor2} : {valor1+valor2}"
    if operacao.lower() in ['mult', 'multi', 'multiplicacao', 'multiplicação']:
        return f"A Multiplicação entre {valor1} e {valor2} : {valor1*valor2}"
    if operacao.lower() in ['sub', 'subtracao', 'subtração']:
        return f"A Subtração entre {valor1} e {valor2} : {valor1-valor2}"

@app.route("/api", methods=["POST"])
def api():
    if request.method == "POST":
        json = request.get_json()
        valor1 = list(json.values())[0]
        valor2 = list(json.values())[1]
        if list(json.values())[2] in ['div', 'divisao', 'divisão']:
            return f"A divisão entre {valor1} e {valor2} : {valor1/valor2}"
        if list(json.values())[2] in ['sum', 'soma']:
            return f"A Soma entre {valor1} e {valor2} : {valor1+valor2}"
        if list(json.values())[2] in ['mult', 'multi', 'multiplicacao', 'multiplicação']:
            return f"A Multiplicação entre {valor1} e {valor2} : {valor1*valor2}"
        if list(json.values())[2] in ['sub', 'subtracao', 'subtração']:
            return f"A Subtração entre {valor1} e {valor2} : {valor1-valor2}"
    else:
        return "GET"

