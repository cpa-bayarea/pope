# PoPe - Portal de Pesquisas

[![Build Status](https://travis-ci.org/cpa-bayarea/pope.svg?branch=dev)](https://travis-ci.org/cpa-bayarea/pope)
[![Coverage Status](https://coveralls.io/repos/github/fabricasoftwares/pope/badge.svg?branch=dev)](https://coveralls.io/github/fabricasoftwares/pope?branch=dev)

Portal de pesquisa para serviços prestados por órgãos cadastrados.

## Virtualenv

O virtualenv do python isola as dependências de cada `ambiente` criado por ele, aconselha-se seu uso para esse projeto.

> Ver mais: [virtualenv](https://virtualenv.pypa.io/en/stable/)


## Para instalar as dependências do projeto

```bash
./setup.py install

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

