# -*- coding: utf-8 -*-
import time
import numpy as np


class Simulator():
    '''
    '''

    def __init__(self, noOfPath=25000, method='MonteCarlo', **kwargs):

        self.noOfPath = noOfPath
        self.method = method
        self.params = kwargs

    def unpack_params(self, kwargs):

        try:
            S_0 = kwargs['S_0']
            T = kwargs['T']
            r = kwargs['r']
            sigma = kwargs['sigma']
            steps = kwargs['steps']
            return S_0, T, r, sigma, steps
        except KeyError:
            return -1

    def geometric_brownian_motion(self, **kwargs):

        # Try if the params are provided for the method
        _temp = self.unpack_params(kwargs)
        if _temp==-1:
            # Try if the params are provided for the class
            _temp = self.unpack_params(self.params)
            if _temp==-1: # In neither way are the params provided
                raise KeyError("Some parameters must be missing")
        S_0, T, r, sigma, steps = _temp

        return self._geometric_brownian_motion(S_0, T, r, sigma, steps, self.noOfPath)
    
    @classmethod
    def _geometric_brownian_motion(cls, S_0, T, r, sigma, steps, noOfPath):
        ''' A Optimized Method to Generate GBM Path
        --------------------------------------------
        S_0 : Price of the underlying asset at time 0  
        S : Simulated path of underlying asset S
    
        Using the following method, you can actually test the speed of this function:
    
        >>> %timeit geometric_brownian_motion(S_0, T, r, sigma, steps, noOfPath)
        '''
        dt = T / steps
        
        dS = sigma * np.sqrt(dt) * np.random.standard_normal((steps, noOfPath))
        dS += (r - 0.5 * sigma**2) * dt 
        dS = dS.cumsum(axis=0)
        S = S_0 * np.exp(dS)
        S[0] = S_0
    
        return S
        
    
if __name__ == '__main__':
    sim = Simulator(noOfPath=50000, )
    t0 = time.time()
    print(sim.geometric_brownian_motion(S_0=100, T=1, r=0.04, sigma=0.2, steps=250).shape)
    print("Time elapsed = %.5f s" % (time.time()-t0))
