import csv
import os
from flask import Flask, render_template, url_for, request, redirect
from dotenv import load_dotenv
import google.generativeai as genai
import markdown  # para converter markdown para HTML

load_dotenv()  # Carrega variáveis do .env

app = Flask(__name__)

# Ativa o modo debug se a variável de ambiente FLASK_DEBUG estiver como 'True'
os.environ['FLASK_DEBUG'] = 'True'
app.debug = os.environ.get('FLASK_DEBUG') == 'True'


# Página inicial
@app.route('/')
def home():
    return render_template('inicio.html')


# Página do glossário
@app.route('/glossario')
def index():
    glossario_de_termos = []
    if os.path.exists('bd_glossario.csv'):
        with open('bd_glossario.csv', newline='', encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo, delimiter=';')
            for linha in reader:
                glossario_de_termos.append(linha)
    return render_template('glossario.html', glossario_de_termos=glossario_de_termos)


# Página da equipe
@app.route('/sobre-equipe')
def sobre_equipe():
    return render_template('sobre_equipe.html')


# Tópicos de conteúdo
@app.route('/estruturas-selecao')
def estruturas_selecao():
    return render_template('estruturas_selecao.html')


@app.route('/estruturas-repeticao')
def estruturas_repeticao():
    return render_template('estruturas_repeticao.html')


@app.route('/vetores-matrizes')
def vetores_matrizes():
    return render_template('vetores_matrizes.html')


@app.route('/funcoes-procedimentos')
def funcoes_procedimentos():
    return render_template('funcoes_procedimentos.html')


@app.route('/tratamentos-excecao')
def tratamentos_excecao():
    return render_template('tratamentos_excecao.html')


# Página para tirar dúvidas (API Gemini)
@app.route('/tirar-duvidas', methods=['GET', 'POST'])
def tirar_duvidas():
    resposta_html = None
    if request.method == 'POST':
        pergunta = request.form.get('pergunta')
        api_key = os.getenv('GEMINI_API_KEY')

        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('models/gemini-1.5-flash')
            response = model.generate_content(pergunta)
            texto_markdown = response.text
            
            # Converte markdown para HTML (renderiza código, listas, negrito etc)
            resposta_html = markdown.markdown(texto_markdown, extensions=['fenced_code', 'tables'])
        
        except Exception as e:
            resposta_html = f"<p>Erro ao se comunicar com a API Gemini: {str(e)}</p>"

    return render_template('tirar_duvidas.html', resposta=resposta_html)


# Formulário para adicionar novo termo
@app.route('/novo_termo')
def novo_termo():
    return render_template('novo_termo.html')


# Rota para adicionar o termo ao CSV
@app.route('/criar_termo', methods=['POST'])
def criar_termo():
    termo = request.form.get('termo')
    definicao = request.form.get('definicao')

    if termo and definicao:
        with open('bd_glossario.csv', 'a', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo, delimiter=';')
            writer.writerow([termo, definicao])
        return redirect(url_for('index'))
    else:
        return "Erro: termo e definição devem ser preenchidos", 400


# Página com formulário de edição dos termos
@app.route('/editar_termo')
def editar_termo():
    termos = []
    if os.path.exists('bd_glossario.csv'):
        with open('bd_glossario.csv', newline='', encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo, delimiter=';')
            for linha in reader:
                termos.append(linha)
    return render_template('editar_termo.html', termos=termos)


# Página para deletar termos
@app.route('/deletar_termo')
def deletar_termo_page():
    termos = []
    if os.path.exists('bd_glossario.csv'):
        with open('bd_glossario.csv', newline='', encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo, delimiter=';')
            termos = list(reader)
    return render_template('deletar_termo.html', termos=termos)


# Rota POST para atualizar termo
@app.route('/atualizar_termo', methods=['POST'])
def atualizar_termo():
    termo_original = request.form.get('termo_original')
    novo_termo = request.form.get('novo_termo')
    nova_definicao = request.form.get('nova_definicao')
    termos_atualizados = []

    if os.path.exists('bd_glossario.csv'):
        with open('bd_glossario.csv', newline='', encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo, delimiter=';')
            for linha in reader:
                if linha[0] == termo_original:
                    termos_atualizados.append([novo_termo, nova_definicao])
                else:
                    termos_atualizados.append(linha)

        with open('bd_glossario.csv', 'w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo, delimiter=';')
            writer.writerows(termos_atualizados)

    return redirect(url_for('deletar_termo_page'))


# Rota POST para deletar termo
@app.route('/deletar_termo', methods=['POST'])
def deletar_termo():
    termo = request.form.get('termo')
    termos_atualizados = []

    if termo and os.path.exists('bd_glossario.csv'):
        with open('bd_glossario.csv', newline='', encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo, delimiter=';')
            for linha in reader:
                if linha[0] != termo:
                    termos_atualizados.append(linha)

        with open('bd_glossario.csv', 'w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo, delimiter=';')
            writer.writerows(termos_atualizados)

    return redirect(url_for('deletar_termo_page'))


if __name__ == '__main__':
    app.run()
