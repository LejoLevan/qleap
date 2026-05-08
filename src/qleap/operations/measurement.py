"""
measurement.py

This module provides the Measurement class, which represents a measurement operation in the QLeap framework.
"""

from .operation import Operation
from ..qstate import QState
from ..circuit import Circuit

class Measurement(Operation):
    """Measurement is a class that represents a measurement operation in the QLeap framework.

    The Measurement operation measures the state of the target qubits and collapses them to a classical state. The measurement results are recorded in the QLeap framework for later retrieval.
    """

    def __init__(self, *args: QState):
        """Creates a Measurement instance that represents a measurement operation in computational/Z basis on the given QState instances.

        Parameters
        ----------
        *args : QState
            The QState instances to be measured by this measurement operation.
        """

        super().__init__(args)
    
    def _apply(self, qi):
        """overrides the _apply method of the Operation class to apply the Measurement gate to the target qubits.

        Args:
            qi (QuantumInterface): The quantum interface to which the Measurement is applied.
        """
        
        for target in self._targets:
            Circuit._record_measurement(target) # notifies the Circuit to save the measurement done to the target qState.
            qi.measure(
                start=target._start, 
                end=target._end
            )

    def _has_measurement(self):
        """
        Overrides _has_measurement in Operation to indicate that this class performs a measurement.
        """
        return True
