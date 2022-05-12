from typing import List, Dict
from abc import ABC, abstractclassmethod

class HtmlCollectorInterface(ABC):

    @abstractclassmethod
    def collect_essential_information(self, html: str) -> List[Dict[str, str]]:
        pass