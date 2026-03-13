from scipy.stats import rv_discrete
from typing import override

from .operation import Operation
from ..qstate import QState
from ..qleap import Qleap

class Measurement(Operation):

    def __init__(self, *args: QState):
        """
        targets: List of Qubit objects
        
        Creates a new Measurement object and assigns the qubits in targets as its arguments
        """

        super().__init__(args)
    
    @override
    def _apply(self, qi):
        
        for target in self._targets:
            Qleap.record_measurement(target)
            qi.measure(
                start=target._start, 
                end=target._end
            )

    @override
    def has_measurement(self):
        return True
