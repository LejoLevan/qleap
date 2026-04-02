from .gate import Gate
from typing import override

class Swap(Gate):
    def __init__(self, q1, q2, control=None):
        super().__init__((q1, q2))

        self.control = control
        if len(q1) > 1 or len(q2) > 1:
            raise ValueError("Swap targets should be single qubits")
        
        if control is not None and len(control) > 1:
            raise ValueError("Control should be a single qubit")

    @override
    def _apply(self, qi):

        if self.control is None:
            qi.swap(self._targets[0]._start, self._targets[1]._start)
        else:
            qi.cswap(control, self._targets[0]._start, self._targets[1]._start)

    @override
    def _apply_inverse(self, qi):
        self._apply(qi)
