from vars import ziped_dir,trnscript_dir,file_name,zip_format,dwload_dir
from .zip_rm_cr import rm_dir
from shutil import make_archive

def get_zip(zip_filename):
    """
    Compacta arquivo.
    """
    try:
        rm_dir(zip_filename)
    except:
        print(f"Diretorio '{zip_filename}' será criado")

    make_archive(f'{ziped_dir}{file_name}',f"{zip_format}",f'{dwload_dir}{trnscript_dir}')
    print(f"Arquivo '{file_name}.{zip_format}' foi retornado.")
    name = f"{file_name}.{zip_format}"
    return name