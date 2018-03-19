from abc import ABC, abstractmethod

class harvester(ABC):
    @abstractmethod
    def harvest(self):
        pass
