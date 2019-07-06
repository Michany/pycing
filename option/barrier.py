import numpy as np
from ..core.derivative import Derivative

class UpInOption(Derivative):

    def __init__(
        self, S, K, T, r, sigma, 
        knockInPrice, knockPrenium=0, 
        steps=300, **kwargs):
        ''' Up-and-in Option
        ---------------------
        If the underlying price has ever go above the knock-in-price, 
        the option is said to be 'knocked in' and the option is just priced
         as an ordinary European Call Option
       
        If not, the buyer will only receive a small compensation called `knockPrenium`.
        '''
        super().__init__(S_0=S, T=T, r=r, sigma=sigma, steps=steps, **kwargs)
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.knockInPrice = knockInPrice
        self.knockPrenium = knockPrenium

    def payoff(self, underlyingAssetPath, **kwargs):

        if max(underlyingAssetPath) >= self.knockInPrice:
            return max(underlyingAssetPath[-1] - self.K, 0) * np.exp(-self.r * self.T)
        return self.knockPrenium * np.exp(-self.r * self.T)

class UpOutOption(Derivative):

    def __init__(
        self, S, K, T, r, sigma, 
        knockOutPrice, knockOutPrenium=0, 
        steps=300, **kwargs):
        ''' Up-and-out Option
        ---------------------
        If the underlying price has ever go above the knock-out-price, 
        the option is said to be 'knocked out' and the buyer will only 
        receive a small compensation called `knockOutPrenium`.

        If not, the option is just priced as an ordinary European Call Option
        '''
        super().__init__(S_0=S, T=T, r=r, sigma=sigma, steps=steps, **kwargs)
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.knockOutPrice = knockOutPrice
        self.knockOutPrenium = knockOutPrenium

    def payoff(self, underlyingAssetPath, **kwargs):

        if max(underlyingAssetPath) >= self.knockOutPrice:
            return self.knockOutPrenium * np.exp(-self.r * self.T)
        return max(underlyingAssetPath[-1] - self.K, 0) * np.exp(-self.r * self.T)

class DownInOption(Derivative):

    def __init__(
        self, S, K, T, r, sigma, 
        knockInPrice, knockPrenium=0, 
        steps=300, **kwargs):
        ''' Up-and-in Option
        ---------------------
        If the underlying price has ever go below the knock-in-price, 
        the option is said to be 'knocked in' and the option is just priced
         as an ordinary European Put Option
       
        If not, the buyer will only receive a small compensation called `knockPrenium`.
        '''
        super().__init__(S_0=S, T=T, r=r, sigma=sigma, steps=steps, **kwargs)
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.knockInPrice = knockInPrice
        self.knockPrenium = knockPrenium

    def payoff(self, underlyingAssetPath, **kwargs):

        if max(underlyingAssetPath) <= self.knockInPrice:
            return max(underlyingAssetPath[-1] - self.K, 0) * np.exp(-self.r * self.T)
        return self.knockPrenium * np.exp(-self.r * self.T)
        
class DownOutOption(Derivative):

    def __init__(
        self, S, K, T, r, sigma, 
        knockOutPrice, knockOutPrenium=0, 
        steps=300, **kwargs):
        ''' Down-and-out Option
        ---------------------
        If the underlying price has ever go below the knock-out-price, 
        the option is said to be 'knocked out' and the buyer will only 
        receive a small compensation called `knockOutPrenium`.

        If not, the option is just priced as an ordinary European Put Option
        '''
        super().__init__(S_0=S, T=T, r=r, sigma=sigma, steps=steps, **kwargs)
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.knockOutPrice = knockOutPrice
        self.knockOutPrenium = knockOutPrenium

    def payoff(self, underlyingAssetPath, **kwargs):

        if max(underlyingAssetPath) <= self.knockOutPrice:
            return self.knockOutPrenium * np.exp(-self.r * self.T)
        return max(self.K - underlyingAssetPath[-1], 0) * np.exp(-self.r * self.T)
