from flask import Flask, render_template, request, redirect, flash, url_for
import mysql.connector

app = Flask(__name__)

# Configuração do banco de dados MySQL
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '',
    'database': 'saep_db'
}

# Rota para a tela de login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Pegando os dados do formulário
        email = request.form['email']
        senha = request.form['senha']  # Corrigido para pegar a senha corretamente

        # Conectando no banco
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        # Verificando se o usuário existe
        query = "SELECT * FROM USUARIO WHERE EMAIL = %s AND SENHA = %s"
        cursor.execute(query, (email, senha))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user:
            return f"Login bem-sucedido! Bem-vindo, {user['NOME']}."
        else:
            return "Usuário ou senha incorretos."

    return render_template("login.html")

@app.route("/cadastro_peca", methods=["GET", "POST"])
def cadastro_peca():
    return render_template("cadastro_peca.html")

if __name__ == "__main__":
    app.run(debug=True)

