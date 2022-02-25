from fastapi import HTTPException
import speech_recognition as sr
from pydub import AudioSegment
import io

export_audio = "wav"

def transcription(file,language_audio):
     """
     Gera transcrição
     """
     try:
          sound=AudioSegment.from_file_using_temporary_files(file)
          sound_export = io.BytesIO()
          sound.export(sound_export,format=export_audio)
          
          r=sr.Recognizer()
          with sr.AudioFile(sound_export) as source:
               audio=r.record(source)
          return r.recognize_google(audio,language=language_audio,show_all=True)
     except:
          raise HTTPException(400,detail=f"Erro ao transcrever o audio na linguagem '{language_audio}'.")