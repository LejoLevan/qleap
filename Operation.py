from typing import Collection

from QState import QState
from QPP import QPP

class Operation():

    def __init__(self, target: QState):
        """
        target: QState
        
        Creates a new Operation object and assigns the qubits in targets as its arguments
        """

        self._target = target
        QPP._add_operation(self)

    def _apply(self, qi):
        raise NotImplementedError
