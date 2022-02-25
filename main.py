from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.__init__ import router

app = FastAPI()

app.include_router(
    router,
    prefix="/api",                
    tags=["Transcription"],
)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

