import numpy as np
import math 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

class SpectralSolver:
    def __init__(self, initialConditions, spatialDimensions=1.0, temperalResolution=0.1, waveSpeed=1.0):
        print("-> Spectral Solver v0.0")
        time.sleep(0.5)
        # Parameters
        self.initialConditions = initialConditions
        self.spatialDimensions = spatialDimensions
        self.temporaryResolution = temperalResolution
        self.waveSpeed = waveSpeed
        # Data
        self.spatialResolution = self.spatialDimensions/self.initialConditions.shape[0]
        self.spatialRange = self.initialConditions.shape[0]
        self.history = [self.initialConditions]
        self.time = 0.0
        # Wave numbers
        kx = 2 * np.pi / self.spatialDimensions * np.fft.fftfreq(self.spatialRange, d=self.spatialResolution)
        ky = 2 * np.pi / self.spatialDimensions * np.fft.fftfreq(self.spatialRange, d=self.spatialResolution)
        self.normedXFreqs, self.normedYFreqs = np.meshgrid(kx, ky)
        self.angularFreqs = self.waveSpeed*np.sqrt(self.normedXFreqs**2 + self.normedYFreqs**2) 
        # Coefficients
        self.coefficients = np.fft.fft2(self.initialConditions) #/ self.spatialRange**2
        print("-> Parameters initialized")

    def simulate(self, timeLimit=10.0):
        print("-> Simulating for " + str(timeLimit) + " seconds...")
        iterations = 0
        totIterations = timeLimit/self.temporaryResolution
        while self.time < timeLimit:
            self.coefficients = self.updateCoefficients(self.coefficients, self.temporaryResolution)
            self.history.append(np.real(np.fft.ifft2(self.coefficients)))
            self.time += self.temporaryResolution
            iterations += 1
            print("-> Completion: " + str(round(iterations/totIterations*100, 2)) + "%", end="\r")
        print("-> Simulation complete")

    def updateCoefficients(self, currentCoefficients, timeStep):
        newCoefficients = currentCoefficients * np.exp(-1j * self.angularFreqs * timeStep)
        newCoefficients[0, :] = 0
        newCoefficients[-1, :] = 0
        newCoefficients[:, 0] = 0
        newCoefficients[:, -1] = 0
        return newCoefficients
    
    def animate(self, save=True, timeStep=10):
        print("-> Animating...")
        historyData = self.history
        def update(frame):
            ax.clear()
            ax.set_xticks([])  
            ax.set_yticks([])  
            ax.imshow(historyData[frame], cmap='viridis', extent=[0, Lx, 0, Ly], origin='lower')
            ax.patch.set_visible(False)
            ax.axis('off')
        fig, ax = plt.subplots()
        Lx, Ly = historyData[0].shape[1], historyData[0].shape[0]
        animation = FuncAnimation(fig, update, frames=len(historyData), interval=timeStep, repeat=False)
        plt.show()
        if save:
            print("-> Saving animation to ./Media/animation.gif...")
            animation.save('./Media/animation.gif', writer='ffmpeg', fps=30, savefig_kwargs={'transparent': True, 'bbox_inches': 'tight', 'pad_inches': 0})
            print("-> Animation saved")
