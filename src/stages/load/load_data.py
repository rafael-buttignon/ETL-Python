from src.infra.interfaces.database_repository import DatabaseRepositoryInterface
from src.stages.extract.contracts.transform_contract import TransformContract
from src.errors.load_error import LoadError

class LoadData():

    def __init__(self, repository: DatabaseRepositoryInterface) -> None:
        self.__repository = repository

    def load(self, transformed_data_contract: TransformContract) -> None:
        try:
            load_content = transformed_data_contract.load_content
            for data in load_content:
                self.__repository.insert_artist(data)
        except Exception as message:
            raise LoadError(str(message)) from message