import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import xml.etree.ElementTree as et


def extract_cancelamento(file):
    """
    Extrair e tratar os dados do arquivo de cancelamento,
    chamar a função responsável por inseri-los no banco de dados.
    """
    arquivo = et.parse(file)
    root = arquivo.getroot()
    cartorio = root.find("cartorio")
    titulos = root.find("titulos")

    lista_titulos = []
    lista_devedores = []
    lista_contatos = []
    lista_geral = []

    for i, titulo in enumerate(titulos.findall("titulo")):

        # Extrair as informações do titulo
        cartorio_id = int(cartorio.find("codigo").text.strip())
        protocolo = titulo.find("protocolo").text.strip()
        credor = titulo.find("credor").text.strip().strip()
        valorprotestado = float((titulo.find("valorprotestado").text).replace(",", "."))
        numerotitulo = titulo.find("numerotitulo").text.strip()
        dataprotesto = titulo.find("dataprotesto").text
        mesano = dataprotesto[0:-2].replace("-", "")  # <------------- CAMPO NOVO
        valorboleto = float((titulo.find("valorboleto").text))

        # Extrair informações dos devedores
        devedores = titulo.find("devedores")
        for devedor in devedores.findall("devedor"):
            nome_devedor = devedor.find("nome").text.strip()
            documento_devedor = devedor.find("documento").text

            # Extrair os contatos dos devedores
            telefones = devedor.find("telefones")
            for telefone in telefones.findall("telefone"):
                whatsapp = ""
                if not telefone.text == None and telefone.text.isnumeric():
                    if telefone.text[2] != "3":
                        whatsapp = f"55{telefone.text}"

                lista_contatos.append((documento_devedor, whatsapp))
            lista_devedores.append((documento_devedor, nome_devedor))
        lista_titulos.append(
            (
                cartorio_id,
                protocolo,
                credor,
                valorprotestado,
                numerotitulo,
                dataprotesto,
                mesano,
                valorboleto,
            )
        )

    """                
        reg_titulo = (
            cartorio_id,
            credor,
            protocolo,         
            numerotitulo,
            dataprotesto,
            valorprotestado,
            nome_devedor,
            documento_devedor,
            contato,
        )
        lista_titulos.append(reg_titulo)
        add_titulos.append(titulo_tuple)
    for titulo in add_titulos[0:10]:        
        print(titulo)
    """
    

extract_cancelamento(
    "src/data/CartaCancelamento_005_01102024_a_31102024_vcto_29112024_TODOS_04112024_140302.xml"
)
