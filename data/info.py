
env_config_map: dict = {
    "nitlab": {
        "mimiciv": "F:/datasets/MIMIC-IV 3.0/physionet.org/files/mimiciv/3.0"
    },
    "superpc": {
        "mimiciv": "C:/out_the_drive/datasets_in_use/MIMIC-IV-3.0/files/mimiciv/3.0"
    }
}

class InfoData():
    def __init__(self, 
        env: str = "nitlab"
    ) -> None:
        
        self.mimiciv_directory_path = env_config_map["superpc"]["mimiciv"]