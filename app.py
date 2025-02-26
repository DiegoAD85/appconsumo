from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        try:
            km_por_litro = float(request.form['km_por_litro'])
            distancia_km = float(request.form['distancia_km'])
            valor_litro = float(request.form['valor_litro'])

            consumo_litros = distancia_km / km_por_litro
            custo_total = consumo_litros * valor_litro

            resultado = f"Consumo: {consumo_litros:.2f}L<br>Custo total: R$ {custo_total:.2f}"

        except ValueError:
            resultado = "Entrada inválida."

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
