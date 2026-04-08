""" 
qft.py

This module provides the QFT class, which represents the QFT gate operation in the QLeap framework.
"""

from .gate import Gate
from typing import override

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
        """

        super().__init__(target)
        self._invert = invert
    
    @override
    def _apply(self, qi):

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

    @override
    def _apply_inverse(self, qi):

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

