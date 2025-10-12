import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator, Statevector
from qiskit.visualization import plot_state_city
import matplotlib.pyplot as plt

Y= np.array([[0,-1j],[1j,0]])
H=(1/np.sqrt(2))*np.array([[1,1],[1,-1]])

qc = QuantumCircuit(2)

qc.unitary(Operator(H),[0],label="H")
print("First Act")
unitary_reordered = Operator(qc.reverse_bits()).data
print(np.round(unitary_reordered, 3))
print("-----------")
qc.cy(1,0)
#################################
# Qiskit is really dumb when it 
# comes to bit ordering. It looks like
# the order os backwards, but this matches
# what you get via manual computation.
##################################
print("Second Act")
unitary_reordered = Operator(qc.reverse_bits()).data
print(np.round(unitary_reordered, 3))
print("-----------")
qc.unitary(Operator(H),[1],label="H")
print("Echoes Act 3")
unitary_reordered = Operator(qc.reverse_bits()).data
print(np.round(unitary_reordered, 3))
print("-----------")

initial_state = Statevector.from_label('00')
final_state=initial_state.evolve(qc)
final_state_dict=final_state.to_dict()
print("Evolution of |00>")
for basis, amplitude in final_state_dict.items():
    print(f"|{basis}>: {amplitude}")
print("---------------")
print("drawing of Circuit")
print(qc)

if (1==1):
    print("-------------")
    print("-------------")
    print("second circuit, isolated CNOT-Y unitary")
    qc2 = QuantumCircuit(2)
    qc2.cy(0,1)
    unitary2 = Operator(qc2.reverse_bits()).data
    print(unitary2)
    print(qc2)


print("-----------")
print("Unitary for Reordered Qubits")
unitary_reordered = Operator(qc.reverse_bits()).data
print(np.round(unitary_reordered, 3))

