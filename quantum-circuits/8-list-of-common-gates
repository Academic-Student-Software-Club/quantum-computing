import numpy as np
import sympy
from sympy import symbols
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator, Statevector
from qiskit.visualization import plot_state_city
import matplotlib.pyplot as plt

qc = QuantumCircuit(2)


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


print(qc)

