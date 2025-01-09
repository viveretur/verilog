// Viveretur : cogitatio.sv
// Ab https://github.com/cocotb/cocotb/blob/master/examples/doc_examples/quickstart/my_design.sv

module cogitatio(input logic horo);

    timeunit 1ns;
    timeprecision 1ns;

    logic res_1;
    logic res_2;

    assign res_1 = 1'bx;
    assign res_2 = 0;

endmodule

