import os
from urllib import request

def download_file(url, file, subscribe):
    if subscribe == True:
        if os.path.isfile(file):
            print(f'Arquivo "{file}" excluido')
        else:
            print(f'não existe arquivo "{file}" para excluir')
        
        try:
            request.urlretrieve(url , file)
            print(f'Arquivo "{file}" Baixado')
        except:
            print(f'Arquivo "{file}" não foi baixado a partir da URL: {url}')
    
    elif subscribe == False:
        if os.path.isfile(file):
            print(f'Arquivo "{file}" Já existe, não é necessário baixar')
        else:
            try:
                request.urlretrieve(url , file)
                print(f'Arquivo "{file}" Baixado')
            except:
                print(f'Arquivo "{file}" não foi baixado a partir da URL: {url}')       

