import requests
import holidays
import datetime
import smtplib
import os
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from bs4 import BeautifulSoup
from cidades import listaCidades, mes, ano, hoje

listaDeFeriadosDoAno = []
feriados = holidays.country_holidays("BR", subdiv="CE")
feriadoDoAno= feriados["2024-01-01":"2024-12-31"]
sem = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")

for feriado in feriadoDoAno:
    listaDeFeriadosDoAno.append(feriado)
    
def pegarDataDoPortal(cidade):
    for dados in cidade:
        datasAux = []
        
        html = requests.get(dados[0]).content    
        soup = BeautifulSoup(html, 'html.parser')
        rowsTable = soup.find_all('tbody')[0].find_all('tr')
        
        if dados[2] != 's' and not rowsTable:
            mesAux = int(mes)
            
            while mesAux > 0:
                if dados[2] == 'r':
                    url = dados[0] + str(mesAux) + "/" + ano
                else:
                    url = (dados[0]).replace('data','pordata') + str(mesAux) + "/" + ano
                
                html = requests.get(url).content
                soup = BeautifulSoup(html, 'html.parser')
                rowsTable = soup.find_all('tbody')[0].find_all('tr')
                
                if rowsTable:
                    break
                
                mesAux = mesAux - 1
        
        for row in rowsTable:
        #Verificar despesa ou receita com base na posição da tabela
            if dados[2] == 'r':
                tdData =row.find('td').text
            elif dados[2] == 'd':
                tdData = row.find_all('td')[1:2][0].text
            else:
                tdData = '01/' + row.find('td').text
            
            data = datetime.datetime.strptime(tdData, "%d/%m/%Y").date()
            datasAux.append(data)
        
        dados.append(datasAux)
        
    
    return cidade
    
def validarDataPortal(cidade):
    erro = False
    dayAux = 1
    
    while True:
        dataTeste = datetime.timedelta(days=dayAux)
        auxData = hoje - dataTeste
        
        if(auxData.weekday() < 5):
            if(auxData not in listaDeFeriadosDoAno):
                break
        dayAux = dayAux + 1
        
    for dados in cidade:
        if (auxData not in dados[5]) and (hoje not in dados[5]) and (dados[2] != 's') and (dados[3] == 'p'):
            erro = True
            dados.append(True)

        elif dados[3] == 'c' and dados[2] != 's':
            if (hoje.day >= 10) and (auxData.month != max(sorted(dados[5])).month):
                erro = True
                dados.append(True)
                
            else:
                dados.append(False)

        elif (dados[2] == 's') and (not dados[5]) and (hoje.day >= 10):
            erro = True
            dados.append(True)
            
        else:
            dados.append(False)
            
    if erro:
        print("Mandar email para prefeitura de " + dados[4]) if dados[3] == 'p' else print("Mandar email para camara de " + dados[4])
        enviarEmail(cidade)
        
    else:
        print("Não enviar email para prefeitura de " + dados[4]) if dados[3] == 'p' else print("Não enviar email para camara de " + dados[4])

def enviarEmail(cidade):
    try:
        ultimaDataReceita = ""
        ultimaDespesa = ""
        ultimaServidor = ""
        if(cidade[0][6] and cidade[0][5]):
            ultimaDataReceita = "Receitas:\n  Ultima data cadastrada: " + max(sorted(cidade[0][5])).strftime("%d/%m/%Y") + "\n\n\n"
            
        if(cidade[1][6] and cidade[1][5]):
            ultimaDespesa = "Despesas:\n  Ultima data cadastrada: " + max(sorted(cidade[1][5])).strftime("%d/%m/%Y") + "\n\n\n"
        
        if not cidade[2][5] and cidade[2][6]:
            ultimaServidor = "Servidores:\n  Nenhum dado para o mês " + mes + '/' + ano +" \n"
            
        print(ultimaDataReceita + ultimaDespesa + ultimaServidor)
            
        sender = 'natanael@digimax.com.br'
        sender_title = "Digimax"
        recipient = cidade[0][1]
        
        msg = MIMEText( ultimaDataReceita  + ultimaDespesa +  ultimaServidor, 'plain', 'utf-8')
        msg['Subject'] =  Header("PORTAL DE TRANSPARENCIA DA " + ("PREFEITURA " if cidade[0][3] == 'p' else 'CAMARA ') + ('DE ' + cidade[0][4]) + ' ' + str(hoje.strftime("%d/%m/%Y")), 'utf-8')
        msg['From'] = formataddr((str(Header(sender_title, 'utf-8')), sender))
        msg['To'] = recipient

        server = smtplib.SMTP_SSL('smtp.zoho.com', 465)

        server.login('', '')
        server.sendmail(sender, [cidade[0][1],'vitorianoduomariana@gmail.com'], msg.as_string())
        
    except Exception as e:
        print(f"Erro ao enviar email: {e}")

    finally:
        server.quit()

for cidade in listaCidades:
    pegarDataDoPortal(cidade)
    validarDataPortal(cidade)

os.system("PAUSE")