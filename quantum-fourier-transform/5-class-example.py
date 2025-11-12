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


def R(k):
    R = np.array([[1,0],[0,np.e**(2*np.pi*1j/(2**k))]])
    Rgate = UnitaryGate(R,label=("R"+str(k+1)))
    cR = Rgate.control(1,label=("R"+str(k+1)))
    return cR

def QFT(circuit,n):
    for j in range(n):
        circuit.h(j)

        for k in range(j+1,n):
        
            
            circuit.append(R(k),[k,j])
        circuit.barrier()
    
    for i in range(n//2):
        circuit.swap(i,n-i-1)
    return circuit

n = 9

qc = QuantumCircuit(n)

QFT(qc,n)
print(qc)