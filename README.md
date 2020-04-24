# GenGauss

A simple package for fitting a Gaussian distribuion to data. This is only a practice code, nothing substantial here...


`pip install gengauss'

```
from gengauss import GaussianModel
model = GaussianModel()
model.fit(data)
samples = model.sample(num_samples=100)
```
