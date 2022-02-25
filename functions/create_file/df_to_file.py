from vars import dwload_dir,trnscript_dir,file_name
from fastapi import HTTPException
import pandas as pd

def file_res(t,formato_saida):
    """
    Gera arquivo contendo as transcrições.
    """
    
    df = pd.DataFrame(t)

    if formato_saida == "json":
        df.to_json(f'{dwload_dir}{trnscript_dir}/{file_name}.json',indent=4,force_ascii=False,orient='records')
    elif formato_saida in ["xlsx","excel"]:
        df.to_excel(f'{dwload_dir}{trnscript_dir}/{file_name}.xlsx')
    elif formato_saida == "csv":
        df.to_csv(f'{dwload_dir}{trnscript_dir}/{file_name}.csv')
    else:
        raise HTTPException(406,detail = "Formato inválido.")