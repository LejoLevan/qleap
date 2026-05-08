"""
operation.py

This module provides the Operation class, which represents an arbitrary quantum operation, such as a gate or a measurement.
"""

from ..qstate import QState
from ..circuit import Circuit

class Operation():

    def __init__(self, args: tuple[QState]):
        """
        target: QState tuple
        
        Creates a new Operation object and assigns the qstates in args as its targets. While applying Operation(q) is instantiating an operation with q, the user should think of it as applying an Operation method to q.
        """

        self._targets = args
        Circuit._add_operation(self)

    def _apply(self, qi):
        """Applies the operation to self._targets. Abstract method to be implemented by child classes.

        Args:
            qi (QuantumInterface): The quantum interface to which the operation is applied.
        """

        raise NotImplementedError
    
    def _apply_inverse(self, qi):
        """Applies the inverse of the operation in to self._targets. Abstract method to be implemented by child classes.

        Args:
            qi (QuantumInterface): The quantum interface to which the operation is applied.
        """
        raise NotImplementedError
    
    def _has_measurement(self):
        """Indicates whether this operation applies a measurement to its targets. The backend relies on this information when building a QLeap program to execute."""
        raise NotImplementedError