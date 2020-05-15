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
        if volatile_acidity<0.37:
            if sulphates<1.1:
                return 5.809523809523816
            else: 
                return 6.75
        else: 
            if volatile_acidity<0.655:
                if alcohol<9.9:
                    if free_sulfur_dioxide<10:
                        if sulphates<0.54:
                            return 5.083333333333333
                        else: 
                            if pH<3.12:
                                return 5.0
                            else: 
                                if residual_sugar<1.7:
                                    return 6.0
                                else: 
                                    if fixed_acidity<7.8:
                                        return 5.230769230769231
                                    else: 
                                        if pH<3.36:
                                            if free_sulfur_dioxide<8:
                                                return 5.833333333333332
                                            else: 
                                                return 5.0
                                        else: 
                                            return 7.0
                    else: 
                        if pH<3.43:
                            if density<1.001:
                                if density<1.0008:
                                    return 5.0777777777777775
                                else: 
                                    return 3.0
                            else: 
                                return 6.0
                        else: 
                            return 5.444444444444444
                else: 
                    if sulphates<0.69:
                        if pH<3.46:
                            return 5.5348837209302335
                        else: 
                            return 4.833333333333333
                    else: 
                        if free_sulfur_dioxide<32:
                            if alcohol<10.2:
                                return 6.5
                            else: 
                                return 5.666666666666667
                        else: 
                            return 4.666666666666667
            else: 
                if density<0.9983:
                    if citric_acid<0.07:
                        if residual_sugar<5.7:
                            if volatile_acidity<1.04:
                                if volatile_acidity<0.975:
                                    return 4.857142857142855
                                else: 
                                    return 3.5
                            else: 
                                return 6.0
                        else: 
                            return 3.0
                    else: 
                        return 5.111111111111117
                else: 
                    return 5.533333333333332
    else: 
        if volatile_acidity<0.875:
            if alcohol<11.5:
                if volatile_acidity<0.32:
                    if volatile_acidity<0.24:
                        return 5.333333333333333
                    else: 
                        return 6.526315789473684
                else: 
                    if total_sulfur_dioxide<72:
                        if sulphates<0.58:
                            if alcohol<10.6:
                                return 6.4
                            else: 
                                return 5.318181818181821
                        else: 
                            if alcohol<10.8:
                                return 5.7
                            else: 
                                if volatile_acidity<0.37:
                                    return 6.6
                                else: 
                                    if residual_sugar<5.5:
                                        return 5.95744680851064
                                    else: 
                                        if sulphates<0.59:
                                            return 5.0
                                        else: 
                                            return 7.0
                    else: 
                        return 5.181818181818182
            else: 
                if sulphates<0.64:
                    if volatile_acidity<0.6:
                        return 6.242424242424243
                    else: 
                        if residual_sugar<2.5:
                            return 5.866666666666668
                        else: 
                            return 4.8
                else: 
                    if fixed_acidity<13:
                        if free_sulfur_dioxide<15:
                            return 6.976190476190477
                        else: 
                            if pH<3.5:
                                return 6.350000000000001
                            else: 
                                return 7.25
                    else: 
                        return 5.5
        else: 
            if fixed_acidity<6.7:
                return 5.250000000000001
            else: 
                return 4.375
