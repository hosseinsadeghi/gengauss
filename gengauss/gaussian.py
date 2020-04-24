import numpy as np

class GaussianModel:
    def __init__(self):
        pass
    
    def fit(self, data):
        self.mu = np.mean(data)
        self.stdev = np.std(data)
        
    def sample(self, num_samples=100):
        return self._snd(num_samples) * self.stdev + mu
    
    def _snd(self, num_samples):
        cached = num_samples
        if num_samples % 2 == 1:
            num_samples += 1
        z1 = np.random.rand(num_samples // 2)
        z2 = np.random.rand(num_samples // 2)
        n1 = np.sqrt(-2 * np.log(z1)) * np.cos(2 * np.pi * z2)
        n2 = np.sqrt(-2 * np.log(z1)) * np.sin(2 * np.pi * z2)
        return np.concatenate((n1, n2))[:cached]   
    
    def pdf(self, x):
        return np.exp(-(x - self.mu)**2 / (2 * np.stdev ** 2)) / np.sqrt(2 * np.pi * self.stdev ** 2)
    
    def __repr__(self):
        return "Mean: %.2f, stdev: %.2f" % (self.mu, self.stdev)
        
    