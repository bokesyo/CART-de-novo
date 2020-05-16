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
            return 6.041666666666663
        else: 
            if volatile_acidity<0.67:
                if alcohol<9.9:
                    return 5.266666666666665
                else: 
                    if sulphates<0.69:
                        return 5.448979591836735
                    else: 
                        if free_sulfur_dioxide<32:
                            return 6.249999999999999
                        else: 
                            return 4.666666666666667
            else: 
                return 5.049999999999995
    else: 
        if sulphates<0.59:
            if volatile_acidity<1.02:
                if pH<3.37:
                    return 5.933333333333335
                else: 
                    return 5.3870967741935525
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
                    return 5.39130434782609
            else: 
                if free_sulfur_dioxide<15:
                    return 6.95121951219512
                else: 
                    return 6.250000000000002
