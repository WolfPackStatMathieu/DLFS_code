import numpy as np
from numpy import ndarray


def assert_same_shape(array: ndarray,
                      array_grad: ndarray):
    assert array.shape == array_grad.shape, \
        '''
        Two ndarrays should have the same shape;
        instead; first ndarray's shape is {0}
        and second ndarray's shape is {1}
        '''.format(tuple(array.shape), tuple(array_grad.shape))
    return None


def run_tests():
    # Test avec des tableaux de même forme
    try:
        a = np.array([[1, 2, 3], [4, 5, 6]])
        b = np.array([[7, 8, 9], [10, 11, 12]])
        assert_same_shape(a, b)
        print("Test 1 Passé: Les formes correspondent.")
    except AssertionError as e:
        print("Test 1 Échoué:", e)

    # Test avec des tableaux de formes différentes
    try:
        c = np.array([[1, 2], [3, 4], [5, 6]])
        d = np.array([[7, 8, 9], [10, 11, 12]])
        assert_same_shape(c, d)
        print("Test 2 Passé: Les formes correspondent.")
    except AssertionError as e:
        print("Test 2 Échoué:", e)

if __name__ == '__main__':
    run_tests()
