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