""" 
z.py

This module provides the Z class, which represents the Z gate operation in the QLeap framework.
"""

from .gate import Gate
from ...qstate import QState

class Z(Gate):
    """Z is a class that represents the Z gate operation in the QLeap framework.

    The Z gate is a single-qubit gate that flips the phase of a qubit. It transforms the :math:`|0\\rangle + |1\\rangle` state into the :math:`|0\\rangle - |1\\rangle` state and the :math:`|0\\rangle - |1\\rangle` state into the :math:`|0\\rangle + |1\\rangle` state.
    """

    def __init__(self, *args: QState):
        """Creates a Z instance that represents a Z gate operation on the given QState instances.

        Parameters
        ----------
        *args : QState
            The QState instances to be acted on by this Z gate operation. Since this accepts an arbitrary number of arguments, Z(q1, q2) is equivalent to `Z(q1)` and then `Z(q2)`.
        """
        super().__init__(args)
    
    def _apply(self, qi):
        """overrides the _apply method of the Gate class to apply the Z gate to the target qubits.

        Args:
            qi (QuantumInterface): The quantum interface to which the gate is applied.
        """

        for target in self._targets:
            qi.z(
                start=target._start, 
                end=target._end
            )

    def _apply_inverse(self, qi):
        """overrides the _apply_inverse method of the Gate class to apply the inverse of the Z gate, which is the same as the Z gate itself.

        Args:
            qi (QuantumInterface): The quantum interface to which the gate is applied.
        """

        self._apply(qi)
