"""Hadamard Gate
"""

from .gate import Gate
from ...qstate import QState
from typing import override

class Hadamard(Gate):
    """The Hadamard gate is a single-qubit operation that creates superposition by changing into the Hadamard basis. 
    """
    def __init__(self, *args: QState):
        """
        Initializes the Hadamard gate.

        Args:
            *args (QState): The qubit(s) to which the gate is applied.
        """
        super().__init__(args)
    
    @override
    def _apply(self, qi):
        """overrides the _apply method of the Gate class to apply the Hadamard gate to the target qubits.

        Args:
            qi (QuantumInterface): The quantum interface to which the gate is applied.
        """

        for target in self._targets:
            qi.hadamard(
                start=target._start, 
                end=target._end
            )
    
    @override
    def _apply_inverse(self, qi):
        """overrides the _apply_inverse method of the Gate class to apply the inverse of the Hadamard gate, which is the same as the Hadamard gate itself.

        Args:
            qi (QuantumInterface): The quantum interface to which the gate is applied.
        """
        self._apply(qi)