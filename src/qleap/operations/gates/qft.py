from .gate import Gate
from typing import override

class QFT(Gate):
    
    def __init__(self, target, invert=False):
        super().__init__(target)
        self._invert = invert
    
    @override
    def _apply(self, qi):

        if self._invert:
            self._apply_inverse(qi)
        else:
            qi.QFT(
                start=self._targets._start, 
                end=self._targets._end
            )

    @override
    def _apply_inverse(self, qi):

        if self._invert:
            self._apply(qi)
        else:
            qi.invQFT(
                start=self._targets._start, 
                end=self._targets._end
            )
