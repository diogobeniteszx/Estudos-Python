# Crie um código em python que testa se o site Pudim está acessível pelo computador usado.

import urllib.request
import urllib.error

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')
