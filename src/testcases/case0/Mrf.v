module top(in, a, b, out);
input [1:0] in, a, b;
output [1:0] out;
wire [1:0] n2, n1, en1, en2b, en1b, out, b, a, in;
mnand en1b_ins(en1b, a, b);
mnot en2b_ins(en2b, a);
mnot en1_ins(en1, en1b);
m_DC buf1(n1, in, en1b);
mand iso(n2, n1, en1);
m_DC buf2(out, n2, en2b);
endmodule
