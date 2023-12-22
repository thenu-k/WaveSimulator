## Wave Simulator

<centre>
<img src="https://raw.githubusercontent.com/thenu-k/WaveSimulator/main/Media/animation_2023-12-22_15-18-02.gif" height="500">
</centre>

This programme simulates the propogation of waves using the 2D wave equation via the fourier-spectral method. It can also solve it via the finite differences method.

To run the programme simply run the `main.py` file or by using `npm run start` if you have node installed.

### Methodology

The two dimensional wave equation is given by:
\[
    u_{tt} = c^2 \left( u_{xx} + u_{yy} \right)  
\\
\Rightarrow \frac{\partial^2 u}{\partial t^2} = c^2 \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} \right)
\]
 
