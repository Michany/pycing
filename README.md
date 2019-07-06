# pycing: Derivative pricing tools based on MonteCarlo Simulations.

Most of the codes are implemented with Numpy grammar. 
You can take it that these codes are highly optimized.

## Features
### Built-in Derivatives
- European Option (欧式期权)
- Asian Option (亚式期权)
  - Path-denpendent
- Barrier Option (障碍期权)
  - Up-and-in Option (向上敲入)
  - Up-and-out Option (向上敲出)
  - Down-and-in Option (向下敲入)
  - Down-and-out Option (向下敲出)

### Customized Derivatives Support
You can override the payoff function to price a custimized derivative.

### Numpy Optimized
It takes only 0.2 seconds for `pycing` to perform a simulation that generates 10000 paths with 300 steps.

## Examples

### Use built-in option
```py
import pycing
op = pycing.UpOutOption(noOfPath=10000, S=100, K=105, T=20/365, r=0.04, sigma=0.3, steps=300, knockOutPrice=130)
op.pricing()
```

### Customize your own derivative
```py
class YourOwnDerivative(Derivative):

    def __init__(self, S, K, T, r, sigma, steps=300, **kwargs):
        # Initilize the parent class
        super().__init__(S_0=S, T=T, r=r, sigma=sigma, steps=steps, **kwargs)
        # It is necessary to define some necessary attribution
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma

    def payoff(self, underlyingAssetPath, **kwargs):
        # The <class Derivative> will input a price path of the underlying asset
        # underlyingAssetPath : 1-D np.array
        
        # You can specify any condition...
        if max(underlyingAssetPath) <= self.knockOutPrice:
            return self.knockOutPrenium * np.exp(-self.r * self.T)

        # You can specify the payoff function...
        return max(self.K - underlyingAssetPath[-1], 0) * np.exp(-self.r * self.T)

```

-------------------------------------------
## Acknowledgement
Thanks to [@Starishli](https://github.com/Starishli/SimPricing) for a clear and well-established framework.
