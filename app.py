from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':

        num1 = request.form.get('num1', default=0, type=float)
        num2 = request.form.get('num2', default=0, type=float)
        operation = request.form.get('operation')

        if operation == 'add':
            result = num1 + num2
            operation_symbol = '+'
        elif operation == 'subtract':
            result = num1 - num2
            operation_symbol = '-'

        return f"""
            <h1>Wynik operacji: {num1} {operation_symbol} {num2} = {result}</h1>
            <a href="/">Powrót</a>
        """
    
    return """
        <form method="POST">
            <label for="num1">Liczba 1:</label>
            <input type="number" step="any" id="num1" name="num1" required>
            <br>
            <label for="num2">Liczba 2:</label>
            <input type="number" step="any" id="num2" name="num2" required>
            <br>
            <label for="operation">Operacja:</label>
            <select id="operation" name="operation">
                <option value="add">Dodawanie</option>
                <option value="subtract">Odejmowanie</option>
            </select>
            <br><br>
            <button type="submit">Oblicz</button>
        </form>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
