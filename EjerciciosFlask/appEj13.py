from flask import Flask,Blueprint, request, url_for
from Ej13_Pseu import principal
app = Flask(__name__)

appEj13= Blueprint('appEj13',__name__,static_folder='static', template_folder='template' )

@appEj13.route("/appEj13")

def home():
    
    return f"""
        <html>
        <body>
            <h1>Volumen y Area de un cubo</h1>
            <form method="post" action="/vej13">
                <label for="numero">Lado del cubo:</label>
                <input type="number" name="lado" id="lado">
                <br>

                <input type="button" value="Volver" onclick="history.back(-1)" />    
                <input type="submit" value="Entrar">
                
            </form>
        </body>
        </html>
    """
@appEj13.route('/vej13', methods=['POST'])

def vej13():
    lado=request.form["lado"]
    resultado= principal(lado)
    return f"""
        <html>
        <body>
            <h1>Volumen y Area de un cubo</h1>
            <p>{resultado}</p>
            <input type="button" value="Volver" onclick="history.back(-1)" />
        </body>
        </html>
    """


if __name__ == '__main__':
   app.run(debug=True)