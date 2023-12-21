import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class WaveSimulator:
    def __init__(
            self,
            mediumX:float, 
            mediumY: float,
            mediumWaveSpeed: float, 
            temporalResolution:float,
            initialAmplitudes=np.zeros((100,100)),
        ):
        # Paramaters
        self.mediumX = mediumX
        self.mediumY = mediumY
        self.mediumWaveSpeed = mediumWaveSpeed
        self.temporalResolution = temporalResolution
        self.prevAmplitudes = initialAmplitudes.copy()
        # Data
        self.xRange = initialAmplitudes.shape[1]
        self.yRange = initialAmplitudes.shape[0]
        self.spatialResolution = self.mediumX/self.xRange # Assuming a symmetric medium
        # Initial Conditions
        self.currentAmplitudes = initialAmplitudes.copy()
        self.currentAmplitudes[int(self.xRange/2)-1][int(self.yRange/2) -1]=100
        self.history = [self.prevAmplitudes.copy(), self.currentAmplitudes.copy()]
        self.scalarConstant = (self.mediumWaveSpeed*self.temporalResolution)/self.spatialResolution
        if self.scalarConstant<1/(math.sqrt(2)):
            print('-> Scalar constant is within stable parameter...')
        else:
            print('-> Scalar constant beyond stable parameter:'+str(self.scalarConstant)+'. Should be less than: '+str(1/(math.sqrt(2)))+'!')
    
    def updateFn(self, CA, PA):
        NA = np.zeros((self.xRange, self.yRange))
        for i in range(self.xRange-1):
            for j in range(self.yRange-1):
                if i==0 or j==0: NA[i][j]=0
                NA[i][j] = self.scalarConstant**2*(CA[i-1][j]+CA[i+1][j]+CA[i][j-1]+CA[i][j+1]-4*CA[i][j]) + 2*CA[i][j] - PA[i][j]
        return NA
    
    def simulate(self, timeLimit=10.0, saveData=False, fileName='waveSimData.npy'):
        time=0.0
        count = 0
        totSteps = self.xRange*self.yRange*(int(timeLimit/self.temporalResolution))
        print('-> Simulation Started')
        while time<timeLimit:
            newAmplitudes = self.updateFn(
                CA=self.currentAmplitudes,
                PA=self.prevAmplitudes
            )
            self.history.append(newAmplitudes)
            self.prevAmplitudes = self.currentAmplitudes
            self.currentAmplitudes = newAmplitudes
            time += self.temporalResolution
            count += 1
            output = f'-> Completion: {100*count*self.xRange*self.yRange/totSteps:.2f}%'
            print(output, end='\r')
        print('')
        print('-> Simulation Complete')
        if saveData:
            np.save(fileName, self.history)
            print('-> Data saved to: '+fileName)
    
    def animate(self, save, fileName):
        # get nmpy data from npy file
        historyData = np.load(fileName)
        def update(frame):
            ax.clear()
            ax.set_title(f'Time Step: {frame}')
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.imshow(historyData[frame], cmap='viridis', extent=[0, Lx, 0, Ly], origin='lower')
        fig, ax = plt.subplots()
        Lx, Ly = historyData[0].shape[1], historyData[0].shape[0]
        animation = FuncAnimation(fig, update, frames=len(historyData), interval=10, repeat=False)
        plt.show()
        if save:
            animation.save('waveSimAnimation.gif', fps=30)
            print('-> Animation saved to waveSimAnimation.gif. ')
        
        

