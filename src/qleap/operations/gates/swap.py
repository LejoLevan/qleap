from .gate import Gate
from typing import override

class Swap(Gate):
    def __init__(self, q1, q2):
        super().__init__((q1, q2))

        if len(q1) > 1 or len(q2) > 1:
            raise ValueError("Swap targets should be single qubits")
        
    @override
    def _apply(self, qi):
        qi.swap(self._targets[0]._start, self._targets[1]._start)

    @override
    def _apply_inverse(self, qi):
        self._apply(qi)
