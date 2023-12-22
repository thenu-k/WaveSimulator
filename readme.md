## Wave Simulator

<centre>
<img src="https://raw.githubusercontent.com/thenu-k/WaveSimulator/main/Media/animation_2023-12-22_15-18-02.gif" height="500">
</centre>

This programme simulates the propogation of waves using the 2D wave equation via the fourier-spectral method. It can also solve it via the finite differences method.

To run the programme simply run the `main.py` file or by using `npm run start` if you have node installed.

### Methodology

The two dimensional wave equation is given by:



$$ \frac{\partial^2 u}{\partial t^2} = \alpha^2 \cdot \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} \right)$$

Where $\alpha$ is the wave speed and $u$ is the wave function or amplitude. We write an ansatz for the solution in the form:

$$ u(x,y,t) = \sum_{n=0}^{\infty} \sum_{m=0}^{\infty} U_{mn}(t) \cdot \sin(\frac{m \pi}{L} x) \cdot \sin(\frac{n\pi}{L} y) $$

Where $U_{mn}(t)$ are the fourier coefficients. We can then substitute this into the wave equation to get:

$$ \sum_{n=0}^{\infty} \sum_{m=0}^{\infty} \frac{\partial^2 U_{mn}}{\partial t^2} \cdot \sin(\frac{m \pi}{L} x) \cdot \sin(\frac{n\pi}{L} y) = \alpha^2 \cdot \sum_{n=0}^{\infty} \sum_{m=0}^{\infty} U_{mn}(t) \cdot \left( -\frac{m^2 \pi^2}{L^2} - \frac{n^2 \pi^2}{L^2} \right) \cdot \sin(\frac{m \pi}{L} x) \cdot \sin(\frac{n\pi}{L} y) $$

Note that the fourier series is orthogonal so we can multiply both sides by $\sin(\frac{m \pi}{L} x) \cdot \sin(\frac{n\pi}{L} y)$ and integrate over the domain:

$$ \int_{0}^{L} \int_{0}^{L} \sum_{n=0}^{\infty} \sum_{m=0}^{\infty} \frac{\partial^2 U_{mn}}{\partial t^2} \cdot \sin(\frac{m \pi}{L} x) \cdot \sin(\frac{n\pi}{L} y) \cdot \sin(\frac{m \pi}{L} x) \cdot \sin(\frac{n\pi}{L} y) \,dx\,dy = \int_{0}^{L} \int_{0}^{L} \alpha^2 \cdot \sum_{n=0}^{\infty} \sum_{m=0}^{\infty} U_{mn}(t) \cdot \left( -\frac{m^2 \pi^2}{L^2} - \frac{n^2 \pi^2}{L^2} \right) \cdot \sin(\frac{m \pi}{L} x) \cdot \sin(\frac{n\pi}{L} y) \cdot \sin(\frac{m \pi}{L} x) \cdot \sin(\frac{n\pi}{L} y) \,dx\,dy $$

We can then use the orthogonality of the fourier series to simplify the equation:

$$ \sum_{n=0}^{\infty} \sum_{m=0}^{\infty} \frac{\partial^2 U_{mn}}{\partial t^2} \cdot \int_{0}^{L} \int_{0}^{L} \sin(\frac{m \pi}{L} x) \cdot \sin(\frac{n\pi}{L} y) \cdot \sin(\frac{m \pi}{L} x) \cdot \sin(\frac{n\pi}{L} y) \,dx\,dy = \alpha^2 \cdot \sum_{n=0}^{\infty} \sum_{m=0}^{\infty} U_{mn}(t) \cdot \left( -\frac{m^2 \pi^2}{L^2} - \frac{n^2 \pi^2}{L^2} \right) \cdot \int_{0}^{L} \int_{0}^{L} \sin(\frac{m \pi}{L} x) \cdot \sin(\frac{n\pi}{L} y) \cdot \sin(\frac{m \pi}{L} x) \cdot \sin(\frac{n\pi}{L} y) \,dx\,dy $$

We can then use the following identity to simplify the equation further:

$$ \int_{0}^{L} \sin(\frac{m \pi}{L} x) \cdot \sin(\frac{n\pi}{L} y) \,dx = \begin{cases} 0 & \text{if } m \neq n \\ \frac{L}{2} & \text{if } m = n \end{cases} $$

