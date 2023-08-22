from utils import load_data, load_template, add_note, build_response
from urllib.parse import unquote_plus

def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        titulo, detalhe = corpo.split("&")
        params['titulo'] = unquote_plus(titulo.split("=")[1], encoding='utf-8', errors='replace')
        params['detalhes'] = unquote_plus(detalhe.split("=")[1], encoding='utf-8', errors='replace')
        add_note(params)
        # ou, se eu quisesse fazer com for:
        # for chave_valor in corpo.split("&"):
        #     params[unquote_plus(chave_valor.split("=")[0], encoding='utf-8', errors='replace')] = unquote_plus(chave_valor.split("=")[1], encoding="utf-8", errors="replace")

        return build_response(code=303, reason='See Other', headers='Location: /')

    note_template = load_template("components/note.html")
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    return build_response(body=load_template('index.html').format(notes=notes))