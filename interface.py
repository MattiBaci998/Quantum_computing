# Libraries needed 
from abc import ABCMeta, ABC, abstractmethod
from contextlib import contextmanager

# Creation of an object for representing the main operations allowed on a single qubit
class Qubit(metaclass = ABCMeta):
  # Hadamard operator: transforms the state of the qubit (|0> into |+> and |1> into |->)
  # It does not create any copy of it
  @abstractmethod
  def h(self):
    pass
  # Measure operation: it measures the state of the qubit
  @abstractmethod
  def measure(self) -> bool:
    pass 
  # Reset method: it resets the state of the qubit from the scratch
  @abstractmethod
  def reset(self):
    pass 
  
# Defines the basic functions a quantum computing program must have 
class QuantumDevice(metaclass=ABCMeta):
  @abstractmethod
  def allocate_qubit(self) -> Qubit: 
    pass 
  
  @abstractmethod
  def deallocate_qubit(self, qubit:Qubit) -> Qubit: 
    pass 
  
  @contextmanager
  def using_qubit(self):
    qubit = self.allocate_qubit() 
    try:
      yield qubit 
    finally:
      qubit.reset()
      self.deallocate_qubit() 

  








  
