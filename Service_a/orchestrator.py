from pathlib import Path


class Orchestrator:
    def __init__(self,config, g_metadata, publisher, logger):
        self.config = config
        self.g_metadata = g_metadata
        self.publisher = publisher
        self.logger = logger

    def process_audio(self):
        folder = Path(self.config.project_dir)
        try:
            for file_path in folder.iterdir():
                if file_path.is_file():
                    res = self.g_metadata.get_metadata(file_path)
                    res['path'] = f"{self.config.project_dir}/{res['name']}"
                    self.logger.info(res)
                    self.publisher.send_to_kafka(res)
                    self.logger.info(f"sending to kafka event audio: {res['name']}")
        except Exception as e:
            self.logger.error(f"Failed to send to kafka: {e}")