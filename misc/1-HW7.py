# Fractional Quantum Hall States
import numpy as np
# Sets the numpy arrays to truncate numbers with many digits down to 4.
np.set_printoptions(suppress=True,formatter={'all': lambda x: "{:.4g}".format(x)})
from sympy import symbols
from qiskit import QuantumCircuit
from qiskit.circuit.library import UnitaryGate
from qiskit.quantum_info import Operator, Statevector, SparsePauliOp,Pauli
from qiskit.visualization import plot_state_city
from qiskit.primitives import StatevectorEstimator as Estimator

from qiskit.circuit.library import HGate
import cmath
import numpy as np

############################
# -- Initialization     -- #
############################

t = float(input("input t parameter (real): "))
M = int(input("input # of electrons M (integer): "))  
qubits = 3*M - 2
qc = QuantumCircuit(qubits)


def stage0(circuit,qubits):
    i = 0
    while i<qubits:
        circuit.h(i)
        i+=3
    return circuit

list_phi = []

def angles(list_phi,k,t):
    if k>M-2:
        return list_phi
    elif k==0:
        list_phi.append(np.arctan(-t))
        angles(list_phi,k+1,t)
    else:
        list_phi.append(np.arctan(-t*np.cos(list_phi[k-1])))
        angles(list_phi, k+1,t)

def stage1(circuit,qubits,list):
    index = 0
    for i in range(qubits):
        if i%3==1:
            print(i)
            if i==1:
                circuit.ry(-2*list[index],i)
                index+=1
            else:
                circuit.cry(-2*list[index],i-3,i)
                index +=1
    return circuit


def stage2a(circuit,qubits):
    for index in range(qubits):
        if index%3==1:
            circuit.cx(index,index+1)

def stage2b(circuit,qubits):
    for index in range(1,qubits):
        if index%3==1:
            circuit.rz(np.pi,index)
        if index%3==0:
            circuit.cx(index-1,index)

def stage2c(circuit,qubits):
    for index in range(qubits):
        if index%3==1:
            circuit.cx(index,index-1)
        if (index%3==0) and (index!=0):
            circuit.rz(np.pi,index-1)

angles(list_phi,0,t)
list_phi.reverse()

stage0(qc,qubits)
qc.barrier()
stage1(qc,qubits,list_phi)
qc.barrier()
stage2a(qc,qubits)
stage2b(qc,qubits)
stage2c(qc,qubits)

print("----------")
print("")

#observable = SparsePauliOp.from_sparse_list(
#    [("Z",[i],1 / qubits) for i in range(qubits)]
#    ,num_qubits=qubits)
#print(observable)

sv = Statevector.from_instruction(qc)
amplitudes = sv.data
probabilities = np.abs(amplitudes)** 2
n_states = probabilities.size
print(n_states)
indeces = np.arange(n_states,dtype=np.uint64) #standard list of indeces, but large.
ev_list = []
for k in range(qubits): # for each qubit, calculate it's corresponding < Z_j > and append to a list.
    # Pauli string: Z on qubit k, I on all others
    pauli_str = ['I'] * qubits
    pauli_str[k] = 'Z'
    pauli_op = Pauli(''.join(pauli_str)) 
    # Computes expectation value
    ev = sv.expectation_value(pauli_op) # calculates the expectation value for the jth qubit
    ev_list.append(np.real(ev))  # convert to float if complex with zero imaginary part


