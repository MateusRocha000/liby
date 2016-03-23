# liby

Trabalho Engenharia de Software 2016


## Instalação


### Intalar pip

**pip** é um sistema de gerenciamento de pacotes usado para instalar e gerenciar pacotes de software escritos na linguagem de programação Python.

Para instalar, basta executar o comando:

`$ sudo apt-get install python-pip`


### Instalar virtualenv

**virtualenv** é uma ferramenta para criação de ambientes virtuais.

Para instalar, basta executar o comando:

`$ sudo pip install virtualenv`


### Criando ambiente virtual

Para criar um novo ambiente virtual, basta executar o comando:

`$ virtualenv -p python3 myenv`

Onde `myenv` é o nome do ambiente virtual a ser criado, e o parâmetro `-p` específica a versão do Python a ser utilizada.

### Ativando o ambiente virtual

Além de instalar, é necessário ativar o ambiente virtual que foi criado. Para isto, dentro da pasta do ambiente virtual que foi criado, basta executar o comando:

`$ source bin/activate`


### Desativando o ambiente virtual

Para desativar o ambiente virtual, não importa o diretório que esteja, basta executar o comando:

`$ deactivate`


### Clonado o repositório

Dentro do ambiente virtual, basta executar:

`$ git clone https://github.com/sauloantuness/liby.git`


### Instalando dependências

Dentro da pasta raiz do repositório, para instalar todas as dependências do projeto, basta executar:

`$ pip install -r requirements.txt`

Serão instalados todos os pacotes listados em requirements.txt


### Atualizando dependências

Sempre que novos pacotes forem instalados, o arquivo requirements.txt deve ser atualizado. Para isto, dentro da pasta raiz do repositório, basta executar:

`pip freeze > requirements.txt`