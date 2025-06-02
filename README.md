# Projeto_Flask

Este projeto é um site educacional feito com Flask, voltado ao ensino dos Fundamentos da Programação em Python. Ele apresenta um glossário interativo, páginas com conteúdo explicativo e uma seção de dúvidas com IA.

## 📁 Estrutura do Site

- **Página Inicial**: Apresenta o objetivo do projeto.
- **/glossario**: Lista de termos em Python com definições do `glossario.csv`.
- **/novo_termo**: Adiciona novos termos via formulário.
- **/tirar_duvidas**: Campo para perguntas com resposta via API Gemini.
- **/tratamentos_excecao** e **/vetores_matrizes**: Conteúdo teórico.
- **/sobre_equipe**: Informações sobre o autor.

## ⚙️ Tecnologias Utilizadas

- **Python 3**, **Flask**
- Bibliotecas: `flask`, `csv`, `dotenv`, `os`, `google.generativeai`
- Front-end com HTML5 e CSS3

## 🤖 Integração com API Gemini

A API do Gemini foi integrada via biblioteca `google.generativeai`. A chave é armazenada em `.env`. O modelo `gemini-pro` é usado na rota `/tirar_duvidas` para gerar respostas em tempo real às perguntas dos usuários.

## 🚀 Executando o Projeto Localmente

1. Clone o repositório:
2. Crie o ambiente virtual e ative:
3. Instale as dependências:
4. Crie um arquivo `.env` com sua chave:
5. Inicie a aplicação:
6. Acesse em:`http://127.0.0.1:5000`

## 🔍 Principais Arquivos

- `app.py`: Código principal com rotas e lógica da aplicação.
- `templates/`: Arquivos HTML.
- `glossario.csv`: Base com os termos.
- `.env`: Armazena a chave da API.


## 🎥 Apresentação do Projeto

Assista à demonstração do funcionamento do site clicando no link abaixo:

👉 [Ver vídeo da apresentação no Google Drive]([https://drive.google.com/SEU-LINK-AQUI](https://drive.google.com/file/d/1iaTD81m8Q23x13XzcC6UgJcc2BoO6Wkd/view?usp=sharing))

---

Obrigado por visitar!


