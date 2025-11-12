# This file contains the template for 
# all the libraries/initial definitions
# I like using with qiskit.

import numpy as np
# Sets the numpy arrays to truncate numbers with many digits down to 4.
np.set_printoptions(suppress=True,formatter={'all': lambda x: "{:.4g}".format(x)})
from sympy import symbols
from qiskit import QuantumCircuit
from qiskit.circuit.library import UnitaryGate
from qiskit.quantum_info import Operator, Statevector
from qiskit.visualization import plot_state_city

from qiskit.circuit.library import HGate
import cmath

NUM_BITS = ""
qc = QuantumCircuit(NUM_BITS)


unitary = Operator(qc.reverse_bits()).data


# This, for every initial state I want, 
# displays the final state(s) 
# as a result of evolution through the circuit.
initial_states=['000','010','100','110','111']
    
for state in initial_states:
    psi_in = Statevector.from_label(state)
    # I had to reverse the bits here to make it a little
    # easier to see. Same answer, just with *our* 
    # notation of qubit order.
    psi_out = psi_in.evolve(qc.reverse_bits())
    psi_out_dict = psi_out.to_dict()
    print(" ")
    print("Evolution of |"+state+">")
    for basis, amplitude in psi_out_dict.items():
        print(f"|{basis}>: {amplitude}")

# This suppresses the tiny tiny numbers 
# that result from Python being Python.
threshold = 1e-10
unitary.real[np.abs(unitary.real) < threshold] = 0
unitary.imag[np.abs(unitary.imag) < threshold] = 0

U = Operator(qc)
# --- MATRIX & DIMENSIONS ---
print("=== MATRIX & DIMENSIONS ===")
print("Matrix (U.data):\n", U.data)
print("Matrix shape (U.shape):", U.shape)
print("Dimension tuple (U.dim):", U.dim)
print("Input dims (U.input_dims()):", U.input_dims())
print("Output dims (U.output_dims()):", U.output_dims())
print("Number of qubits (U.num_qubits):", U.num_qubits)

# --- OPERATOR PROPERTIES ---
print("\n=== OPERATOR PROPERTIES ===")
print("Is unitary (U.is_unitary()):", U.is_unitary())
print("Is identity (U.is_identity()):", U.is_identity())
print("Adjoint (U.adjoint().data):\n", U.adjoint().data)
print("Inverse (U.inverse().data):\n", U.inverse().data)

# --- TRANSFORMATIONS & CONVERSIONS ---
print("\n=== TRANSFORMATIONS & CONVERSIONS ===")
print("Matrix from U.to_matrix():\n", U.to_matrix())
print("Equivalent to itself (U.equiv(U)):", U.equiv(U))
print("Convert to instruction (U.to_instruction()):", U.to_instruction())

# Compose and tensor examples
U2 = Operator(QuantumCircuit(1))
print("\nTensor product (U.tensor(U2)).shape:", U.tensor(U2).shape)
print("Expanded tensor (U.expand(U2)).shape:", U.expand(U2).shape)

# --- EXTRA USEFUL METHODS ---
print("\n=== EXTRA USEFUL METHODS ===")
# You can use NumPy for eigenvalues or powers, etc.
eigs = np.linalg.eigvals(U.data)
print("Eigenvalues (np.linalg.eigvals(U.data)):\n", eigs)
print("U squared (U.power(2)).data:\n", U.power(2).data)
print("Copy of operator (U.copy()):", U.copy())

# --- SUMMARY ---
print("\n=== SUMMARY ===")
print(f"U acts on {U.num_qubits} qubits, has shape {U.shape}, and is unitary:", U.is_unitary())

# -- Hadamard -- #
# The Hadamard gate is a rotation of pi around an axis 
# halfway between the x and z axes on the bloch sphere.
H = 1/np.sqrt(2)*np.array([[1,1]
                        ,[1,-1]])
qc.h(0)
# Qiskit has a defined H gate as shown above..


# -- The Paulis -- #
X = np.array([[0,1],
            [1,0]])
# X is a rotation about the x axis of the bloch sphere by a factor of pi.
Y = np.array([[0,-1j],
            [1j,0]])
# Y is a rotation about the y axis of the bloch sphere by a factor of pi.
Z = np.array([[1,0],
            [0,-1]])
# Z is a rotation about the z axis of the bloch sphere by a factor of pi.

# Qiskit has pre-defined transformation as shown:
qc.x(0)
qc.y(0)
qc.z(0)

# -- Phase Gate -- #
S = np.array([[1,0],
            [0,1j]])
# Qiskit has a predefined S Gate as shown:
qc.s(0)


# -- pi/8 Gate (T) -- #
T = np.array([[1,0],
            [0,np.exp(1j*(np.pi)/4)]])
# Qiskit has a predefined T-gate as shown:
qc.t(0)