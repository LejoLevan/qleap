""" 
z.py

This module provides the Z class, which represents the Z gate operation in the QLeap framework.
"""

from .gate import Gate
from ...qstate import QState
from typing import override

class Z(Gate):
    """Z is a class that represents the Z gate operation in the QLeap framework.

    The Z gate is a single-qubit gate that flips the phase of a qubit. It transforms the :math:`|0\\rangle + |1\\rangle` state into the :math:`|0\\rangle - |1\\rangle` state and the :math:`|0\\rangle - |1\\rangle` state into the :math:`|0\\rangle + |1\\rangle` state.
    """

    def __init__(self, *args: QState):
        """Creates a Z instance that represents a Z gate operation on the given QState instances.

        Parameters
        ----------
        *args : QState
            The QState instances to be acted on by this Z gate operation.
        """
        super().__init__(args)
    
    @override
    def _apply(self, qi):

        for target in self._targets:
            qi.z(
                start=target._start, 
                end=target._end
            )

    @override
    def _apply_inverse(self, qi):
        self._apply(qi)
