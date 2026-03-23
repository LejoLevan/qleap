How To: Access Quantum Registers
================================

After creating quantum registers using the `QState` class or individual `Qubit` instances, you can access and manipulate them in various ways.
To access individual qubits within a quantum register created with `QState`, you can use indexing. For example, if you have a quantum register with 3 qubits, you can access the first qubit using `qreg[0]`, the second qubit using `qreg[1]`, and the third qubit using `qreg[2]`.
You can also apply quantum gates to specific qubits within a quantum register. For example, if you want to apply a Hadamard gate to the first qubit in the register, you can do so by calling `Hadamard(qreg[0])`.
If you have created individual `Qubit` instances, you can access and manipulate them directly by using their variable names. For example, if you have created three qubits named `q1`, `q2`, and `q3`, you can apply gates to them by calling `Hadamard(q1)`, `Hadamard(q2)`, and `Hadamard(q3)`.

`QState` splice objects also support slicing, allowing you to access a range of qubits within the register. For example, if you want to access the first two qubits in a register, you can use `qreg[0:2]`, which will return a new `QState` object containing those qubits.
You can also use negative indexing to access qubits from the end of the register. For example, `qreg[-1]` will give you the last qubit in the register, `qreg[-2]` will give you the second-to-last qubit, and so on. This allows for flexible access to qubits within a quantum register, making it easier to manipulate and apply gates to specific qubits as needed.

Then both `QState` and `Qubit` objects can return length using the `len()` function, which will return the number of qubits in the register or the number of qubits in a `QState` slice. This can be useful for iterating over qubits in a register or for checking the size of a quantum register before applying gates or measurements.

.. code-block:: python

    from qleap import QLeap, QState, Qubit, Hadamard, Measurement

    # Create a quantum register with 3 qubits
    qreg = QState(3)

    # Access individual qubits using indexing
    q1 = qreg[0]  # First qubit
    
    # Access a range of qubits using slicing
    q_slice = qreg[1:3]  # Last two qubits

    # Loop over qubits in the register and apply a Hadamard gate to each
    for i in range(len(qreg)):
        Hadamard(qreg[i])
    
    # Measure the qubits in the register
    Measurement(qreg)

    # Run the quantum program
    QLeap.run()

    # Print the measurement result
    print(f'Measurement result: {QLeap.get_results()}')

In this code, we first create a quantum register with 3 qubits using the `QState` class. 
We then access the first qubit using indexing and store it in the variable `q1`. We also access a range of qubits (the last two) using slicing and store them in the variable `q_slice`.
Next, we loop over all qubits in the register using `len(qreg)` to get the number of qubits and apply a Hadamard gate to each qubit in the register.
Finally, we measure the qubits in the register, run the quantum program, and print the measurement result. The results, if working correctly, should show that all qubits in the register are in a superposition state before measurement, and the measurement results will be either 0 or 1 for each qubit, demonstrating that they were in superposition before measurement.

    



    

