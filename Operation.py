from typing import Collection

from QState import QState
from QPP import QPP

class Operation():

    def __init__(self, targets: Collection[QState]):
        """
        targets: List of Qubit objects
        
        Creates a new Operation object and assigns the qubits in targets as its arguments
        An operation might be a gate or a measurement
        """

        self.targets = targets
        QPP.get_instance()._add_operation(self)

    def execute(self, qInterface):
        pass