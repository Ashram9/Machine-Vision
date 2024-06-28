import numpy as np

from functions import ScalarFunction


class FiniteDifference(ScalarFunction):
    def __init__(self, h=1e-3):
        super(FiniteDifference, self).__init__()
        self.h = h

    def jacobian(self, x):
        # TO DO: Replace this with the finite difference approximation of the first derivatives.
        # Remember that this should be a vector of partial derivatives (e.g. a 2x1 vector for a 2D function)
        # Calculate the finite difference approximation of the first derivatives using central differences
        n = len(x)
        jacobian_vector = np.zeros((n, 1))

        for i in range(n):
            # Perturb the i-th component of x
            x_plus_h = np.copy(x).astype(np.float64)
            x_plus_h[i] += self.h

            # Evaluate the function at x and x_plus_h
            f_x = self.__call__(x)
            f_x_plus_h = self.__call__(x_plus_h)

            # Calculate the finite difference approximation of the i-th partial derivative
            jacobian_vector[i] = (f_x_plus_h - f_x) / self.h

        return jacobian_vector
        

    def hessian(self, x):
        raise NotImplementedError('finite difference has not been defined for hessian')


def finite_difference(function_type, *args, **kwargs):
    """Create an instance of a function with finite differences instead of analytical derivatives

    Examples:
        For a function that implements derivatives this uses finite differences instead. For a relatively smooth
        function you would expect the value to be comparable to the exact derivative.

        >>> rosenbrock = functions.Rosenbrock()
        >>> type(rosenbrock)
        functions.Rosenbrock
        >>> rosenbrock.jacobian(np.array([[1, 2]]).T)
        array([[-400],
               [ 200]])

        >>> rosenbrock = finite_difference(functions.Rosenbrock)
        >>> type(rosenbrock)
        numerical.RosenbrockFiniteDifference
        >>> rosenbrock.jacobian(np.array([[1, 2]]).T)
        array([[-400.0008006],
               [ 200.       ]])
    """
    name = '{}FiniteDifference'.format(function_type.__name__)
    finite_difference_function = type(name, (FiniteDifference, function_type), {})  # type()动态创建新类, 继承自(FiniteDifference, function_type), finite_difference_function是这个新类的引用
    return finite_difference_function(*args, **kwargs)  # 返回finite_difference_function类的一个实例

