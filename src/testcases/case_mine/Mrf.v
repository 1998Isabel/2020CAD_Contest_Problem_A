//
// Conformal-LEC Version 19.20-d218 (25-Feb-2020)
//
module top(A, C, D, O);
input [1:0] C,D;
output [1:0] O;
wire [1:0] w1;

mor \g11877/U$2 ( w1, C, D );
mnot \112 (O, w1);
endmodule

