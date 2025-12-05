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
while m <= M:
    j = 0
    while j<=(N-1):
        qc.rx(2*(t/M)*B,j)
        j+=1
    j = 0
    while j<=(N-2):
        qc.rzz(2*(t/M),j,j+1)
        j+=1
    m+=1
    qc.barrier()

psi_in = Statevector.from_instruction(qc)

psi_out = psi_in.evolve(qc.reverse_bits())
psi_out_dict = psi_out.to_dict()
print(" ")
print("Evolution of |0>")
for basis, amplitude in psi_out_dict.items():
    print(f"|{basis}>: {amplitude}")

qc.draw('mpl')