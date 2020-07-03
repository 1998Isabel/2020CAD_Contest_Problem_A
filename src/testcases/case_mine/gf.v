//
// Conformal-LEC Version 19.20-d218 (25-Feb-2020)
//
module top( A, C, D, O);
input C, D;
output O;
wire w1, w2;

_DC \223 (w1, C, A);
_DC \222 (w2, D, A)
nor \n6_5[1] ( O, w1, w2);

endmodule

