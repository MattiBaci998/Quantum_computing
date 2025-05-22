# Libraries needed 
from abc import ABCMeta

# Defines the basic functions a quantum computing program must have 
class QuantumDevice(metaclass=ABCMeta):
  @abstractmethod
  def allocate_qubit(self)->Qubit:
    pass 

  @abstractmethod
  
