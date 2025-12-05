from Qubit import Qubit
from Hadamard import Hadamard
from Measurement import Measurement
from Cnot import Cnot
from QPP import QPP

if __name__ == '__main__':
    print('running')

    """
    # Simple program
    q = Qubit()
    Hadamard(q)
    m = Measurement(q)

    QPP.run()"""

    q1 = Qubit()
    q2 = Qubit()
    
    Hadamard(q1)
    Cnot(q1, q2)
    Measurement(q1, q2)

    QPP.run()