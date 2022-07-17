import json
from typing import Dict, Optional, List, Union

numbers: List[Union[int, float]] = [1, 2.2, 3, 4, 5.0]
# List of numbers that can be int or float


class Packet:
  """The structure of packets for both receiver and sender"""

  def __init__(self):
    """Initial data setup"""
    self.flags: Dict[str, bool] = {
        # Type describes a dictionary that maps strings -> booleans
        "syn": False,
        "ack": False,
        "fin": False,
    }
    self.seq: Optional[int] = None
    self.ack: Optional[int] = None
    # Optional type as in the type can be None or an int
    self.data = None
