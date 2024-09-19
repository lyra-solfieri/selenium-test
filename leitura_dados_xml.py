import xml.etree.ElementTree as ET

def ler_dados_xml(caminho_arquivo):
    tree = ET.parse(caminho_arquivo)
    root = tree.getroot()

    procedimentos = []
    for procedimento in root.findall('procedimento'):
        nome_procedimento = procedimento.get('nome')
        casos = []
        for caso in procedimento.findall('caso'):
            dados_caso = {element.tag: element.text for element in caso}
            casos.append(dados_caso)
        procedimentos.append({'nome': nome_procedimento, 'casos': casos})

    return procedimentos
