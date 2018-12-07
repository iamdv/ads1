import numpy as np
import pandas as pd

## Numpy

"""
Randomisation can be a good way to generate arbitrary outputs
and make sure your function works "as expected" with those inputs
in that case, it's still useful to SEED the random number generator
so that your tests are reproducible which is very important.
To seed the random number generator use `np.random.seed(12333)` where
the number doesn't really matter (pick any integer you want).
"""

## Exercise 1:

"""
* create an array a1 of 100 random values, don't forget to seed with np.random.seed(NUMBER)
* compute the array a2 where elements are squares of the elements of a1
* compute an array a3 where elements are square roots of the elements of a2
* test that a3 is close to a1
"""

# TODO

## Pandas

"""
Pandas offers similar testing than Numpy but specifically for the structures
it defines like the pd.Series object.
"""

## Exercise 2:

"""
perform the exact same exercise as exercise 1 but storing the initial array
in a pd.Series with name `values` and testing using
`pd.testing.assert_series_equal`, you may want to check the doc first.
PS: use `np.power` and not `np.sqrt` for the `pd.Series`
"""

# TODO