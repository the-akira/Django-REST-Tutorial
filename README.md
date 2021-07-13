# Django REST API Tutorial

Neste guia vamos desenvolver uma REST API com o framework Django REST.

**[Leia o Tutorial](https://akiradev.netlify.app/posts/django-rest-api/)**

--- 

## Instalação

### Clone o Repositório

```
git clone https://github.com/the-akira/Django-REST-Tutorial.git
```

### Dentro do Diretório Principal

Crie um Ambiente Virtual

```
python -m venv myvenv
```

Ative o Ambiente Virtual

```
source myvenv/bin/activate
```

Instale os Requeriments

```
pip install -r requirements.txt
```

Sincronize o banco de dados

```
python manage.py migrate
```

Execute a aplicação

```
python manage.py runserver
```

Faça [Requisições](https://github.com/the-akira/Django-REST-Tutorial/blob/master/requests.md).