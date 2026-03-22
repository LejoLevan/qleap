""" 
x.py

This module provides the X class, which represents the X gate operation in the QLeap framework.
"""

from .gate import Gate
from ...qstate import QState
from typing import override

class X(Gate):
    """X is a class that represents the X gate operation in the QLeap framework.

    The X gate, also known as the NOT gate, is a single-qubit gate that flips the state of a qubit. It transforms the :math:`|0\\rangle` state into the :math:`|1\\rangle` state and the :math:`|1\\rangle` state into the :math:`|0\\rangle` state.
    """

    def __init__(self, *args: QState):
        """Creates an X instance that represents an X gate operation on the given QState instances.

        Parameters
        ----------
        *args : QState
            The QState instances to be acted on by this X gate operation.
        """
        super().__init__(args)
    
    @override
    def _apply(self, qi):

        for target in self._targets:
            qi.x(
                start=target._start, 
                end=target._end
            )

    @override
    def _apply_inverse(self, qi):
        self._apply(qi)
