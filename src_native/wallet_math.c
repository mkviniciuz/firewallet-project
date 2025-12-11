#include "wallet_math.h"

double cal_balance(double total_in, double total_out){
    return total_in - total_out;
}

double compound_interest(double principal, double rate, int month){
    double result = principal;

    for (int i = 0; i < month; i++)
    {
        result *=(1 + rate);
    }
    return result;
}

double percent_change(double old_value, double new_value){
    if(old_value == 0){

        return 0;
    }

return ((new_value - old_value) / old_value) * 100;
}
