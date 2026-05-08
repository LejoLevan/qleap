""" 
swap.py

This module provides the swap class, which represents the swap gate operation in the QLeap framework.
"""

from .gate import Gate

class Swap(Gate):
    """Swap is a class that represents the Swap gate operation in the QLeap framework.

    The Swap gate switches the state of 2 qubits. For example, it maps :math:`|01\\rangle` to math:`|10\\rangle` and vice versa. An optional control qubit makes this a controlled swap gate, which will only perform the operation if the control is in the state :math:`|1\\rangle`.
    """

    def __init__(self, q1, q2, control=None):
        """Creates a Swap instance that represents a Swap gate operation with the two given qubits. If an optional control qubit is given, this becomes a controlled swap gate.

        Parameters
        ----------
        q1 : QState
            The first qubit in the swap operation.
        q2 : QState
            The second qubit in the swap operation
        control : QState, optional
            The control qubit, which if not None, makes this a controlled swap, by default None.
        
        Raises
        ------
        ValueError
            If q1, q2, or the control argument contain more than one qubit.
        """
        super().__init__((q1, q2))

        self.control = control
        if len(q1) > 1 or len(q2) > 1:
            raise ValueError("Swap targets should be single qubits")
        
        if control is not None and len(control) > 1:
            raise ValueError("Control should be a single qubit")

    def _apply(self, qi):
        """overrides the _apply method of the Gate class to apply the Swap/CSwap gate to the target qubits.

        Args:
            qi (QuantumInterface): The quantum interface to which the gate is applied.
        """
        if self.control is None:
            qi.swap(self._targets[0]._start, self._targets[1]._start)
        else:
            qi.cswap(self.control._start, self._targets[0]._start, self._targets[1]._start)

    def _apply_inverse(self, qi):
        """overrides the _apply_inverse method of the Gate class to apply the inverse of the Swap/CSwap gate, which is the same as itself.

        Args:
            qi (QuantumInterface): The quantum interface to which the gate is applied.
        """
        self._apply(qi)
