from Gate import Gate
from QState import QState
from typing import override

class Hadamard(Gate):
    def __init__(self, target: QState):
        super().__init__(target)
    
    @override
    def _apply(self, qi):
        qi.hadamard(
            start=self._target._start, 
            end=self._target._end
        )