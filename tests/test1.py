
import pytest


class Tests:

    @pytest.mark.parametrize("a,b,c",[(11,12,23),(13,14,27),(15,16,31)])
    def test_add(self,a,b,c):
        print("a value: {0} b value: {1} c value: {2}".format(a,b,c))
        assert a + b == c

    @pytest.mark.parametrize("a,b,c",[(11,12,1),(13,14,1),(15,16,1)])
    def test_sub(self,a,b,c):
        print("a value: {0} b value: {1} c value: {2}".format(a,b,c))
        assert b - a == c

    @pytest.mark.parametrize("a,b,c",[(2,3,6),(3,4,12),(5,7,35)])
    def test_mul(self,a,b,c):
        print("a value: {0} b value: {1} c value: {2}".format(a,b,c))
        assert a * b == c

#
#
# # @pytest.parametrize("input_value,exp_value",[(11,12),(13,14),(15,16)])
# test_add(3,4)
#
#
# test_sub(3,4)
# test_mul(3,4)

