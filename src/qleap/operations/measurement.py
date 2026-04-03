"""
measurement.py

This module provides the Measurement class, which represents a measurement operation in the QLeap framework.
"""

from scipy.stats import rv_discrete
from typing import override

from .operation import Operation
from ..qstate import QState
from ..qleap import QLeap

class Measurement(Operation):
    """Measurement is a class that represents a measurement operation in the QLeap framework.

    The Measurement operation measures the state of the target qubits and collapses them to a classical state. The measurement results are recorded in the QLeap framework for later retrieval.
    """

    def __init__(self, *args: QState):
        """Creates a Measurement instance that represents a measurement operation on the given QState instances.

        Parameters
        ----------
        *args : QState
            The QState instances to be measured by this measurement operation.
        """

        super().__init__(args)
    
    @override
    def _apply(self, qi):
        
        for target in self._targets:
            QLeap._record_measurement(target)
            qi.measure(
                start=target._start, 
                end=target._end
            )

    @override
    def _has_measurement(self):
        return True
