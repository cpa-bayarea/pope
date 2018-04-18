# PoPe - Portal de Pesquisas

Portal de pesquisa para serviços prestados por órgãos cadastrados.

## Virtualenv

O virtualenv do python isola as dependências de cada `ambiente` criado por ele, aconselha-se seu uso para esse projeto.

> Ver mais: [virtualenv](https://virtualenv.pypa.io/en/stable/)


## Para instalar as dependências do projeto

As dependências estão listadas no arquivo `requirements.txt`

```bash

pip install -r requirements.txt

```

## Para montar o banco de dados que será utilizado

```bash

cd /path/to/project

./manage.py migrate

```


## Para rodar a aplicação local

A aplicação, por default, fica disponível em `localhost:8000`

```bash

cd /path/to/project

./manage.py runserver

```

## Para rodar os testes

```bash

cd /path/to/project

./manage.py test

```

