# evoe
API Todolist Evoe - Desenvolvido com Django e Django Rest Framework.

Para visualizar a documentação da API, acesse o endereço abaixo:
http://localhost:8000/docs/

Caso não deseje utilizar em sua máquina é possível acessar através do endpoint abaixo:
https://teste-evoe.herokuapp.com/

Para acessar a documentação, utilize o endereço abaixo:
https://teste-evoe.herokuapp.com/docs/


Acesso a API

1) Para acessar os recursos da API acesse o endpoint:
https://teste-evoe.herokuapp.com/api-auth/ passando como parâmetros via post o username e o password que informamos no e-mail.
Será retornado o token do usuário.

2) Com o token recebido acesse as demais urls presentes na documentação passando no header o parâmetro Authorization e "Token TOKEN-DO-USUARIO" como valor.