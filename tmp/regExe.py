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
    if alcohol<10.55:
        if volatile_acidity<0.34:
            if sulphates<0.66:
                if total_sulfur_dioxide<32:
                    if alcohol<10.5:
                        if alcohol<10.4:
                            if alcohol<10.3:
                                return 6.0
                            else: 
                                return 6.0
                        else: 
                            return 6.0
                    else: 
                        return 5.0
                else: 
                    if density<0.9976:
                        if alcohol<9.5:
                            if sulphates<0.65:
                                return 4.0
                            else: 
                                return 5.0
                        else: 
                            if alcohol<10.1:
                                if alcohol<9.6:
                                    return 5.0
                                else: 
                                    return 5.0
                            else: 
                                return 5.0
                    else: 
                        return 6.0
            else: 
                if density<0.99648:
                    if sulphates<1.1:
                        return 7.0
                    else: 
                        return 8.0
                else: 
                    if fixed_acidity<11.8:
                        if alcohol<9.8:
                            if total_sulfur_dioxide<19:
                                if alcohol<9.7:
                                    return 5.0
                                else: 
                                    return 5.0
                            else: 
                                if total_sulfur_dioxide<83:
                                    if alcohol<9.7:
                                        if alcohol<9.6:
                                            if alcohol<9.4:
                                                if alcohol<9.3:
                                                    if alcohol<9.2:
                                                        return 6.0
                                                    else: 
                                                        return 6.0
                                                else: 
                                                    return 6.0
                                            else: 
                                                return 6.0
                                        else: 
                                            return 6.0
                                    else: 
                                        return 6.0
                                else: 
                                    return 5.0
                        else: 
                            if volatile_acidity<0.25:
                                if alcohol<10.4:
                                    if alcohol<10.3:
                                        if alcohol<10.2:
                                            if alcohol<10.1:
                                                if alcohol<10:
                                                    return 6.0
                                                else: 
                                                    return 6.0
                                            else: 
                                                return 6.0
                                        else: 
                                            return 6.0
                                    else: 
                                        return 6.0
                                else: 
                                    if sulphates<0.81:
                                        if alcohol<10.5:
                                            return 5.0
                                        else: 
                                            return 5.0
                                    else: 
                                        return 6.0
                            else: 
                                if alcohol<10.5:
                                    if sulphates<0.82:
                                        if alcohol<10.2:
                                            if alcohol<10.1:
                                                return 6.0
                                            else: 
                                                return 6.0
                                        else: 
                                            return 6.0
                                    else: 
                                        if sulphates<0.9:
                                            if alcohol<10.3:
                                                return 7.0
                                            else: 
                                                return 7.0
                                        else: 
                                            if total_sulfur_dioxide<28:
                                                return 7.0
                                            else: 
                                                if alcohol<10.3:
                                                    if alcohol<10:
                                                        return 6.0
                                                    else: 
                                                        return 6.0
                                                else: 
                                                    return 6.0
                                else: 
                                    return 7.0
                    else: 
                        if alcohol<9.2:
                            return 6.0
                        else: 
                            if alcohol<10.2:
                                if alcohol<9.9:
                                    if alcohol<9.8:
                                        return 7.0
                                    else: 
                                        return 7.0
                                else: 
                                    return 7.0
                            else: 
                                return 7.0
        else: 
            if volatile_acidity<0.655:
                if alcohol<9.9:
                    if total_sulfur_dioxide<42:
                        if sulphates<0.57:
                            if total_sulfur_dioxide<12:
                                return 6.0
                            else: 
                                if pH<3.37:
                                    if pH<3.13:
                                        return 6.0
                                    else: 
                                        if residual_sugar<2.7:
                                            if volatile_acidity<0.585:
                                                if alcohol<9.8:
                                                    if alcohol<9.7:
                                                        if alcohol<9.6:
                                                            if alcohol<9.5:
                                                                if alcohol<9.4:
                                                                    return 5.0
                                                                else: 
                                                                    return 5.0
                                                            else: 
                                                                return 5.0
                                                        else: 
                                                            return 5.0
                                                    else: 
                                                        return 5.0
                                                else: 
                                                    return 5.0
                                            else: 
                                                if volatile_acidity<0.6:
                                                    return 6.0
                                                else: 
                                                    if alcohol<9.8:
                                                        return 5.0
                                                    else: 
                                                        return 5.0
                                        else: 
                                            if alcohol<9.5:
                                                return 6.0
                                            else: 
                                                return 5.0
                                else: 
                                    return 6.0
                        else: 
                            if fixed_acidity<6.8:
                                if sulphates<0.64:
                                    if sulphates<0.63:
                                        return 5.0
                                    else: 
                                        return 6.0
                                else: 
                                    if alcohol<9.8:
                                        if alcohol<9.7:
                                            if alcohol<9.5:
                                                if alcohol<9.4:
                                                    return 5.0
                                                else: 
                                                    return 5.0
                                            else: 
                                                return 5.0
                                        else: 
                                            return 5.0
                                    else: 
                                        return 5.0
                            else: 
                                if volatile_acidity<0.61:
                                    if citric_acid<0.2:
                                        if sulphates<0.59:
                                            return 7.0
                                        else: 
                                            if alcohol<9.8:
                                                if alcohol<9.7:
                                                    if alcohol<9.6:
                                                        if alcohol<9.5:
                                                            if alcohol<9.4:
                                                                if alcohol<9.2:
                                                                    return 6.0
                                                                else: 
                                                                    return 6.0
                                                            else: 
                                                                return 6.0
                                                        else: 
                                                            return 6.0
                                                    else: 
                                                        return 6.0
                                                else: 
                                                    return 6.0
                                            else: 
                                                return 6.0
                                    else: 
                                        if alcohol<9.4:
                                            if pH<3.48:
                                                if sulphates<0.8:
                                                    if alcohol<9.3:
                                                        if alcohol<9.2:
                                                            return 6.0
                                                        else: 
                                                            return 6.0
                                                    else: 
                                                        return 6.0
                                                else: 
                                                    if alcohol<9.3:
                                                        if alcohol<9.2:
                                                            return 6.0
                                                        else: 
                                                            return 6.0
                                                    else: 
                                                        return 5.0
                                            else: 
                                                return 5.0
                                        else: 
                                            if chlorides<0.171:
                                                if total_sulfur_dioxide<38:
                                                    if alcohol<9.8:
                                                        if alcohol<9.6:
                                                            if alcohol<9.5:
                                                                return 5.0
                                                            else: 
                                                                return 5.0
                                                        else: 
                                                            return 5.0
                                                    else: 
                                                        return 6.0
                                                else: 
                                                    if alcohol<9.8:
                                                        return 6.0
                                                    else: 
                                                        return 6.0
                                            else: 
                                                if alcohol<9.5:
                                                    return 6.0
                                                else: 
                                                    return 6.0
                                else: 
                                    if citric_acid<0.05:
                                        if alcohol<9.7:
                                            if alcohol<9.5:
                                                if alcohol<9.4:
                                                    if alcohol<9.2:
                                                        return 6.0
                                                    else: 
                                                        return 6.0
                                                else: 
                                                    return 6.0
                                            else: 
                                                return 6.0
                                        else: 
                                            if alcohol<9.8:
                                                return 5.0
                                            else: 
                                                return 5.0
                                    else: 
                                        if alcohol<9.7:
                                            if alcohol<9.6:
                                                if alcohol<9.4:
                                                    if alcohol<9.3:
                                                        return 5.0
                                                    else: 
                                                        return 5.0
                                                else: 
                                                    return 5.0
                                            else: 
                                                return 5.0
                                        else: 
                                            return 5.0
                    else: 
                        if citric_acid<0.66:
                            if pH<3.41:
                                if free_sulfur_dioxide<7:
                                    if sulphates<1.09:
                                        if alcohol<9.5:
                                            return 6.0
                                        else: 
                                            return 6.0
                                    else: 
                                        return 5.0
                                else: 
                                    if density<1.0014:
                                        if total_sulfur_dioxide<115:
                                            if total_sulfur_dioxide<79:
                                                if fixed_acidity<10.5:
                                                    if sulphates<0.62:
                                                        if alcohol<9.8:
                                                            if alcohol<9.7:
                                                                if alcohol<9.6:
                                                                    if alcohol<9.5:
                                                                        if alcohol<9.4:
                                                                            if alcohol<9.3:
                                                                                if alcohol<9.2:
                                                                                    return 5.0
                                                                                else: 
                                                                                    return 5.0
                                                                            else: 
                                                                                return 5.0
                                                                        else: 
                                                                            return 5.0
                                                                    else: 
                                                                        return 5.0
                                                                else: 
                                                                    return 5.0
                                                            else: 
                                                                return 5.0
                                                        else: 
                                                            return 5.0
                                                    else: 
                                                        if residual_sugar<2.5:
                                                            if alcohol<9.7:
                                                                if alcohol<9.5:
                                                                    if alcohol<9.3:
                                                                        if alcohol<9.2:
                                                                            return 5.0
                                                                        else: 
                                                                            return 5.0
                                                                    else: 
                                                                        return 5.0
                                                                else: 
                                                                    return 5.0
                                                            else: 
                                                                return 5.0
                                                        else: 
                                                            if fixed_acidity<8.7:
                                                                if alcohol<9.6:
                                                                    return 6.0
                                                                else: 
                                                                    return 6.0
                                                            else: 
                                                                if alcohol<9.8:
                                                                    if alcohol<9.6:
                                                                        return 5.0
                                                                    else: 
                                                                        return 5.0
                                                                else: 
                                                                    return 5.0
                                                else: 
                                                    if alcohol<9.6:
                                                        return 5.0
                                                    else: 
                                                        return 4.0
                                            else: 
                                                if total_sulfur_dioxide<84:
                                                    if alcohol<9.7:
                                                        return 6.0
                                                    else: 
                                                        return 6.0
                                                else: 
                                                    if chlorides<0.073:
                                                        return 6.0
                                                    else: 
                                                        if sulphates<0.51:
                                                            if alcohol<9.6:
                                                                return 5.0
                                                            else: 
                                                                if alcohol<9.8:
                                                                    return 6.0
                                                                else: 
                                                                    return 6.0
                                                        else: 
                                                            if total_sulfur_dioxide<101:
                                                                if alcohol<9.5:
                                                                    if alcohol<9.4:
                                                                        if alcohol<9.3:
                                                                            if alcohol<9.2:
                                                                                if alcohol<9.1:
                                                                                    if alcohol<9:
                                                                                        return 5.0
                                                                                    else: 
                                                                                        return 5.0
                                                                                else: 
                                                                                    return 5.0
                                                                            else: 
                                                                                return 5.0
                                                                        else: 
                                                                            return 5.0
                                                                    else: 
                                                                        return 5.0
                                                                else: 
                                                                    if density<0.99616:
                                                                        if alcohol<9.8:
                                                                            return 5.0
                                                                        else: 
                                                                            return 5.0
                                                                    else: 
                                                                        if pH<3.37:
                                                                            if alcohol<9.8:
                                                                                return 6.0
                                                                            else: 
                                                                                return 6.0
                                                                        else: 
                                                                            return 5.0
                                                            else: 
                                                                if alcohol<9.8:
                                                                    if alcohol<9.7:
                                                                        if alcohol<9.5:
                                                                            if alcohol<9.4:
                                                                                if alcohol<9.3:
                                                                                    return 5.0
                                                                                else: 
                                                                                    return 5.0
                                                                            else: 
                                                                                return 5.0
                                                                        else: 
                                                                            return 5.0
                                                                    else: 
                                                                        return 5.0
                                                                else: 
                                                                    return 5.0
                                        else: 
                                            if residual_sugar<1.8:
                                                return 4.0
                                            else: 
                                                if alcohol<9.8:
                                                    if alcohol<9.7:
                                                        if alcohol<9.5:
                                                            if alcohol<9.4:
                                                                if alcohol<9.3:
                                                                    if alcohol<9.2:
                                                                        return 5.0
                                                                    else: 
                                                                        return 5.0
                                                                else: 
                                                                    return 5.0
                                                            else: 
                                                                return 5.0
                                                        else: 
                                                            return 5.0
                                                    else: 
                                                        return 5.0
                                                else: 
                                                    return 5.0
                                    else: 
                                        if alcohol<9:
                                            return 5.0
                                        else: 
                                            if alcohol<9.5:
                                                return 6.0
                                            else: 
                                                return 6.0
                            else: 
                                if citric_acid<0.33:
                                    if sulphates<0.55:
                                        if pH<3.55:
                                            if density<0.9993:
                                                if alcohol<9.7:
                                                    if alcohol<9.5:
                                                        return 5.0
                                                    else: 
                                                        return 5.0
                                                else: 
                                                    return 5.0
                                            else: 
                                                return 6.0
                                        else: 
                                            return 6.0
                                    else: 
                                        if volatile_acidity<0.52:
                                            if alcohol<9.8:
                                                if alcohol<9.7:
                                                    return 6.0
                                                else: 
                                                    return 6.0
                                            else: 
                                                return 6.0
                                        else: 
                                            if chlorides<0.079:
                                                if alcohol<9.8:
                                                    return 5.0
                                                else: 
                                                    return 5.0
                                            else: 
                                                if sulphates<0.79:
                                                    if alcohol<9.8:
                                                        if alcohol<9.7:
                                                            if alcohol<9.3:
                                                                return 6.0
                                                            else: 
                                                                return 6.0
                                                        else: 
                                                            return 6.0
                                                    else: 
                                                        return 6.0
                                                else: 
                                                    return 5.0
                                else: 
                                    if alcohol<9.7:
                                        if alcohol<9.5:
                                            if alcohol<9.2:
                                                if alcohol<9.1:
                                                    return 5.0
                                                else: 
                                                    return 5.0
                                            else: 
                                                return 5.0
                                        else: 
                                            return 5.0
                                    else: 
                                        return 5.0
                        else: 
                            if alcohol<9.3:
                                return 3.0
                            else: 
                                if alcohol<9.4:
                                    return 5.0
                                else: 
                                    return 4.0
                else: 
                    if pH<3.49:
                        if total_sulfur_dioxide<87:
                            if total_sulfur_dioxide<10:
                                if sulphates<0.47:
                                    return 4.0
                                else: 
                                    if alcohol<10.4:
                                        return 5.0
                                    else: 
                                        return 5.0
                            else: 
                                if residual_sugar<1.6:
                                    if total_sulfur_dioxide<21:
                                        return 6.0
                                    else: 
                                        if alcohol<10:
                                            return 7.0
                                        else: 
                                            return 7.0
                                else: 
                                    if chlorides<0.122:
                                        if sulphates<0.63:
                                            if citric_acid<0.02:
                                                return 7.0
                                            else: 
                                                if density<0.99575:
                                                    if sulphates<0.53:
                                                        return 5.0
                                                    else: 
                                                        if alcohol<10.5:
                                                            if alcohol<10.4:
                                                                if alcohol<10.3:
                                                                    return 6.0
                                                                else: 
                                                                    return 6.0
                                                            else: 
                                                                return 6.0
                                                        else: 
                                                            return 6.0
                                                else: 
                                                    if fixed_acidity<7.7:
                                                        if free_sulfur_dioxide<6:
                                                            if alcohol<10.3:
                                                                return 6.0
                                                            else: 
                                                                return 6.0
                                                        else: 
                                                            if alcohol<10.5:
                                                                if alcohol<10.3:
                                                                    if alcohol<10.2:
                                                                        if alcohol<10.1:
                                                                            return 5.0
                                                                        else: 
                                                                            return 5.0
                                                                    else: 
                                                                        return 5.0
                                                                else: 
                                                                    return 5.0
                                                            else: 
                                                                return 6.0
                                                    else: 
                                                        if citric_acid<0.39:
                                                            if density<0.99613:
                                                                if alcohol<10.4:
                                                                    if alcohol<10.3:
                                                                        if alcohol<10.2:
                                                                            return 5.0
                                                                        else: 
                                                                            return 5.0
                                                                    else: 
                                                                        return 5.0
                                                                else: 
                                                                    return 6.0
                                                            else: 
                                                                if citric_acid<0.06:
                                                                    if sulphates<0.61:
                                                                        return 6.0
                                                                    else: 
                                                                        return 5.0
                                                                else: 
                                                                    if alcohol<10.5:
                                                                        if alcohol<10.2:
                                                                            if alcohol<10.1:
                                                                                if alcohol<10:
                                                                                    return 6.0
                                                                                else: 
                                                                                    return 6.0
                                                                            else: 
                                                                                return 6.0
                                                                        else: 
                                                                            return 6.0
                                                                    else: 
                                                                        return 6.0
                                                        else: 
                                                            if total_sulfur_dioxide<64:
                                                                if alcohol<10.5:
                                                                    if alcohol<10.4:
                                                                        if alcohol<10.3:
                                                                            return 5.0
                                                                        else: 
                                                                            return 5.0
                                                                    else: 
                                                                        return 5.0
                                                                else: 
                                                                    return 5.0
                                                            else: 
                                                                return 6.0
                                        else: 
                                            if pH<3.06:
                                                return 5.0
                                            else: 
                                                if residual_sugar<6.1:
                                                    if residual_sugar<5.6:
                                                        if alcohol<10:
                                                            if free_sulfur_dioxide<29:
                                                                return 6.0
                                                            else: 
                                                                return 5.0
                                                        else: 
                                                            if alcohol<10.2:
                                                                if total_sulfur_dioxide<49:
                                                                    if volatile_acidity<0.415:
                                                                        return 7.0
                                                                    else: 
                                                                        if alcohol<10.1:
                                                                            return 6.0
                                                                        else: 
                                                                            return 6.0
                                                                else: 
                                                                    if density<0.9992:
                                                                        return 7.0
                                                                    else: 
                                                                        return 6.0
                                                            else: 
                                                                if citric_acid<0.66:
                                                                    if fixed_acidity<12.5:
                                                                        if total_sulfur_dioxide<41:
                                                                            if sulphates<0.67:
                                                                                if pH<3.26:
                                                                                    return 6.0
                                                                                else: 
                                                                                    if alcohol<10.5:
                                                                                        return 5.0
                                                                                    else: 
                                                                                        return 5.0
                                                                            else: 
                                                                                if alcohol<10.5:
                                                                                    if alcohol<10.4:
                                                                                        return 6.0
                                                                                    else: 
                                                                                        return 6.0
                                                                                else: 
                                                                                    return 6.0
                                                                        else: 
                                                                            if alcohol<10.5:
                                                                                if alcohol<10.4:
                                                                                    if alcohol<10.3:
                                                                                        return 6.0
                                                                                    else: 
                                                                                        return 6.0
                                                                                else: 
                                                                                    return 6.0
                                                                            else: 
                                                                                return 6.0
                                                                    else: 
                                                                        return 5.0
                                                                else: 
                                                                    return 7.0
                                                    else: 
                                                        if alcohol<10.5:
                                                            if alcohol<10.1:
                                                                return 7.0
                                                            else: 
                                                                return 7.0
                                                        else: 
                                                            return 7.0
                                                else: 
                                                    return 5.0
                                    else: 
                                        if alcohol<10.2:
                                            return 4.0
                                        else: 
                                            return 5.0
                        else: 
                            if sulphates<1.18:
                                if alcohol<10.5:
                                    if alcohol<10.1:
                                        if alcohol<10:
                                            return 5.0
                                        else: 
                                            return 5.0
                                    else: 
                                        return 5.0
                                else: 
                                    return 5.0
                            else: 
                                if alcohol<10.5:
                                    return 6.0
                                else: 
                                    return 6.0
                    else: 
                        if total_sulfur_dioxide<23:
                            return 4.0
                        else: 
                            if density<0.99547:
                                if alcohol<10.3:
                                    return 5.0
                                else: 
                                    return 6.0
                            else: 
                                if alcohol<10.5:
                                    if alcohol<10.4:
                                        return 5.0
                                    else: 
                                        return 5.0
                                else: 
                                    return 5.0
            else: 
                if density<0.9983:
                    if density<0.99502:
                        if alcohol<10:
                            return 3.0
                        else: 
                            if alcohol<10.5:
                                return 5.0
                            else: 
                                return 4.0
                    else: 
                        if residual_sugar<5.7:
                            if residual_sugar<5.2:
                                if pH<3.55:
                                    if total_sulfur_dioxide<11:
                                        if sulphates<0.48:
                                            return 5.0
                                        else: 
                                            if alcohol<9.7:
                                                return 6.0
                                            else: 
                                                return 6.0
                                    else: 
                                        if sulphates<0.5:
                                            if volatile_acidity<0.755:
                                                if alcohol<10:
                                                    if alcohol<9.7:
                                                        if alcohol<9.6:
                                                            if alcohol<9.5:
                                                                if alcohol<9.4:
                                                                    return 5.0
                                                                else: 
                                                                    return 5.0
                                                            else: 
                                                                return 5.0
                                                        else: 
                                                            return 5.0
                                                    else: 
                                                        return 5.0
                                                else: 
                                                    return 5.0
                                            else: 
                                                if chlorides<0.092:
                                                    if residual_sugar<2.3:
                                                        if alcohol<10:
                                                            if alcohol<9.8:
                                                                if alcohol<9.7:
                                                                    return 4.0
                                                                else: 
                                                                    return 4.0
                                                            else: 
                                                                return 4.0
                                                        else: 
                                                            return 4.0
                                                    else: 
                                                        if alcohol<9.9:
                                                            return 5.0
                                                        else: 
                                                            return 5.0
                                                else: 
                                                    if alcohol<10:
                                                        if alcohol<9.6:
                                                            return 5.0
                                                        else: 
                                                            return 5.0
                                                    else: 
                                                        return 5.0
                                        else: 
                                            if chlorides<0.063:
                                                return 3.0
                                            else: 
                                                if chlorides<0.066:
                                                    if pH<3.32:
                                                        return 5.0
                                                    else: 
                                                        if alcohol<10.2:
                                                            return 6.0
                                                        else: 
                                                            return 6.0
                                                else: 
                                                    if pH<2.99:
                                                        return 6.0
                                                    else: 
                                                        if alcohol<9.5:
                                                            if density<0.9959:
                                                                return 4.0
                                                            else: 
                                                                if density<0.99623:
                                                                    return 6.0
                                                                else: 
                                                                    if residual_sugar<1.5:
                                                                        return 4.0
                                                                    else: 
                                                                        if free_sulfur_dioxide<12:
                                                                            if sulphates<0.55:
                                                                                if sulphates<0.53:
                                                                                    return 5.0
                                                                                else: 
                                                                                    return 4.0
                                                                            else: 
                                                                                if alcohol<9.4:
                                                                                    if alcohol<9.2:
                                                                                        return 5.0
                                                                                    else: 
                                                                                        return 5.0
                                                                                else: 
                                                                                    return 5.0
                                                                        else: 
                                                                            if alcohol<9.4:
                                                                                if alcohol<9.3:
                                                                                    if alcohol<9.2:
                                                                                        if alcohol<9.1:
                                                                                            return 5.0
                                                                                        else: 
                                                                                            return 5.0
                                                                                    else: 
                                                                                        return 5.0
                                                                                else: 
                                                                                    return 5.0
                                                                            else: 
                                                                                return 5.0
                                                        else: 
                                                            if free_sulfur_dioxide<17:
                                                                if volatile_acidity<1.04:
                                                                    if total_sulfur_dioxide<64:
                                                                        if pH<3.5:
                                                                            if total_sulfur_dioxide<20:
                                                                                if total_sulfur_dioxide<19:
                                                                                    if alcohol<10.4:
                                                                                        if alcohol<9.6:
                                                                                            if alcohol<9.55:
                                                                                                return 5.0
                                                                                            else: 
                                                                                                return 5.0
                                                                                        else: 
                                                                                            return 5.0
                                                                                    else: 
                                                                                        return 5.0
                                                                                else: 
                                                                                    if alcohol<10.5:
                                                                                        return 6.0
                                                                                    else: 
                                                                                        return 6.0
                                                                            else: 
                                                                                if density<0.9974:
                                                                                    if alcohol<10.3:
                                                                                        if alcohol<10.2:
                                                                                            if alcohol<10.1:
                                                                                                if alcohol<10:
                                                                                                    if alcohol<9.9:
                                                                                                        if alcohol<9.8:
                                                                                                            if alcohol<9.7:
                                                                                                                if alcohol<9.6:
                                                                                                                    return 5.0
                                                                                                                else: 
                                                                                                                    return 5.0
                                                                                                            else: 
                                                                                                                return 5.0
                                                                                                        else: 
                                                                                                            return 5.0
                                                                                                    else: 
                                                                                                        return 5.0
                                                                                                else: 
                                                                                                    return 5.0
                                                                                            else: 
                                                                                                return 5.0
                                                                                        else: 
                                                                                            return 5.0
                                                                                    else: 
                                                                                        return 5.0
                                                                                else: 
                                                                                    if density<0.9976:
                                                                                        return 6.0
                                                                                    else: 
                                                                                        if alcohol<10.5:
                                                                                            if alcohol<10.2:
                                                                                                if alcohol<9.6:
                                                                                                    return 5.0
                                                                                                else: 
                                                                                                    return 5.0
                                                                                            else: 
                                                                                                return 5.0
                                                                                        else: 
                                                                                            return 5.0
                                                                        else: 
                                                                            return 6.0
                                                                    else: 
                                                                        if total_sulfur_dioxide<86:
                                                                            if alcohol<10.1:
                                                                                if alcohol<9.8:
                                                                                    return 6.0
                                                                                else: 
                                                                                    return 6.0
                                                                            else: 
                                                                                return 5.0
                                                                        else: 
                                                                            if alcohol<10.1:
                                                                                if alcohol<9.8:
                                                                                    if alcohol<9.7:
                                                                                        return 5.0
                                                                                    else: 
                                                                                        return 5.0
                                                                                else: 
                                                                                    return 5.0
                                                                            else: 
                                                                                return 5.0
                                                                else: 
                                                                    return 6.0
                                                            else: 
                                                                if alcohol<10.3:
                                                                    if alcohol<10.1:
                                                                        if alcohol<10:
                                                                            if alcohol<9.9:
                                                                                if alcohol<9.8:
                                                                                    if alcohol<9.7:
                                                                                        return 5.0
                                                                                    else: 
                                                                                        return 5.0
                                                                                else: 
                                                                                    return 5.0
                                                                            else: 
                                                                                return 5.0
                                                                        else: 
                                                                            return 5.0
                                                                    else: 
                                                                        return 5.0
                                                                else: 
                                                                    return 5.0
                                else: 
                                    if sulphates<0.67:
                                        return 3.0
                                    else: 
                                        if alcohol<10.2:
                                            return 5.0
                                        else: 
                                            return 5.0
                            else: 
                                if alcohol<9.6:
                                    return 6.0
                                else: 
                                    return 6.0
                        else: 
                            if alcohol<10.2:
                                return 5.0
                            else: 
                                return 3.0
                else: 
                    if chlorides<0.087:
                        if alcohol<10.4:
                            if alcohol<10.1:
                                if alcohol<9.9:
                                    if alcohol<9.5:
                                        return 6.0
                                    else: 
                                        return 6.0
                                else: 
                                    return 6.0
                            else: 
                                return 6.0
                        else: 
                            return 6.0
                    else: 
                        if total_sulfur_dioxide<58:
                            if pH<3.35:
                                if alcohol<9.9:
                                    if alcohol<9.5:
                                        return 6.0
                                    else: 
                                        return 6.0
                                else: 
                                    return 6.0
                            else: 
                                if sulphates<0.86:
                                    if alcohol<10:
                                        if alcohol<9.8:
                                            return 5.0
                                        else: 
                                            return 5.0
                                    else: 
                                        return 5.0
                                else: 
                                    return 6.0
                        else: 
                            if alcohol<10.2:
                                if alcohol<9.9:
                                    if alcohol<9.8:
                                        if alcohol<9.6:
                                            if alcohol<9.3:
                                                return 5.0
                                            else: 
                                                return 5.0
                                        else: 
                                            return 5.0
                                    else: 
                                        return 5.0
                                else: 
                                    return 5.0
                            else: 
                                return 5.0
    else: 
        if sulphates<0.65:
            if volatile_acidity<0.6:
                if alcohol<11.7:
                    if pH<3.46:
                        if volatile_acidity<0.59:
                            if density<0.99517:
                                if citric_acid<0.42:
                                    if total_sulfur_dioxide<34:
                                        if alcohol<11.5:
                                            if alcohol<11.4:
                                                if alcohol<11.3:
                                                    return 7.0
                                                else: 
                                                    return 7.0
                                            else: 
                                                return 7.0
                                        else: 
                                            return 6.0
                                    else: 
                                        if density<0.9948:
                                            if alcohol<11.4:
                                                return 5.0
                                            else: 
                                                return 6.0
                                        else: 
                                            if alcohol<11.2:
                                                if alcohol<10.8:
                                                    return 6.0
                                                else: 
                                                    return 6.0
                                            else: 
                                                return 6.0
                                else: 
                                    if total_sulfur_dioxide<29:
                                        return 5.0
                                    else: 
                                        if alcohol<11.5:
                                            return 6.0
                                        else: 
                                            return 6.0
                            else: 
                                if fixed_acidity<7.4:
                                    if alcohol<10.9:
                                        if alcohol<10.8:
                                            return 5.0
                                        else: 
                                            return 5.0
                                    else: 
                                        return 4.0
                                else: 
                                    if residual_sugar<5.15:
                                        if chlorides<0.071:
                                            return 5.0
                                        else: 
                                            if sulphates<0.55:
                                                if alcohol<11:
                                                    return 6.0
                                                else: 
                                                    return 5.0
                                            else: 
                                                if alcohol<11.4:
                                                    if alcohol<11.3:
                                                        if alcohol<11.1:
                                                            if alcohol<10.9:
                                                                if alcohol<10.8:
                                                                    return 6.0
                                                                else: 
                                                                    return 6.0
                                                            else: 
                                                                return 6.0
                                                        else: 
                                                            return 6.0
                                                    else: 
                                                        return 6.0
                                                else: 
                                                    return 6.0
                                    else: 
                                        if alcohol<11.2:
                                            return 5.0
                                        else: 
                                            return 5.0
                        else: 
                            if alcohol<10.8:
                                return 6.0
                            else: 
                                if alcohol<11.5:
                                    return 7.0
                                else: 
                                    return 7.0
                    else: 
                        if pH<3.62:
                            if pH<3.56:
                                if alcohol<11.4:
                                    if alcohol<11.3:
                                        if alcohol<11.2:
                                            if alcohol<11:
                                                if alcohol<10.7:
                                                    return 5.0
                                                else: 
                                                    return 5.0
                                            else: 
                                                return 5.0
                                        else: 
                                            return 5.0
                                    else: 
                                        return 5.0
                                else: 
                                    return 5.0
                            else: 
                                if pH<3.61:
                                    if alcohol<11.6:
                                        if alcohol<11.5:
                                            return 6.0
                                        else: 
                                            return 6.0
                                    else: 
                                        return 6.0
                                else: 
                                    return 5.0
                        else: 
                            return 4.0
                else: 
                    if residual_sugar<3.8:
                        if total_sulfur_dioxide<17:
                            if sulphates<0.55:
                                if alcohol<12.2:
                                    return 6.0
                                else: 
                                    return 6.0
                            else: 
                                if alcohol<12.8:
                                    if alcohol<12.4:
                                        return 7.0
                                    else: 
                                        return 7.0
                                else: 
                                    return 7.0
                        else: 
                            if volatile_acidity<0.58:
                                if sulphates<0.44:
                                    return 7.0
                                else: 
                                    if volatile_acidity<0.56:
                                        if alcohol<13:
                                            if fixed_acidity<6:
                                                if alcohol<12.8:
                                                    return 7.0
                                                else: 
                                                    return 6.0
                                            else: 
                                                if alcohol<12.8:
                                                    if alcohol<12.7:
                                                        if alcohol<12.5:
                                                            if alcohol<12.4:
                                                                if alcohol<12.2:
                                                                    if alcohol<12.1:
                                                                        if alcohol<12:
                                                                            if alcohol<11.9:
                                                                                if alcohol<11.8:
                                                                                    return 6.0
                                                                                else: 
                                                                                    return 6.0
                                                                            else: 
                                                                                return 6.0
                                                                        else: 
                                                                            return 6.0
                                                                    else: 
                                                                        return 6.0
                                                                else: 
                                                                    return 6.0
                                                            else: 
                                                                return 6.0
                                                        else: 
                                                            return 6.0
                                                    else: 
                                                        return 6.0
                                                else: 
                                                    return 6.0
                                        else: 
                                            if alcohol<13.3:
                                                return 5.0
                                            else: 
                                                return 6.0
                                    else: 
                                        return 7.0
                            else: 
                                return 5.0
                    else: 
                        if chlorides<0.118:
                            if alcohol<12.5:
                                if alcohol<12.3:
                                    if alcohol<12.2:
                                        if alcohol<12.1:
                                            return 7.0
                                        else: 
                                            return 7.0
                                    else: 
                                        return 7.0
                                else: 
                                    return 7.0
                            else: 
                                if alcohol<13:
                                    return 6.0
                                else: 
                                    return 7.0
                        else: 
                            if alcohol<13.2:
                                return 6.0
                            else: 
                                return 6.0
            else: 
                if volatile_acidity<1.04:
                    if residual_sugar<2.5:
                        if citric_acid<0.06:
                            if chlorides<0.1:
                                if total_sulfur_dioxide<13:
                                    return 7.0
                                else: 
                                    if total_sulfur_dioxide<52:
                                        if alcohol<12.8:
                                            if alcohol<12.5:
                                                if alcohol<12.2:
                                                    if alcohol<11.9:
                                                        if alcohol<11.8:
                                                            if alcohol<11.5:
                                                                if alcohol<11.2:
                                                                    if alcohol<11:
                                                                        if alcohol<10.9:
                                                                            if alcohol<10.8:
                                                                                if alcohol<10.75:
                                                                                    return 6.0
                                                                                else: 
                                                                                    return 6.0
                                                                            else: 
                                                                                return 6.0
                                                                        else: 
                                                                            return 6.0
                                                                    else: 
                                                                        return 6.0
                                                                else: 
                                                                    return 6.0
                                                            else: 
                                                                return 6.0
                                                        else: 
                                                            return 6.0
                                                    else: 
                                                        return 6.0
                                                else: 
                                                    return 6.0
                                            else: 
                                                return 6.0
                                        else: 
                                            return 6.0
                                    else: 
                                        return 5.0
                            else: 
                                if alcohol<11:
                                    return 5.0
                                else: 
                                    return 5.0
                        else: 
                            if alcohol<11.4:
                                if alcohol<10.7:
                                    return 6.0
                                else: 
                                    if sulphates<0.64:
                                        if alcohol<11:
                                            if alcohol<10.9:
                                                return 5.0
                                            else: 
                                                return 5.0
                                        else: 
                                            return 5.0
                                    else: 
                                        return 4.0
                            else: 
                                if residual_sugar<1.7:
                                    if alcohol<12.1:
                                        return 5.0
                                    else: 
                                        return 5.0
                                else: 
                                    if alcohol<12.9:
                                        if alcohol<11.8:
                                            if alcohol<11.6:
                                                if alcohol<11.5:
                                                    return 6.0
                                                else: 
                                                    return 6.0
                                            else: 
                                                return 6.0
                                        else: 
                                            return 6.0
                                    else: 
                                        return 6.0
                    else: 
                        if free_sulfur_dioxide<15:
                            if free_sulfur_dioxide<11:
                                if free_sulfur_dioxide<9:
                                    if total_sulfur_dioxide<11:
                                        if alcohol<13:
                                            return 4.0
                                        else: 
                                            return 5.0
                                    else: 
                                        if alcohol<12.9:
                                            if alcohol<12.6:
                                                if alcohol<12.2:
                                                    if alcohol<11.5:
                                                        if alcohol<11.4:
                                                            if alcohol<11.3:
                                                                if alcohol<10.9:
                                                                    if alcohol<10.8:
                                                                        return 5.0
                                                                    else: 
                                                                        return 5.0
                                                                else: 
                                                                    return 5.0
                                                            else: 
                                                                return 5.0
                                                        else: 
                                                            return 5.0
                                                    else: 
                                                        return 5.0
                                                else: 
                                                    return 5.0
                                            else: 
                                                return 5.0
                                        else: 
                                            return 5.0
                                else: 
                                    return 6.0
                            else: 
                                if alcohol<11.8:
                                    return 4.0
                                else: 
                                    return 4.0
                        else: 
                            if sulphates<0.62:
                                if alcohol<12.7:
                                    if alcohol<11.3:
                                        return 6.0
                                    else: 
                                        return 6.0
                                else: 
                                    return 6.0
                            else: 
                                if alcohol<12:
                                    return 5.0
                                else: 
                                    return 5.0
                else: 
                    if residual_sugar<2.1:
                        if alcohol<11.5:
                            return 5.0
                        else: 
                            return 5.0
                    else: 
                        if alcohol<11:
                            return 3.0
                        else: 
                            if alcohol<11.4:
                                if alcohol<11.2:
                                    return 4.0
                                else: 
                                    return 4.0
                            else: 
                                return 4.0
        else: 
            if alcohol<11.6:
                if total_sulfur_dioxide<50:
                    if volatile_acidity<0.4:
                        if pH<3.26:
                            if volatile_acidity<0.35:
                                if fixed_acidity<10.1:
                                    if density<0.99534:
                                        return 7.0
                                    else: 
                                        if alcohol<11.4:
                                            if alcohol<11.2:
                                                return 6.0
                                            else: 
                                                return 6.0
                                        else: 
                                            return 6.0
                                else: 
                                    if alcohol<11.4:
                                        if alcohol<11.2:
                                            if alcohol<11:
                                                if alcohol<10.9:
                                                    return 7.0
                                                else: 
                                                    return 7.0
                                            else: 
                                                return 7.0
                                        else: 
                                            return 7.0
                                    else: 
                                        return 7.0
                            else: 
                                if chlorides<0.085:
                                    if sulphates<0.73:
                                        if alcohol<11.4:
                                            return 8.0
                                        else: 
                                            return 8.0
                                    else: 
                                        if citric_acid<0.32:
                                            return 8.0
                                        else: 
                                            if alcohol<11.3:
                                                return 7.0
                                            else: 
                                                return 7.0
                                else: 
                                    if alcohol<11.1:
                                        return 7.0
                                    else: 
                                        return 7.0
                        else: 
                            if pH<3.4:
                                if alcohol<10.8:
                                    if total_sulfur_dioxide<25:
                                        return 5.0
                                    else: 
                                        return 6.0
                                else: 
                                    if volatile_acidity<0.26:
                                        return 5.0
                                    else: 
                                        if total_sulfur_dioxide<29:
                                            if sulphates<0.8:
                                                if alcohol<11.2:
                                                    return 7.0
                                                else: 
                                                    return 7.0
                                            else: 
                                                if alcohol<11.2:
                                                    return 6.0
                                                else: 
                                                    return 6.0
                                        else: 
                                            if residual_sugar<8.9:
                                                if alcohol<11.5:
                                                    if alcohol<11.1:
                                                        if alcohol<11:
                                                            return 6.0
                                                        else: 
                                                            return 6.0
                                                    else: 
                                                        return 6.0
                                                else: 
                                                    return 6.0
                                            else: 
                                                return 7.0
                            else: 
                                if alcohol<11.3:
                                    if alcohol<11:
                                        return 7.0
                                    else: 
                                        return 7.0
                                else: 
                                    return 7.0
                    else: 
                        if pH<3.34:
                            if chlorides<0.095:
                                if density<0.99518:
                                    if alcohol<11.4:
                                        return 5.0
                                    else: 
                                        return 6.0
                                else: 
                                    if density<0.996:
                                        if sulphates<0.85:
                                            return 7.0
                                        else: 
                                            return 6.0
                                    else: 
                                        if alcohol<11.4:
                                            if alcohol<11.3:
                                                if alcohol<11.2:
                                                    if alcohol<11:
                                                        if alcohol<10.9:
                                                            if alcohol<10.8:
                                                                return 6.0
                                                            else: 
                                                                return 6.0
                                                        else: 
                                                            return 6.0
                                                    else: 
                                                        return 6.0
                                                else: 
                                                    return 6.0
                                            else: 
                                                return 6.0
                                        else: 
                                            return 6.0
                            else: 
                                if sulphates<0.71:
                                    return 7.0
                                else: 
                                    if alcohol<11.5:
                                        if alcohol<11.2:
                                            if alcohol<11.1:
                                                return 5.0
                                            else: 
                                                return 5.0
                                        else: 
                                            return 5.0
                                    else: 
                                        return 5.0
                        else: 
                            if density<0.99736:
                                if chlorides<0.066:
                                    if alcohol<11.5:
                                        return 7.0
                                    else: 
                                        return 7.0
                                else: 
                                    if chlorides<0.089:
                                        if alcohol<11.5:
                                            if alcohol<11.4:
                                                if alcohol<11.3:
                                                    if alcohol<11.2:
                                                        if alcohol<11.1:
                                                            if alcohol<11:
                                                                if alcohol<10.9:
                                                                    if alcohol<10.8:
                                                                        if alcohol<10.7:
                                                                            return 6.0
                                                                        else: 
                                                                            return 6.0
                                                                    else: 
                                                                        return 6.0
                                                                else: 
                                                                    return 6.0
                                                            else: 
                                                                return 6.0
                                                        else: 
                                                            return 6.0
                                                    else: 
                                                        return 6.0
                                                else: 
                                                    return 6.0
                                            else: 
                                                return 6.0
                                        else: 
                                            return 6.0
                                    else: 
                                        if sulphates<0.68:
                                            return 6.0
                                        else: 
                                            if alcohol<11.3:
                                                return 7.0
                                            else: 
                                                return 7.0
                            else: 
                                if alcohol<10.8:
                                    return 7.0
                                else: 
                                    return 7.0
                else: 
                    if residual_sugar<3.2:
                        if free_sulfur_dioxide<53:
                            if total_sulfur_dioxide<65:
                                if residual_sugar<2.3:
                                    if pH<3.2:
                                        if alcohol<11.5:
                                            return 7.0
                                        else: 
                                            return 6.0
                                    else: 
                                        if alcohol<11.5:
                                            if alcohol<11.4:
                                                if alcohol<11.2:
                                                    if alcohol<10.9:
                                                        return 6.0
                                                    else: 
                                                        return 6.0
                                                else: 
                                                    return 6.0
                                            else: 
                                                return 6.0
                                        else: 
                                            return 6.0
                                else: 
                                    if total_sulfur_dioxide<55:
                                        if alcohol<11.4:
                                            if alcohol<11:
                                                return 6.0
                                            else: 
                                                return 6.0
                                        else: 
                                            return 6.0
                                    else: 
                                        if total_sulfur_dioxide<60:
                                            if alcohol<11:
                                                if alcohol<10.9:
                                                    return 5.0
                                                else: 
                                                    return 5.0
                                            else: 
                                                return 5.0
                                        else: 
                                            if alcohol<11.4:
                                                return 6.0
                                            else: 
                                                return 6.0
                            else: 
                                if pH<3.33:
                                    if alcohol<10.9:
                                        return 5.0
                                    else: 
                                        if alcohol<11.1:
                                            if alcohol<11:
                                                return 6.0
                                            else: 
                                                return 6.0
                                        else: 
                                            return 6.0
                                else: 
                                    if alcohol<11.4:
                                        if alcohol<11.3:
                                            if alcohol<11.2:
                                                if alcohol<11:
                                                    return 5.0
                                                else: 
                                                    return 5.0
                                            else: 
                                                return 5.0
                                        else: 
                                            return 5.0
                                    else: 
                                        if sulphates<0.77:
                                            return 5.0
                                        else: 
                                            return 6.0
                        else: 
                            return 7.0
                    else: 
                        if sulphates<0.71:
                            if alcohol<11.3:
                                if alcohol<11:
                                    return 6.0
                                else: 
                                    return 6.0
                            else: 
                                return 6.0
                        else: 
                            if alcohol<11.5:
                                return 7.0
                            else: 
                                return 7.0
            else: 
                if fixed_acidity<13:
                    if density<0.99264:
                        if citric_acid<0.03:
                            return 6.0
                        else: 
                            if sulphates<0.85:
                                if alcohol<14:
                                    if alcohol<13.1:
                                        return 8.0
                                    else: 
                                        return 8.0
                                else: 
                                    return 8.0
                            else: 
                                if alcohol<13:
                                    return 7.0
                                else: 
                                    return 7.0
                    else: 
                        if total_sulfur_dioxide<20:
                            if density<0.9976:
                                if residual_sugar<1.9:
                                    if sulphates<0.74:
                                        if alcohol<12.5:
                                            return 8.0
                                        else: 
                                            return 8.0
                                    else: 
                                        if alcohol<11.9:
                                            return 7.0
                                        else: 
                                            return 7.0
                                else: 
                                    if volatile_acidity<0.42:
                                        if total_sulfur_dioxide<9:
                                            return 6.0
                                        else: 
                                            if alcohol<12.8:
                                                if alcohol<12.5:
                                                    if alcohol<12.1:
                                                        if alcohol<12:
                                                            if alcohol<11.8:
                                                                return 7.0
                                                            else: 
                                                                return 7.0
                                                        else: 
                                                            return 7.0
                                                    else: 
                                                        return 7.0
                                                else: 
                                                    return 7.0
                                            else: 
                                                return 7.0
                                    else: 
                                        if sulphates<0.7:
                                            if alcohol<12.7:
                                                return 7.0
                                            else: 
                                                return 7.0
                                        else: 
                                            if alcohol<14:
                                                if alcohol<12.5:
                                                    if alcohol<12.3:
                                                        return 6.0
                                                    else: 
                                                        return 6.0
                                                else: 
                                                    return 6.0
                                            else: 
                                                return 6.0
                            else: 
                                if alcohol<12.6:
                                    return 7.0
                                else: 
                                    if alcohol<13.4:
                                        return 8.0
                                    else: 
                                        return 8.0
                        else: 
                            if sulphates<0.74:
                                if density<1.0014:
                                    if pH<3.4:
                                        if alcohol<13.4:
                                            if alcohol<12.8:
                                                if alcohol<12.5:
                                                    if alcohol<12.4:
                                                        if alcohol<11.9:
                                                            if alcohol<11.8:
                                                                return 6.0
                                                            else: 
                                                                return 6.0
                                                        else: 
                                                            return 6.0
                                                    else: 
                                                        return 6.0
                                                else: 
                                                    return 6.0
                                            else: 
                                                return 6.0
                                        else: 
                                            return 6.0
                                    else: 
                                        if alcohol<12.1:
                                            return 5.0
                                        else: 
                                            return 6.0
                                else: 
                                    return 7.0
                            else: 
                                if fixed_acidity<8.7:
                                    if pH<3.52:
                                        if sulphates<0.78:
                                            if alcohol<12.1:
                                                return 7.0
                                            else: 
                                                return 7.0
                                        else: 
                                            if sulphates<1.01:
                                                if alcohol<12.8:
                                                    if alcohol<12.4:
                                                        if alcohol<12.1:
                                                            if alcohol<12:
                                                                if alcohol<11.9:
                                                                    if alcohol<11.8:
                                                                        return 6.0
                                                                    else: 
                                                                        return 6.0
                                                                else: 
                                                                    return 6.0
                                                            else: 
                                                                return 6.0
                                                        else: 
                                                            return 6.0
                                                    else: 
                                                        return 6.0
                                                else: 
                                                    return 6.0
                                            else: 
                                                return 7.0
                                    else: 
                                        if alcohol<12.9:
                                            if alcohol<12.5:
                                                if alcohol<12.4:
                                                    return 7.0
                                                else: 
                                                    return 7.0
                                            else: 
                                                return 7.0
                                        else: 
                                            return 7.0
                                else: 
                                    if free_sulfur_dioxide<10:
                                        if alcohol<12.1:
                                            if alcohol<12:
                                                return 6.0
                                            else: 
                                                return 6.0
                                        else: 
                                            return 7.0
                                    else: 
                                        if alcohol<13.4:
                                            if alcohol<13.3:
                                                if alcohol<12.6:
                                                    if alcohol<12.5:
                                                        if alcohol<12.1:
                                                            if alcohol<12:
                                                                if alcohol<11.9:
                                                                    if alcohol<11.7:
                                                                        return 7.0
                                                                    else: 
                                                                        return 7.0
                                                                else: 
                                                                    return 7.0
                                                            else: 
                                                                return 7.0
                                                        else: 
                                                            return 7.0
                                                    else: 
                                                        return 7.0
                                                else: 
                                                    return 7.0
                                            else: 
                                                return 7.0
                                        else: 
                                            return 7.0
                else: 
                    if alcohol<13:
                        return 6.0
                    else: 
                        if alcohol<14.9:
                            return 5.0
                        else: 
                            return 5.0
