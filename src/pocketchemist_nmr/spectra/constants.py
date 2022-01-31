"""
Constants and enum types for NMRSpectra
"""
from enum import Enum

__all__ = ('DomainType',)


# Enumeration types
class DomainType(Enum):
    """The data domain type for a dimension"""
    UNKNOWN = 0  # Unknown domain type
    TIME = 1  # Time domain data (in sec)
    FREQ = 2  # frequency domain data (in Hz)


class DataType(Enum):
    """The type of data values"""
    UNKNOWN = 0  # Unknown data type
    REAL = 1  # Real data
    IMAG = 2  # Imaginary data
    COMPLEX = 3  # Complex data containing real and imag components