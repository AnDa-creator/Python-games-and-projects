from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram
import numpy
import matplotlib

n = 8
n_q = n
n_b = 8

q_c = QuantumCircuit(n_q, n_b)

for j in range(n):
    q_c.measure(j,j)

q_c.draw()

counts = execute(q_c,Aer.get_backend('qasm_simulator')).result().get_counts()
plot_histogram(counts)

