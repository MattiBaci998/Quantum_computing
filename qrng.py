# Mattia Bacigalupo, 2025/05/24
# Creation of random states of the qubit using a quantum computer generator
# Reference to the book "Learn Quantum Computing with Python and Q#" by
# Sarah Kaiser and Cassandra Granade, published by Manning Publications Co.
# Book ISBN 9781617296130.

import interface as irf 
import simulator as sim 

def qrng(device: irf.QuantumDevice) -> bool:
    with device.using_qubit() as q:
        q.h() 
        return q.measure() 
    
# Main program 
if __name__ == "__main__":
    qsim = sim.SingleQubitSimulator()
    for i in range(100):
        random_sample = qrng(qsim)
        print(f"Our quantum random number generator returned:\n{random_sample}")







