import numpy as np
from ..core.derivative import Derivative

class EuropeanCallOption(Derivative):

    def __init__(self, S, K, T, r, sigma, steps, **kwargs):
        
        super().__init__(S_0=S, T=T, r=r, sigma=sigma, steps=steps, **kwargs)
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma

    def payoff(self, underlyingAssetPath, **kwargs):

        return max(underlyingAssetPath[-1] - self.K, 0) * np.exp(-self.r * self.T)

class EuropeanPutOption(Derivative):

    def __init__(self, S, K, T, r, sigma, steps, **kwargs):
        
        super().__init__(S_0=S, T=T, r=r, sigma=sigma, steps=steps, **kwargs)
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma

    def payoff(self, underlyingAssetPath, **kwargs):

        return max(self.K - underlyingAssetPath[-1], 0) * np.exp(-self.r * self.T)


if __name__ == "__main__":
    eo = EuropeanCallOption(noOfPath=10000,S=100,K=105,T=20/365,r=0.04,sigma=0.2,steps=300)
    eo.pricing()