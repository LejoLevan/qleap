"""
gate.py

This module provides the Gate class, which represents a gate(unitary quantum operation) in the QLeap framework.
"""

from ..operation import Operation

class Gate(Operation):
    def __init__(self, target):
        """
        target: QState collection
        
        Creates a new Gate object and assigns the qubits in target as its arguments. Note that while the Gate is instantiated like an object, the user should treat it like a function being applied to the targets QStates.
        """
        super().__init__(target)

    def _has_measurement(self):
        """
        Overrides _has_measurement in Operation to return false, since Gates do not measure qubits.
        """
        return False