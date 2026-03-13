class RunArguments:
    """
    RunArguments for quantum program
    """

    def __init__(self, shots=2**10, trace=False):
        self.shots = shots
        self.trace = trace