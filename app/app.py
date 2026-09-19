from flask import Flask

app = Flask(__name__)

style = """
<style>
body { background-color: #1a1a2e; color: #eee; font-family: Arial; text-align: center; padding-top: 50px; }
nav { margin-top: 20px; }
nav a { color: #8ecae6; margin: 0 15px; text-decoration: none; font-weight: bold; }
nav a:hover { text-decoration: underline; }
</style>
"""

nav = """
<nav>
    <a href="/">Início</a>
    <a href="/sobre">Sobre</a>
    <a href="/contato">Contato</a>
</nav>
"""


@app.route('/')
def home():
    return f"""
    <html>
    <head><title>Início</title>{style}</head>
    <body>
        <h1>Bem-vindo ao Flask no Docker</h1>
        <p>[Gustavo Alves e Maria Júllia Mello]</p>
        {nav}
    </body>
    </html>
    """


@app.route('/sobre')
def sobre():
    return f"""
    <html>
    <head><title>Sobre</title>{style}</head>
    <body>
        <h1>Sobre este projeto</h1>
        <p>Trabalho de Redes e Administração de Sistemas - Docker + Flask.</p>
        {nav}
    </body>
    </html>
    """


@app.route('/contato')
def contato():
    return f"""
    <html>
    <head><title>Contato</title>{style}</head>
    <body>
        <h1>Contato</h1>
        <p>IFSP - Campus Campos do Jordão</p>
        {nav}
    </body>
    </html>
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
