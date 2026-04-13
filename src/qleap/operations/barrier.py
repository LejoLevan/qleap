"""
barrier.py

This module provides the Barrier class, which represents a barrier operation in the QLeap framework.
"""

from .operation import Operation
from ..qstate import QState

class Barrier(Operation):
    """Barrier is a class that represents a barrier operation in the QLeap framework.

    The Barrier operation is used to separate different sections of a quantum circuit. It does not perform any actual quantum operation, but serves as a visual and logical separator in the circuit. The barrier can be applied to one or more qubits, and it indicates that all operations before the barrier should be completed before any operations after the barrier are executed.
    """

    def __init__(self, *args: QState):
        """Creates a Barrier instance that represents a barrier operation on the given QState instances.

        Parameters
        ----------
        *args : QState
            The QState instances to which this barrier operation will be applied.
        """

        super().__init__(args)
    
    def _apply(self, qi):
        """overrides the _apply method of the Operation class to apply the barrier operation to the target qubits.
        
        Args:
            qi (QuantumInterface): The quantum interface to which the barrier operation is applied.
        """
        for target in self._targets:
            qi.barrier(
                start=target._start, 
                end=target._end
            )

    def _apply_inverse(self, qi):
        pass

