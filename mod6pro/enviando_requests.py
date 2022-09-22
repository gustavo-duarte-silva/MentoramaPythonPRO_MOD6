from requests import get, post

# Realizando o Calculo usando o Método POST
resp1 = post('http://127.0.0.1:5000/api', json={"valor1": 3, "valor2":3, "operacao":"multi"})
print('Utilizando o Método POST')
print(resp1.text)

print('---'*9)
# Realizando o Calculo usando o Método GET
resp2 = get('http://127.0.0.1:5000/sum/6/2')
print('Utilizando Metodo GET')
print(resp2.text)
