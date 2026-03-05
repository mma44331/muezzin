from orchestrator import Orchestrator
from config import MetadataConfig
from get_metadata import GetMetadata
from publish_kafka import PublishKafka
from pathlib import Path
from shards.logger_menager import Logger
from shards.audio_utils import LoadAudio



logger = Logger.get_logger(name="SERVICE_A",index="muezzin_metadata_a")

config = MetadataConfig()
load_audio = LoadAudio(config.source_path,config.project_dir,logger)
get_metadata = GetMetadata(logger)
publisher = PublishKafka(config.bootstrap_servers,config.topic_metadata,logger)
orchestrator = Orchestrator(config,get_metadata,publisher,logger)

def main():
    load_audio.copy_audio_file(Path(config.source_path), Path(config.project_dir))
    orchestrator.process_audio()

if __name__ == "__main__":
    main()