from backend.services.calc_service import (
    calc_balance_py,
    compound_interest_py,
    percent_change_py
)


print("Saldo:", cal_balance_py(1000,300))
print("Juros:", compound_interest_py(1000, 0.02, 12))
print("Variação:", percent_change_py(200, 260))