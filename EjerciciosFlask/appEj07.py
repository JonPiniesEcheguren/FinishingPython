from flask import Flask,Blueprint, request, url_for
from Ej07_Pseu import principal
app = Flask(__name__)

appEj07= Blueprint('appEj07',__name__,static_folder='static', template_folder='template' )

@appEj07.route("/appEj07")

def home():
    
    return f"""
        <html>
        <body>
            <h1>Determinar si es Par o Impar</h1>
            <form method="post" action="/vej07">
                <label for="numero">Numero:</label>
                <input type="number" name="parimpar" id="parimpar">
                <br>
                <input type="button" value="Volver" onclick="history.back(-1)" /> 
                <input type="submit" value="Entrar">
            </form>
        </body>
        </html>
    """
@appEj07.route('/vej07', methods=['POST'])

def vej07():
    parimpar=request.form["parimpar"]
    resultado= principal(parimpar)
    return f"""
        <html>
        <body>
            <h1>Determinar si es Par o Impar</h1>
            <p>{resultado}</p>
            <input type="button" value="Volver" onclick="history.back(-1)" /> 
        </body>
        </html>
    """


if __name__ == '__main__':
   app.run(debug=True)