# Libraries needed 
from abc import ABCMeta, ABC, abstractmethod
from contextlib import contextmanager

# Defines the basic functions a quantum computing program must have 
class QuantumDevice(metaclass=ABCMeta):
  @abstractmethod
  def allocate_qubit(self) -> Qubit: 
    pass 
  
  @abstractmethod
  def deallocate_qubit(self) -> Qubit: 
    pass 
  
  @contextmanager
  def using_qubit(self):
    qubit = self.allocate_qubit() 
    try:
      yield qubit 
    finally:
      qubit.reset()
      self.deallocate_qubit() 

      

  
