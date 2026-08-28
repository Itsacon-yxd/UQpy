from typing import Union

import scipy.stats as stats
from beartype import beartype

from UQpy.distributions.baseclass import DistributionContinuous1D



class Triangular(DistributionContinuous1D):
    @beartype
    def __init__(
        self,c, loc: Union[None, float, int] = 0.0, scale: Union[None, float, int] = 1.0
    ):
        """

        :param loc: lower bound
        :param scale: range
        """
        super().__init__(c=c,loc=loc, scale=scale, ordered_parameters=("c", "loc", "scale"))
        self._construct_from_scipy(scipy_name=stats.triang)

if __name__ == "__main__":
    dist = Triangular(c=0.5, loc=0, scale=1)
    print(dist.pdf(0.5))
    print(dist.cdf(0.5))
    # print(dist.ppf(0.5))
    # print(dist.rvs())
