set logscale x
set dgrid3d 30,30
set pm3d
splot "res.dat" using 1:2:3 with lines
pause -1  "Hit return to continue"