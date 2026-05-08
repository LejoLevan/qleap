""" 
qft.py

This module provides the QFT class, which represents the QFT gate operation in the QLeap framework.
"""

from .gate import Gate

class Qft(Gate):
    """Qft is a class that represents the QFT gate operation in the QLeap framework.
    
    The QFT gate is a gate that performs the quantum Fourier transform (https://en.wikipedia.org/wiki/Quantum_Fourier_transform). It can act on any number of qubits. It is important for quantum algorithms such as Shor's algorithm.
    """
    def __init__(self, target, invert=False):
        """Creates a Qft instance that represents a QFT gate operation with the given target qubits.

        Parameters
        ----------
        target : QState
            The targets qubit(s) for the QFT gate.
        inverse: boolean, optional
            If True, this gate is an inverse QFT instead. By default, False.
        """

        super().__init__(target)
        self._invert = invert
    
    def _apply(self, qi):
        """overrides the _apply method of the Gate class to apply the QFT or inverse QFT gate to the target qubits.

        Args:
            qi (QuantumInterface): The quantum interface to which the gate is applied.
        """

        if self._invert:
            qi.invQFT(
                start=self._targets._start, 
                end=self._targets._end
            )
        else:
            qi.QFT(
                start=self._targets._start, 
                end=self._targets._end
            )

    def _apply_inverse(self, qi):
        """overrides the _apply_inverse method of the QFT class to apply the inverse of this gate. This is the same as calling _apply with invert=True.

        Args:
            qi (QuantumInterface): The quantum interface to which the gate is applied.
        """
        
        if self._invert:
            qi.QFT(
                start=self._targets._start, 
                end=self._targets._end
            )
        else:
            qi.invQFT(
                start=self._targets._start, 
                end=self._targets._end
            )

