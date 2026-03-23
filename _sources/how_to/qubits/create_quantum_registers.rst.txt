How To: Create Quantum Registers
================================

To create a quantum register in QLeap, you can either use the `QState` class to create a quantum register with a specified number of qubits, 
or you can create individual `Qubit` instances.

.. code-block:: python

    from qleap import QLeap, QState, Qubit, Measurement

    # Create a Leap instance
    qleap = QLeap()

    # Create a quantum register with 3 qubits
    qreg = QState(3)

    # Alternatively, create individual qubits
    q1 = Qubit()
    q2 = Qubit()
    q3 = Qubit()

    # Measure the quantum register
    Measurement(qreg)

    # Run the quantum program
    qleap.run()

    # Print the measurement result
    print(f'Measurement result: {qleap.get_results()}')

In this code, we first create an instance of the `QLeap` class, which serves as the main interface for building and running quantum programs.
Next, we create a quantum register with 3 qubits using the `QState` class. This allows us to represent multiple qubits as a single entity, which can be useful for applying gates and measurements to multiple qubits at once.
Alternatively, we can create individual `Qubit` instances for each qubit we want to use in our quantum program. This gives us more flexibility to manipulate each qubit separately.
Finally, we measure the quantum register, run the quantum program, and print the measurement result. The results, if working correctly, should all be 0 since the qubits are initialized in the :math:`\ket{0}` state by default.