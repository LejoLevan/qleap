from typing import Collection

from QState import QState
from QPP import QPP

class Gate():

    def __init__(self, target: QState):
        """
        targets: List of Qubit objects
        
        Creates a new Gate object and assigns the qubits in targets as its arguments
        """

        self._target = target
        QPP._add_gate(self)

    def _apply(self, qi):
        raise NotImplementedError