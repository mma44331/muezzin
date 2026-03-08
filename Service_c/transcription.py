import os.path

import speech_recognition as sr

r = sr.Recognizer()
class Transcription:
    def __init__(self,logger):
        self.logger = logger
        self.r = sr.Recognizer()


    def extract_text(self, path_file):
        if not path_file or not os.path.exists(path_file):
            self.logger.error(f"file not found at path: {path_file}")
            return None
        try:
            with sr.AudioFile(path_file) as s:
                audio_data = r.record(s)
            self.logger.info(f"Starting transcription for: {path_file}")
            text = self.r.recognize_google(audio_data)
            self.logger.info(f"Transcription successful for {os.path.basename(path_file)}")
            return text
        except Exception as e:
            self.logger.error(f"An unexpected error occurred: {e}")

        return None



