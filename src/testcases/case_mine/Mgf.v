//
// Conformal-LEC Version 19.20-d218 (25-Feb-2020)
//
module top( A, C, D, O);
input [1:0] C, D;
output [1:0] O;
wire [1:0] w1, w2;

m_DC \223 (w1, C, A);
m_DC \222 (w2, D, A);
mnor \n6_5[1] ( O, w1, w2);

endmodule

