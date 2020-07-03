module top( a, b , c, d, y);
input [1:0] a, b, c, d;
output [1:0] y;

wire [1:0] w1, w2;

mand label1 ( w1, a, b);
mand label2 ( w2, c, d);
mand label3 ( y, w1, w2);
endmodule