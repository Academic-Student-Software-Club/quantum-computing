import numpy as np
import sympy
from sympy import symbols
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator, Statevector
from qiskit.visualization import plot_state_city
import matplotlib.pyplot as plt

X = np.array([[0,1],[1,0]])
Y = np.array([[0,-1j],[1j,0]])
Z = np.array([[1,0],[0,-1]])

a, b, c = symbols('a b c')

U = np.exp(a)
print(U)


