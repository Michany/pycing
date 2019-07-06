import numpy as np
from ..core.derivative import Derivative

class AsianCallOption(Derivative):

    def __init__(self, S, K, T, r, sigma, steps, **kwargs):
        
        super().__init__(S_0=S, T=T, r=r, sigma=sigma, steps=steps, **kwargs)
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma

    def payoff(self, underlyingAssetPath, **kwargs):

        return max(underlyingAssetPath.mean() - self.K, 0) * np.exp(-self.r * self.T)

class AsianPutOption(Derivative):

    def __init__(self, S, K, T, r, sigma, steps, **kwargs):
        
        super().__init__(S_0=S, T=T, r=r, sigma=sigma, steps=steps, **kwargs)
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma

    def payoff(self, underlyingAssetPath, **kwargs):

        return max(self.K - underlyingAssetPath.mean(), 0) * np.exp(-self.r * self.T)

