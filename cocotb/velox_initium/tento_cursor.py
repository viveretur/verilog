"""
Viveretur : tento_cursor.py
Ab https://docs.cocotb.org/en/stable/quickstart.html#running-a-test
"""

import os
from pathlib import Path

from cocotb.runner import get_runner


def tento_cogitatio_cursor():
    """
    Currite cum pytest cum 'tento'
    """
    sim = os.getenv("SIM", "icarus")
    prop = Path(__file__).resolve().parent
    fons = [prop / "cogitatio.sv"]

    cursor = get_runner(sim)
    cursor.build(
        sources=fons,
        hdl_toplevel="cogitatio"
    )

    cursor.test(
        hdl_toplevel="cogitatio",
        test_module="tento_cogitatio"
    )


if __name__ == "__main__":
    tento_cogitatio_cursor()
