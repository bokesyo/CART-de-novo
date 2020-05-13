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
    if alcohol<9.9:
        if sulphates<0.58:
            if pH<3.55:
                if chlorides<0.07:
                    if alcohol<9.8:
                        if alcohol<9.3:
                            if sulphates<0.57:
                                if alcohol<9.2:
                                    if alcohol<9.1:
                                        return 1
                                    else: 
                                        return 1
                                else: 
                                    return 1
                            else: 
                                return -1
                        else: 
                            if density<0.9973:
                                if pH<3.41:
                                    if alcohol<9.7:
                                        if alcohol<9.6:
                                            if alcohol<9.5:
                                                if alcohol<9.4:
                                                    if sulphates<0.53:
                                                        if sulphates<0.51:
                                                            return -1
                                                        else: 
                                                            return -1
                                                    else: 
                                                        return -1
                                                else: 
                                                    if sulphates<0.55:
                                                        if sulphates<0.47:
                                                            return -1
                                                        else: 
                                                            return -1
                                                    else: 
                                                        return -1
                                            else: 
                                                if sulphates<0.51:
                                                    if sulphates<0.45:
                                                        return -1
                                                    else: 
                                                        return -1
                                                else: 
                                                    return -1
                                        else: 
                                            return -1
                                    else: 
                                        return -1
                                else: 
                                    if alcohol<9.6:
                                        return 1
                                    else: 
                                        return -1
                            else: 
                                return 1
                    else: 
                        if sulphates<0.54:
                            return 1
                        else: 
                            return 1
                else: 
                    if residual_sugar<10.7:
                        if density<0.9973:
                            if residual_sugar<5.2:
                                if fixed_acidity<7.7:
                                    if total_sulfur_dioxide<89:
                                        if citric_acid<0.31:
                                            if alcohol<9.8:
                                                if alcohol<9.7:
                                                    if alcohol<9.6:
                                                        if alcohol<9.5:
                                                            if alcohol<9.4:
                                                                if alcohol<9.3:
                                                                    if sulphates<0.56:
                                                                        if sulphates<0.54:
                                                                            if sulphates<0.48:
                                                                                if sulphates<0.47:
                                                                                    if sulphates<0.44:
                                                                                        return -1
                                                                                    else: 
                                                                                        return -1
                                                                                else: 
                                                                                    return -1
                                                                            else: 
                                                                                return -1
                                                                        else: 
                                                                            return -1
                                                                    else: 
                                                                        return -1
                                                                else: 
                                                                    if sulphates<0.52:
                                                                        if sulphates<0.5:
                                                                            return -1
                                                                        else: 
                                                                            return -1
                                                                    else: 
                                                                        return -1
                                                            else: 
                                                                if sulphates<0.55:
                                                                    if sulphates<0.52:
                                                                        if sulphates<0.5:
                                                                            if sulphates<0.48:
                                                                                return -1
                                                                            else: 
                                                                                if pH<3.45:
                                                                                    return -1
                                                                                else: 
                                                                                    return -1
                                                                        else: 
                                                                            return -1
                                                                    else: 
                                                                        return -1
                                                                else: 
                                                                    return -1
                                                        else: 
                                                            if sulphates<0.54:
                                                                if sulphates<0.52:
                                                                    if sulphates<0.5:
                                                                        if sulphates<0.47:
                                                                            if sulphates<0.45:
                                                                                return -1
                                                                            else: 
                                                                                return -1
                                                                        else: 
                                                                            return -1
                                                                    else: 
                                                                        return -1
                                                                else: 
                                                                    return -1
                                                            else: 
                                                                return -1
                                                    else: 
                                                        if sulphates<0.56:
                                                            if sulphates<0.53:
                                                                if sulphates<0.49:
                                                                    return -1
                                                                else: 
                                                                    return -1
                                                            else: 
                                                                return -1
                                                        else: 
                                                            return -1
                                                else: 
                                                    if sulphates<0.55:
                                                        return -1
                                                    else: 
                                                        if pH<3.37:
                                                            return -1
                                                        else: 
                                                            return -1
                                            else: 
                                                if sulphates<0.57:
                                                    if sulphates<0.56:
                                                        if sulphates<0.54:
                                                            if sulphates<0.53:
                                                                if sulphates<0.51:
                                                                    if sulphates<0.5:
                                                                        if pH<3.5:
                                                                            return -1
                                                                        else: 
                                                                            return -1
                                                                    else: 
                                                                        return -1
                                                                else: 
                                                                    return -1
                                                            else: 
                                                                return -1
                                                        else: 
                                                            return -1
                                                    else: 
                                                        return -1
                                                else: 
                                                    return -1
                                        else: 
                                            if alcohol<9.5:
                                                if density<0.9972:
                                                    return -1
                                                else: 
                                                    return -1
                                            else: 
                                                return 1
                                    else: 
                                        if alcohol<9.4:
                                            return 1
                                        else: 
                                            if alcohol<9.7:
                                                return -1
                                            else: 
                                                return -1
                                else: 
                                    if chlorides<0.08:
                                        if alcohol<9.4:
                                            if alcohol<9.3:
                                                if alcohol<9.2:
                                                    return -1
                                                else: 
                                                    if sulphates<0.51:
                                                        return -1
                                                    else: 
                                                        return -1
                                            else: 
                                                return -1
                                        else: 
                                            if citric_acid<0.02:
                                                if alcohol<9.8:
                                                    return -1
                                                else: 
                                                    return -1
                                            else: 
                                                if total_sulfur_dioxide<120:
                                                    if total_sulfur_dioxide<25:
                                                        if sulphates<0.57:
                                                            if alcohol<9.6:
                                                                return -1
                                                            else: 
                                                                return -1
                                                        else: 
                                                            return 1
                                                    else: 
                                                        if alcohol<9.8:
                                                            if alcohol<9.7:
                                                                if alcohol<9.6:
                                                                    if alcohol<9.5:
                                                                        return 1
                                                                    else: 
                                                                        return 1
                                                                else: 
                                                                    if sulphates<0.54:
                                                                        return 1
                                                                    else: 
                                                                        return 1
                                                            else: 
                                                                return 1
                                                        else: 
                                                            if sulphates<0.5:
                                                                if pH<3.35:
                                                                    return 1
                                                                else: 
                                                                    return 1
                                                            else: 
                                                                return 1
                                                else: 
                                                    if alcohol<9.5:
                                                        return -1
                                                    else: 
                                                        return -1
                                    else: 
                                        if density<0.99578:
                                            return 1
                                        else: 
                                            if pH<3.37:
                                                if alcohol<9.8:
                                                    if alcohol<9.7:
                                                        if alcohol<9.5:
                                                            if alcohol<9.4:
                                                                if alcohol<9.3:
                                                                    if alcohol<9.2:
                                                                        if alcohol<9.1:
                                                                            return -1
                                                                        else: 
                                                                            return -1
                                                                    else: 
                                                                        return -1
                                                                else: 
                                                                    return -1
                                                            else: 
                                                                if sulphates<0.56:
                                                                    if sulphates<0.53:
                                                                        if sulphates<0.52:
                                                                            if sulphates<0.49:
                                                                                return -1
                                                                            else: 
                                                                                return -1
                                                                        else: 
                                                                            return -1
                                                                    else: 
                                                                        if pH<3.17:
                                                                            return -1
                                                                        else: 
                                                                            return -1
                                                                else: 
                                                                    return -1
                                                        else: 
                                                            if sulphates<0.55:
                                                                if sulphates<0.54:
                                                                    if sulphates<0.5:
                                                                        return -1
                                                                    else: 
                                                                        return -1
                                                                else: 
                                                                    if pH<3.33:
                                                                        return -1
                                                                    else: 
                                                                        return -1
                                                            else: 
                                                                if pH<3.28:
                                                                    return -1
                                                                else: 
                                                                    return -1
                                                    else: 
                                                        return -1
                                                else: 
                                                    if sulphates<0.53:
                                                        if sulphates<0.5:
                                                            return -1
                                                        else: 
                                                            return -1
                                                    else: 
                                                        return -1
                                            else: 
                                                if alcohol<9.5:
                                                    return 1
                                                else: 
                                                    return -1
                            else: 
                                if alcohol<9.6:
                                    return 1
                                else: 
                                    return 1
                        else: 
                            if residual_sugar<2.8:
                                if alcohol<9.8:
                                    if alcohol<9.7:
                                        if alcohol<9.6:
                                            if alcohol<9.5:
                                                if alcohol<9.4:
                                                    if alcohol<9.2:
                                                        if alcohol<9.1:
                                                            return -1
                                                        else: 
                                                            if sulphates<0.5:
                                                                return -1
                                                            else: 
                                                                return -1
                                                    else: 
                                                        if sulphates<0.56:
                                                            if sulphates<0.53:
                                                                if sulphates<0.52:
                                                                    return -1
                                                                else: 
                                                                    if pH<3.49:
                                                                        if pH<3.2:
                                                                            return -1
                                                                        else: 
                                                                            return -1
                                                                    else: 
                                                                        return -1
                                                            else: 
                                                                return -1
                                                        else: 
                                                            return -1
                                                else: 
                                                    if sulphates<0.57:
                                                        if sulphates<0.56:
                                                            if sulphates<0.55:
                                                                if sulphates<0.54:
                                                                    if sulphates<0.53:
                                                                        if sulphates<0.51:
                                                                            if sulphates<0.46:
                                                                                return -1
                                                                            else: 
                                                                                return -1
                                                                        else: 
                                                                            return -1
                                                                    else: 
                                                                        if density<0.9979:
                                                                            return -1
                                                                        else: 
                                                                            return -1
                                                                else: 
                                                                    return -1
                                                            else: 
                                                                if pH<3.28:
                                                                    if pH<3.27:
                                                                        return -1
                                                                    else: 
                                                                        return -1
                                                                else: 
                                                                    return -1
                                                        else: 
                                                            if total_sulfur_dioxide<40:
                                                                return -1
                                                            else: 
                                                                return -1
                                                    else: 
                                                        return -1
                                            else: 
                                                if sulphates<0.57:
                                                    if sulphates<0.55:
                                                        if sulphates<0.54:
                                                            if sulphates<0.53:
                                                                if sulphates<0.51:
                                                                    if sulphates<0.5:
                                                                        return -1
                                                                    else: 
                                                                        return -1
                                                                else: 
                                                                    if pH<3.18:
                                                                        return -1
                                                                    else: 
                                                                        return -1
                                                            else: 
                                                                if pH<3.45:
                                                                    if pH<3.44:
                                                                        return -1
                                                                    else: 
                                                                        return -1
                                                                else: 
                                                                    return -1
                                                        else: 
                                                            return -1
                                                    else: 
                                                        if pH<3.53:
                                                            return -1
                                                        else: 
                                                            return -1
                                                else: 
                                                    return -1
                                        else: 
                                            if sulphates<0.56:
                                                if sulphates<0.51:
                                                    if sulphates<0.46:
                                                        if sulphates<0.44:
                                                            return -1
                                                        else: 
                                                            if pH<3.22:
                                                                return -1
                                                            else: 
                                                                return -1
                                                    else: 
                                                        return -1
                                                else: 
                                                    return -1
                                            else: 
                                                return -1
                                    else: 
                                        if sulphates<0.57:
                                            if sulphates<0.56:
                                                if sulphates<0.54:
                                                    return -1
                                                else: 
                                                    return -1
                                            else: 
                                                return -1
                                        else: 
                                            if pH<3.53:
                                                if pH<3.5:
                                                    return -1
                                                else: 
                                                    return -1
                                            else: 
                                                return -1
                                else: 
                                    if sulphates<0.54:
                                        return -1
                                    else: 
                                        if pH<3.48:
                                            return -1
                                        else: 
                                            return -1
                            else: 
                                if fixed_acidity<9.1:
                                    if alcohol<9.7:
                                        if alcohol<9.5:
                                            if alcohol<9.4:
                                                if alcohol<9.3:
                                                    if sulphates<0.54:
                                                        return -1
                                                    else: 
                                                        return -1
                                                else: 
                                                    return -1
                                            else: 
                                                if sulphates<0.54:
                                                    if sulphates<0.53:
                                                        if sulphates<0.49:
                                                            return -1
                                                        else: 
                                                            if density<0.9982:
                                                                return -1
                                                            else: 
                                                                return -1
                                                    else: 
                                                        return -1
                                                else: 
                                                    return -1
                                        else: 
                                            if sulphates<0.55:
                                                if sulphates<0.54:
                                                    return -1
                                                else: 
                                                    return -1
                                            else: 
                                                return -1
                                    else: 
                                        return -1
                                else: 
                                    if alcohol<9.6:
                                        if sulphates<0.55:
                                            return 1
                                        else: 
                                            return 1
                                    else: 
                                        return -1
                    else: 
                        return 1
            else: 
                if alcohol<9.7:
                    return 1
                else: 
                    return 1
        else: 
            if fixed_acidity<10.1:
                if total_sulfur_dioxide<92:
                    if fixed_acidity<9.2:
                        if volatile_acidity<0.56:
                            if volatile_acidity<0.51:
                                if volatile_acidity<0.39:
                                    if density<0.99661:
                                        if sulphates<0.67:
                                            return -1
                                        else: 
                                            return -1
                                    else: 
                                        if chlorides<0.113:
                                            if alcohol<9.8:
                                                if alcohol<9.7:
                                                    if alcohol<9.6:
                                                        if alcohol<9.5:
                                                            if alcohol<9.4:
                                                                return 1
                                                            else: 
                                                                return 1
                                                        else: 
                                                            if sulphates<0.62:
                                                                if pH<3.42:
                                                                    return 1
                                                                else: 
                                                                    return 1
                                                            else: 
                                                                return 1
                                                    else: 
                                                        if sulphates<0.8:
                                                            if pH<3.34:
                                                                return 1
                                                            else: 
                                                                return 1
                                                        else: 
                                                            return 1
                                                else: 
                                                    if sulphates<0.77:
                                                        return 1
                                                    else: 
                                                        return 1
                                            else: 
                                                return 1
                                        else: 
                                            if alcohol<9.4:
                                                return 1
                                            else: 
                                                if alcohol<9.5:
                                                    return -1
                                                else: 
                                                    return -1
                                else: 
                                    if residual_sugar<1.7:
                                        if alcohol<9.8:
                                            if alcohol<9.5:
                                                if alcohol<9.4:
                                                    if alcohol<9.3:
                                                        if alcohol<9.2:
                                                            return -1
                                                        else: 
                                                            return -1
                                                    else: 
                                                        return -1
                                                else: 
                                                    return -1
                                            else: 
                                                if sulphates<0.91:
                                                    return -1
                                                else: 
                                                    return -1
                                        else: 
                                            return -1
                                    else: 
                                        if total_sulfur_dioxide<62:
                                            if sulphates<0.72:
                                                if free_sulfur_dioxide<21:
                                                    if fixed_acidity<8:
                                                        if free_sulfur_dioxide<18:
                                                            if alcohol<9.8:
                                                                if alcohol<9.6:
                                                                    if alcohol<9.5:
                                                                        if alcohol<9.4:
                                                                            if alcohol<9.2:
                                                                                return -1
                                                                            else: 
                                                                                return -1
                                                                        else: 
                                                                            return -1
                                                                    else: 
                                                                        if sulphates<0.62:
                                                                            return -1
                                                                        else: 
                                                                            return -1
                                                                else: 
                                                                    return -1
                                                            else: 
                                                                return -1
                                                        else: 
                                                            if alcohol<9.7:
                                                                return 1
                                                            else: 
                                                                return -1
                                                    else: 
                                                        return 1
                                                else: 
                                                    if alcohol<9.7:
                                                        return 1
                                                    else: 
                                                        return 1
                                            else: 
                                                if alcohol<9.8:
                                                    if alcohol<9.6:
                                                        if alcohol<9.5:
                                                            if alcohol<9.1:
                                                                return 1
                                                            else: 
                                                                return 1
                                                        else: 
                                                            return 1
                                                    else: 
                                                        return 1
                                                else: 
                                                    return 1
                                        else: 
                                            if free_sulfur_dioxide<29:
                                                if alcohol<9.6:
                                                    if alcohol<9.5:
                                                        if alcohol<9.3:
                                                            if sulphates<1.17:
                                                                return -1
                                                            else: 
                                                                return -1
                                                        else: 
                                                            return -1
                                                    else: 
                                                        if sulphates<0.64:
                                                            return -1
                                                        else: 
                                                            return -1
                                                else: 
                                                    return -1
                                            else: 
                                                if alcohol<9.5:
                                                    return -1
                                                else: 
                                                    if sulphates<0.65:
                                                        return 1
                                                    else: 
                                                        return 1
                            else: 
                                if total_sulfur_dioxide<66:
                                    if alcohol<9.7:
                                        if alcohol<9.6:
                                            if alcohol<9.5:
                                                if alcohol<9.4:
                                                    if alcohol<9.3:
                                                        if alcohol<9.2:
                                                            if sulphates<0.65:
                                                                return 1
                                                            else: 
                                                                return 1
                                                        else: 
                                                            return 1
                                                    else: 
                                                        return 1
                                                else: 
                                                    if sulphates<0.91:
                                                        if sulphates<0.63:
                                                            return 1
                                                        else: 
                                                            return 1
                                                    else: 
                                                        return 1
                                            else: 
                                                return 1
                                        else: 
                                            if sulphates<0.81:
                                                return 1
                                            else: 
                                                return 1
                                    else: 
                                        return 1
                                else: 
                                    if alcohol<9.4:
                                        return -1
                                    else: 
                                        return -1
                        else: 
                            if residual_sugar<1.9:
                                if pH<3:
                                    return 1
                                else: 
                                    if citric_acid<0.15:
                                        if total_sulfur_dioxide<64:
                                            if density<0.9972:
                                                if alcohol<9.8:
                                                    if alcohol<9.7:
                                                        if alcohol<9.6:
                                                            if alcohol<9.5:
                                                                if alcohol<9.4:
                                                                    return -1
                                                                else: 
                                                                    return -1
                                                            else: 
                                                                return -1
                                                        else: 
                                                            return -1
                                                    else: 
                                                        return -1
                                                else: 
                                                    return -1
                                            else: 
                                                if alcohol<9.6:
                                                    return -1
                                                else: 
                                                    return 1
                                        else: 
                                            return 1
                                    else: 
                                        if alcohol<9.8:
                                            if alcohol<9.5:
                                                if alcohol<9.4:
                                                    if alcohol<9.3:
                                                        if alcohol<9.2:
                                                            if sulphates<1.56:
                                                                return -1
                                                            else: 
                                                                return -1
                                                        else: 
                                                            if sulphates<1.17:
                                                                return -1
                                                            else: 
                                                                return -1
                                                    else: 
                                                        if sulphates<1.15:
                                                            if sulphates<1.09:
                                                                if sulphates<0.79:
                                                                    return -1
                                                                else: 
                                                                    return -1
                                                            else: 
                                                                return -1
                                                        else: 
                                                            return -1
                                                else: 
                                                    return -1
                                            else: 
                                                if sulphates<1.59:
                                                    if sulphates<0.93:
                                                        return -1
                                                    else: 
                                                        return -1
                                                else: 
                                                    return -1
                                        else: 
                                            if pH<3.59:
                                                return -1
                                            else: 
                                                return -1
                            else: 
                                if sulphates<0.59:
                                    if alcohol<9.8:
                                        if alcohol<9.3:
                                            if alcohol<9.2:
                                                return 1
                                            else: 
                                                return 1
                                        else: 
                                            return 1
                                    else: 
                                        if pH<3.53:
                                            return 1
                                        else: 
                                            return 1
                                else: 
                                    if pH<3.16:
                                        if alcohol<9.5:
                                            return 1
                                        else: 
                                            return 1
                                    else: 
                                        if residual_sugar<2.5:
                                            if chlorides<0.075:
                                                if sulphates<0.67:
                                                    if alcohol<9.5:
                                                        return -1
                                                    else: 
                                                        return -1
                                                else: 
                                                    if alcohol<9.8:
                                                        if alcohol<9.5:
                                                            return 1
                                                        else: 
                                                            if sulphates<0.82:
                                                                return 1
                                                            else: 
                                                                return 1
                                                    else: 
                                                        return -1
                                            else: 
                                                if total_sulfur_dioxide<16:
                                                    return 1
                                                else: 
                                                    if citric_acid<0.31:
                                                        if alcohol<9.8:
                                                            if alcohol<9.7:
                                                                if alcohol<9.6:
                                                                    if alcohol<9.5:
                                                                        if alcohol<9.4:
                                                                            if sulphates<0.73:
                                                                                if sulphates<0.64:
                                                                                    if sulphates<0.63:
                                                                                        if sulphates<0.62:
                                                                                            return -1
                                                                                        else: 
                                                                                            return -1
                                                                                    else: 
                                                                                        return -1
                                                                                else: 
                                                                                    return -1
                                                                            else: 
                                                                                return -1
                                                                        else: 
                                                                            if sulphates<0.7:
                                                                                if sulphates<0.64:
                                                                                    if pH<3.41:
                                                                                        return -1
                                                                                    else: 
                                                                                        return -1
                                                                                else: 
                                                                                    return -1
                                                                            else: 
                                                                                if pH<3.19:
                                                                                    return -1
                                                                                else: 
                                                                                    return -1
                                                                    else: 
                                                                        if sulphates<0.69:
                                                                            return -1
                                                                        else: 
                                                                            return -1
                                                                else: 
                                                                    if sulphates<0.82:
                                                                        if sulphates<0.73:
                                                                            return -1
                                                                        else: 
                                                                            return -1
                                                                    else: 
                                                                        return -1
                                                            else: 
                                                                if sulphates<0.8:
                                                                    if sulphates<0.74:
                                                                        if sulphates<0.73:
                                                                            return -1
                                                                        else: 
                                                                            return -1
                                                                    else: 
                                                                        return -1
                                                                else: 
                                                                    return -1
                                                        else: 
                                                            if pH<3.26:
                                                                return 1
                                                            else: 
                                                                if sulphates<0.75:
                                                                    if sulphates<0.65:
                                                                        return -1
                                                                    else: 
                                                                        return -1
                                                                else: 
                                                                    return -1
                                                    else: 
                                                        if sulphates<0.69:
                                                            return -1
                                                        else: 
                                                            return 1
                                        else: 
                                            if alcohol<9.8:
                                                if sulphates<0.6:
                                                    return -1
                                                else: 
                                                    if density<0.99745:
                                                        if alcohol<9.6:
                                                            return -1
                                                        else: 
                                                            return 1
                                                    else: 
                                                        if alcohol<9.7:
                                                            if alcohol<9.4:
                                                                if alcohol<9.3:
                                                                    if alcohol<9.25:
                                                                        if alcohol<9.1:
                                                                            return 1
                                                                        else: 
                                                                            return 1
                                                                    else: 
                                                                        return 1
                                                                else: 
                                                                    return 1
                                                            else: 
                                                                return 1
                                                        else: 
                                                            return 1
                                            else: 
                                                if sulphates<0.72:
                                                    if sulphates<0.68:
                                                        if sulphates<0.63:
                                                            return -1
                                                        else: 
                                                            return -1
                                                    else: 
                                                        return -1
                                                else: 
                                                    return -1
                    else: 
                        if alcohol<9.8:
                            if alcohol<9.7:
                                if alcohol<9.6:
                                    if alcohol<9.5:
                                        if alcohol<9.4:
                                            if alcohol<8.8:
                                                return -1
                                            else: 
                                                return -1
                                        else: 
                                            if sulphates<2:
                                                return -1
                                            else: 
                                                return -1
                                    else: 
                                        return -1
                                else: 
                                    if sulphates<0.82:
                                        if sulphates<0.78:
                                            return -1
                                        else: 
                                            return -1
                                    else: 
                                        return -1
                            else: 
                                return -1
                        else: 
                            if sulphates<0.71:
                                if sulphates<0.59:
                                    return -1
                                else: 
                                    return -1
                            else: 
                                return -1
                else: 
                    if total_sulfur_dioxide<102:
                        if fixed_acidity<7.9:
                            if alcohol<9.8:
                                if alcohol<9.5:
                                    if alcohol<9.4:
                                        if alcohol<9.2:
                                            return -1
                                        else: 
                                            if pH<3.32:
                                                return -1
                                            else: 
                                                return -1
                                    else: 
                                        if sulphates<0.77:
                                            if sulphates<0.67:
                                                return -1
                                            else: 
                                                return -1
                                        else: 
                                            return -1
                                else: 
                                    return -1
                            else: 
                                if sulphates<0.62:
                                    return -1
                                else: 
                                    return -1
                        else: 
                            if sulphates<0.63:
                                return 1
                            else: 
                                return 1
                    else: 
                        if alcohol<9.8:
                            if alcohol<9.7:
                                if alcohol<9.5:
                                    if alcohol<9.4:
                                        if alcohol<9.3:
                                            if alcohol<9.2:
                                                return -1
                                            else: 
                                                if sulphates<0.93:
                                                    if sulphates<0.88:
                                                        if sulphates<0.73:
                                                            if sulphates<0.61:
                                                                return -1
                                                            else: 
                                                                return -1
                                                        else: 
                                                            return -1
                                                    else: 
                                                        return -1
                                                else: 
                                                    return -1
                                        else: 
                                            if sulphates<1.14:
                                                if sulphates<1.07:
                                                    if sulphates<1.03:
                                                        if sulphates<1.02:
                                                            if sulphates<0.71:
                                                                if sulphates<0.69:
                                                                    return -1
                                                                else: 
                                                                    return -1
                                                            else: 
                                                                return -1
                                                        else: 
                                                            return -1
                                                    else: 
                                                        return -1
                                                else: 
                                                    return -1
                                            else: 
                                                return -1
                                    else: 
                                        if sulphates<0.66:
                                            return -1
                                        else: 
                                            return -1
                                else: 
                                    if sulphates<1.22:
                                        if sulphates<0.64:
                                            if sulphates<0.61:
                                                if sulphates<0.6:
                                                    if sulphates<0.59:
                                                        return -1
                                                    else: 
                                                        return -1
                                                else: 
                                                    if density<0.9982:
                                                        return -1
                                                    else: 
                                                        return -1
                                            else: 
                                                if pH<3.38:
                                                    return -1
                                                else: 
                                                    return -1
                                        else: 
                                            return -1
                                    else: 
                                        return -1
                            else: 
                                return -1
                        else: 
                            if sulphates<1.98:
                                if sulphates<0.66:
                                    return -1
                                else: 
                                    if pH<3.17:
                                        if total_sulfur_dioxide<111:
                                            return -1
                                        else: 
                                            return -1
                                    else: 
                                        return -1
                            else: 
                                return -1
            else: 
                if density<0.9982:
                    if alcohol<9.5:
                        return 1
                    else: 
                        if alcohol<9.6:
                            if sulphates<0.62:
                                return -1
                            else: 
                                return -1
                        else: 
                            return -1
                else: 
                    if chlorides<0.088:
                        if free_sulfur_dioxide<6:
                            return -1
                        else: 
                            if alcohol<9.8:
                                if alcohol<9.7:
                                    if alcohol<9.5:
                                        if alcohol<9.4:
                                            if alcohol<9.3:
                                                if alcohol<9.2:
                                                    return 1
                                                else: 
                                                    if sulphates<1.18:
                                                        if sulphates<0.84:
                                                            return 1
                                                        else: 
                                                            return 1
                                                    else: 
                                                        return 1
                                            else: 
                                                if sulphates<0.82:
                                                    if sulphates<0.7:
                                                        if sulphates<0.67:
                                                            return 1
                                                        else: 
                                                            return 1
                                                    else: 
                                                        return 1
                                                else: 
                                                    return 1
                                        else: 
                                            return 1
                                    else: 
                                        return 1
                                else: 
                                    return 1
                            else: 
                                if sulphates<1.36:
                                    return 1
                                else: 
                                    return 1
                    else: 
                        if alcohol<9.5:
                            if alcohol<9.3:
                                return 1
                            else: 
                                if alcohol<9.4:
                                    if sulphates<0.8:
                                        return -1
                                    else: 
                                        return -1
                                else: 
                                    if sulphates<1.06:
                                        if sulphates<1.05:
                                            return -1
                                        else: 
                                            return -1
                                    else: 
                                        return -1
                        else: 
                            if alcohol<9.8:
                                if sulphates<0.81:
                                    if sulphates<0.63:
                                        return 1
                                    else: 
                                        return 1
                                else: 
                                    return 1
                            else: 
                                if sulphates<0.75:
                                    return 1
                                else: 
                                    return 1
    else: 
        if sulphates<0.55:
            if volatile_acidity<0.46:
                if density<0.99772:
                    if fixed_acidity<6.3:
                        if total_sulfur_dioxide<32:
                            return -1
                        else: 
                            return -1
                    else: 
                        if residual_sugar<1.7:
                            if residual_sugar<1.6:
                                if alcohol<12.7:
                                    if alcohol<11.5:
                                        return 1
                                    else: 
                                        return 1
                                else: 
                                    return 1
                            else: 
                                if alcohol<11.4:
                                    return -1
                                else: 
                                    return -1
                        else: 
                            if alcohol<13.3:
                                if alcohol<12.7:
                                    if alcohol<12.5:
                                        if alcohol<12.4:
                                            if alcohol<12.3:
                                                if alcohol<12.2:
                                                    if alcohol<12:
                                                        if alcohol<11.9:
                                                            if alcohol<11.8:
                                                                if alcohol<11.7:
                                                                    if alcohol<11.5:
                                                                        if alcohol<11.3:
                                                                            if alcohol<10.8:
                                                                                if alcohol<10.3:
                                                                                    if alcohol<10.2:
                                                                                        if alcohol<10.1:
                                                                                            return 1
                                                                                        else: 
                                                                                            if sulphates<0.54:
                                                                                                return 1
                                                                                            else: 
                                                                                                return 1
                                                                                    else: 
                                                                                        return 1
                                                                                else: 
                                                                                    return 1
                                                                            else: 
                                                                                return 1
                                                                        else: 
                                                                            return 1
                                                                    else: 
                                                                        return 1
                                                                else: 
                                                                    return 1
                                                            else: 
                                                                return 1
                                                        else: 
                                                            if sulphates<0.53:
                                                                return 1
                                                            else: 
                                                                return 1
                                                    else: 
                                                        return 1
                                                else: 
                                                    return 1
                                            else: 
                                                if total_sulfur_dioxide<289:
                                                    return 1
                                                else: 
                                                    return 1
                                        else: 
                                            return 1
                                    else: 
                                        return 1
                                else: 
                                    return 1
                            else: 
                                return 1
                else: 
                    if alcohol<10.5:
                        return -1
                    else: 
                        if sulphates<0.53:
                            return -1
                        else: 
                            return -1
            else: 
                if density<0.99546:
                    if density<0.9948:
                        if density<0.99286:
                            return 1
                        else: 
                            if residual_sugar<1.4:
                                return 1
                            else: 
                                if volatile_acidity<0.96:
                                    if alcohol<13:
                                        if alcohol<12.6:
                                            if alcohol<12.1:
                                                if alcohol<11.95:
                                                    if alcohol<11.7:
                                                        if alcohol<11.6:
                                                            if alcohol<11.4:
                                                                if alcohol<11.2:
                                                                    if alcohol<11:
                                                                        if alcohol<10.4:
                                                                            if alcohol<10:
                                                                                return -1
                                                                            else: 
                                                                                if sulphates<0.52:
                                                                                    return -1
                                                                                else: 
                                                                                    return -1
                                                                        else: 
                                                                            return -1
                                                                    else: 
                                                                        if sulphates<0.54:
                                                                            return -1
                                                                        else: 
                                                                            return -1
                                                                else: 
                                                                    return -1
                                                            else: 
                                                                return -1
                                                        else: 
                                                            return -1
                                                    else: 
                                                        return -1
                                                else: 
                                                    return -1
                                            else: 
                                                return -1
                                        else: 
                                            return -1
                                    else: 
                                        return -1
                                else: 
                                    if alcohol<11.9:
                                        if alcohol<10.9:
                                            return -1
                                        else: 
                                            return -1
                                    else: 
                                        return 1
                    else: 
                        if alcohol<10.5:
                            if alcohol<10.1:
                                return -1
                            else: 
                                return -1
                        else: 
                            if volatile_acidity<1.09:
                                if residual_sugar<2.8:
                                    if alcohol<11.8:
                                        if alcohol<11.5:
                                            if alcohol<11.4:
                                                if alcohol<11.2:
                                                    if alcohol<10.8:
                                                        if alcohol<10.7:
                                                            return 1
                                                        else: 
                                                            return 1
                                                    else: 
                                                        return 1
                                                else: 
                                                    return 1
                                            else: 
                                                return 1
                                        else: 
                                            return 1
                                    else: 
                                        return 1
                                else: 
                                    if alcohol<12.7:
                                        return -1
                                    else: 
                                        return 1
                            else: 
                                return -1
                else: 
                    if residual_sugar<1.9:
                        if pH<3.41:
                            if alcohol<10.4:
                                if sulphates<0.53:
                                    return 1
                                else: 
                                    return 1
                            else: 
                                return 1
                        else: 
                            if alcohol<10.9:
                                return -1
                            else: 
                                if sulphates<0.49:
                                    return -1
                                else: 
                                    return -1
                    else: 
                        if residual_sugar<4:
                            if alcohol<11.5:
                                if alcohol<11:
                                    if alcohol<10.9:
                                        if alcohol<10.8:
                                            if alcohol<10.7:
                                                if alcohol<10.5:
                                                    if alcohol<10.3:
                                                        if alcohol<10.2:
                                                            if alcohol<10.1:
                                                                if alcohol<10:
                                                                    if sulphates<0.52:
                                                                        if sulphates<0.51:
                                                                            if sulphates<0.49:
                                                                                if sulphates<0.48:
                                                                                    return -1
                                                                                else: 
                                                                                    return -1
                                                                            else: 
                                                                                return -1
                                                                        else: 
                                                                            return -1
                                                                    else: 
                                                                        if pH<3.28:
                                                                            if pH<3.26:
                                                                                if pH<3.21:
                                                                                    return -1
                                                                                else: 
                                                                                    return -1
                                                                            else: 
                                                                                return -1
                                                                        else: 
                                                                            return -1
                                                                else: 
                                                                    if sulphates<0.53:
                                                                        if sulphates<0.48:
                                                                            if sulphates<0.47:
                                                                                return -1
                                                                            else: 
                                                                                if pH<3.46:
                                                                                    if pH<3.4:
                                                                                        if pH<3.26:
                                                                                            return -1
                                                                                        else: 
                                                                                            return -1
                                                                                    else: 
                                                                                        return -1
                                                                                else: 
                                                                                    return -1
                                                                        else: 
                                                                            return -1
                                                                    else: 
                                                                        return -1
                                                            else: 
                                                                if sulphates<0.54:
                                                                    return -1
                                                                else: 
                                                                    if pH<3.35:
                                                                        return -1
                                                                    else: 
                                                                        return -1
                                                        else: 
                                                            return -1
                                                    else: 
                                                        if sulphates<0.53:
                                                            return -1
                                                        else: 
                                                            return -1
                                                else: 
                                                    if sulphates<0.48:
                                                        return -1
                                                    else: 
                                                        return -1
                                            else: 
                                                return -1
                                        else: 
                                            if fixed_acidity<6.5:
                                                return -1
                                            else: 
                                                return -1
                                    else: 
                                        return -1
                                else: 
                                    if sulphates<0.52:
                                        if sulphates<0.5:
                                            return -1
                                        else: 
                                            return -1
                                    else: 
                                        return -1
                            else: 
                                return -1
                        else: 
                            if pH<3.4:
                                if alcohol<10.8:
                                    return 1
                                else: 
                                    return 1
                            else: 
                                if alcohol<12.2:
                                    if alcohol<10.9:
                                        if alcohol<10.7:
                                            if alcohol<10.2:
                                                return -1
                                            else: 
                                                return -1
                                        else: 
                                            return -1
                                    else: 
                                        return -1
                                else: 
                                    return -1
        else: 
            if alcohol<11.5:
                if volatile_acidity<0.64:
                    if sulphates<0.64:
                        if chlorides<0.077:
                            if pH<3.34:
                                if citric_acid<0.42:
                                    if alcohol<11.4:
                                        if alcohol<11.3:
                                            if alcohol<10.4:
                                                if alcohol<10.3:
                                                    return 1
                                                else: 
                                                    return 1
                                            else: 
                                                if sulphates<0.63:
                                                    return 1
                                                else: 
                                                    return 1
                                        else: 
                                            return 1
                                    else: 
                                        if sulphates<0.58:
                                            return 1
                                        else: 
                                            return 1
                                else: 
                                    if pH<3.13:
                                        if alcohol<10:
                                            return -1
                                        else: 
                                            if alcohol<10.8:
                                                return 1
                                            else: 
                                                return 1
                                    else: 
                                        if alcohol<11.4:
                                            if sulphates<0.63:
                                                return -1
                                            else: 
                                                return -1
                                        else: 
                                            if sulphates<0.57:
                                                return -1
                                            else: 
                                                return -1
                            else: 
                                if residual_sugar<2.5:
                                    if alcohol<11.4:
                                        if alcohol<11.3:
                                            if alcohol<10.9:
                                                if alcohol<10.7:
                                                    if alcohol<10.5:
                                                        if alcohol<10.2:
                                                            if alcohol<10.1:
                                                                return -1
                                                            else: 
                                                                if sulphates<0.62:
                                                                    if sulphates<0.59:
                                                                        return -1
                                                                    else: 
                                                                        return -1
                                                                else: 
                                                                    return -1
                                                        else: 
                                                            if sulphates<0.61:
                                                                return -1
                                                            else: 
                                                                return -1
                                                    else: 
                                                        return -1
                                                else: 
                                                    return -1
                                            else: 
                                                if sulphates<0.58:
                                                    return -1
                                                else: 
                                                    return -1
                                        else: 
                                            return -1
                                    else: 
                                        if sulphates<0.58:
                                            return -1
                                        else: 
                                            return -1
                                else: 
                                    if density<0.99639:
                                        if alcohol<11.2:
                                            if alcohol<10.8:
                                                return 1
                                            else: 
                                                return 1
                                        else: 
                                            return 1
                                    else: 
                                        return -1
                        else: 
                            if density<0.99669:
                                if pH<3.52:
                                    if pH<3.17:
                                        if alcohol<11:
                                            return 1
                                        else: 
                                            return -1
                                    else: 
                                        if sulphates<0.63:
                                            if alcohol<11.4:
                                                if alcohol<11.3:
                                                    if alcohol<11.1:
                                                        if alcohol<11:
                                                            if alcohol<10.9:
                                                                if alcohol<10.8:
                                                                    if alcohol<10.7:
                                                                        if alcohol<10.6:
                                                                            if alcohol<10.5:
                                                                                if alcohol<10.4:
                                                                                    if alcohol<10.3:
                                                                                        if alcohol<10.2:
                                                                                            return 1
                                                                                        else: 
                                                                                            return 1
                                                                                    else: 
                                                                                        return 1
                                                                                else: 
                                                                                    if pH<3.47:
                                                                                        return 1
                                                                                    else: 
                                                                                        return 1
                                                                            else: 
                                                                                if sulphates<0.6:
                                                                                    if sulphates<0.57:
                                                                                        return 1
                                                                                    else: 
                                                                                        return 1
                                                                                else: 
                                                                                    return 1
                                                                        else: 
                                                                            return 1
                                                                    else: 
                                                                        if sulphates<0.59:
                                                                            return 1
                                                                        else: 
                                                                            return 1
                                                                else: 
                                                                    if sulphates<0.62:
                                                                        return 1
                                                                    else: 
                                                                        return 1
                                                            else: 
                                                                if sulphates<0.61:
                                                                    return 1
                                                                else: 
                                                                    return 1
                                                        else: 
                                                            return 1
                                                    else: 
                                                        return 1
                                                else: 
                                                    if sulphates<0.62:
                                                        return 1
                                                    else: 
                                                        return 1
                                            else: 
                                                if sulphates<0.6:
                                                    return 1
                                                else: 
                                                    return 1
                                        else: 
                                            if alcohol<10.5:
                                                return 1
                                            else: 
                                                return -1
                                else: 
                                    if density<0.99648:
                                        if alcohol<10.7:
                                            if alcohol<10.6:
                                                if alcohol<10.4:
                                                    return -1
                                                else: 
                                                    return -1
                                            else: 
                                                return -1
                                        else: 
                                            return -1
                                    else: 
                                        if alcohol<11.1:
                                            return 1
                                        else: 
                                            return 1
                            else: 
                                if total_sulfur_dioxide<58:
                                    if pH<3.39:
                                        if total_sulfur_dioxide<42:
                                            if free_sulfur_dioxide<13:
                                                if pH<3.22:
                                                    if alcohol<10.9:
                                                        return 1
                                                    else: 
                                                        return 1
                                                else: 
                                                    if alcohol<10:
                                                        return 1
                                                    else: 
                                                        if alcohol<11.2:
                                                            if alcohol<11:
                                                                if alcohol<10.9:
                                                                    if alcohol<10.3:
                                                                        return -1
                                                                    else: 
                                                                        return -1
                                                                else: 
                                                                    return -1
                                                            else: 
                                                                return -1
                                                        else: 
                                                            return -1
                                            else: 
                                                if alcohol<11.3:
                                                    if alcohol<10.8:
                                                        if alcohol<10.7:
                                                            return 1
                                                        else: 
                                                            return 1
                                                    else: 
                                                        return 1
                                                else: 
                                                    return 1
                                        else: 
                                            if alcohol<10.8:
                                                if alcohol<10.5:
                                                    if alcohol<10.4:
                                                        if alcohol<10.3:
                                                            if sulphates<0.59:
                                                                return -1
                                                            else: 
                                                                return -1
                                                        else: 
                                                            return -1
                                                    else: 
                                                        return -1
                                                else: 
                                                    return -1
                                            else: 
                                                return -1
                                    else: 
                                        if pH<3.46:
                                            if alcohol<10.7:
                                                if alcohol<10.2:
                                                    if alcohol<10.1:
                                                        if sulphates<0.63:
                                                            return 1
                                                        else: 
                                                            return 1
                                                    else: 
                                                        return 1
                                                else: 
                                                    return 1
                                            else: 
                                                return 1
                                        else: 
                                            return -1
                                else: 
                                    if alcohol<10.5:
                                        if alcohol<10.2:
                                            if sulphates<0.61:
                                                return 1
                                            else: 
                                                return 1
                                        else: 
                                            if pH<3.26:
                                                return 1
                                            else: 
                                                return 1
                                    else: 
                                        return 1
                    else: 
                        if total_sulfur_dioxide<55:
                            if chlorides<0.122:
                                if pH<3.69:
                                    if chlorides<0.082:
                                        if pH<3.02:
                                            if alcohol<10.2:
                                                return 1
                                            else: 
                                                return -1
                                        else: 
                                            if volatile_acidity<0.19:
                                                if alcohol<11.2:
                                                    return -1
                                                else: 
                                                    return 1
                                            else: 
                                                if chlorides<0.056:
                                                    if chlorides<0.055:
                                                        if alcohol<11.4:
                                                            if alcohol<11:
                                                                if alcohol<10.9:
                                                                    if alcohol<10.8:
                                                                        if alcohol<10.6:
                                                                            return 1
                                                                        else: 
                                                                            return 1
                                                                    else: 
                                                                        if sulphates<0.81:
                                                                            return 1
                                                                        else: 
                                                                            return 1
                                                                else: 
                                                                    if sulphates<0.83:
                                                                        return 1
                                                                    else: 
                                                                        return 1
                                                            else: 
                                                                return 1
                                                        else: 
                                                            return 1
                                                    else: 
                                                        return -1
                                                else: 
                                                    if chlorides<0.065:
                                                        if citric_acid<0.55:
                                                            if density<0.9984:
                                                                if alcohol<11.3:
                                                                    if alcohol<11.2:
                                                                        if alcohol<11.1:
                                                                            if alcohol<11:
                                                                                if alcohol<10.9:
                                                                                    if alcohol<10.8:
                                                                                        if alcohol<10.7:
                                                                                            if alcohol<10.6:
                                                                                                if alcohol<10.5:
                                                                                                    if alcohol<10.3:
                                                                                                        if alcohol<10.1:
                                                                                                            if alcohol<10:
                                                                                                                return 1
                                                                                                            else: 
                                                                                                                if sulphates<1.1:
                                                                                                                    if sulphates<0.66:
                                                                                                                        return 1
                                                                                                                    else: 
                                                                                                                        return 1
                                                                                                                else: 
                                                                                                                    return 1
                                                                                                        else: 
                                                                                                            if sulphates<0.76:
                                                                                                                return 1
                                                                                                            else: 
                                                                                                                return 1
                                                                                                    else: 
                                                                                                        if sulphates<0.83:
                                                                                                            return 1
                                                                                                        else: 
                                                                                                            return 1
                                                                                                else: 
                                                                                                    if sulphates<0.74:
                                                                                                        return 1
                                                                                                    else: 
                                                                                                        return 1
                                                                                            else: 
                                                                                                return 1
                                                                                        else: 
                                                                                            return 1
                                                                                    else: 
                                                                                        return 1
                                                                                else: 
                                                                                    if sulphates<0.94:
                                                                                        return 1
                                                                                    else: 
                                                                                        return 1
                                                                            else: 
                                                                                return 1
                                                                        else: 
                                                                            if sulphates<0.89:
                                                                                return 1
                                                                            else: 
                                                                                return 1
                                                                    else: 
                                                                        if sulphates<0.8:
                                                                            if sulphates<0.76:
                                                                                if sulphates<0.69:
                                                                                    return 1
                                                                                else: 
                                                                                    return 1
                                                                            else: 
                                                                                return 1
                                                                        else: 
                                                                            return 1
                                                                else: 
                                                                    if sulphates<0.76:
                                                                        if sulphates<0.73:
                                                                            return 1
                                                                        else: 
                                                                            return 1
                                                                    else: 
                                                                        return 1
                                                            else: 
                                                                if sulphates<0.73:
                                                                    return -1
                                                                else: 
                                                                    if alcohol<11:
                                                                        return 1
                                                                    else: 
                                                                        return 1
                                                        else: 
                                                            if alcohol<10.6:
                                                                return 1
                                                            else: 
                                                                return -1
                                                    else: 
                                                        if alcohol<11.4:
                                                            if alcohol<11.3:
                                                                if alcohol<11.2:
                                                                    if alcohol<11.1:
                                                                        if alcohol<11:
                                                                            if alcohol<10.9:
                                                                                if alcohol<10.8:
                                                                                    if alcohol<10.7:
                                                                                        if alcohol<10.6:
                                                                                            if alcohol<10.55:
                                                                                                if alcohol<10.5:
                                                                                                    if alcohol<10.4:
                                                                                                        if alcohol<10.3:
                                                                                                            if alcohol<10.2:
                                                                                                                if alcohol<10.1:
                                                                                                                    if alcohol<10:
                                                                                                                        if sulphates<0.89:
                                                                                                                            if pH<3.47:
                                                                                                                                return 1
                                                                                                                            else: 
                                                                                                                                return 1
                                                                                                                        else: 
                                                                                                                            return 1
                                                                                                                    else: 
                                                                                                                        if sulphates<0.82:
                                                                                                                            if sulphates<0.78:
                                                                                                                                if sulphates<0.7:
                                                                                                                                    return 1
                                                                                                                                else: 
                                                                                                                                    return 1
                                                                                                                            else: 
                                                                                                                                return 1
                                                                                                                        else: 
                                                                                                                            return 1
                                                                                                                else: 
                                                                                                                    return 1
                                                                                                            else: 
                                                                                                                if sulphates<0.75:
                                                                                                                    return 1
                                                                                                                else: 
                                                                                                                    if pH<3.34:
                                                                                                                        return 1
                                                                                                                    else: 
                                                                                                                        return 1
                                                                                                        else: 
                                                                                                            if sulphates<0.87:
                                                                                                                if sulphates<0.76:
                                                                                                                    return 1
                                                                                                                else: 
                                                                                                                    return 1
                                                                                                            else: 
                                                                                                                return 1
                                                                                                    else: 
                                                                                                        if sulphates<0.81:
                                                                                                            return 1
                                                                                                        else: 
                                                                                                            return 1
                                                                                                else: 
                                                                                                    if sulphates<0.86:
                                                                                                        if sulphates<0.75:
                                                                                                            return 1
                                                                                                        else: 
                                                                                                            return 1
                                                                                                    else: 
                                                                                                        return 1
                                                                                            else: 
                                                                                                return 1
                                                                                        else: 
                                                                                            if sulphates<1.16:
                                                                                                if sulphates<1.04:
                                                                                                    if sulphates<0.81:
                                                                                                        return 1
                                                                                                    else: 
                                                                                                        return 1
                                                                                                else: 
                                                                                                    return 1
                                                                                            else: 
                                                                                                return 1
                                                                                    else: 
                                                                                        return 1
                                                                                else: 
                                                                                    if sulphates<0.78:
                                                                                        return 1
                                                                                    else: 
                                                                                        return 1
                                                                            else: 
                                                                                if sulphates<0.87:
                                                                                    if sulphates<0.81:
                                                                                        if sulphates<0.78:
                                                                                            if sulphates<0.69:
                                                                                                if sulphates<0.68:
                                                                                                    if sulphates<0.66:
                                                                                                        return 1
                                                                                                    else: 
                                                                                                        return 1
                                                                                                else: 
                                                                                                    return 1
                                                                                            else: 
                                                                                                return 1
                                                                                        else: 
                                                                                            return 1
                                                                                    else: 
                                                                                        return 1
                                                                                else: 
                                                                                    return 1
                                                                        else: 
                                                                            if sulphates<1.11:
                                                                                if sulphates<0.91:
                                                                                    if sulphates<0.9:
                                                                                        if sulphates<0.86:
                                                                                            if sulphates<0.85:
                                                                                                if sulphates<0.81:
                                                                                                    if sulphates<0.75:
                                                                                                        if sulphates<0.69:
                                                                                                            if sulphates<0.66:
                                                                                                                return 1
                                                                                                            else: 
                                                                                                                return 1
                                                                                                        else: 
                                                                                                            return 1
                                                                                                    else: 
                                                                                                        return 1
                                                                                                else: 
                                                                                                    return 1
                                                                                            else: 
                                                                                                return 1
                                                                                        else: 
                                                                                            return 1
                                                                                    else: 
                                                                                        return 1
                                                                                else: 
                                                                                    return 1
                                                                            else: 
                                                                                return 1
                                                                    else: 
                                                                        if sulphates<0.79:
                                                                            if sulphates<0.77:
                                                                                return 1
                                                                            else: 
                                                                                return 1
                                                                        else: 
                                                                            if pH<3.38:
                                                                                return 1
                                                                            else: 
                                                                                return 1
                                                                else: 
                                                                    if sulphates<0.84:
                                                                        if sulphates<0.83:
                                                                            if sulphates<0.82:
                                                                                return 1
                                                                            else: 
                                                                                return 1
                                                                        else: 
                                                                            return 1
                                                                    else: 
                                                                        return 1
                                                            else: 
                                                                if sulphates<0.83:
                                                                    if sulphates<0.78:
                                                                        return 1
                                                                    else: 
                                                                        return 1
                                                                else: 
                                                                    return 1
                                                        else: 
                                                            if sulphates<0.87:
                                                                if sulphates<0.76:
                                                                    if sulphates<0.73:
                                                                        if sulphates<0.71:
                                                                            return 1
                                                                        else: 
                                                                            return 1
                                                                    else: 
                                                                        return 1
                                                                else: 
                                                                    return 1
                                                            else: 
                                                                return 1
                                    else: 
                                        if pH<3.49:
                                            if sulphates<0.72:
                                                if citric_acid<0.33:
                                                    if alcohol<11.3:
                                                        if alcohol<11.2:
                                                            if alcohol<10.6:
                                                                if alcohol<10.3:
                                                                    return 1
                                                                else: 
                                                                    if sulphates<0.7:
                                                                        return 1
                                                                    else: 
                                                                        return 1
                                                            else: 
                                                                return 1
                                                        else: 
                                                            return 1
                                                    else: 
                                                        return 1
                                                else: 
                                                    if pH<3.24:
                                                        if pH<3.04:
                                                            return -1
                                                        else: 
                                                            if alcohol<11.4:
                                                                if alcohol<11.2:
                                                                    if alcohol<11:
                                                                        if alcohol<10.6:
                                                                            if alcohol<10.03333333:
                                                                                return 1
                                                                            else: 
                                                                                return 1
                                                                        else: 
                                                                            return 1
                                                                    else: 
                                                                        return 1
                                                                else: 
                                                                    return 1
                                                            else: 
                                                                return 1
                                                    else: 
                                                        if alcohol<10.8:
                                                            if alcohol<10.6:
                                                                return -1
                                                            else: 
                                                                return -1
                                                        else: 
                                                            return -1
                                            else: 
                                                if alcohol<11.3:
                                                    if alcohol<11.2:
                                                        if alcohol<11.1:
                                                            if alcohol<11:
                                                                if alcohol<10.8:
                                                                    if alcohol<10.6:
                                                                        if alcohol<10.5:
                                                                            if alcohol<10.4:
                                                                                if alcohol<10.1:
                                                                                    if alcohol<10:
                                                                                        if sulphates<0.91:
                                                                                            return 1
                                                                                        else: 
                                                                                            return 1
                                                                                    else: 
                                                                                        if sulphates<0.9:
                                                                                            if sulphates<0.8:
                                                                                                if sulphates<0.74:
                                                                                                    return 1
                                                                                                else: 
                                                                                                    return 1
                                                                                            else: 
                                                                                                return 1
                                                                                        else: 
                                                                                            return 1
                                                                                else: 
                                                                                    return 1
                                                                            else: 
                                                                                if sulphates<0.85:
                                                                                    return 1
                                                                                else: 
                                                                                    return 1
                                                                        else: 
                                                                            if sulphates<0.8:
                                                                                return 1
                                                                            else: 
                                                                                return 1
                                                                    else: 
                                                                        if sulphates<1.02:
                                                                            return 1
                                                                        else: 
                                                                            return 1
                                                                else: 
                                                                    return 1
                                                            else: 
                                                                return 1
                                                        else: 
                                                            return 1
                                                    else: 
                                                        return 1
                                                else: 
                                                    return 1
                                        else: 
                                            if alcohol<10.5:
                                                return -1
                                            else: 
                                                if sulphates<0.68:
                                                    return -1
                                                else: 
                                                    return -1
                                else: 
                                    return -1
                            else: 
                                if sulphates<0.79:
                                    if alcohol<11.2:
                                        if alcohol<10.5:
                                            return -1
                                        else: 
                                            return -1
                                    else: 
                                        return -1
                                else: 
                                    if pH<3.38:
                                        if alcohol<10.7:
                                            return 1
                                        else: 
                                            return 1
                                    else: 
                                        return -1
                        else: 
                            if residual_sugar<5.5:
                                if sulphates<0.67:
                                    if alcohol<11.2:
                                        if alcohol<10.3:
                                            return -1
                                        else: 
                                            return -1
                                    else: 
                                        return -1
                                else: 
                                    if citric_acid<0.57:
                                        if fixed_acidity<7.5:
                                            if volatile_acidity<0.38:
                                                if alcohol<11:
                                                    return -1
                                                else: 
                                                    if sulphates<0.78:
                                                        return -1
                                                    else: 
                                                        return -1
                                            else: 
                                                if fixed_acidity<7.2:
                                                    if alcohol<11.4:
                                                        if alcohol<11:
                                                            if alcohol<10.5:
                                                                return 1
                                                            else: 
                                                                return 1
                                                        else: 
                                                            return 1
                                                    else: 
                                                        if sulphates<0.77:
                                                            return 1
                                                        else: 
                                                            return 1
                                                else: 
                                                    if alcohol<11:
                                                        return -1
                                                    else: 
                                                        return -1
                                        else: 
                                            if chlorides<0.111:
                                                if chlorides<0.06:
                                                    return -1
                                                else: 
                                                    if density<1.0001:
                                                        if alcohol<11.4:
                                                            if alcohol<11:
                                                                if alcohol<10.9:
                                                                    if alcohol<10.8:
                                                                        if alcohol<10.7:
                                                                            if alcohol<10.5:
                                                                                if alcohol<10.3:
                                                                                    if alcohol<10.2:
                                                                                        if alcohol<10.1:
                                                                                            if alcohol<10:
                                                                                                return 1
                                                                                            else: 
                                                                                                return 1
                                                                                        else: 
                                                                                            return 1
                                                                                    else: 
                                                                                        if sulphates<0.9:
                                                                                            return 1
                                                                                        else: 
                                                                                            return 1
                                                                                else: 
                                                                                    return 1
                                                                            else: 
                                                                                if sulphates<0.75:
                                                                                    return 1
                                                                                else: 
                                                                                    return 1
                                                                        else: 
                                                                            return 1
                                                                    else: 
                                                                        return 1
                                                                else: 
                                                                    if sulphates<0.75:
                                                                        return 1
                                                                    else: 
                                                                        return 1
                                                            else: 
                                                                if sulphates<0.87:
                                                                    if sulphates<0.85:
                                                                        if sulphates<0.82:
                                                                            return 1
                                                                        else: 
                                                                            return 1
                                                                    else: 
                                                                        return 1
                                                                else: 
                                                                    return 1
                                                        else: 
                                                            return 1
                                                    else: 
                                                        if alcohol<11:
                                                            if alcohol<10.8:
                                                                return 1
                                                            else: 
                                                                return 1
                                                        else: 
                                                            return -1
                                            else: 
                                                if pH<3.23:
                                                    if alcohol<10.9:
                                                        return -1
                                                    else: 
                                                        return -1
                                                else: 
                                                    return 1
                                    else: 
                                        if alcohol<10.7:
                                            return -1
                                        else: 
                                            return -1
                            else: 
                                if sulphates<0.83:
                                    if sulphates<0.8:
                                        if sulphates<0.76:
                                            if sulphates<0.72:
                                                return -1
                                            else: 
                                                return -1
                                        else: 
                                            return -1
                                    else: 
                                        return -1
                                else: 
                                    return -1
                else: 
                    if citric_acid<0.19:
                        if pH<3.44:
                            if free_sulfur_dioxide<8:
                                if sulphates<0.69:
                                    if alcohol<11:
                                        if alcohol<10.9:
                                            if alcohol<10.4:
                                                return -1
                                            else: 
                                                return -1
                                        else: 
                                            return -1
                                    else: 
                                        return -1
                                else: 
                                    if sulphates<0.7:
                                        return 1
                                    else: 
                                        return 1
                            else: 
                                if free_sulfur_dioxide<48:
                                    if citric_acid<0.14:
                                        if alcohol<11.3:
                                            if alcohol<11.1:
                                                if alcohol<10.9:
                                                    if alcohol<10.75:
                                                        if alcohol<10.7:
                                                            if alcohol<10.5:
                                                                if alcohol<10.4:
                                                                    if alcohol<10.2:
                                                                        if alcohol<10:
                                                                            return 1
                                                                        else: 
                                                                            return 1
                                                                    else: 
                                                                        return 1
                                                                else: 
                                                                    if sulphates<0.64:
                                                                        if sulphates<0.62:
                                                                            return 1
                                                                        else: 
                                                                            return 1
                                                                    else: 
                                                                        return 1
                                                            else: 
                                                                return 1
                                                        else: 
                                                            return 1
                                                    else: 
                                                        return 1
                                                else: 
                                                    if sulphates<0.82:
                                                        return 1
                                                    else: 
                                                        return 1
                                            else: 
                                                if sulphates<0.72:
                                                    return 1
                                                else: 
                                                    if pH<3.43:
                                                        return 1
                                                    else: 
                                                        return 1
                                        else: 
                                            return 1
                                    else: 
                                        if sulphates<0.67:
                                            return -1
                                        else: 
                                            if alcohol<11.3:
                                                return 1
                                            else: 
                                                return 1
                                else: 
                                    return -1
                        else: 
                            if volatile_acidity<0.91:
                                if alcohol<10.8:
                                    if fixed_acidity<6.9:
                                        if alcohol<10.7:
                                            if alcohol<10.3:
                                                if alcohol<10.2:
                                                    if alcohol<9.95:
                                                        return -1
                                                    else: 
                                                        return -1
                                                else: 
                                                    if sulphates<0.72:
                                                        if sulphates<0.71:
                                                            return -1
                                                        else: 
                                                            return -1
                                                    else: 
                                                        return -1
                                            else: 
                                                return -1
                                        else: 
                                            if sulphates<0.58:
                                                return -1
                                            else: 
                                                return -1
                                    else: 
                                        if density<0.9994:
                                            if alcohol<10.6:
                                                if sulphates<0.96:
                                                    return 1
                                                else: 
                                                    return 1
                                            else: 
                                                return 1
                                        else: 
                                            return -1
                                else: 
                                    if alcohol<11.4:
                                        if alcohol<11.3:
                                            if alcohol<11:
                                                if alcohol<10.9:
                                                    if sulphates<0.66:
                                                        return 1
                                                    else: 
                                                        return 1
                                                else: 
                                                    return 1
                                            else: 
                                                return 1
                                        else: 
                                            return 1
                                    else: 
                                        return 1
                            else: 
                                if alcohol<11.4:
                                    if alcohol<11.2:
                                        if alcohol<11:
                                            if alcohol<10.9:
                                                return -1
                                            else: 
                                                return -1
                                        else: 
                                            return -1
                                    else: 
                                        return -1
                                else: 
                                    return -1
                    else: 
                        if density<0.99815:
                            if total_sulfur_dioxide<15:
                                return 1
                            else: 
                                if residual_sugar<2.8:
                                    if alcohol<11.3:
                                        if alcohol<11:
                                            if alcohol<10.9:
                                                if alcohol<10.3:
                                                    if alcohol<10.2:
                                                        if alcohol<10.1:
                                                            if alcohol<10:
                                                                return -1
                                                            else: 
                                                                if sulphates<0.94:
                                                                    if sulphates<0.67:
                                                                        return -1
                                                                    else: 
                                                                        return -1
                                                                else: 
                                                                    return -1
                                                        else: 
                                                            if sulphates<0.66:
                                                                return -1
                                                            else: 
                                                                return -1
                                                    else: 
                                                        return -1
                                                else: 
                                                    return -1
                                            else: 
                                                return -1
                                        else: 
                                            if sulphates<0.61:
                                                if sulphates<0.58:
                                                    return -1
                                                else: 
                                                    return -1
                                            else: 
                                                return -1
                                    else: 
                                        return -1
                                else: 
                                    if alcohol<10.3:
                                        return 1
                                    else: 
                                        return -1
                        else: 
                            if chlorides<0.087:
                                if alcohol<11:
                                    if alcohol<10.6:
                                        if alcohol<10.1:
                                            return 1
                                        else: 
                                            return 1
                                    else: 
                                        return 1
                                else: 
                                    return 1
                            else: 
                                if chlorides<0.107:
                                    if density<1.0032:
                                        if alcohol<11.3:
                                            if alcohol<11.2:
                                                if alcohol<11.1:
                                                    if alcohol<10.2:
                                                        return -1
                                                    else: 
                                                        return -1
                                                else: 
                                                    if fixed_acidity<15.6:
                                                        return -1
                                                    else: 
                                                        return -1
                                            else: 
                                                return -1
                                        else: 
                                            return -1
                                    else: 
                                        return 1
                                else: 
                                    if alcohol<10.4:
                                        return 1
                                    else: 
                                        return 1
            else: 
                if fixed_acidity<13.5:
                    if volatile_acidity<1.04:
                        if fixed_acidity<6.6:
                            if total_sulfur_dioxide<27:
                                if pH<3.67:
                                    if density<0.99256:
                                        return 1
                                    else: 
                                        if alcohol<12.9:
                                            if alcohol<12:
                                                if alcohol<11.8:
                                                    return -1
                                                else: 
                                                    return -1
                                            else: 
                                                return -1
                                        else: 
                                            return -1
                                else: 
                                    if alcohol<12.8:
                                        return 1
                                    else: 
                                        return 1
                            else: 
                                if total_sulfur_dioxide<99:
                                    if alcohol<14:
                                        if alcohol<13:
                                            if alcohol<12.9:
                                                if alcohol<12.8:
                                                    if alcohol<12.5:
                                                        if alcohol<12.4:
                                                            if alcohol<11.9:
                                                                if alcohol<11.7:
                                                                    if alcohol<11.6:
                                                                        if sulphates<0.7:
                                                                            return 1
                                                                        else: 
                                                                            return 1
                                                                    else: 
                                                                        if sulphates<0.82:
                                                                            return 1
                                                                        else: 
                                                                            return 1
                                                                else: 
                                                                    return 1
                                                            else: 
                                                                return 1
                                                        else: 
                                                            return 1
                                                    else: 
                                                        if sulphates<0.84:
                                                            if sulphates<0.65:
                                                                if sulphates<0.61:
                                                                    if pH<4.01:
                                                                        return 1
                                                                    else: 
                                                                        if fixed_acidity<5.4:
                                                                            return 1
                                                                        else: 
                                                                            return 1
                                                                else: 
                                                                    return 1
                                                            else: 
                                                                return 1
                                                        else: 
                                                            return 1
                                                else: 
                                                    if sulphates<0.62:
                                                        return 1
                                                    else: 
                                                        return 1
                                            else: 
                                                if sulphates<0.94:
                                                    return 1
                                                else: 
                                                    return 1
                                        else: 
                                            return 1
                                    else: 
                                        if sulphates<0.82:
                                            if sulphates<0.75:
                                                if pH<3.72:
                                                    return 1
                                                else: 
                                                    return 1
                                            else: 
                                                return 1
                                        else: 
                                            return 1
                                else: 
                                    if alcohol<13:
                                        if alcohol<12.9:
                                            return 1
                                        else: 
                                            if sulphates<0.87:
                                                return 1
                                            else: 
                                                return 1
                                    else: 
                                        return -1
                        else: 
                            if citric_acid<0.68:
                                if residual_sugar<4.5:
                                    if chlorides<0.058:
                                        if chlorides<0.056:
                                            if alcohol<13.4:
                                                if alcohol<13.3:
                                                    if alcohol<12.8:
                                                        if alcohol<12.7:
                                                            if alcohol<12.5:
                                                                if alcohol<12.4:
                                                                    if alcohol<12.1:
                                                                        if alcohol<11.9:
                                                                            if alcohol<11.7:
                                                                                return 1
                                                                            else: 
                                                                                return 1
                                                                        else: 
                                                                            if sulphates<0.82:
                                                                                return 1
                                                                            else: 
                                                                                return 1
                                                                    else: 
                                                                        if sulphates<0.71:
                                                                            return 1
                                                                        else: 
                                                                            return 1
                                                                else: 
                                                                    if sulphates<1.01:
                                                                        return 1
                                                                    else: 
                                                                        return 1
                                                            else: 
                                                                return 1
                                                        else: 
                                                            return 1
                                                    else: 
                                                        return 1
                                                else: 
                                                    return 1
                                            else: 
                                                return 1
                                        else: 
                                            return -1
                                    else: 
                                        if alcohol<14:
                                            if alcohol<13.2:
                                                if alcohol<13.1:
                                                    if alcohol<12.9:
                                                        if alcohol<12.8:
                                                            if alcohol<12.7:
                                                                if alcohol<12.5:
                                                                    if alcohol<12.4:
                                                                        if alcohol<12.3:
                                                                            if alcohol<12.2:
                                                                                if alcohol<12.1:
                                                                                    if alcohol<12:
                                                                                        if alcohol<11.9:
                                                                                            if alcohol<11.8:
                                                                                                if alcohol<11.7:
                                                                                                    if alcohol<11.6:
                                                                                                        if sulphates<1:
                                                                                                            if sulphates<0.84:
                                                                                                                if sulphates<0.77:
                                                                                                                    if sulphates<0.72:
                                                                                                                        if sulphates<0.71:
                                                                                                                            if sulphates<0.68:
                                                                                                                                if sulphates<0.62:
                                                                                                                                    if sulphates<0.59:
                                                                                                                                        return 1
                                                                                                                                    else: 
                                                                                                                                        return 1
                                                                                                                                else: 
                                                                                                                                    return 1
                                                                                                                            else: 
                                                                                                                                return 1
                                                                                                                        else: 
                                                                                                                            return 1
                                                                                                                    else: 
                                                                                                                        if pH<3.44:
                                                                                                                            return 1
                                                                                                                        else: 
                                                                                                                            return 1
                                                                                                                else: 
                                                                                                                    return 1
                                                                                                            else: 
                                                                                                                return 1
                                                                                                        else: 
                                                                                                            return 1
                                                                                                    else: 
                                                                                                        if sulphates<1.03:
                                                                                                            if sulphates<0.8:
                                                                                                                if sulphates<0.76:
                                                                                                                    if sulphates<0.74:
                                                                                                                        return 1
                                                                                                                    else: 
                                                                                                                        return 1
                                                                                                                else: 
                                                                                                                    return 1
                                                                                                            else: 
                                                                                                                return 1
                                                                                                        else: 
                                                                                                            return 1
                                                                                                else: 
                                                                                                    if sulphates<0.85:
                                                                                                        if sulphates<0.84:
                                                                                                            if sulphates<0.75:
                                                                                                                if sulphates<0.74:
                                                                                                                    if sulphates<0.71:
                                                                                                                        if sulphates<0.69:
                                                                                                                            if sulphates<0.66:
                                                                                                                                return 1
                                                                                                                            else: 
                                                                                                                                return 1
                                                                                                                        else: 
                                                                                                                            return 1
                                                                                                                    else: 
                                                                                                                        return 1
                                                                                                                else: 
                                                                                                                    return 1
                                                                                                            else: 
                                                                                                                return 1
                                                                                                        else: 
                                                                                                            if total_sulfur_dioxide<27:
                                                                                                                return 1
                                                                                                            else: 
                                                                                                                return 1
                                                                                                    else: 
                                                                                                        return 1
                                                                                            else: 
                                                                                                if sulphates<0.93:
                                                                                                    if sulphates<0.89:
                                                                                                        if sulphates<0.79:
                                                                                                            if sulphates<0.78:
                                                                                                                if sulphates<0.74:
                                                                                                                    if sulphates<0.72:
                                                                                                                        if sulphates<0.71:
                                                                                                                            if sulphates<0.66:
                                                                                                                                if sulphates<0.65:
                                                                                                                                    if sulphates<0.63:
                                                                                                                                        if pH<3.41:
                                                                                                                                            return 1
                                                                                                                                        else: 
                                                                                                                                            return 1
                                                                                                                                    else: 
                                                                                                                                        return 1
                                                                                                                                else: 
                                                                                                                                    return 1
                                                                                                                            else: 
                                                                                                                                return 1
                                                                                                                        else: 
                                                                                                                            return 1
                                                                                                                    else: 
                                                                                                                        return 1
                                                                                                                else: 
                                                                                                                    return 1
                                                                                                            else: 
                                                                                                                return 1
                                                                                                        else: 
                                                                                                            return 1
                                                                                                    else: 
                                                                                                        return 1
                                                                                                else: 
                                                                                                    return 1
                                                                                        else: 
                                                                                            if sulphates<0.76:
                                                                                                if sulphates<0.73:
                                                                                                    if sulphates<0.69:
                                                                                                        if sulphates<0.67:
                                                                                                            return 1
                                                                                                        else: 
                                                                                                            return 1
                                                                                                    else: 
                                                                                                        return 1
                                                                                                else: 
                                                                                                    return 1
                                                                                            else: 
                                                                                                return 1
                                                                                    else: 
                                                                                        if sulphates<1.13:
                                                                                            if sulphates<0.99:
                                                                                                if sulphates<0.86:
                                                                                                    if sulphates<0.78:
                                                                                                        if sulphates<0.77:
                                                                                                            if sulphates<0.76:
                                                                                                                if sulphates<0.73:
                                                                                                                    return 1
                                                                                                                else: 
                                                                                                                    return 1
                                                                                                            else: 
                                                                                                                return 1
                                                                                                        else: 
                                                                                                            return 1
                                                                                                    else: 
                                                                                                        return 1
                                                                                                else: 
                                                                                                    return 1
                                                                                            else: 
                                                                                                return 1
                                                                                        else: 
                                                                                            return 1
                                                                                else: 
                                                                                    if sulphates<0.96:
                                                                                        if sulphates<0.79:
                                                                                            if sulphates<0.77:
                                                                                                if sulphates<0.64:
                                                                                                    if sulphates<0.61:
                                                                                                        return 1
                                                                                                    else: 
                                                                                                        return 1
                                                                                                else: 
                                                                                                    return 1
                                                                                            else: 
                                                                                                if pH<3.35:
                                                                                                    return 1
                                                                                                else: 
                                                                                                    return 1
                                                                                        else: 
                                                                                            return 1
                                                                                    else: 
                                                                                        return 1
                                                                            else: 
                                                                                if pH<3.22:
                                                                                    return 1
                                                                                else: 
                                                                                    return 1
                                                                        else: 
                                                                            if sulphates<0.89:
                                                                                return 1
                                                                            else: 
                                                                                return 1
                                                                    else: 
                                                                        if sulphates<0.8:
                                                                            if sulphates<0.66:
                                                                                return 1
                                                                            else: 
                                                                                return 1
                                                                        else: 
                                                                            return 1
                                                                else: 
                                                                    if sulphates<0.81:
                                                                        if sulphates<0.78:
                                                                            if sulphates<0.69:
                                                                                return 1
                                                                            else: 
                                                                                return 1
                                                                        else: 
                                                                            return 1
                                                                    else: 
                                                                        return 1
                                                            else: 
                                                                return 1
                                                        else: 
                                                            if sulphates<0.78:
                                                                if sulphates<0.76:
                                                                    if sulphates<0.66:
                                                                        if sulphates<0.61:
                                                                            return 1
                                                                        else: 
                                                                            return 1
                                                                    else: 
                                                                        return 1
                                                                else: 
                                                                    return 1
                                                            else: 
                                                                return 1
                                                    else: 
                                                        return 1
                                                else: 
                                                    return 1
                                            else: 
                                                return 1
                                        else: 
                                            return 1
                                else: 
                                    if alcohol<11.6:
                                        return -1
                                    else: 
                                        if alcohol<13.4:
                                            if alcohol<12.6:
                                                if alcohol<12.5:
                                                    if alcohol<12.2:
                                                        if alcohol<12.1:
                                                            if alcohol<12:
                                                                if alcohol<11.7:
                                                                    return 1
                                                                else: 
                                                                    if sulphates<0.82:
                                                                        return 1
                                                                    else: 
                                                                        return 1
                                                            else: 
                                                                return 1
                                                        else: 
                                                            return 1
                                                    else: 
                                                        return 1
                                                else: 
                                                    return 1
                                            else: 
                                                if sulphates<0.82:
                                                    return 1
                                                else: 
                                                    return 1
                                        else: 
                                            return 1
                            else: 
                                if alcohol<12:
                                    return -1
                                else: 
                                    if alcohol<13.4:
                                        if alcohol<13:
                                            if alcohol<12.8:
                                                return 1
                                            else: 
                                                return 1
                                        else: 
                                            return 1
                                    else: 
                                        return 1
                    else: 
                        return -1
                else: 
                    if alcohol<14.9:
                        return -1
                    else: 
                        return -1
