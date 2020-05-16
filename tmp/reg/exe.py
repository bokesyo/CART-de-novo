def classifier(data_list):
    fixed_acidity = data_list[0]
    volatile_acidity = data_list[1]
    citric_acid = data_list[2]
    residual_sugar = data_list[3]
    chlorides = data_list[4]
    free_sulfur_dioxide = data_list[5]
    total_sulfur_dioxide = data_list[6]
    density = data_list[7]
    pH = data_list[8]
    sulphates = data_list[9]
    alcohol = data_list[10]
    if alcohol<10.5:
        if volatile_acidity<0.32:
            return 138.83922152682135 + fixed_acidity * 138.83922152682135 + density * 0.15008044669719034 + sulphates * -135.56391013241227
        else: 
            if volatile_acidity<0.67:
                if alcohol<9.9:
                    return 5.266666666666667
                else: 
                    if sulphates<0.69:
                        return 5.448979591836734
                    else: 
                        if free_sulfur_dioxide<32:
                            return 17.51565074136306 + alcohol * 17.51565074136306
                        else: 
                            return 132.0 + fixed_acidity * 132.0 + citric_acid * -4.25 + residual_sugar * 64.0 + chlorides * 20.0 + free_sulfur_dioxide * 128.0 + density * -5.625 + pH * 36.0 + sulphates * -59.0 + alcohol * 101.5
            else: 
                return 5.050000000000001
    else:
        if sulphates<0.59:
            if volatile_acidity<1.02:
                if pH<3.37:
                    return 4.572578520865818 + fixed_acidity * 4.572578520865818 + citric_acid * -0.15995256053624907 + sulphates * -0.30470763806534507
                else: 
                    return 26.22528096420865 + free_sulfur_dioxide * 26.22528096420865 + density * 0.02003677844681029 + alcohol * -24.291151052246278
            else: 
                return 4.0
        else: 
            if alcohol<11.6:
                if total_sulfur_dioxide<58:
                    if residual_sugar<5.5:
                        if pH<3.2:
                            if volatile_acidity<0.4:
                                return 7.000000000000002
                            else: 
                                return 6.0
                        else: 
                            return 6.035714285714283
                    else: 
                        return 7.0
                else: 
                    return 5.478948479967009 + residual_sugar * 5.478948479967009 + free_sulfur_dioxide * -0.13954884928230626
            else: 
                if free_sulfur_dioxide<15:
                    return 6.951219512195122
                else: 
                    return 91.0280531491153 + fixed_acidity * 91.0280531491153 + chlorides * -0.049620603597077206 + density * -3.799200128938537
