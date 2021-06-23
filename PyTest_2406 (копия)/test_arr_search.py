import pytest

from arr_2406 import FromArraySearch
arr = [1,2,3]
# arr = list(map(int,(input())))
arr_1 = [7,8,9]
ar_str = [1,'string','any_string']


@pytest.mark.parametrize('ar, expected', [(arr, max(arr)), 
                                        # (ar_str, max(ar_str)),
                                        (arr, 1),
                                        (arr_1, max(arr_1))])
def test_max_arr(ar, expected):
    elemsearch = FromArraySearch()
    assert elemsearch.max_arr(ar) == expected

@pytest.mark.parametrize('ar, expected', [(arr, sum(arr)), 
                                        # (ar_str, sum(ar_str)),
                                        (arr, 1),
                                        (arr_1, sum(arr_1))])
def test_summ_arr(ar, expected):
    elemsearch = FromArraySearch()
    assert elemsearch.summ_arr(ar) == expected
    # assert elemsearch.summ_arr(arr) == 6

@pytest.mark.parametrize('ar, expected', [(arr, sum(arr)/len(arr)), 
                                        # (ar_str, sum(ar_str)/len(ar_str)),
                                        (arr, 1),
                                        (arr_1, sum(arr_1)/len(arr_1))])
def test_mean_arr(ar,expected):
    elemsearch = FromArraySearch()
    assert elemsearch.mean_arr(ar) == expected
#     # assert elemsearch.mean_arr(arr) == 2

            
@pytest.mark.parametrize('ar, expected', [(arr, min(arr)),
                                           (arr, 100), 
                                        # (ar_str, sum(ar_str)/len(ar_str)),
                                        (arr_1, min(arr_1))])
def test_min_arr(ar,expected):
    elemsearch = FromArraySearch()
    assert elemsearch.min_arr(ar) == expected
    # assert elemsearch.min_arr(arr) == 1