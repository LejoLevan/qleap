from Qubit import Qubit
from Hadamard import Hadamard
from Measurement import Measurement
from Cnot import Cnot
from QPP import QPP
from QState import QState

if __name__ == '__main__':
    print('running')

    """
    # Simple program
    q = Qubit()
    Hadamard(q)
    m = Measurement(q)

    QPP.run()"""

    """
    q1 = Qubit()
    q2 = Qubit()
    q3 = Qubit()

    Hadamard(q1, q2)
    #Cnot(q1, q2)
    Measurement(q1, q2)

    QPP.run()

    print({f'The Measurement results are: {QPP.get_results().counts}'})
    QPP.draw()

    print(f'q1: {q1.get_results()}')
    print(f'q2: {q2.get_results()}')
    print(f'q3: {q3.get_results()}')

    print(QPP.get_results())
    """

    qs = QState(2)
    q0 = qs[0]
    q1 = Qubit()

    Hadamard(qs[0])
    Cnot(q0, qs[1])
    Hadamard(q1)

    Measurement(qs, q1)
    QPP.run()
    QPP.draw()

    print(QPP.get_results())
    print(qs.get_results())
    print(q1.get_results())