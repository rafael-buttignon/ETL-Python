from .transform_raw_data import TransformRawData
from src.stages.extract.contracts.mocks.extract_contract import extract_contract_mock

def test_transform():
    transform_raw_data = TransformRawData()
    transformed_information = transform_raw_data.transform(extract_contract_mock)