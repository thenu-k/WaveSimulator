## Wave Simulator

<centre>
<img src="https://raw.githubusercontent.com/thenu-k/WaveSimulator/main/Media/animation_2023-12-22_15-18-02.gif" height="500">
</centre>

This programme simulates the propogation of waves using the 2D wave equation via the fourier-spectral method. It can also solve it via the finite differences method.

To run the programme simply run the `main.py` file or by using `npm run start` if you have node installed.

### Methodology

The wave equation is a second order partial differential equation that describes the propagation of waves through a medium. It is given by:

<img src="https://render.githubusercontent.com/render/math?math=\frac{\partial^2 u}{\partial t^2} = c^2 \nabla^2 u">

where <img src="https://render.githubusercontent.com/render/math?math=u"> is the displacement of the wave, <img src="https://render.githubusercontent.com/render/math?math=c"> is the speed of the wave and <img src="https://render.githubusercontent.com/render/math?math=\nabla^2"> is the laplacian operator.s
