import numpy as np
import matplotlib.pyplot as plt

def simulate():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    plt.plot(x, y)
    plt.title("Robot Path Simulation")
    plt.show()

if __name__ == "__main__":
    simulate()
