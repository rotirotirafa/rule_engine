# Rule Engine

É uma API RESTFul para gerenciamento do motor de regras, 
básicamente é aqui que é feito o controle das regras da aplicação.

### Install & Run

`python -m venv venv`

Ative o ambiente virtual no <b> Linux </b> ou <b> Mac </b>:

`source venv/bin/activate`

<b> Windows </b>

terminal: `venv\Scripts\activate.bat`

PowerShell `venv\Scripts\Activate.ps1`

Instale as dependências com o comando:

`pip install -r requirements.txt`

É necessário criar o banco de dados, para isso deve-se possuir o [Docker instalado](https://docs.docker.com/get-docker/)

Para subir o container do Postgres `docker compose up -d`

Rode as migrations no banco de dados `dotenv run alembic upgrade head`

Para rodar a api: `dotenv run uvicorn app.main:app --reload`

Swagger [localhost:8000/docs/](localhost:8000/docs)
![doc](/docs/swagger.png)