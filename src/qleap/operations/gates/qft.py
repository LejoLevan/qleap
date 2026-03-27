from ._Gate import Gate
from typing import override

class QFT(Gate):
    
    def __init__(self, target):
        super().__init__(target)
    
    @override
    def _apply(self, qi):

        qi.QFT(
            start=self._targets._start, 
            end=self._targets._end
        )

    @override
    def _apply_inverse(self, qi):
        qi.invQFT(
            start=self._targets._start, 
            end=self._targets._end
        )