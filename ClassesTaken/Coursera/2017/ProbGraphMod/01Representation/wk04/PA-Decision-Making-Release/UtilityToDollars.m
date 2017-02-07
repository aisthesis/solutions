function dollars = UtilityToDollars(utility)
    dollars = 0;
    tmp = utility / 100.0;
    tmp = exp(tmp);
    dollars = tmp - 1.0;
endfunction;
