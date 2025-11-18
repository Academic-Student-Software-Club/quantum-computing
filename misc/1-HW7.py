# Fractional Quantum Hall States
# Example, with M=4 electrons and 3M - 2 qubits.
# Write code that takes integer M and real number t as input.

import numpy as np
# Sets the numpy arrays to truncate numbers with many digits down to 4.
np.set_printoptions(suppress=True,formatter={'all': lambda x: "{:.4g}".format(x)})
from sympy import symbols
from qiskit import QuantumCircuit
from qiskit.circuit.library import UnitaryGate
from qiskit.quantum_info import Operator, Statevector, SparsePauliOp,Pauli
from qiskit.visualization import plot_state_city
from qiskit.primitives import EstimatorResult
from qiskit.primitives import StatevectorEstimator as Estimator
from qiskit_ibm_runtime import EstimatorV2

from qiskit.circuit.library import HGate
import cmath




import numpy as np

t = 0.4
M = 4
qubits = 3*M-2

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

print(qc)
print("----------")
print("")

#observable = SparsePauliOp.from_sparse_list(
#    [("Z",[i],1 / qubits) for i in range(qubits)]
#    ,num_qubits=qubits)
#print(observable)

zop_list = []
for k in range(qubits):
    string="".join("Z"if i==k else "I" for i in range(qubits)  )
    zop_list.append(Pauli(string))
print(zop_list)

pairs = [(qc,observable) for observable in zop_list]

estimator = Estimator()
job = estimator.run(pairs)
print("---------")
result = job.result()
evs = [pub.data.evs for pub in result]
for item in evs:
    print(item)

# and now I move to a python notebook to use matplotlib.

