from Logic.Spectral import SpectralSolver
import numpy as np

dimension = 201
x = np.linspace(0, 1, dimension)
y = np.linspace(0, 1, dimension)
X, Y = np.meshgrid(x, y)

# Initial Conditions
rainDrop = np.zeros((dimension,dimension))
rainDrop[int(dimension/2),int(dimension/2)] = 100.0

# Traveling wave
sineConditions = np.sin(2*np.pi*X)*np.sin(2*np.pi*Y)

# Central circle
circleConditions = np.zeros((dimension,dimension))
for i in range(dimension):
    for j in range(dimension):
        if np.sqrt((i-dimension/2)**2 + (j-dimension/2)**2) < dimension/4:
            circleConditions[i,j] = 1.0

# Solver
solver = SpectralSolver(
    initialConditions=circleConditions,
    spatialDimensions=1.0,
    temperalResolution=0.01,
    waveSpeed=1.0
)

# Simulation
solver.simulate(timeLimit=10.0)
solver.animate(
    save=True,
    timeStep=50,
)
