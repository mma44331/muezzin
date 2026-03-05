import shutil
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()


class LoadAudio:
    def __init__(self,source_path: Path, project_dir: Path, logger):
        self.logger = logger
        self.source_path = source_path
        self.project_dir = project_dir


    def copy_audio_file(self, source_path: Path, project_dir: Path):
        if not project_dir.exists():
            project_dir.mkdir(parents=True, exist_ok=True)
        try:
            valid_extensions = ['.mp4', '.mp3', '.wav']
            for podcasts in source_path.iterdir():
                if podcasts.is_file() and podcasts.suffix.lower() in valid_extensions:
                    shutil.copy2(podcasts,project_dir / podcasts.name)
            self.logger.info("Copying of files completed successfully.")
            return project_dir
        except Exception as e:
            self.logger.error(f"Copying the files failed {e}")
