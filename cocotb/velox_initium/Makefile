# Viveretur : Makefile
# Ab https://docs.cocotb.org/en/stable/quickstart.html

# regula
SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/cogitatio.sv

TOPLEVEL = cogitatio

MODULE = tento_cogitatio

include $(shell cocotb-config --makefile)/Makefile.sim

