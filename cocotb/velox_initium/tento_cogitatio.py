"""
Viveretur : tento_cogitatio.py
Ab https://docs.cocotb.org/en/stable/quickstart.html
"""
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def tentum_primum(mit):
    """
    Accessum MIT (cogitatio).
    """

    for r in range(10):
        mit.horo.value = 0
        await Timer(1, units="ns")
        mit.horo.value = 1
        await Timer(1, units="ns")

    mit._log.info("res_1 est %s", mit.res_1.value)
    assert mit.res_2.value[0] == 0, "res_2[0] non est 0!"
