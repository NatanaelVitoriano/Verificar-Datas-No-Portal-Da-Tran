import datetime

hoje = datetime.date.today()
mes = str(12 if hoje.month -1 == 0 else hoje.month -1)
ano = str(hoje.year - 1 if hoje.month == 1 else hoje.year)

listaCidades = [
    [
        ['https://eusebio.tudotransparente.com.br/receitas/data/', '', 'r','p','EUSEBIO'],
        ['https://eusebio.tudotransparente.com.br/despesas/data/', '', 'd','p','EUSEBIO'],
        ['https://eusebio.tudotransparente.com.br/servidores/data/' + ano + '/' + mes, '', 's','p','EUSEBIO']
    ],
    [
        ['https://parambu.tudotransparente.com.br/receitas/data/', '', 'r','p','PARAMBU'],
        ['https://parambu.tudotransparente.com.br/despesas/data/', '', 'd','p','PARAMBU'],
        ['https://parambu.tudotransparente.com.br/servidores/data/' + ano + '/' + mes, '', 's','p','PARAMBU']
    ],
    [
        ['https://potengi.tudotransparente.com.br/receitas/data/', '', 'r','p','POTENGI'],
        ['https://potengi.tudotransparente.com.br/despesas/data/', '','d','p','POTENGI'],
        ['https://potengi.tudotransparente.com.br/servidores/data/' + ano + '/' + mes, '', 's','p','POTENGI']
    ],
    [
        ['https://crateus.tudotransparente.com.br/receitas/data/', '','r','p','CRATEUS'],
        ['https://crateus.tudotransparente.com.br/despesas/data/', '','d','p','CRATEUS'],
        ['https://crateus.tudotransparente.com.br/servidores/data/' + ano + '/' + mes, '', 's','p','CRATEUS']   
    ],
    [
        ['https://santanadocariri.tudotransparente.com.br/receitas/data/', '', 'r','p','SANTANA DO CARIRI'],
        ['https://santanadocariri.tudotransparente.com.br/despesas/data/', '', 'd','p','SANTANA DO CARIRI'],
        ['https://santanadocariri.tudotransparente.com.br/servidores/data/' + ano + '/' + mes, '', 's','p','SANTANA DO CARIRI']
    ],
    [
        ['https://cmeusebio.tudotransparente.com.br/receitas/data/', '', 'r','c','EUSEBIO'],
        ['https://cmeusebio.tudotransparente.com.br/despesas/data/', '', 'd','c','EUSEBIO'],
        ['https://cmeusebio.tudotransparente.com.br/servidores/data/' + ano + '/' + mes, '', 's','c','EUSEBIO']    
    ],
    [
        ['https://cmparambu.tudotransparente.com.br/receitas/data/', '', 'r','c','PARAMBU'],
        ['https://cmparambu.tudotransparente.com.br/despesas/data/', '', 'd','c','PARAMBU'],
        ['https://cmparambu.tudotransparente.com.br/servidores/data/' + ano + '/' + mes, '', 's','c','PARAMBU']
    ],
    [
        ['https://cmpotengi.tudotransparente.com.br/receitas/data/', '', 'r','c','POTENGI'],
        ['https://cmpotengi.tudotransparente.com.br/despesas/data/', '', 'd','c','POTENGI'],
        ['https://cmpotengi.tudotransparente.com.br/servidores/data/' + ano + '/' + mes, '', 's','c','POTENGI']
    ],
    [
        ['https://cmmombaca.tudotransparente.com.br/receitas/data/', '', 'r','c','MOMBAÇA'],
        ['https://cmmombaca.tudotransparente.com.br/despesas/data/', '', 'd','c','MOMBAÇA'],
        ['https://cmmombaca.tudotransparente.com.br/servidores/data/' + ano + '/' + mes, '', 's','c','MOMBAÇA']        
    ]
]