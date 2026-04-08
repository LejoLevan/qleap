from ..qstate import QState
from ..circuit import Circuit

class Operation():

    def __init__(self, args: tuple[QState]):
        """
        target: QState
        
        Creates a new Operation object and assigns the qubits in targets as its arguments
        """

        self._targets = args
        Circuit._add_operation(self)

    def _apply(self, qi):
        raise NotImplementedError
    
    def _apply_inverse(self, qi):
        raise NotImplementedError
    
    def _has_measurement(self):
        raise NotImplementedError