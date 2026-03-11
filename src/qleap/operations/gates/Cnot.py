from ._Gate import Gate
from ...QState import QState
from typing import override

class Cnot(Gate):
    def __init__(self, control: QState, *args: QState):
        super().__init__(args)
        self._control = control

        if len(control) > 1:
            raise ValueError("CNOT control should be a single qubit")
        
    @override
    def _apply(self, qi):
        for target in self._targets:
            qi.cnot(self._control._start, target._start) # type: ignore

    @override
    def _apply_inverse(self, qi):
        self._apply(qi)