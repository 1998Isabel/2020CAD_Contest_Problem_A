module top( a, b , c, d, y);
input a, b, c, d;
output y;

wire w1, w2;

and label1 ( w1, a, b)
and label2 ( w2, c, d);
and label3 ( y, w1, w2); 
endmodule