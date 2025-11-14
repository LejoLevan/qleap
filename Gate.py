from abc import ABC, abstractmethod
from typing import Collection

from Qubit import Qubit
from Operation import Operation

class Gate(ABC):

    def __init__(self, targets: Collection[Qubit]):
        """
        targets: List of Qubit objects
        
        Creates a new Gate object and assigns the qubits in targets as its arguments
        """

        self.targets = targets

    @abstractmethod
    def execute(self):
        pass