import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector,Pauli

N = int(input("Input N qubits:"))
M = int(input("Input steps # M:"))
B = float(input("Input scalar B:"))
t = int(input("Input time t:"))

qc = QuantumCircuit(N)

m=1
while m < M:
    j = 0
    while j<=(N-2):
        qc.rzz(2*(t/M),j,j+1)
        j+=1
    j = 0
    while j<=(N-1):
        qc.rx(2*(t/M)*B,j)
        j+=1
    m+=1

print(qc)