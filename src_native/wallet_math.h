#ifndef WALLET_MATH_H
#define WALLET_MATH_H

//Calcula entrada e saida
double cal_balance(double total_in, double total_out);

//JUros compostos
double compound_interest(double principal, double rate, int month);

//Variação percentual
double percent_change(double old_value, double new_value);

#endif