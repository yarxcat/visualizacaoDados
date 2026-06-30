
import requests

def enviar_arquivos():
    #caminho do arquivo para upload
    caminho = r'C:/Users/Yara/Downloads/produtos_informatica.xlsx'

    # OBTEM SERVIDOR DE UPLOAD
    resposta = requests.get("https://api.gofile.io/servers")
    servidor = resposta.json()['data']['servers'][0]['name']

    # ENVIAR ARQUIVO
    with open(caminho, 'rb') as arquivo:
        upload = requests.post(
            f"https://{servidor}.gofile.io/uploadFile",
            files={'file': arquivo}
        )

    return upload.json()

def receber_arquivos(dados):
    link = dados['data']['downloadPage']
    arquivo = dados['data']['name']
    tamanho = dados['data']['size']
    print("Nome:", arquivo, '\nTamanho:', tamanho, '\nLink:', link)
    
    

dados = enviar_arquivos()
link2 =receber_arquivos(dados)  
print(link2)





