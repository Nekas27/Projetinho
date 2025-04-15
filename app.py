from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculadora():
    resultado = None
    if request.method == 'POST':
        try:
            # Pegando os valores dos inputs
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operacao = request.form['operacao']
            
            # Realizando o cálculo
            if operacao == 'soma':
                resultado = num1 + num2
            elif operacao == 'subtracao':
                resultado = num1 - num2
            elif operacao == 'multiplicacao':
                resultado = num1 * num2
            elif operacao == 'divisao':
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    resultado = "Erro: Divisão por zero"
            else:
                resultado = "Operação inválida"
        except ValueError:
            resultado = "Erro: Insira números válidos"

    return render_template_string("""
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Calculadora</title>
        </head>
        <body>
            <h1>Calculadora Simples</h1>
            <form method="POST">
                <label for="num1">Número 1:</label>
                <input type="text" id="num1" name="num1" required><br><br>

                <label for="num2">Número 2:</label>
                <input type="text" id="num2" name="num2" required><br><br>

                <label for="operacao">Operação:</label>
                <select id="operacao" name="operacao">
                    <option value="soma">Soma</option>
                    <option value="subtracao">Subtração</option>
                    <option value="multiplicacao">Multiplicação</option>
                    <option value="divisao">Divisão</option>
                </select><br><br>

                <button type="submit">Calcular</button>
            </form>
            {% if resultado is not none %}
                <h2>Resultado: {{ resultado }}</h2>
            {% endif %}
        </body>
        </html>
    """, resultado=resultado)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


