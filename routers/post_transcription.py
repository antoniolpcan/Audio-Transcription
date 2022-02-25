from functions.transcription import transcription_audio
from fastapi import Depends
from fastapi.responses import FileResponse
from .router_config import router
from vars import ziped_dir,zip_format,name_routers

@router.post(f"{name_routers[0]}")
async def post_transcription(response = Depends(transcription_audio)):
    return FileResponse(path = f'{ziped_dir}{response}',filename = f'{response}',media_type=zip_format)