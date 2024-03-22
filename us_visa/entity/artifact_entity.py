from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    trained_file_path:str # it returns the path to the trained model
    test_file_path:str  # it returns the path to the test data