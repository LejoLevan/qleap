""" 
hadamard.py

This module provides the Hadamard class, which represents the Hadamard gate operation in the QLeap framework.
"""

from .gate import Gate
from ...qstate import QState

class Hadamard(Gate):
    """Hadamard is a class that represents the Hadamard gate operation in the QLeap framework. 

    The Hadamard gate is a single-qubit gate that creates a superposition of the :math:`|0\\rangle` and :math:`|1\\rangle` states. It transforms the :math:`|0\\rangle` state into :math:`(|0\\rangle + |1\\rangle)/\\sqrt{2}` or known as :math:`|+\\rangle` and the :math:`|1\\rangle` state into :math:`(|0\\rangle - |1\\rangle)/\\sqrt{2}` or known as :math:`|-\\rangle`.
    """
    
    def __init__(self, *args: QState):
        """Creates a Hadamard instance that represents a Hadamard gate operation on the given QState instances.

        Parameters
        ----------
        *args : QState
            The QState instances to be acted on by this Hadamard gate operation.
        """
        super().__init__(args)

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

    def _apply_inverse(self, qi):
        """overrides the _apply_inverse method of the Gate class to apply the inverse of the Hadamard gate, which is the same as the Hadamard gate itself.

        Args:
            qi (QuantumInterface): The quantum interface to which the gate is applied.
        """
        self._apply(qi)
