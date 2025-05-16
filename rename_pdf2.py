import os
import pandas as pd
from pdfquery import PDFQuery
from tqdm.auto import tqdm
import random

caminho_pdf = './pdfs'
caminho_xml = './xml'

names_files = {
    'Nome': {
        'precisa_extrair_codigo': True,
        'xml_codigo': [
            '204.777, 395.127, 435.936, 407.127',
            '239.875, 380.127, 432.994, 392.127',
            '204.777, 395.127, 447.244, 407.127',
            '204.777, 395.127, 446.617, 407.127',
            '204.777, 395.127, 446.576, 407.127',
            '204.777, 395.127, 445.709, 407.127',
            '204.777, 395.127, 441.83, 407.127',
            '204.777, 395.127, 441.801, 407.127',
            '204.777, 395.127, 422.629, 407.127',
            '239.875, 395.127, 407.242, 407.127',
            '204.777, 395.127, 403.955, 407.127',
            '204.777, 395.127, 403.937, 407.127',
            '204.777, 395.127, 399.801, 407.127',
            '239.875, 410.127, 446.793, 422.127',
            '204.777, 425.127, 343.926, 437.127',
            '204.777, 425.127, 333.244, 437.127',
            '204.777, 425.127, 326.564, 437.127',

        ],
    },
}

def extrair_pdf_conteudo(pdf, nome_do_arquivo):
    conteudo = {}
    for chave, valor in names_files.items():
        texto = ''
        for codigo in valor.get('xml_codigo', []):
            texto = pdf.pq(f'LTTextLineHorizontal:in_bbox("{codigo}")').text().strip()
            if texto:
                break

        conteudo[chave] = texto
    
    return conteudo


# Lista para armazenar os nomes dos arquivos antigos e novos
nomes_arquivos = []

# Percorrer os arquivos PDF no diretório
for pdf_nome in tqdm(os.listdir(caminho_pdf)):
    if pdf_nome.endswith('.pdf'):
        caminho_do_pdf = os.path.join(caminho_pdf, pdf_nome)
        nome_do_arquivo, _ = os.path.splitext(pdf_nome)

        # Extrair informações do PDF usando o pdfquery
        pdf = PDFQuery(caminho_do_pdf)
        pdf.load()

        # Transformar o PDF em XML para obter os códigos das colunas
        pdf.tree.write(f'{caminho_xml}/{nome_do_arquivo}.xml', pretty_print=True)

        # Extraindo informações do PDF
        dados = extrair_pdf_conteudo(pdf, nome_do_arquivo)

        # Fechar o arquivo PDF
        pdf.file.close()

        # Obter o novo nome do arquivo
        if 'Nome' in dados and dados['Nome'] and dados['Nome'] != ' ':
            novo_nome_pdf = f"{dados['Nome']}.pdf"  # Usando o campo 'Nome' para renomear
            
            # Verificar se o arquivo PDF existe antes de tentar renomeá-lo
            if os.path.exists(os.path.join(caminho_pdf, pdf_nome)):
                nomes_arquivos.append({'antigo': pdf_nome, 'novo': novo_nome_pdf})
            else:
                print(f"O arquivo {pdf_nome} não foi encontrado.")

# Renomear os arquivos
for arquivo in nomes_arquivos:
    caminho_antigo = os.path.join(caminho_pdf, arquivo['antigo'])
    caminho_novo = os.path.join(caminho_pdf, arquivo['novo'])
    
    # Verificar se o arquivo antigo existe antes de tentar renomeá-lo
    try:
        if os.path.exists(caminho_antigo):
            os.rename(caminho_antigo, caminho_novo)     
            print(f"Arquivo renomeado para {arquivo['novo']}")     
        else:
            print(f"O arquivo {arquivo['antigo']} não foi encontrado.")
    except FileExistsError as e:
        print(f"Erro de arquivo com o mesmo nome: {e}")
        pass
