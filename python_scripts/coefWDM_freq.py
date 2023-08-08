import math
import os
from tqdm.auto import tqdm, trange

OUTDIR = 'coeffs_py'

def phitilde(f, insDOM, A, B):
    return math.exp(-0.5 * ((f - A) * insDOM) ** 2) * math.cos(2 * math.pi * f)

def coefficientWDM_freq(dt, Nf, Nt, mult, Nst, dtdf):

    os.makedirs(OUTDIR, exist_ok=True)

    PI = math.pi

    Ntd = 100  # Set the value of Ntd accordingly

    DT = dt * Nf
    DF = 1.0 / (2.0 * dt * Nf)

    OM = PI / dt
    DOM = OM / Nf
    insDOM = 1.0 / math.sqrt(DOM)

    B = OM / (2 * Nf)
    A = (DOM - B) / 2.0

    K = mult * 2 * Nf

    Tfilt = dt * K
    Tobs = dt * (Nt * Nf)

    print("In coefficientWDM_freq")
    print("Filter length (seconds)", Tfilt)

    BW = (A + B) / PI
    Np = int(BW * Tobs)

    dom = 2.0 * (A + B) / Np

    phi = [0.0] * Np

    for i in range(Np):
        f = -BW / 2.0 + (i / Tobs)
        phi[i] = phitilde(math.pi * f, insDOM, A, B)

    nrm = math.sqrt(sum(phi[i] ** 2 for i in range(Np))) * (math.sqrt(2.0) * Nf * dt)

    delt = (Tfilt / 2.0) / Nst

    td = [0.0] * Ntd
    td[1] = dtdf / (DF ** 2)
    for j in range(2, Ntd):
        td[j] = j * td[1]

    Nfsam = [0] * Ntd

    for j in range(Ntd):
        Nfsam[j] = int((Tfilt / 2.0 + 0.5 * td[j] * DF) / delt)

    print("Writing coefficients coeffs/WDMcoeffsf")

    pbar = trange(Ntd, desc="WDMcoeffsf")
    for k in pbar:
        pbar.set_postfix({f'Nfsamp[{k}]': f"{Nfsam[k]:,}"})
        filename = f"{OUTDIR}/WDMcoeffsf{k}.dat"
        with open(filename, "w") as out:
            for j in range(-Nfsam[k], Nfsam[k]):
                t = delt * j
                x = 0.0
                y = 0.0
                for i in range(Np):
                    f = -BW / 2.0 + (i / Tobs)
                    c = math.cos(2.0 * math.pi * (t * f + 0.5 * td[k] * f * f))
                    s = math.sin(2.0 * math.pi * (t * f + 0.5 * td[k] * f * f))
                    x += c * phi[i] / nrm
                    y += s * phi[i] / nrm
                out.write(f"{j} {x} {y}\n")


if __name__ == "__main__":
    coefficientWDM_freq(
        dt=0.01, Nf=256, Nt=100, mult=2, Nst=1000, dtdf=1
    )
