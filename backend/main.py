from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

# Servidor python criado usando o Flask para servir os dados do arquivo CSV para o Vue
# Configurações do Flask

app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Carregando o arquivo CSV com o pandas que também vai ajudar a fazer as buscas

df = pd.read_csv('Relatorio_cadop.csv', encoding='utf-8', sep=';')

vue_data = {
    'info': 0,
    'search_method': ''
}

# método para buscar os dados no arquivo CSV

def search_data(response_object):

    if vue_data['search_method'] == 'Ans':

        temp = 'Registro_ANS'

    else:
        
        temp = 'CNPJ'

    for index, row in df.iterrows():

        if row[temp] == vue_data['info']:
            
            found_data ={
                
                'Registro_ANS': row['Registro_ANS'],
                'CNPJ': row['CNPJ'],   
                'Razão Social': row['Razao_Social'],
                'Modalidade': row['Modalidade'],
                'CEP': row['UF'] + ' ' + str(row['CEP']),
                'Telefone': str(row['DDD']).split('.')[0] + ' ' + str(row['Telefone']),
                'Email': row['Endereco_eletronico'],
                'Representante': row['Representante'],
                'Regiao_de_Comercializacao': row['Regiao_de_Comercializacao'],
                'Data_Registro_ANS': row['Data_Registro_ANS'],

            }

            response_object['message'] = 'Registro encontrado!'
            response_object['data'] = found_data

            return response_object

    response_object['message'] = 'Registro não encontrado!'

    return response_object

# endpoint para receber os dados do Vue e retornar os dados do CSV
@app.route('/', methods=['GET','POST'])
def get_data():

    response_object = {}

    if request.method == 'POST':
        
        data = request.get_json()
        vue_data['info']= data.get('info')
        vue_data['search_method'] = data.get('method')
    
    else:

        response_object = search_data(response_object)
    
    return jsonify(response_object)
        

if __name__ == '__main__':

    app.run(debug=True)