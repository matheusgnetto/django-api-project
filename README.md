Tecnologias Utilizadas
==========
- Python 3.9.4
- Django 4.0
- Django Rest Framework 3.13.1

Para Consumo 
=============
O projeto encontra-se para utilização neste [Link](https://djgestao-funcionarios.herokuapp.com).

Para requisição CREATE
`https://djgestao-funcionarios.herokuapp.com/funcionarios`

Para requisição GET
`https://djgestao-funcionarios.herokuapp.com/funcionarios`

Para requisção PUT
`https://djgestao-funcionarios.herokuapp.com/funcionarios/:id`

Para requisção DELETE
`https://djgestao-funcionarios.herokuapp.com/funcionarios/:id`

Para requisção GET (Salário em Real)
`https://djgestao-funcionarios.herokuapp.com/funcionarios_brl`

Sobre o Projeto
==========
- Foi desenvolvido com o objetivo de atender o cenário de uma empresa dos Estados Unidos que começou sua operação no Brasil, e quer fazer a gestão de seus funcionários estadunidenses. A receita de empresa é em real, porém o salário de seus funcionários está em dólar. O presidente da empresa quer um sistema (API) que traduza a remuneração de seus funcionários de dólar para o real (BRL) e tenha a capacidade de cadastrar, editar e deletar novos colaboradores ao sistema (CRUD).
- A entidade funcionário deverá obrigatoriamente ter os seguintes atributos: id, name, salary (em dólar), age, role e email.
- Possuí um “endpoint” do tipo “GET” que retorna todos os dados de um ou mais funcionários, traduzindo seus salários de dólar para o real.
- É obtido em tempo real a cotação do dólar através da api pública "awesomeAPI".

Observações
==========
O descritivo com o "passo-a-passo" do projeto, bem como todos os comandos utilizados se encontra disponível no diretório [docs](https://github.com/matheusgnetto/django-api-project/tree/master/docs).

