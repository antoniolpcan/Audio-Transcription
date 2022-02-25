from fastapi import HTTPException

def check_content_type(i):
    """
    Verifica conteudo recebido.
    """
    if i.content_type not in ["audio/mpeg"]:
        raise HTTPException(415,detail="Arquivo inválido.")
    else:
        print(f"Audio '{i.filename}' válido.")