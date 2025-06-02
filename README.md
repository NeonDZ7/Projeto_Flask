# Projeto_Flask

Este é um site educacional desenvolvido com **Flask** com o objetivo de ensinar os **Fundamentos da Programação em Python**. A aplicação oferece uma interface interativa, glossário de termos, explicações sobre conceitos fundamentais e integração com a API do **Gemini**, permitindo tirar dúvidas automaticamente com base em inteligência artificial.

## 📁 Estrutura do Site

O site possui as seguintes seções principais:

- **Página Inicial (`/`)**  
  Introdução ao conteúdo do site, com links para as demais seções.

- **Glossário (`/glossario`)**  
  Mostra uma tabela interativa com os termos e definições presentes no arquivo CSV. Há também a opção de adicionar novos termos.

- **Adicionar Termo (`/novo_termo`)**  
  Permite ao usuário adicionar um novo termo e definição ao glossário.

- **Tirar Dúvidas (`/tirar_duvidas`)**  
  Seção onde o usuário escreve sua dúvida, que é enviada para a API do Gemini. A resposta é retornada e exibida na página.

- **Conteúdo de Aprendizado**  
  - `/tratamentos_excecao` – Explica como funciona o tratamento de exceções em Python.
  - `/vetores_matrizes` – Aborda o uso de vetores e matrizes.
  
- **Sobre a Equipe (`/sobre_equipe`)**  
  Página institucional com informações sobre o criador do site.

## 🛠 Tecnologias Utilizadas

- **Linguagem Principal**: Python 3
- **Framework Web**: Flask
- **Front-end**: HTML5, CSS3 (com foco em acessibilidade e design responsivo)
- **Bibliotecas**:
  - `Flask` – Para construção da aplicação web
  - `csv` – Para manipulação de arquivos do glossário
  - `google.generativeai` – Integração com a API do Gemini
  - `dotenv` – Para carregar variáveis de ambiente
  - `os` – Para manipulação segura de arquivos e caminhos

## 🤖 Integração com a API do Gemini

A integração com o **Gemini** foi feita utilizando a biblioteca `google.generativeai`.

- A chave da API está armazenada no arquivo `.env`.
- O código carrega essa chave com `dotenv` e instancia o modelo com `GenerativeModel('gemini-pro')`.
- Quando o usuário envia uma pergunta pela rota `/tirar_duvidas`, a pergunta é enviada para o Gemini com `model.generate_content(pergunta)`, e a resposta gerada é exibida na mesma página.
- A resposta é exibida com o filtro `| safe` porque ela pode conter tags HTML.

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu_usuario/Projeto_Flask.git
   cd Projeto_Flask
