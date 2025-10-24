
import numpy as np
from sympy import symbols
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator, Statevector
from qiskit.visualization import plot_state_city

from qiskit.circuit.library import HGate
import cmath


# Decompose the doubly controlled Hadamard gate below in terms of
#CNOT and single-qubit gates. You will need to find a matrix V such
#that V^2 = H and decompose V as e^iαAXBXC with ABC = I


if 1==2:
    qc1 = QuantumCircuit(3)
    h_gate = HGate()
    cch_gate = h_gate.control(1)
    
    qc1.append(cch_gate,[0,1])
    unitary1 = Operator(qc1.reverse_bits()).data
    print(np.round(unitary1,2))
    print(qc1)

# HW 4 problem 1
# This is just finding eigenvalues/vectors bruh
# At least thisll be practice for doing it in python 
# cuz its easy AF for 2x2 matrices by hand
a = symbols('a')

H = (1/np.sqrt(2))*np.array([[1,1],[1,-1]])
e_val,P = np.linalg.eig(H)
P2 = np.array([[1+np.sqrt(2),1],[1-np.sqrt(2),1]])
D=np.array([[e_val[0],0],[0,e_val[1]]])
P_inv = np.linalg.inv(P)
P2_inv = np.linalg.inv(P2)
print(P2@D@P2_inv)
print("----------------")

# Create V and V_dagger.
# They are defined as P (sqrt(D)) P^-1

D2=np.array([[cmath.sqrt(e_val[0]),0],[0,np.round(cmath.sqrt(e_val[1]))]])
V = P@D2@P_inv
V_dagger = V.conj().T
print(V)
print(V_dagger)
print("--------------")
print(V@V_dagger)
print(np.round(V@V_dagger))

print("-------------------")




