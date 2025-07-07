from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.json
    try:
        op1 = float(data.get('op1', 0))
        op2 = float(data.get('op2', 0))
        operacion = data.get('operacion')
        resultado = None
        if operacion == '+':
            resultado = op1 + op2
        elif operacion == '-':
            resultado = op1 - op2
        elif operacion == '*':
            resultado = op1 * op2
        elif operacion == '/':
            resultado = 'Error' if op2 == 0 else op1 / op2
        else:
            return jsonify({'error': 'Operación no soportada'}), 400
        return jsonify({'resultado': resultado})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)


   # Cambio para disparar el pipeline intento2
