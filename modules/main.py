import time, manager_file as manager_file, pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

list_locais = [41366093, 41153421, 41366085, 41155521, 41149890, 41366115, 41375572, 41153413, 41366107, 41159276, 41366131, 41389417, 41145496, 41025067, 41025083, 41025091, 41025270, 41025148, 41366182, 41025172, 41025180, 41025199, 41025245, 41389409, 41354770, 41025253, 41025261, 41025288, 41025202]

def baixar_csv():
    options = Options()
    options.add_argument('-headless')
    browser = webdriver.Firefox(options=options)
    browser.get('https://api.simet.nic.br/simet-mapa-escolas/')
    time.sleep(5)
    link_csv = browser.find_element(By.ID, value='downloadCSV').get_attribute('href')
    manager_file.download_file(file='dados.csv', url=link_csv, subscribe=True)
    time.sleep(1)
    browser.quit()

def get_info(list_locais):
    baixar_csv()
    pandas.set_option('display.max_columns', None)
    dados = pandas.read_csv('dados.csv')
    dados = dados.drop(columns=['RTT_MS','RTT_LOST_PCT', 'NU_ANO_CENSO','NM_ESTADO', 'NM_REGIAO', 'SG_UF','QT_DESKTOP_ALUNO','QT_COMP_PORTATIL_ALUNO','QT_TABLET_ALUNO','QT_SALAS_UTILIZADAS','IN_LABORATORIO_INFORMATICA','IN_BANDA_LARGA','IN_INTERNET_ALUNOS','IN_ACES_INTERNET_DISP_PESSOAIS','PRESENCIAL','SEMIPRESENCIAL','EAD','QT_EQUIP_TV','TP_LOCALIZACAO','JITTER_DOWNLOAD_MS','TP_DEPENDENCIA','NM_MUNICIP'])
    filtro = dados['CO_ENTIDADE'].isin(list_locais)
    locais_escolhidos = dados[filtro]
    return locais_escolhidos


print(get_info(list_locais=list_locais))