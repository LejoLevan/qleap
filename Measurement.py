from scipy.stats import rv_discrete
from typing import override

from Operation import Operation
from QState import QState
from QPP import QPP

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
            QPP.record_measurement(target)
            qi.measure(
                start=target._start, 
                end=target._end
            )