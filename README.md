# 📚 Python: Avançando na Orientação a Objetos e Consumo de API

Repositório dedicado ao projeto final do curso "Python: avance na Orientação a Objetos e consuma API" da [Alura](https://www.alura.com.br/).

## 🎯 Objetivo do Projeto

O objetivo principal foi aplicar na prática os conceitos de Orientação a Objetos em Python e desenvolver uma API simples utilizando o framework FastAPI para consumir, filtrar e organizar dados de uma fonte externa no formato JSON.

## ✨ Tecnologias e Conceitos Utilizados

- **Linguagem:** Python 3
- **Framework:** FastAPI
- **Bibliotecas:** Requests
- **Conceitos:**
  - Consumo de APIs REST
  - Manipulação de dados JSON
  - Orientação a Objetos (Herança, Polimorfismo)
  - Ambientes Virtuais (`venv`)

## 🚀 Como Executar o Projeto

Siga os passos abaixo para executar a API localmente:

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/Baroli03/Python-Estudo-API
    cd Python-Estudo-API
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Inicie o servidor da API:**
    ```bash
    uvicorn main:app --reload
    ```

5.  Abra seu navegador e acesse `http://127.0.0.1:8000/restaurantes` para ver os dados salvos.

## 📖 Principais Aprendizados

- **Desenvolvimento de APIs:** Compreensão do ciclo de vida de uma requisição e desenvolvimento de endpoints com FastAPI.
- **Manipulação de Dados:** Leitura e processamento de arquivos JSON de fontes externas.
- **Frameworks Web:** Visão geral sobre as diferenças e casos de uso de **FastAPI**, **Django** e **Flask**.
