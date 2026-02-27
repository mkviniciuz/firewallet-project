import os
from ctypes import CDLL, c_double, c_int

LIB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),"../../src_native/build/wallet_math.dll"))

lib = CDLL(LIB_PATH)

lib.cal_balance.argtypes = [c_double,c_double]
lib.cal_balance.restype = c_double

lib.compound_interest.argtypes = [c_double, c_double, c_int]
lib.compound_interest.restype = c_double

lib.percent_change.argtypes = [c_double, c_double]
lib.percent_change.restype = c_double


def cal_balance_py(total_in: float, total_out: float) -> float:
    return lib.cal_balance(total_in, total_out)

def compound_interest(principal: float, rate: float, months: int) -> float:
    return lib.compound_interest(principal, rate, months)

def percent_change_py(old: float, new: float) -> float:
    return lib.percent_change(old, new)