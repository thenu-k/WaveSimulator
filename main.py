from Logic.Spectral import SpectralSolver
import numpy as np

# Initial Conditions
dimension = 201
rainDrop = np.zeros((dimension,dimension))
rainDrop[int(dimension/2),int(dimension/2)] = 100.0

# Solver
solver = SpectralSolver(
    initialConditions=rainDrop,
    spatialDimensions=1.0,
    temperalResolution=0.01,
    waveSpeed=1.0
)

# Simulation
solver.simulate(timeLimit=1.0)
solver.animate()
