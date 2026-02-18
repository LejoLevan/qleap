from ._Gate import Gate
from ...QState import QState
from typing import override

class Hadamard(Gate):
    def __init__(self, *args: QState):
        super().__init__(args)
    
    @override
    def _apply(self, qi):

        for target in self._targets:
            qi.hadamard(
                start=target._start, 
                end=target._end
            )