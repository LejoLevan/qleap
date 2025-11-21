from Qubit import Qubit
from Hadamard import Hadamard
from Measurement import Measurement
from QPP import QPP

if __name__ == '__main__':

    # Simple program
    q = Qubit()
    Hadamard(q)
    Measurement(q)

    QPP.run()