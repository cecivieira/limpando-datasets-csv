import pandas as pd

class LimparConjuntoDados:
    def __init__(self, arquivo, titulo):
        self.arquivo = arquivo
        self.titulo = titulo
        self.colunasRemover = []


    def ler_arquivo(): #Ler o arquivo CSV a ser tratado
        while True:

            try:
                arquivo = str(input('Digite o caminho completo para o arquivo CSV que deseja tratar (ex. /home/anacecilia/Documentos/cursos-graduacao/cursos-graduacao.csv): '))        
                conjuntoDados = pd.read_csv(arquivo, encoding = "ISO-8859-1") 
                # conjuntoDados.to_csv('TESTANDO FUNCAO LER ARQUIVO.csv', index='False')           
                return conjuntoDados
            
            except:
                print('Arquivo não localizado. Verifique o formato do arquivo e o caminho digitado.')


    def titulo_conjunto_dados(): #Define o título que o arquivo CSV terá  
        titulo = str(input('Digite o nome do CSV que você deseja criar: '))
        tituloCsv = titulo + '.csv'

        return tituloCsv


    def precisa_limpar(): #Verifica se existe coluna a ser removida do conjunto de dados
        while True:
        
            try:
                precisaLimpar = str(input('Existem colunas a serem removidas do conjunto de dados (S/N)? '))
                upperPrecisaLimpar = precisaLimpar.upper()
                    
                if upperPrecisaLimpar == 'N':                    
                    return 0
                elif upperPrecisaLimpar == 'S':
                    return 1
                else:
                    raise Exception

            except:
                print("Não entendemos sua resposta.\nDigite S se existem colunas a serem removidas do conjunto de dados e N se não houver.")