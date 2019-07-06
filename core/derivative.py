import abc
import time
import numpy as np
from .simulator import Simulator

class Derivative(Simulator):
    ''' A Base Class for Derivatives
    --------------------------------

    Based on <class Simulator>
    '''
    def __init__(self, **kwargs):

        super().__init__(**kwargs)

    @abc.abstractmethod
    def payoff(self, underlyingAssetPaths, **kwargs):
        ''' Payoff Function
        -------------------
        This is the part where you specify the payoff of a derivative
        '''
        return 

    def pricing(self, verbose=True, **kwargs):
        if verbose:
            print("[Simulating]", end='... ')
        t0 = time.time()
        underlyingAssetPaths = self.geometric_brownian_motion()
        if verbose:
            print("Time elapsed = %.5f s" % (time.time()-t0))
            print("[Simulation complete] Generated %s paths with %s steps" % (underlyingAssetPaths.T.shape))
            print("[Pricing]", end='... ')
        price_sim = np.apply_along_axis(self.payoff, axis=0, arr=underlyingAssetPaths)
        price_mean = price_sim.mean()
        if verbose:
            print(self.method, "price = %s" % price_mean)

        return price_mean
        
