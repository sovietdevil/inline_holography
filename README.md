#### Fast electron approximation

Strong electrostatic potential of atoms traps electrons in the column, which acts as a channel. Electrons are scattered dynamically without leaving it.
Here an atom acts as a thin lens.
*factors*:

1) Chemical composition
2) Zone axis (atomic distance)

**Quantum theory basics**:
*Incoherent imaging using dynamically scattered coherent electrons*: 1s-type bound states dominates the image contrast for typical experimental conditions. The column intensity is related to the transverse kinetic energy of the 1st states.

*For STEM*: ***incoherent***, the image intensity is a convolution between the intensity of teh microscope's pointspread function (illuminating probe) and an object function with localised peaks at the column positions.
*For HRTEM*: does not give intuitively interpretable images because of multiple scattering of the electron wave in the crystal and the coherent nature of the image formation.

Consider the electron density within a crystal, when a focused probe is incident at its surface. It is described by the wave function $\Psi(\mathbf{R}, z)$, neglecting the gradient in the $z$ direction (consider it equivalently as $t$ which refers to the approximation made), this satisfies:

$$
-\frac{\hbar}{\mathrm{i}} \frac{\partial}{\partial t} \Psi(\mathbf{R}, t)=H \Psi(\mathbf{R}, t)=[-\frac{\hbar^2}{2 m} \Delta_\mathbf{R}-e U(\boldsymbol{R}, t)] \Psi(\mathbf{R},t)
$$

Here the wave vector and direction is separated by perpendicular direction and parallel dirction, i.e., $\mathbf{r}=(\mathbf{R}, z)$ and $\mathbf{k}=(\mathbf{K}, k_z)$

The approximation is made:

1) Make high-energy approximation
2) Neglect Higher-Order Laue Zone (HOLZ) reflections (but useful in ADF)

Therefore, the time $t$ has the linear response with the vertical direction $z$, which is: 

$$
z=vt=\frac{p}{m}t=\frac{\hbar k}{m}\cdot t
$$

Therefore,

$$
\frac{\partial}{\partial z}\Psi(\mathbf{R}, z)=\frac{i}{2k}(\Delta_{\mathbf{R}}+\frac{2me}{\hbar^2}U(\mathbf{R},z))\Psi(\mathbf{R}, z)
$$

This can also be derived from the stationary Schordinger equation in the forward scattering approximation.

#### Multislice theory

plane waves provides a complete basis for any wave function
**Key:** use projected potential of each slice.
The solution of the partial differential equation above has a general solution:

$$
\frac{\partial}{\partial z}\Psi(\mathbf{R}, z)=\exp \{\int_{0}^{h}[\frac{i}{2k}\Delta_\mathbf{R}+\frac{ime}{k\hbar^2}U(\mathbf{R},z)]dz\}\Psi(\mathbf{R}, z)
$$

Let $A=\frac{i}{2k}\Delta_\mathbf{R}, B=\frac{ime}{k\hbar^2}U(\mathbf{R},z)=i\sigma V(\mathbf{R},z)$
The multislice algorithm separates $z$ into small $\Delta z$, thus

$$
\Psi(x, y, z+\Delta z)=\exp [\int_z^{z+\Delta z}(\frac{\mathrm{i} \lambda}{4 \pi} \nabla_{x y}^2+i \sigma V(x, y, z^{\prime})) \mathrm{d} z^{\prime}] \Psi(x, y, z)
$$

For small $\Delta z$, it takes the approximation

$$
\psi(x, y, z+\Delta z)=\exp [\frac{\mathrm{i} \lambda}{4 \pi} \Delta z \nabla_{x y}^2+i \sigma v_{\Delta z}(x, y, z)] \psi(x, y, z)
$$

Here $v_{\Delta z}(x, y, z)=\int_z^{z+\Delta z} V(x, y, z^{\prime}) \mathrm{d} z^{\prime}$
The approximation is taken as commutator is not considered (or take average of two sequences):

$$
\psi(x, y, z+\Delta z)  =\exp (\frac{\mathrm{i} \lambda \Delta z}{4 \pi} \nabla_{x y}^2) \exp [i \sigma v_{\Delta z}(x, y, z)] \psi(x, y, z)+\mathscr{O}(\Delta z^2) 
$$


$$
 =\exp (\frac{\mathrm{i} \lambda \Delta z}{4 \pi} \nabla_{x y}^2) t(x, y, z) \psi(x, y, z)+\mathscr{O}(\Delta z^2)
$$

Here $t(x, y, z)=\exp [i \sigma \int_z^{z+\Delta z} V(x, y, z^{\prime}) \mathrm{d} z^{\prime}]$
To inteprete $A$, Fourier transform is used:

$$
\mathrm{FT}[\exp (\frac{\mathrm{i} \lambda \Delta z}{4 \pi} \nabla_{x y}^2)(t \psi)]
$$


$$
=\int[\exp (\frac{\mathrm{i} \lambda \Delta z}{4 \pi} \nabla_{x y}^2)(t \psi)] \exp [2 \pi \mathrm{i}(k_x x+k_y y)] \mathrm{d} x d y
$$


$$
=\int[\exp (\frac{\mathrm{i} \lambda \Delta z}{4 \pi} \frac{\partial^2}{\partial x^2}) \exp (\frac{\mathrm{i} \lambda \Delta z}{4 \pi} \frac{\partial^2}{\partial y^2})(t \psi)]\times \exp [2 \pi \mathrm{i}(k_x x+k_y y)] \mathrm{d} x \mathrm{d} y
$$


$$
=\exp [-i \pi \lambda \Delta z(k_x^2+k_y^2)] \mathrm{FT}[(t \psi)]
$$

Thus in real space,

$$
p(x, y, \Delta z)=\mathrm{FT}^{-1}[P(k, \Delta z)]=\frac{1}{\mathrm{i} \lambda \Delta z} \exp [\frac{\mathrm{i} \pi}{\lambda \Delta z}(x^2+y^2)]
$$

such that

$$
\psi(x, y, z+\Delta z)=p(x, y, \Delta z) \otimes[t(x, y, z) \psi(x, y, z)]+\mathscr{O}(\Delta z^2)
$$

in numerical computation, it is noted as

$$
\psi_{n+1}(x, y)=p_n(x, y, \Delta z_n) \otimes[t_n(x, y) \psi_n(x, y)]+\mathscr{O}(\Delta z^2)
$$

which can also be expressed as

$$
\psi_{n+1}(x, y)=t_n(x, y)[p_n(x, y, \Delta z_n) \otimes \psi_n(x, y)]+\mathscr{O}(\Delta z^2)
$$


#### Channeling theory

**Key**: basis of eigenstates of the projected atom columns leading to a simple closed-form expression for the exit wave

**Plane wave expansion:** The solution of this differential equation can be expanded in eigenfunctions of the Hamiltonion,

$$
\Psi(\boldsymbol{R}, z)=\sum_n C_n \Phi_n(\boldsymbol{R}) \exp \{-\mathrm{i} \frac{E_n}{2E_{0}} k z\}
$$

Here $\Phi_n(\mathbf{R})$ are eigenbasis, while $E_0=\hbar^2k^2/2m$, which refers to the incident electron energy.

The coefficients $C_n$ can be determined by the boundary condition (upper space) due to the orthogonal property:

$$
C_n=\int \Phi_n^*(\boldsymbol{R}) \Psi(\boldsymbol{R}, 0) \mathrm{d} \boldsymbol{R}
$$

The wave at the upper surface is assumed to be the plane wave, therefore,

$$
\Psi(\mathbf{R},0)=\sum_nC_n\Phi_n(\mathbf{R})=1
$$

Take this back to the differential equation, the result is

$$
\sum_n C_nE_n\Phi_n(\mathbf{R})=H\Psi(\mathbf{R},0)=-eU(\mathbf{R})
$$

In case $E_n<0$, the states are bound to the columns (properties of central force problems), therefore $-i\pi E_n kz/E_0>0$. 

Here the potential is treated as averaged value:

$$
U(\mathbf{R})=\frac{1}{T}\int_0^TU(\mathbf{R},z)dz
$$

To deal with the following steps, only the first-order term of the exponential term is used, which refers to the Weak Phase Object Approximation (WPOA). The plane wave expansion form can be rewritten as:

$$
\Psi(\mathbf{R},z)=\sum_n C_n\Phi_n(\mathbf{R})[1-i\frac{E_n}{2E_0}kz]
$$


$$
+\sum_n C_n\Phi_n(\mathbf{R})[exp\{-i\frac{E_n}{2E_0}kz\}-1+i\frac{E_n}{2E_0}kz]
$$


$$
=1+i\frac{eU(\mathbf{R})}{2E_0}kz
$$


$$
+\sum_n C_n\Phi_n(\mathbf{R})[exp\{-i\frac{E_n}{2E_0}kz\}-1+i\frac{E_n}{2E_0}kz]
$$

The basis can be based on **atomic columns** (each column represents an eigenbase), which is similar to Tight Binding (TB) method. In a single column,

$$
\Psi(\mathbf{R},z)= 1+\mathrm{i} \frac{e U(\boldsymbol{R})}{2E_{0}} k z 
$$


$$
 +C \Phi(\boldsymbol{R})[\exp \{-\mathrm{i} \frac{E}{2E_{0}} k z\}-1+\mathrm{i} \frac{E}{2E_{0}} k z]
$$

Here only one eigenstate (1S) is considered as dynamically scattering wave function. Other terms are not significant for the HRTEM image formation.

Therefore, the total wave function can be written as the summation of every columns,

$$
\Psi(\mathbf{R},z)=1+\sum_i\frac{ie}{2E_0}kzU_i(\mathbf{R}-\mathbf{R}_i)
$$


$$
+\sum_iC_i\Phi_i(\mathbf{R}-\mathbf{R}_i)\times[\exp \{-\mathrm{i} \frac{E_i}{2E_{0}} k z\}-1+\mathrm{i} \frac{E_i}{2E_{0}} k z]
$$

Since all the states have very small energies $E_i$, the wave function can be approximated as

$$
\Psi(\boldsymbol{R}, z)=  1+\sum_iC_i \Phi_i(\boldsymbol{R}-\boldsymbol{R}_i)\times[\exp \{-\mathrm{i} \frac{E_i}{2E_{0}} k z\}-1]
$$


$$
=1+\sum_i2C_i \Phi_i(\boldsymbol{R}-\boldsymbol{R}_i)\sin(\frac{E_i}{4E_0}kz)\exp\{-i[\frac{\pi}{2}+\frac{E_i}{4E_0}kz]\}
$$


$$

$$


#### S-state model

*reference: The S-state model: a work horse for HRTEM by P. Geuens, D. Van Dyck*

In the column:

$$
\Psi(\mathbf{R},z)=1+\sum_{nm}2c_{nm}sin(\frac{E_{nm}}{E_0}\frac{k_z}{4}z)\psi_{nm}(\mathbf{R})\times \exp\{-i[\frac{\pi}{2} +\frac{E_{nm}}{E_0}\frac{k_z}{4}z]\}
$$

Here $n$ is the main quantum number, while $m$ is the angular quantum number. Here $\psi_{nm}$ and $E_{nm}$ refers to the solutions of the eigenvalue problem:

$$
\hat{H}\psi_{nm}(\mathbf{R})=E_{nm}\psi_{nm}(\mathbf{R})
$$

Here $H=-\frac{\hbar^2}{2\mu}\Delta_\mathbf{R}-eU(\mathbf{R})$
For one column, the solution of the wave function is separated into two terms: the radical term $R_{nm}(\rho)$ and the angular term $\Phi_m(\varphi)$, i.e., $\psi_{nm}(\mathbf{R})=R_{nm}(\rho)\Phi_m(\varphi)$. Thus the differential equation is separated into two terms:

$$
\frac{\partial^2}{\partial \varphi^2} \Phi_m(\varphi)=-m^2 \Phi_m(\varphi)
$$

Which has the solutions $\Phi_m(\varphi)=\frac{1}{\sqrt{2 \pi}} \mathrm{e}^{\mathrm{i} m \varphi}$,
and

$$
-\{\frac{\hbar^2}{2 \mu}(\frac{\partial^2}{\partial \rho^2}+\frac{1}{\rho} \frac{\partial}{\partial \rho}-\frac{m^2}{\rho^2})+e U(\rho)\}R_{n m}(\rho)=E_{n m} R_{n m}(\rho)
$$


When only 1s state is considered, the expression is:

$$
\psi(\mathbf{r}, z)=1+c_s \varphi_s(\mathbf{r}-\boldsymbol{\beta})[\exp (-i \frac{E_s}{2E_0} k z)-1]
$$

Here $\varphi_s(\mathbf{r})=\frac{1}{a \sqrt{2 \pi}} \exp (-\frac{r^2}{4 a^2})$, $c_s=2 \sqrt{2 \pi} a$.

###### Pertubation model of doping

It explains the effect of doping.
In case of perfect column (without doping), the equation is:

$$
\frac{d\varphi}{dt}=\hat{H}\varphi=(\nabla^2+V)\varphi
$$

This has the solution of:

$$
\varphi(t)=e^{\hat{H}t}\cdot\varphi(0)
$$

In case the column is doped with other atoms, the potential is changed to $V(t)+W(t)$ instead of $V(t)$, here $W=V_{Ag}-V_{Al}$

Therefore, the Hamiltonion is changed to $\hat{H}+W$, while the solution is assumbed to be  $\psi(t)=\theta(t)\cdot \exp(\hat{H}t)$, at the upper surface $\theta(0)=\varphi(0)$.

Take $\psi(t)$ into the differential equation $\frac{d\varphi}{dt}=(\hat{H}+W)\varphi$, it can be expanded into:

$$
\exp(\hat{H}t)(\frac{d\theta}{dt}+\hat{H}\theta)=\exp(\hat{H}t)(\hat{H}+W)\theta
$$

According to the linearity rules, the term $\hat{H}\theta\exp(\hat{H}t)$ can be eliminated, thus

$$
\exp(\hat{H}t)\cdot\frac{d\theta}{dt}=W\exp(\hat{H}t)\cdot\theta
$$

which can also be written as:

$$
\frac{d\theta}{dt}=\exp(-\hat{H}t)W\exp(\hat{H}t)\theta
$$

Therefore,

$$
\psi(t)=\varphi(t)+\int_0^t\exp(\hat{H}(t-t'))W(t')\psi(t')dt'
$$

The ***approximation*** is taken by replacing $\psi$ with $\varphi$, while $W(t)=W_p\delta(t-T)$, therefore

$$
\psi(t)=\varphi(t)+W_p\exp(\hat{H}(t-T))\varphi(T)
$$


$$
=\varphi(0)\exp(\hat{H}t)+W_p\varphi(T)\exp(\hat{H}(t-T))
$$


$$

$$

The influence of vertical direction is included in the term $W_p\varphi(T)\exp(\hat{H}(t-T))$, which can be confirmed by the experiments.
