from datetime import datetime
from pathlib import Path


class GetMetadata:
    def __init__(self,logger):
        self.logger = logger

    def get_metadata(self,audio_path:Path):
        try:
            if not audio_path.exists():
                self.logger.info(f"File: {audio_path}  not found")
                return None
            stats = audio_path.stat()
            self.logger.info("Metadata extraction completed successfully.")
            return {
                "name":audio_path.name,
                "size_bytes": stats.st_size,
                "format": audio_path.suffix.lower().replace('.',''),
                "create_at": datetime.fromtimestamp(stats.st_ctime).isoformat()
            }
        except Exception as e:
            self.logger.error(f"Error extracting metadata from {audio_path}: {e}")
            raise