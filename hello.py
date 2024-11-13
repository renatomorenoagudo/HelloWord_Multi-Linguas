
#!/usr/bin/env python3
# # acima qdo usa ! (shibang) indica o caminho do python antes do programa rodar
#para pesquisar o caminho, no termimal bash,digite which python.
#este programa imprime o ola mundo!

"""
hello world multi linguas

dependendo da lingua configurada no ambiente o progrma
exibe a correspodente.

Como Usar:

Tenha avariável LANG devidamente configurada ex:
      export LANG=pt_br

Execução:
    python3 hello.py
    ou
    ./hello.py

"""
__version__="0.0.1"
__author__="Renato Moreno"
__license__="Unlicense"
#'dander' significa que tem dois underlines antes e depois.

#Code:
import os  

currente_language=os.getenv("LANG","en_US")[:5]

msg="Hello, World!"
if currente_language =="pt_BR":
    msg ="Olá, Mundo!"
elif currente_language=="it_IT":
    msg="CIao, Mondo!"
elif currente_language=="es_SP":
    msg="Holla, Mundo!"
elif currente_language=="es_SP":
    msg="Bonjour, Monde!"


#!/usr/bin/env python3
# # acima qdo usa ! (shibang) indica o caminho do python antes do programa rodar
#para pesquisar o caminho, no termimal bash,digite which python.
#este programa imprime o ola mundo!

"""
hello world multi linguas

dependendo da lingua configurada no ambiente o progrma
exibe a correspodente.

Como Usar:

Tenha avariável LANG devidamente configurada ex:
      export LANG=pt_br

Execução:
    python3 hello.py
    ou
    ./hello.py

"""
__version__="0.0.1"
__author__="Renato Moreno"
__license__="Unlicense"
#'dander' significa que tem dois underlines antes e depois.

#Code:
import os  

currente_language=os.getenv("LANG","en_US")[:5]

msg="Hello, World!"
if currente_language =="pt_BR":
    msg ="Olá, Mundo!"
elif currente_language=="it_IT":
    msg="CIao, Mondo!"
elif currente_language=="es_SP":
    msg="Holla, Mundo!"
elif currente_language=="es_SP":
    msg="Bonjour, Monde!"

#!/usr/bin/env python3
# # acima qdo usa ! (shibang) indica o caminho do python antes do programa rodar
#para pesquisar o caminho, no termimal bash,digite which python.
#este programa imprime o ola mundo!

"""
hello world multi linguas

dependendo da lingua configurada no ambiente o progrma
exibe a correspodente.

Como Usar:

Tenha avariável LANG devidamente configurada ex:
      export LANG=pt_br

Execução:
    python3 hello.py
    ou
    ./hello.py

"""
__version__="0.0.1"
__author__="Renato Moreno"
__license__="Unlicense"
#'dander' significa que tem dois underlines antes e depois.

#Code:
import os  
import sys

arguments={
    "lang": None,
    "count":None,
}
for arg in sys.argv[1:]:
   # print(f"{sys.argv=}")
   #print(arg.split("="))
   # TODO: tratar ValueError
    key,value=arg.split("=")


currente_language=os.getenv("LANG","en_US")[:5]

msg={
    "en_US":"Hello, World!",
    "pt_BR":"Olá, Mundo!",
    "it_IT":"CIao, Mondo!",
    "fr_FR":"Bonjour, Monde!",
    "es_SP":"Holla, Mundo!"
}

print(msg[currente_language])
