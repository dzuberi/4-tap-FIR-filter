output_wf 1
vname X<3:0> B0<3:0> B1<3:0>, B2<3:0>, B3<3:0> CLK Y<5:4> Y<3:0>
io i i i i i i o o
radix 4 4 4 4 4 1 2 4
tunit 1ns
period 10
chk_window 5 5 0
trise .001
tfall .001
vih 1.0
vil 0.0
voh 0.6
vol 0.4

0 1 0 0 0 1
0 2 0 0 0 2
0 3 0 0 0 3
0 1 0 1 0 2
0 2 0 3 0 5
