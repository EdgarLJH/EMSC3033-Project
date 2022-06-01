import pytest
from src.functions import *



def test_random_points(rtol = 50 * 3):
    data = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
    result = len(random_points(data, 50)[1])
    print(result)
    assert result == rtol, " *** Number of random onshore points not as requested by user "
    
    
    
def test_get_cdf(rtol = 1e-13):
    result = len(get_cdf(np.arange(100), 10)[0])
    assert result > rtol, " *** Bin size is too large - please reduce bin_interval or increase size of input data """
    
    
    
def test_get_std(rtol = np.std(np.array([600, 470, 170, 430, 300]))):
    result = get_std(np.array([600, 470, 170, 430, 300]), 1000)
    assert result == rtol, " *** Standard deviation calculation error "
    
    
    
def test_ks2(rtol = 10):
    a = np.random.random(100)
    b = np.random.random(1000)
    ks2(a, b, 10)
    result = len(b) / len(a)
    assert result == rtol, " *** size of data2 is not completely divisible by n "
    
    

