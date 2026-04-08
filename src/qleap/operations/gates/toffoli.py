""" 
toffoli.py

This module provides the Toffoli class, which represents the Toffoli gate operation in the QLeap framework.
"""

from .gate import Gate
from ...qstate import QState
from typing import override

class Toffoli(Gate):
    """Toffoli is a class that represents the Toffoli gate operation in the QLeap framework.

    The Toffoli gate is a three-qubit gate that performs a NOT operation on the target qubit if both control qubits are in the state :math:`|1\\rangle`, and does nothing otherwise.
    """
    def __init__(self, control1: QState, control2: QState, *args: QState):
        """Creates a Toffoli instance that represents a Toffoli gate operation with the given control qubits and target qubit.

        Parameters
        ----------
        control1 : QState
            The first control qubit for the Toffoli gate.
        control2 : QState
            The second control qubit for the Toffoli gate.
        *args : QState
            The target qubit for the Toffoli gate.
        
        Raises
        ------
        ValueError
            If the control argument contains more than one qubit.
        """

        super().__init__(args)
        self._control1 = control1
        self._control2 = control2

        if len(control1) > 1:
            raise ValueError("Toffoli control 1 should be a single qubit")
        if len(control2) > 1:
            raise ValueError("Toffoli control 2 should be a single qubit")
        
    @override
    def _apply(self, qi):
        for target in self._targets:
            qi.toffoli(self._control1._start, self._control2._start, target._start) # type: ignore

    @override
    def _apply_inverse(self, qi):
        self._apply(qi)
