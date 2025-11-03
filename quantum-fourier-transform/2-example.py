from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np

# THIS IS NOT MY WORK!!!
# I pulled this from ChatGPT,
# and tried commenting over it,
# for my own learning benefit.


# This defines a function to perform the Quantum Fourier Transform 
# on the first n qubits of a circuit.
def qft(circuit, n):
    # Loops over each qubit j (from 0 to n-1)
    for j in range(n):
        # Applies a Hadamard gate to qubit j.
        # This creates a superposition, which is the first step of the QFT.
        circuit.h(j)
        # Loops over the qubits after j to apply controlled phase rotations, 
        # which encode the relative phases in the Fourier basis.
        for k in range(j+1, n):
            # Computes the rotation angle for the controlled phase
            angle = np.pi / 2**(k-j)
            # Applies a controlled-phase gate:
            # qubit k is the control, qubit j is the target, 
            # and the target’s phase is rotated by angle if the control is |1>.
            circuit.cp(angle, k, j)
    for i in range(n//2):
        # After the rotations, QFT reverses the order of qubits.
        # This loop swaps qubits from start to end to correct the order.
        circuit.swap(i, n-i-1)
    return circuit

# Circuit
n = 2
qc = QuantumCircuit(n)
qc.x(0)
qc.x(n-1)
qft(qc, n)

# Get statevector without Aer
state = Statevector.from_instruction(qc)
state_dict = state.to_dict()
for basis, amplitude in state_dict.items():
            print(f"|{basis}>: {amplitude}")

print("------")
print(qc)
