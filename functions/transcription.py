from functions.check.__init__ import check_content_type
from .transcript.__init__ import transcription
from .create_file.__init__ import file_res,cria_pasta,get_zip
from io import BytesIO
from fastapi import UploadFile,File,Body,HTTPException
from typing import List
from vars import file_columns

async def transcription_audio(file: List[UploadFile] = File(...),language_audio: str = Body("pt-BR"),formato_saida: str = Body("json")):
    """
    Api transcrever áudio.
    """
    t = []
    for i in file:
        name = i.filename
        check_content_type(i)
        arq = await i.read()
        arqu=BytesIO(arq)
        transcript = transcription(arqu,language_audio)
        t.append({f"{file_columns[0]}":name,f"{file_columns[1]}":transcript})
    cria_pasta()
    file_res(t,formato_saida)
    name = get_zip()
    return name