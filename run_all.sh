#!/bin/bash

gcc -o ./build/coefficientsWDM_time ./src/coefficientsWDM_time.c ./src/csubs.c -lm -lgsl
gcc -o ./build/coefficientsWDM_freq ./src/coefficientsWDM_freq.c ./src/csubs.c -lm -lgsl
gcc -o ./build/Chirp_WDM ./src/Chirp_WDM.c -lm -lgsl
gcc -o ./build/transform_time ./src/transform_time.c ./src/csubs.c -lm -lgsl
gcc -o ./build/transform_freq ./src/transform_freq.c ./src/csubs.c -lm -lgsl
gcc -o ./build/match ./src/match.c ./src/csubs.c -lm -lgsl

mkdir coeffs

#compute the fast frequency Taylor expansion coefficients

# if coeffs/WDMcoeffs0.dat does not exist, then run the ./coefficientsWDM_time
if [ ! -f coeffs/WDMcoeffs0.dat ]; then
    ./build/coefficientsWDM_time
fi

# if coeffs/WDMcoeffsf0.dat does not exist, then run the ./coefficientsWDM_freq
if [ ! -f coeffs/WDMcoeffsf0.dat ]; then
    ./build/coefficientsWDM_freq
fi

#generate a time domain chirplet and its fast WDM transform four ways
./build/Chirp_WDM
#compute the WDM transform of the chirplet directly in the time domain
./build/transform_time chrp_time.dat
#compute the WDM transform of the chirplet by FFTing first
./build/transform_freq chrp_time.dat 0
#compute the match between the dirtect time and frequency domain transforms
./build/match BinaryT.dat BinaryF.dat
#compute the match between the dirtect frequency domain transform and each of
#the fast transforms
./build/match BinaryF.dat BinaryTaylorT.dat
./build/match BinaryF.dat BinarySparseT.dat
./build/match BinaryF.dat BinaryTaylorF.dat
./build/match BinaryF.dat BinarySparseF.dat

gnuplot tranf.gnu
pen tranf.png

