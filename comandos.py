""" passo a passo para comandos no terminal, desde para usar o github
como para navegar nos arquivos

no terminal do linux, no meu caso o bash:

python -m site : mostra o sys.path mostrando quais os caminhos que o python 
vai buscar os pacotes
-vai mostrar tbm a pasta de usuario

python - help 
-mostra uma gma de comandos para mexer no terminal py 


modulo tutle demo: diversas aplicaçoes demonstrativas visuais
python -m tutledemo

INTERPRETADOR PYTHON: SÓ DIGITAR PYTHON NO TERMINAL
ELE VAI MUDAR A APARENCIA DAS LETRAS E MUDA PARA ">>>"
- sistema fica em loop, não precisa colocar print, pqp ele sempre 
vai imprimir ja
-para sair é só digitar:
EXIT()   ou CTRL+D 

o help() mostra tutoriais, se vc colocar um objeto especifico dentro dos parenteses
ele vai exemplificar e ensinar como lidar com aquele objeto  que pode ser um numero por 
exemplo.. help(12)
-posso entrar no gelp() e depois digitar modulos, p.ex. que ele vai mostrar
todos modulo instalados no meu PC 

ditiga Q pra sair 

;;;;;;;;;;;;;;;

para criar um ambiente virtual no python para que  nao 
prejudique os arquivos do py é importante criar um .venv

digite no bash 
   python -m venv .venv
o .venv sera o nome da pasta a ser criada

note que se digitar apenas 
  ls 
mostrara apenas os aequivos nomrmais

mas se digitar ls -a , mostrara os ocultos, dentre eles o .venv


para ver o que tem dentro do s.venv
   ls .venv
para ver o ambiente(bin(linux) ou scripts(windows))
:
     ls .venv/scripts
aparecera os aquivos : pip, pip3, python, pythonw

, a pasta .VENV está isolada do sistema, se der algum problema, posso delegar ela 
e começar uma nova venv, pq os arquivos estarão dentro delas e isolados

para awtivar o venv no terminal digite:

    source .venv/Scripts/activate

ou 
    source .venv/bin/activate (linux)


obs: aparecera (.venv) na mensagem do terminal

e quando pesquisar 
    which python
aparecera outro caminho para o python, o caminho da .venv (virtual)
observe que no caminho tem /.venv/Scripts/python no final
que prova isso, essa maquina virtual.

só tem q lembrar de executar o 
source .venv/Scripts/activate
para acessar o seu ambiente virtual e trabalhar
e para confirmar so
dar um which python para confirmar o caminho
do python que estara rodando/salvando
.......................
para resolver o problema com o github
referente essa nova pasta .venv
pq a gente não deve mandar ela pro hub
pra isso tem que criar um arquivo .gitignore
para qdo de um "git status" ela não mostre mais 
a pasta .venv

assim 
precisamos criar esse arquivo e listar "globs"
que são padroes de listagem de arquivos, e assim 
qualquer coisa que faça mach ele vai ignorar..

assim dentro desse novo arquivo .gitignore só digitar .venv
para que a pasta .venv seja ignorada pelo github
na pesquisa git status.
..........................
pode verificar a documentação do ambiente .venv no docs.python:
   https://docs.python.org/pt-br/3/library/venv.html
..........................
toda vez que for fazer um commit de der erro de index.lock

pode executar a remoção do index da seguinte forma:
    rm -f .git/index.lock
..................

no projeto vamos instalar um projeto o pypi.org o  interpretador ipython:
     python -m pip install ipython
(esse interpretador é melho do que o que vem no proprio python(>>>))
o ipython é colorido, tem autocomplete e o help mais poderoso
o ipython tem a versao web, que pe o jupyter, q antes chamava ipython. 

devemos tbm fazer um upgrade no proprio pip para atualizalo com os novos projetos
    python -m pip install --upgrade pip
"""
