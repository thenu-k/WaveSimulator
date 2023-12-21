from Logic.Logic import WaveSimulator
import numpy as np
import datetime

# Initial Conditions
restCondition = np.zeros((200,200))


waveSim = WaveSimulator(
    mediumX=1.0, 
    mediumY=1.0,
    mediumWaveSpeed=0.3,
    temporalResolution=0.01,
    initialAmplitudes=restCondition,
)


# waveSim.simulate(
#     timeLimit=5.0,
#     saveData=True
# )

waveSim.animate(
    save=True,
    fileName='waveSimData.npy'
)
