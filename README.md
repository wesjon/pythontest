# Escopo #
Aplicação console para calcular o balanço da conta corrente de um conjunto de clientes.

# Invocação #

O programa recebe dois argumentos na linha de comando:

1. Nome do arquivo de contas
2. Nome do arquivo de transações

O nome do programa que processa os arquivos é `app.py`

Ex: `app.py contas.csv transacoes.csv`

# Formato dos arquivos de entrada #
### Contas ###
O arquivo de contas deve ser formatado como csv válido e conter 2 colunas: id e balance
* **id**: identificar da conta (inteiro)
* **balance**: Saldo atual da conta como inteiro
Ex.:
```
id,balance
122,0
```
### Transações ###
O arquivo de contas deve ser formatado como csv válido e conter 2 colunas: account_id e value
* **account_id**: ID da conta a qual se refere a transação (inteiro)
* **value**: Valor da transação como inteiro 
Ex.:
```
account_id,value
122,1
122,5
```

# Como executar este programa? #
1. Instalar o [Python 2.7](https://www.python.org/downloads/)
2. Executar o arquivo `app.py` passando como parâmetros os arquivos de contas e o de transações: `app.py <nome_arquivo_contas.csv> <nome_arquivo_transacoes.csv> `
3. A saída deve ser impressa na tela do console

# Como executar os testes? #
1. Com o python instalado executar o comando `python tests.py`

# Como verificar a cobertura dos testes?
1. [Instalar o pip](https://pip.pypa.io/en/stable/installing/)
2. Instalar o package `coverage`: `pip install coverage`
3. Executar o reporting do `coverage` para verificar a cobertura dos testes: `coverage run --source=. tests.py``
4. Para visualizar os resultados:

* `coverage report` para visualizar no console
* `coverage html -d .htmlcov` para gerar uma saída HTML
* `open .htmlcov/index.html ` para abrir o report de coverage formatado em HTML
