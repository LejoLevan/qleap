from typing import Collection

from Gate import Gate

class Operation:

    def __init__(self, gates: Collection[Gate]):
        """
        Creates a new Operation. This represents the action of a quantum circuit at a single time step.
        This class is meant for internal use and should not be instantiated by the user.
        
        gates: a collection of Gate objects to execute
        """

        self.gates = gates

    def execute(self):
        """
        Executes all gates associated with this operation
        """

        for gate in self.gates:
            gate.execute()