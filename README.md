### Python ETL - Referencia Programador Lhama👋

## 01 - ETL Pipeline - Introdução
Apresentamos alguns conceitos relacionados a ETL e Pipeline de dados para exemplificar melhor o seguinte conteúdo.~

Links:
* ETL (Zendesk) - https://www.zendesk.com.br/blog/o-que...
* Data Pipeline (Data Science Academy) - https://blog.dsacademy.com.br/mas-afi...
* Web Scrapping (Digital Ocean) - https://www.digitalocean.com/communit...
## 02 - ETL Pipeline - Princípios de Arquitetura
Breve introdução a respeito de princípios básicos de arquitetura para um bom comportamento do projeto proposto, tais como as regras de execução e atuação sobre erros

Links:
* ETL (Zendesk) - https://www.zendesk.com.br/blog/o-que...
* Data Pipeline (Data Science Academy) - https://blog.dsacademy.com.br/mas-afi...
* Web Scrapping (Digital Ocean) - https://www.digitalocean.com/communit...

## 03 - ETL Pipeline - Configurações de Ambiente

Iniciamos o projeto apresentando algumas configurações interessantes para manter uma qualidade de código e tratamento de pacotes instalados

Links:
* Virtualenv Python - https://docs.python.org/pt-br/3/libra...
* Pylint - https://pypi.org/project/pylint/
* Pre-Commit - https://pre-commit.com/

## 04 - ETL Pipeline - Pasta Drivers e Requisições HTTP

Criamos a pasta Drivers e iniciamos nosso primeiro pacote fazendo requisições HTTP para a pagina desejada. Alem disso, cobrimos todo o processo a partir dos testes unitários

Links:
* GitHub - https://github.com/programadorLhama/E...
* Requests - https://pypi.org/project/requests/
* Requests-mock - https://pypi.org/project/requests-mock/
* Pytest - https://pypi.org/project/pytest/

## 05 - ETL Pipeline - Aplicando BeautifulSoup4 em Drivers

Utilizando a biblioteca beautifulsoup4, conseguimos fazer uma certa seleção dos elementos de desejo de certo html. Lembrando que, de acordo com boas práticas focadas no código, tal html foi utilizado como mock preparado para testes unitários e validação

Links:
* GitHub - https://github.com/programadorLhama/E...
* Beautifulsoup4 - https://pypi.org/project/beautifulsoup4/
* Beautiful Soup Documentation -https://beautiful-soup-4.readthedocs....
* Site para Scrapp utilizado na aula - https://web.archive.org/web/201210071...

## 06 - ETL Pipeline - Iniciando Estágio de Extração

Iniciamos a implementação do estagio de extração na arquitetura do pipeline e utilizamos o conceito de interfaces para ligar o estagio aos elementos da pasta drivers.

Links:
* GitHub - https://github.com/programadorLhama/E...
* Interfaces - https://www.youtube.com/watch?v=_Dwp7...
* Injeção de Dependencia - https://www.youtube.com/watch?v=5DBfV...

## 07 - ETL Pipeline - Contratos e Erros

Seguindo a implementação do estagio de extração, temos o acoplamento e utilização de contratos e tratamento de erros

Links:
* GitHub - https://github.com/programadorLhama/E...
* tratamento de erros - https://www.youtube.com/watch?v=9qLiQ...
* tuplas nomeadas - https://www.youtube.com/watch?v=RMoyc...

## 08 - ETL Pipeline - Finalização de Estágio de Extração

Fechamos a implementação do estagio de extração concentrando no teste unitário e adicionando elementos para melhorar a validação

Links:
* GitHub - https://github.com/programadorLhama/E...

## 09 - ETL Pipeline - Introdução ao Estágio de Transformação

Iniciamos os preparativos e debatemos os princípios iniciais pra direcionar nossa criação do estágio de transformação

Links:
* GitHub - https://github.com/programadorLhama/E...

## 10 - ETL Pipeline - Implementando o Estágio de Transformação

Dada uma introdução básica a respeito dos processos necessários na etapa de transformação, agora adicionamos toda a lógica necessária ao estágio desejado

Links:
* GitHub - https://github.com/programadorLhama/E...

## 11 - ETL Pipeline - Finalização de Estágio de Transformação

Fechamos a implementação do estagio de transformação concentrando no teste unitário e adicionando elementos para melhorar a validação

Links:
* GitHub - https://github.com/programadorLhama/E...

## 12 - ETL Pipeline - Banco de Dados e Conexão

Para introduzir a etapa de Carga, será necessário a implementação de certo mecanismo para interação com bancos de dados. Para isso, iniciamos toda a etapa de manipulação de banco de dados para gerar tabelas e conexões desejadas

Links:
* GitHub - https://github.com/programadorLhama/E...
* Python Mysql - https://www.datacamp.com/community/tu...
* Mysql Connector - https://pypi.org/project/mysql-connec...

## 13 - ETL Pipeline - Inserção de Registros

Após estabelecida conexão em banco de dados e feitas as devidas criações, agora manipulamos registros para inserir e armazenar em banco.

Links:
* GitHub - https://github.com/programadorLhama/E...

## 14 - ETL Pipeline - Estágio de Carga

Feita toda a parte de infraestrutura junto com o mock relativo ao contrato de transformação, agora estamos aptos a implementar o estágio de carga!

Links:
* GitHub - https://github.com/programadorLhama/E...

## 15 - ETL Pipeline - Montagem de Pipeline e Finalização

Finalizamos a montagem de todo o pipeline fazendo todo o encaixe de classes e objetos e analizamos o comportamento do projeto em execução

Links:
* GitHub - https://github.com/programadorLhama/E...