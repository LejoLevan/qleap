How To: Measure Quantum Registers
=================================

Measuring quantum registers in QLeap is a straightforward process that involves using the `Measurement` class to collapse the quantum state of the register into a classical state. 
To measure a quantum register, you can simply pass the `QState` object representing the register to the `Measurement` class. For example, if you have a quantum register with 3 qubits stored in a variable named `qreg`, you can measure it by calling `Measurement(qreg)`.
The results of the measurement will be stored in the `QLeap` instance, and you can retrieve them using the `get_results()` method after running the quantum program. The measurement results will be returned as a list of integers, where each integer represents the measured state of the corresponding qubit in the register (0 for :math:`\ket{0}` and 1 for :math:`\ket{1}`).
They are also stored the `QState` object itself, which can be accessed using the `get_results()` method of the `QState` and `Qubit` class. This allows you to easily access the measurement results directly from the quantum register object after measurement.

.. code-block:: python

    from qleap import QLeap, QState, Measurement

    # Create a Leap instance
    qleap = QLeap()

    # Create a quantum register with 3 qubits
    qreg = QState(3)

    # Measure the quantum register
    Measurement(qreg)

    # Run the quantum program
    qleap.run()

    # Print the measurement result
    print(f'Measurement result: {qleap.get_results()}')

    # Alternatively, you can also access the measurement results directly from the QState object
    print(f'Measurement result from QState: {qreg.get_results()}')

In this code, we first create a quantum register with 3 qubits using the `QState` class. We then measure the quantum register using the `Measurement` class, which collapses the quantum state of the register into a classical state.
After running the quantum program, we print the measurement results using the `get_results()` method of the `QLeap` instance. We also demonstrate how to access the measurement results directly from the `QState` object using its own `get_results()` method.
The results, if working correctly, should show that all qubits in the register are in a superposition state before measurement, and the measurement results will be either 0 or 1 for each qubit, demonstrating that they were in superposition before measurement.
Both methods of accessing the measurement results should yield the same output, confirming that the measurement was successful and the results are consistent.
