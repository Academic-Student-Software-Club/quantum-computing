import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator, Statevector
from qiskit.visualization import plot_state_city

###############
# This circuit has a problem with the second unitary, U2.
# It seems to be something with Qiskit and 
# multi-bit Unitaries.
# Read more below.
###############


# Initial state |000>
initial_state=Statevector.from_label('000')

# set up unitaries/circuit
U1 = (1/np.sqrt(2))*np.array([[1,1j],[1j,1]])
U2 = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])

qc = QuantumCircuit(3,name="ABC")

#  Act on all three qubits with U1
qc.unitary(Operator(U1),[0],label="U1")
qc.unitary(Operator(U1),[1],label="U1")
qc.unitary(Operator(U1),[2],label="U1")
final_state_1=initial_state.evolve(qc)
final_state_1_dict=final_state_1.to_dict()
print(" Only U1 acted on")
for basis, amplitude in final_state_1_dict.items():
    print(f"|{basis}>: {amplitude}")

print("----------")

# Testing two-bit unitary, ordered [1,2]
qc2 = QuantumCircuit(3,name="ABC")
qc2.unitary(Operator(U1),[0],label="U1")
qc2.unitary(Operator(U1),[1],label="U1")
qc2.unitary(Operator(U1),[2],label="U1")
qc2.unitary(Operator(U2),[0,1],label="U2")

final_state_2=initial_state.evolve(qc2)
final_state_2_dict=final_state_2.to_dict()
print(" U2 acted on pair AB")
for basis, amplitude in final_state_2_dict.items():
    print(f"|{basis}>: {amplitude}")

print("----------")

# Testing two-bit unitary, ordered [1,2]
qc3 = QuantumCircuit(3,name="ABC")
qc3.unitary(Operator(U1),[0],label="U1")
qc3.unitary(Operator(U1),[1],label="U1")
qc3.unitary(Operator(U1),[2],label="U1")
qc3.unitary(Operator(U2),[2,1],label="U2")

final_state_3=initial_state.evolve(qc3)
final_state_3_dict=final_state_3.to_dict()
print("U2 acted on pair BC")
for basis, amplitude in final_state_3_dict.items():
    print(f"|{basis}>: {amplitude}")

print(qc2)
print(qc3)

#############################
# Circuit 1 is a "control" circuit before U2.
# The difference between circuit 2 and 3 is in 
# |010>, |011>, |100>, |101>.
# No idea why this happens- its as if the "bit swap"
# on just BC doesnt actually work.
# Furthermore, I don't see a pattern as to 
# who got the wrong dance partner.
#############################