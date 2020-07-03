//
// Conformal-LEC Version 19.20-d218 (25-Feb-2020)
//
module top(A, C, D, O);
input C,D;
output O;
wire w1;

or \g11877/U$2 ( w1, C, D );
not \112 (O, w1)
endmodule

