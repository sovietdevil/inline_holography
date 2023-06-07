#import packages
from abtem.potentials import PotentialArray, Potential
from abtem.waves import PlaneWave, FresnelPropagator
import h5py
import numpy as np
from matplotlib import pyplot as plt

#parameters of propagation
V = 300e3
h = 6.62607015e-34
me= 9.1093837e-31
e = 1.60217663e-19
c = 299792458
lamb = h/np.sqrt(2*me*e*V*(1+(e*V)/(2*me*c**2)))

#construct atoms
from ase import Atoms
a = 2.0247
H = 78.963303
gap = 0.0128
h = np.linspace(gap, H-gap, 20)
wave = PlaneWave(energy=300e3, sampling=0.0656015)
i = 15
Al = Atoms('Al', positions=[(a/2, a/2, h[i])], cell=[a, a, H])
pw_exitwave = wave.multislice(Al)
wave_function = pw_exitwave.array
plt.figure("amplitude")
plt.imshow(np.abs(wave_function))
plt.figure("phase")
plt.imshow(np.angle(wave_function))
ft_pattern = np.fft.fftshift(np.fft.fft2(wave_function))
N = len(wave_function[:,0])
a = 2.0247e-10
d = a/N
kx = np.fft.fftshift(np.fft.fftfreq(N, d))
ky = np.fft.fftshift(np.fft.fftfreq(N, d))
q2 = np.array([[x**2+y**2 for x in kx] for y in ky])
deltaz = ((H - 2*gap)/20)*1e-10
ft_pattern = ft_pattern * np.exp(-1j*np.pi*q2*lamb*deltaz)
wv_func = np.fft.ifft2(np.fft.ifftshift(ft_pattern))
plt.figure('inverse amplitude')
plt.imshow(np.abs(wv_func))
plt.figure('inverse phase')
plt.imshow(np.angle(wv_func))
dz = (H - 2*gap)/20
i = 16
a = 2.0247
Al = Atoms('Al', positions=[(a/2, a/2, h[i])], cell=[a, a, H])
pw_exitwave = wave.multislice(Al)
wave_function = pw_exitwave.array
plt.figure("amplitude1")
plt.imshow(np.abs(wave_function))
plt.figure("phase1")
plt.imshow(np.angle(wave_function))
plt.show()