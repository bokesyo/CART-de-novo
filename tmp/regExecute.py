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
                if fixed_acidity<12:
                    if sulphates<0.51:
                        if alcohol<10.1:
                            if alcohol<9.5:
                                return 5.0
                            else: 
                                return 5.0
                        else: 
                            return 5.0
                    else: 
                        if citric_acid<0.52:
                            if density<0.99556:
                                return 7.0
                            else: 
                                if citric_acid<0.25:
                                    if citric_acid<0.23:
                                        if alcohol<10.1:
                                            return 6.0
                                        else: 
                                            return 6.0
                                    else: 
                                        if alcohol<10.1:
                                            return 5.0
                                        else: 
                                            return 5.0
                                else: 
                                    if total_sulfur_dioxide<67:
                                        if volatile_acidity<0.28:
                                            if sulphates<0.8:
                                                if alcohol<9.7:
                                                    return 5.0
                                                else: 
                                                    return 5.0
                                            else: 
                                                if alcohol<10.4:
                                                    if alcohol<10.1:
                                                        if alcohol<10:
                                                            if alcohol<9.4:
                                                                if alcohol<9.3:
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
                                            if alcohol<10.4:
                                                if alcohol<10.3:
                                                    if alcohol<10.1:
                                                        if alcohol<9.8:
                                                            if alcohol<9.5:
                                                                if alcohol<9.4:
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
                                        if sulphates<0.9:
                                            return 7.0
                                        else: 
                                            return 6.0
                        else: 
                            if total_sulfur_dioxide<15:
                                return 6.0
                            else: 
                                if alcohol<10.4:
                                    if alcohol<9.6:
                                        return 5.0
                                    else: 
                                        return 5.0
                                else: 
                                    return 5.0
                else: 
                    if alcohol<9.2:
                        return 6.0
                    else: 
                        if alcohol<9.9:
                            return 7.0
                        else: 
                            return 7.0
            else: 
                if sulphates<1.18:
                    return 8.0
                else: 
                    if pH<3.12:
                        return 7.0
                    else: 
                        if alcohol<10.3:
                            return 6.0
                        else: 
                            return 6.0
        else: 
            if volatile_acidity<0.655:
                if alcohol<9.9:
                    if free_sulfur_dioxide<10:
                        if sulphates<0.54:
                            if pH<3.37:
                                if alcohol<9.8:
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
                                return 6.0
                        else: 
                            if pH<3.12:
                                if alcohol<9.5:
                                    if alcohol<9.4:
                                        return 5.0
                                    else: 
                                        return 5.0
                                else: 
                                    return 5.0
                            else: 
                                if residual_sugar<1.7:
                                    if alcohol<9.8:
                                        return 6.0
                                    else: 
                                        return 6.0
                                else: 
                                    if fixed_acidity<7.8:
                                        if alcohol<9.5:
                                            if density<0.9972:
                                                if pH<3.4:
                                                    return 5.0
                                                else: 
                                                    if alcohol<9.4:
                                                        return 6.0
                                                    else: 
                                                        return 6.0
                                            else: 
                                                if alcohol<9.3:
                                                    return 5.0
                                                else: 
                                                    return 5.0
                                        else: 
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
                                        if pH<3.36:
                                            if free_sulfur_dioxide<8:
                                                if sulphates<1.05:
                                                    if citric_acid<0.12:
                                                        return 5.0
                                                    else: 
                                                        if alcohol<9.8:
                                                            if alcohol<9.5:
                                                                if alcohol<9.4:
                                                                    if alcohol<9.3:
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
                                                if alcohol<9.7:
                                                    if alcohol<9.6:
                                                        return 5.0
                                                    else: 
                                                        return 5.0
                                                else: 
                                                    return 5.0
                                        else: 
                                            return 7.0
                    else: 
                        if pH<3.43:
                            if density<1.001:
                                if density<1.0008:
                                    if chlorides<0.067:
                                        if pH<3.33:
                                            if alcohol<9.6:
                                                return 6.0
                                            else: 
                                                return 6.0
                                        else: 
                                            if alcohol<9.7:
                                                return 5.0
                                            else: 
                                                return 5.0
                                    else: 
                                        if density<0.99717:
                                            if sulphates<1.61:
                                                if total_sulfur_dioxide<37:
                                                    return 6.0
                                                else: 
                                                    if alcohol<9.6:
                                                        if density<0.99686:
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
                                                            if density<0.9969:
                                                                return 6.0
                                                            else: 
                                                                if alcohol<9.5:
                                                                    if alcohol<9.4:
                                                                        if alcohol<9.2:
                                                                            return 5.0
                                                                        else: 
                                                                            return 5.0
                                                                    else: 
                                                                        return 5.0
                                                                else: 
                                                                    return 5.0
                                                    else: 
                                                        if total_sulfur_dioxide<98:
                                                            if residual_sugar<2:
                                                                if alcohol<9.8:
                                                                    if alcohol<9.7:
                                                                        return 5.0
                                                                    else: 
                                                                        return 5.0
                                                                else: 
                                                                    return 5.0
                                                            else: 
                                                                if alcohol<9.8:
                                                                    return 6.0
                                                                else: 
                                                                    return 6.0
                                                        else: 
                                                            if alcohol<9.8:
                                                                return 5.0
                                                            else: 
                                                                return 5.0
                                            else: 
                                                return 6.0
                                        else: 
                                            if residual_sugar<1.6:
                                                return 4.0
                                            else: 
                                                if chlorides<0.073:
                                                    if alcohol<9.6:
                                                        return 5.0
                                                    else: 
                                                        return 4.0
                                                else: 
                                                    if volatile_acidity<0.38:
                                                        if pH<3.34:
                                                            if alcohol<9.8:
                                                                return 5.0
                                                            else: 
                                                                return 5.0
                                                        else: 
                                                            return 6.0
                                                    else: 
                                                        if alcohol<9.8:
                                                            if alcohol<9.7:
                                                                if alcohol<9.6:
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
                                                                        return 5.0
                                                                else: 
                                                                    return 5.0
                                                            else: 
                                                                return 5.0
                                                        else: 
                                                            return 5.0
                                else: 
                                    return 3.0
                            else: 
                                if alcohol<9.8:
                                    return 6.0
                                else: 
                                    return 6.0
                        else: 
                            if total_sulfur_dioxide<88:
                                if density<0.99689:
                                    return 6.0
                                else: 
                                    if density<0.9984:
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
                                        if alcohol<9.5:
                                            if alcohol<9.4:
                                                if alcohol<9.3:
                                                    return 6.0
                                                else: 
                                                    return 6.0
                                            else: 
                                                return 6.0
                                        else: 
                                            if alcohol<9.7:
                                                return 5.0
                                            else: 
                                                return 5.0
                            else: 
                                if alcohol<9.8:
                                    return 6.0
                                else: 
                                    return 6.0
                else: 
                    if sulphates<0.69:
                        if pH<3.46:
                            if density<0.995:
                                return 7.0
                            else: 
                                if total_sulfur_dioxide<92:
                                    if citric_acid<0.39:
                                        if total_sulfur_dioxide<35:
                                            if alcohol<10.4:
                                                if alcohol<10.3:
                                                    if alcohol<10.2:
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
                                            if total_sulfur_dioxide<58:
                                                if density<0.99575:
                                                    if alcohol<10.4:
                                                        return 6.0
                                                    else: 
                                                        return 6.0
                                                else: 
                                                    if fixed_acidity<8:
                                                        if alcohol<10.3:
                                                            if alcohol<10.1:
                                                                return 5.0
                                                            else: 
                                                                return 5.0
                                                        else: 
                                                            return 5.0
                                                    else: 
                                                        if pH<3.37:
                                                            if pH<3.24:
                                                                return 6.0
                                                            else: 
                                                                if alcohol<10.3:
                                                                    if alcohol<10:
                                                                        return 5.0
                                                                    else: 
                                                                        return 5.0
                                                                else: 
                                                                    return 5.0
                                                        else: 
                                                            if alcohol<10:
                                                                return 6.0
                                                            else: 
                                                                return 6.0
                                            else: 
                                                if alcohol<10.4:
                                                    if alcohol<10.2:
                                                        if alcohol<10.1:
                                                            return 6.0
                                                        else: 
                                                            return 6.0
                                                    else: 
                                                        return 6.0
                                                else: 
                                                    return 6.0
                                    else: 
                                        if alcohol<10.2:
                                            if alcohol<10:
                                                return 5.0
                                            else: 
                                                return 6.0
                                        else: 
                                            if alcohol<10.4:
                                                if alcohol<10.3:
                                                    return 5.0
                                                else: 
                                                    return 5.0
                                            else: 
                                                return 5.0
                                else: 
                                    if alcohol<10.1:
                                        return 5.0
                                    else: 
                                        return 5.0
                        else: 
                            if sulphates<0.62:
                                if alcohol<10.4:
                                    if alcohol<10.2:
                                        if alcohol<10:
                                            return 5.0
                                        else: 
                                            return 5.0
                                    else: 
                                        return 5.0
                                else: 
                                    return 5.0
                            else: 
                                return 4.0
                    else: 
                        if free_sulfur_dioxide<32:
                            if alcohol<10.2:
                                if sulphates<0.78:
                                    if pH<3.47:
                                        if alcohol<10.1:
                                            if alcohol<10:
                                                return 7.0
                                            else: 
                                                return 7.0
                                        else: 
                                            return 7.0
                                    else: 
                                        return 6.0
                                else: 
                                    if alcohol<10:
                                        return 6.0
                                    else: 
                                        return 6.0
                            else: 
                                if free_sulfur_dioxide<10:
                                    return 5.0
                                else: 
                                    if alcohol<10.3:
                                        return 6.0
                                    else: 
                                        return 6.0
                        else: 
                            if sulphates<0.86:
                                if alcohol<10.2:
                                    return 5.0
                                else: 
                                    return 5.0
                            else: 
                                return 4.0
            else: 
                if density<0.9983:
                    if citric_acid<0.07:
                        if residual_sugar<5.7:
                            if volatile_acidity<1.04:
                                if volatile_acidity<0.975:
                                    if fixed_acidity<6.8:
                                        if alcohol<10.3:
                                            return 3.0
                                        else: 
                                            return 5.0
                                    else: 
                                        if sulphates<1.08:
                                            if density<0.9978:
                                                if alcohol<10.2:
                                                    if alcohol<10.1:
                                                        if alcohol<9.9:
                                                            if alcohol<9.8:
                                                                if alcohol<9.7:
                                                                    if alcohol<9.6:
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
                                                                return 5.0
                                                        else: 
                                                            return 5.0
                                                    else: 
                                                        return 5.0
                                                else: 
                                                    return 5.0
                                            else: 
                                                if sulphates<0.52:
                                                    return 4.0
                                                else: 
                                                    if alcohol<10:
                                                        return 5.0
                                                    else: 
                                                        return 5.0
                                        else: 
                                            return 4.0
                                else: 
                                    if alcohol<9.7:
                                        return 4.0
                                    else: 
                                        return 3.0
                            else: 
                                return 6.0
                        else: 
                            return 3.0
                    else: 
                        if citric_acid<0.1:
                            if density<0.9959:
                                if alcohol<10.1:
                                    if alcohol<10:
                                        return 5.0
                                    else: 
                                        return 5.0
                                else: 
                                    return 5.0
                            else: 
                                if pH<3.44:
                                    if alcohol<10.2:
                                        if alcohol<9.8:
                                            if alcohol<9.2:
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
                            if sulphates<1.36:
                                if fixed_acidity<8.1:
                                    if free_sulfur_dioxide<20:
                                        if free_sulfur_dioxide<13:
                                            if alcohol<10.1:
                                                if alcohol<9.7:
                                                    return 5.0
                                                else: 
                                                    return 5.0
                                            else: 
                                                return 5.0
                                        else: 
                                            if alcohol<9.5:
                                                return 5.0
                                            else: 
                                                if alcohol<9.8:
                                                    if alcohol<9.6:
                                                        return 6.0
                                                    else: 
                                                        return 6.0
                                                else: 
                                                    return 6.0
                                    else: 
                                        if alcohol<9.9:
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
                                    if volatile_acidity<0.915:
                                        if alcohol<9.3:
                                            if density<0.9976:
                                                if alcohol<9.2:
                                                    if alcohol<9.1:
                                                        return 5.0
                                                    else: 
                                                        return 5.0
                                                else: 
                                                    return 5.0
                                            else: 
                                                return 4.0
                                        else: 
                                            if alcohol<10.3:
                                                if alcohol<10.2:
                                                    if alcohol<10.1:
                                                        if alcohol<10:
                                                            if alcohol<9.9:
                                                                if alcohol<9.8:
                                                                    if alcohol<9.6:
                                                                        if alcohol<9.55:
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
                                        return 4.0
                            else: 
                                return 6.0
                else: 
                    if total_sulfur_dioxide<92:
                        if sulphates<0.55:
                            return 5.0
                        else: 
                            if alcohol<10:
                                if alcohol<9.9:
                                    if alcohol<9.5:
                                        if alcohol<9.4:
                                            if alcohol<9.25:
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
                                if alcohol<10.1:
                                    return 5.0
                                else: 
                                    return 6.0
                    else: 
                        if alcohol<9.9:
                            if alcohol<9.8:
                                if alcohol<9.3:
                                    return 5.0
                                else: 
                                    return 5.0
                            else: 
                                return 5.0
                        else: 
                            return 5.0
    else: 
        if volatile_acidity<0.875:
            if alcohol<11.5:
                if volatile_acidity<0.32:
                    if volatile_acidity<0.24:
                        if pH<3.34:
                            if alcohol<11.3:
                                return 5.0
                            else: 
                                return 5.0
                        else: 
                            return 6.0
                    else: 
                        if chlorides<0.062:
                            if alcohol<11.3:
                                if alcohol<11.2:
                                    if alcohol<10.9:
                                        if alcohol<10.6:
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
                            if total_sulfur_dioxide<33:
                                if alcohol<11.3:
                                    if alcohol<11.2:
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
                                if sulphates<0.85:
                                    if alcohol<11.4:
                                        if alcohol<11.3:
                                            return 7.0
                                        else: 
                                            return 7.0
                                    else: 
                                        return 7.0
                                else: 
                                    if alcohol<11.4:
                                        return 6.0
                                    else: 
                                        return 6.0
                else: 
                    if total_sulfur_dioxide<72:
                        if sulphates<0.58:
                            if alcohol<10.6:
                                if total_sulfur_dioxide<31:
                                    return 7.0
                                else: 
                                    return 6.0
                            else: 
                                if residual_sugar<3.6:
                                    if volatile_acidity<0.63:
                                        if chlorides<0.106:
                                            if alcohol<11.4:
                                                if alcohol<11.2:
                                                    if alcohol<11:
                                                        if alcohol<10.9:
                                                            if alcohol<10.8:
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
                                                return 5.0
                                        else: 
                                            return 6.0
                                    else: 
                                        if total_sulfur_dioxide<32:
                                            if alcohol<11.3:
                                                return 5.0
                                            else: 
                                                return 5.0
                                        else: 
                                            if alcohol<11.4:
                                                if alcohol<10.8:
                                                    return 6.0
                                                else: 
                                                    return 6.0
                                            else: 
                                                return 6.0
                                else: 
                                    if alcohol<11.3:
                                        if alcohol<10.9:
                                            return 6.0
                                        else: 
                                            return 5.0
                                    else: 
                                        return 7.0
                        else: 
                            if alcohol<10.8:
                                if volatile_acidity<0.36:
                                    if alcohol<10.7:
                                        return 5.0
                                    else: 
                                        return 5.0
                                else: 
                                    if pH<3.44:
                                        if chlorides<0.091:
                                            if volatile_acidity<0.75:
                                                if alcohol<10.7:
                                                    if alcohol<10.6:
                                                        return 6.0
                                                    else: 
                                                        return 6.0
                                                else: 
                                                    return 6.0
                                            else: 
                                                if alcohol<10.7:
                                                    return 5.0
                                                else: 
                                                    return 6.0
                                        else: 
                                            return 7.0
                                    else: 
                                        if alcohol<10.7:
                                            return 5.0
                                        else: 
                                            return 5.0
                            else: 
                                if volatile_acidity<0.37:
                                    if density<0.9972:
                                        if density<0.99534:
                                            if alcohol<11.1:
                                                return 7.0
                                            else: 
                                                return 7.0
                                        else: 
                                            if fixed_acidity<8.2:
                                                return 7.0
                                            else: 
                                                if pH<3.15:
                                                    return 7.0
                                                else: 
                                                    if alcohol<11.4:
                                                        if alcohol<11.3:
                                                            if alcohol<11:
                                                                return 6.0
                                                            else: 
                                                                return 6.0
                                                        else: 
                                                            return 6.0
                                                    else: 
                                                        return 6.0
                                    else: 
                                        return 8.0
                                else: 
                                    if residual_sugar<5.5:
                                        if chlorides<0.058:
                                            if alcohol<11.4:
                                                if alcohol<11.3:
                                                    return 5.0
                                                else: 
                                                    return 5.0
                                            else: 
                                                return 6.0
                                        else: 
                                            if residual_sugar<2.5:
                                                if chlorides<0.12:
                                                    if alcohol<10.9:
                                                        if sulphates<0.69:
                                                            return 6.0
                                                        else: 
                                                            return 7.0
                                                    else: 
                                                        if total_sulfur_dioxide<22:
                                                            if alcohol<11.2:
                                                                if alcohol<11:
                                                                    return 6.0
                                                                else: 
                                                                    if alcohol<11.1:
                                                                        return 7.0
                                                                    else: 
                                                                        return 7.0
                                                            else: 
                                                                if alcohol<11.4:
                                                                    if alcohol<11.3:
                                                                        return 6.0
                                                                    else: 
                                                                        return 6.0
                                                                else: 
                                                                    return 6.0
                                                        else: 
                                                            if alcohol<11.4:
                                                                if alcohol<11.3:
                                                                    if alcohol<11.2:
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
                                                                    return 6.0
                                                            else: 
                                                                return 6.0
                                                else: 
                                                    return 7.0
                                            else: 
                                                if sulphates<0.71:
                                                    if free_sulfur_dioxide<28:
                                                        if alcohol<11.3:
                                                            if alcohol<11.2:
                                                                if alcohol<11:
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
                                                        if alcohol<11.3:
                                                            return 5.0
                                                        else: 
                                                            return 6.0
                                                else: 
                                                    if sulphates<0.81:
                                                        if alcohol<11.1:
                                                            return 5.0
                                                        else: 
                                                            return 5.0
                                                    else: 
                                                        if density<1.0003:
                                                            return 5.0
                                                        else: 
                                                            if alcohol<11:
                                                                return 6.0
                                                            else: 
                                                                return 6.0
                                    else: 
                                        if sulphates<0.59:
                                            return 5.0
                                        else: 
                                            if alcohol<11.2:
                                                if alcohol<10.9:
                                                    return 7.0
                                                else: 
                                                    return 7.0
                                            else: 
                                                return 7.0
                    else: 
                        if chlorides<0.088:
                            if alcohol<11:
                                return 5.0
                            else: 
                                return 5.0
                        else: 
                            if total_sulfur_dioxide<106:
                                if alcohol<11.4:
                                    return 6.0
                                else: 
                                    return 6.0
                            else: 
                                return 5.0
            else: 
                if sulphates<0.64:
                    if volatile_acidity<0.6:
                        if total_sulfur_dioxide<11:
                            if sulphates<0.55:
                                return 6.0
                            else: 
                                if alcohol<12.8:
                                    if alcohol<12.1:
                                        return 7.0
                                    else: 
                                        return 7.0
                                else: 
                                    return 7.0
                        else: 
                            if sulphates<0.63:
                                if sulphates<0.6:
                                    if sulphates<0.44:
                                        return 7.0
                                    else: 
                                        if volatile_acidity<0.59:
                                            if volatile_acidity<0.58:
                                                if alcohol<13.3:
                                                    if alcohol<13.2:
                                                        if alcohol<12.8:
                                                            if alcohol<12.7:
                                                                if alcohol<12.5:
                                                                    if alcohol<12.4:
                                                                        if alcohol<12.2:
                                                                            if alcohol<12:
                                                                                if alcohol<11.9:
                                                                                    if alcohol<11.7:
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
                                            return 7.0
                                else: 
                                    if residual_sugar<2.4:
                                        if total_sulfur_dioxide<106:
                                            if total_sulfur_dioxide<14:
                                                return 7.0
                                            else: 
                                                if alcohol<12.8:
                                                    if alcohol<12.2:
                                                        if alcohol<12.1:
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
                                        if alcohol<13:
                                            return 7.0
                                        else: 
                                            return 7.0
                            else: 
                                if alcohol<13:
                                    return 6.0
                                else: 
                                    return 5.0
                    else: 
                        if residual_sugar<2.5:
                            if sulphates<0.56:
                                if alcohol<12.8:
                                    if alcohol<12.1:
                                        if alcohol<11.95:
                                            return 5.0
                                        else: 
                                            return 5.0
                                    else: 
                                        return 5.0
                                else: 
                                    return 6.0
                            else: 
                                if free_sulfur_dioxide<5:
                                    return 7.0
                                else: 
                                    if alcohol<12.8:
                                        if alcohol<12.5:
                                            if alcohol<12.2:
                                                if alcohol<11.8:
                                                    if alcohol<11.6:
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
                            if alcohol<12:
                                return 4.0
                            else: 
                                if alcohol<13:
                                    if alcohol<12.6:
                                        if alcohol<12.2:
                                            return 5.0
                                        else: 
                                            return 5.0
                                    else: 
                                        return 5.0
                                else: 
                                    return 5.0
                else: 
                    if fixed_acidity<13:
                        if free_sulfur_dioxide<15:
                            if residual_sugar<5.2:
                                if density<0.99638:
                                    if density<0.99264:
                                        if sulphates<0.85:
                                            if alcohol<13.1:
                                                return 8.0
                                            else: 
                                                return 8.0
                                        else: 
                                            return 7.0
                                    else: 
                                        if alcohol<14:
                                            if sulphates<0.7:
                                                if residual_sugar<2.1:
                                                    if alcohol<12.5:
                                                        return 8.0
                                                    else: 
                                                        return 8.0
                                                else: 
                                                    if alcohol<12.7:
                                                        return 7.0
                                                    else: 
                                                        return 7.0
                                            else: 
                                                if sulphates<0.71:
                                                    if alcohol<12.8:
                                                        return 6.0
                                                    else: 
                                                        return 7.0
                                                else: 
                                                    if alcohol<13.4:
                                                        if alcohol<12.9:
                                                            if alcohol<12.5:
                                                                if alcohol<12.4:
                                                                    if alcohol<12:
                                                                        if alcohol<11.9:
                                                                            if alcohol<11.8:
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
                                            return 6.0
                                else: 
                                    if total_sulfur_dioxide<16:
                                        if alcohol<12.2:
                                            if alcohol<11.8:
                                                return 7.0
                                            else: 
                                                return 7.0
                                        else: 
                                            return 7.0
                                    else: 
                                        if sulphates<0.77:
                                            if alcohol<13.4:
                                                if alcohol<12.5:
                                                    if alcohol<12:
                                                        if alcohol<11.9:
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
                                            if alcohol<12.5:
                                                return 7.0
                                            else: 
                                                return 7.0
                            else: 
                                if alcohol<12.6:
                                    return 7.0
                                else: 
                                    if alcohol<13.4:
                                        return 8.0
                                    else: 
                                        return 8.0
                        else: 
                            if pH<3.5:
                                if residual_sugar<2.4:
                                    if sulphates<1.01:
                                        if alcohol<12.8:
                                            if alcohol<12.4:
                                                if alcohol<12.1:
                                                    if alcohol<11.8:
                                                        if alcohol<11.6:
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
                                    if sulphates<0.78:
                                        if alcohol<12.6:
                                            if alcohol<12.1:
                                                if alcohol<11.7:
                                                    if alcohol<11.6:
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
                                        if pH<3.3:
                                            return 7.0
                                        else: 
                                            if alcohol<12.1:
                                                if alcohol<11.8:
                                                    return 6.0
                                                else: 
                                                    return 6.0
                                            else: 
                                                return 6.0
                            else: 
                                if citric_acid<0.03:
                                    if alcohol<14:
                                        return 7.0
                                    else: 
                                        return 6.0
                                else: 
                                    return 8.0
                    else: 
                        if alcohol<13:
                            return 6.0
                        else: 
                            if alcohol<14.9:
                                return 5.0
                            else: 
                                return 5.0
        else: 
            if fixed_acidity<6.7:
                if alcohol<10.8:
                    return 4.0
                else: 
                    if pH<3.56:
                        if alcohol<11.9:
                            return 6.0
                        else: 
                            return 6.0
                    else: 
                        if chlorides<0.041:
                            return 6.0
                        else: 
                            if alcohol<11.5:
                                if alcohol<11.4:
                                    return 5.0
                                else: 
                                    return 5.0
                            else: 
                                return 5.0
            else: 
                if sulphates<0.57:
                    if sulphates<0.44:
                        return 4.0
                    else: 
                        if alcohol<11.5:
                            return 5.0
                        else: 
                            return 5.0
                else: 
                    if alcohol<11.3:
                        if alcohol<11.2:
                            if alcohol<11:
                                return 4.0
                            else: 
                                return 4.0
                        else: 
                            return 4.0
                    else: 
                        return 4.0
