set term png enhanced truecolor crop font Helvetica 18  size 1200,800
set output 'tranf.png'
set pm3d map corners2color c1
set yrange [0:200]
set ylabel 'frequency'
set xlabel 'time'
set cbrange [-4.000000e+00:4.000000e+00]
set palette defined (0 '#b2182b', 1 '#ef8a62', 2 '#fddbc7', 3 '#ffffff', 4 '#d1e5f0', 5 '#67a9cf', 6 '#2166ac')
splot 'BinaryF.dat' using 1:2:3 notitle
