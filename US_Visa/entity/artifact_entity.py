from dataclasses import dataclass


@dataclass # with this, you can declare class variables without needing self keyword
class DataIngestionArtifact:
    trained_file_path:str 
    test_file_path:str 
    
@dataclass # with this, you can declare class variables without needing self keyword
class DataValidationArtifact:
    validation_status:bool 
    message:str 
    drift_report_file_path: str