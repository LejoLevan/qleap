from typing import Collection

from QState import QState
from Operation import Operation

class Gate(Operation):

    def __init__(self, targets: Collection[QState]):
        """
        targets: List of Qubit objects
        
        Creates a new Gate object and assigns the qubits in targets as its arguments
        """

        super().__init__(targets)

    def execute(self, qInterface):
        pass