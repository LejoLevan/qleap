Multiple Circuit
================

In this tutorial, we will learn how to constrcut a program that consists of multiple quantum circuits.
In QLeap, the paradigm is focused on function abstraction to achieve this. 
Circuits should be abstracted into respective functions where a main call function handles how they are ran.

.. code-block:: python

    from qleap import Circuit, Qubit, X, Cnot, Measurement

    # Constructs |10>
    def x_circuit():
        wire1 = Qubit()
        wire2 = Qubit()

        X(wire1)

        Measurement(wire1, wire2)

    # Consctructs |11>
    def x_cnot_circuit():
        wire1 = Qubit()
        wire2 = Qubit()

        X(wire1)
        Cnot(wire1, wire2)

        Measurement(wire1, wire2)
    
    # Main function to run the circuits
    def main():
        x_circuit()
        Circuit.run()
        print(f'Measurement result: {Circuit.get_results()}')

        x_cnot_circuit()
        Circuit.run()
        print(f'Measurement result: {Circuit.get_results()}')
    
    if __name__ == "__main__":
        main()

In this code, we define two functions, `x_circuit()` and `x_cnot_circuit()`, which construct two different quantum circuits. The first circuit creates the state :math:`\ket{10}` by applying an X gate to the first qubit, while the second circuit creates the state :math:`\ket{11}` by applying an X gate to the first qubit followed by a CNOT gate that entangles the two qubits.
In the `main()` function, we call each circuit function and run the quantum program using `Circuit.run()`. After running each circuit, we print the measurement results to the console. This allows us to see the outcomes of both circuits separately. 

When you run this code, you should see that the measurement result for the first circuit is 10 (in binary), and the measurement result for the second circuit is 11 (in binary), demonstrating that both circuits were executed correctly.