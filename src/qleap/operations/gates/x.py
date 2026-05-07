""" 
x.py

This module provides the X class, which represents the X gate operation in the QLeap framework.
"""

from .gate import Gate
from ...qstate import QState

class X(Gate):
    """X is a class that represents the X gate operation in the QLeap framework.

    The X gate, also known as the NOT gate, is a single-qubit gate that flips the state of a qubit. It transforms the :math:`|0\\rangle` state into the :math:`|1\\rangle` state and the :math:`|1\\rangle` state into the :math:`|0\\rangle` state.
    """

    def __init__(self, *args: QState):
        """Creates an X instance that represents an X gate operation on the given QState instances.

        Parameters
        ----------
        *args : QState
            The QState instances to be acted on by this X gate operation. Since this accepts an arbitrary number of arguments, X(q1, q2) is equivalent to `X(q1)` and then `X(q2)`.
        """
        super().__init__(args)
    
    def _apply(self, qi):
        """overrides the _apply method of the Gate class to apply the X gate to the target qubits.

        Args:
            qi (QuantumInterface): The quantum interface to which the gate is applied.
        """
        for target in self._targets:
            qi.x(
                start=target._start, 
                end=target._end
            )

    def _apply_inverse(self, qi):
        """overrides the _apply_inverse method of the Gate class to apply the inverse of the X gate, which is the same as the X gate itself.

        Args:
            qi (QuantumInterface): The quantum interface to which the gate is applied.
        """
        self._apply(qi)
