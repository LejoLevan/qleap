""" 
cnot.py

This module provides the Cnot class, which represents the CNOT gate operation in the QLeap framework.
"""

from .gate import Gate
from ...qstate import QState

class Cnot(Gate):
    """Cnot is a class that represents the CNOT gate operation in the QLeap framework.
    
    The CNOT gate is a two-qubit gate that performs a NOT operation on the target qubit(s) if the control qubit is in the state :math:`|1\\rangle`, and does nothing if the control qubit is in the state :math:`|0\\rangle`.
    """
    def __init__(self, control: QState, *args: QState):
        """Creates a Cnot instance that represents a CNOT gate operation with the given control qubit and target qubits.

        Parameters
        ----------
        control : QState
            The control qubit for the CNOT gate.
        *args : QState
            The target qubit(s) for the CNOT gate.
        
        Raises
        ------
        ValueError
            If the control argument contains more than one qubit.
        """

        super().__init__(args)
        self._control = control

        if len(control) > 1:
            raise ValueError("Cnot control should be a single qubit")
        
    def _apply(self, qi):
        """overrides the _apply method of the Gate class to apply the CNOT gate to the target qubits. Only the first qubit of the target is affected.

        Args:
            qi (QuantumInterface): The quantum interface to which the gate is applied.
        """
        for target in self._targets:
            qi.cnot(self._control._start, target._start) # type: ignore

    def _apply_inverse(self, qi):
        """overrides the _apply_inverse method of the Gate class to apply the inverse of the CNOT gate, which is the same as the CNOT gate itself.

        Args:
            qi (QuantumInterface): The quantum interface to which the gate is applied.
        """
        self._apply(qi)
