# Phantom Dev Tool

## Sobre

Trata-se um projeto voltado a correção e validação de código server side.

## Tecnologias Utilizadas

- MongoDB
- Python
- FastApi

## Instalação

- Com o docker instalado basta rodar o comando `docker-compose build --no-cache && docker-compose up`

## Licença

Copyright (c) 2024, [Ives Costa]
Este projeto está licenciado sob a [Licença BSD](https://pt.wikipedia.org/wiki/Licen%C3%A7a_BSD).

## Contato

Email: <ivespauiniam@gmail.com>
Linkedin: <https://www.linkedin.com/in/ives-costa-082274183/>


.env
```bash
CACHE_TYPE="redis"
REDIS_URL=""
MONGO_HOST='mongodb://root:MongoDB2019!@mongo/?retryWrites=true&w=majority'
MONGO_PORT=27017
OPENAI_KEY=''
# PROJECT_NAME="phantom-dev-tool"
# se você está rodando a aplicação em container deixar o nome do projeto como code
PROJECT_NAME="code"
ENVIRONMENT="STG"
```
