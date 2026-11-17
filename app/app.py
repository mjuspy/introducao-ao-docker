import os
import mysql.connector
from flask import Flask

app = Flask(__name__)

style = """
<style>
body { background-color: #1a1a2e; color: #eee; font-family: Arial; text-align: center; padding-top: 50px; }
nav { margin-top: 20px; }
nav a { color: #8ecae6; margin: 0 15px; text-decoration: none; font-weight: bold; }
nav a:hover { text-decoration: underline; }
ul { list-style: none; padding: 0; }
li { background-color: #16213e; margin: 8px auto; padding: 10px; width: 300px; border-radius: 6px; }
</style>
"""

nav = """
<nav>
    <a href="/">Inicio</a>
    <a href="/sobre">Sobre</a>
    <a href="/contato">Contato</a>
    <a href="/alunos">Alunos</a>
</nav>
"""


def conectar_banco():
    return mysql.connector.connect(
        host=os.environ["DB_HOST"],
        port=int(os.environ.get("DB_PORT", "3306")),
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"]
    )


@app.route("/")
def home():
    return f"""
    <html>
    <head><title>Inicio</title>{style}</head>
    <body>
        <h1>Bem-vindo ao Flask no Docker</h1>
        <p>[Gustavo Alves e Maria Jullia Mello]</p>
        {nav}
    </body>
    </html>
    """

@app.route("/sobre")
def sobre():
    return f"""
    <html>
    <head><title>Sobre</title>{style}</head>
    <body>
        <h1>Sobre este projeto</h1>
        <p>Trabalho de Redes e Administração de Sistemas - Docker + Docker Compose.</p>
        <p>Aplicação Flask integrada a um banco MySQL e servida por um proxy reverso Apache, em três containers orquestrados pelo Docker Compose.</p>
        {nav}
    </body>
    </html>
    """

@app.route("/contato")
def contato():
    return f"""
    <html>
    <head><title>Contato</title>{style}</head>
    <body>
        <h1>Contato</h1>
        <p>IFSP - Campus Campos do Jordao</p>
        {nav}
    </body>
    </html>
    """


@app.route("/alunos")
def alunos():
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)

    try:
        cursor.execute("SELECT id, nome FROM alunos ORDER BY id")
        registros = cursor.fetchall()

        itens = ""
        for aluno in registros:
            itens += f"<li>{aluno['id']} - {aluno['nome']}</li>"

        return f"""
        <html>
        <head><title>Alunos</title>{style}</head>
        <body>
            <h1>Alunos cadastrados no MySQL</h1>
            <ul>{itens}</ul>
            {nav}
        </body>
        </html>
        """

    finally:
        cursor.close()
        conexao.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
