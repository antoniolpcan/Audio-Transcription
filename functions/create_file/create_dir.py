from vars import dwload_dir,trnscript_dir
import os

def cria_pasta():
    """
    Cria pasta para guardar arquivo.
    """
    try:
        for f in os.listdir(f"{dwload_dir}{trnscript_dir}"):
            os.remove(os.path.join(f"{dwload_dir}{trnscript_dir}", f))
        os.rmdir(f"{dwload_dir}{trnscript_dir}")
    except:
        print(f"Pasta '{trnscript_dir}' será criada.")
        
    if not os.path.isdir(f"{dwload_dir}{trnscript_dir}"):
        os.makedirs(f"{dwload_dir}{trnscript_dir}")