from flask import Flask,Blueprint, request, url_for
from EjerciciosFlask.Ej12_Pseu import principal
app = Flask(__name__)

appEj12= Blueprint('appEj12',__name__,static_folder='static', template_folder='template' )

@appEj12.route("/appEj12")

def home():
    
    return f"""
        <html>
        <body>
            <h1>Numero Primo</h1>
            <form method="post" action="/vej12">
                <label for="numero">Numero:</label>
                <input type="number" name="primo" id="primo">
                <br>
                <input type="button" value="Volver" onclick="history.back(-1)" /> 
                <input type="submit" value="Entrar">
            </form>
        </body>
        </html>
    """
@appEj12.route('/vej12', methods=['POST'])

def vej12():
    primo=request.form["primo"]
    resultado= principal(primo)
    return f"""
        <html>
        <body>
            <h1>Numero Primo</h1>
            <p>{resultado}</p>
            <input type="button" value="Volver" onclick="history.back(-1)" /> 
        </body>
        </html>
    """


if __name__ == '__main__':
   app.run(debug=True)