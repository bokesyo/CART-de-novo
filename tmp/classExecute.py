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
    if alcohol<10.4:
        if volatile_acidity<0.37:
            if sulphates<0.51:
                if alcohol<10.1:
                    if alcohol<9.5:
                        return -1
                    else: 
                        return -1
                else: 
                    return -1
            else: 
                if citric_acid<0.59:
                    if sulphates<0.66:
                        if chlorides<0.077:
                            if sulphates<0.54:
                                return 1
                            else: 
                                if alcohol<10.1:
                                    return -1
                                else: 
                                    if sulphates<0.62:
                                        return -1
                                    else: 
                                        return -1
                        else: 
                            if alcohol<10.3:
                                if alcohol<10.1:
                                    return 1
                                else: 
                                    if sulphates<0.6:
                                        return 1
                                    else: 
                                        return 1
                            else: 
                                return 1
                    else: 
                        if total_sulfur_dioxide<20:
                            if pH<3.28:
                                if alcohol<9.9:
                                    return 1
                                else: 
                                    return 1
                            else: 
                                return -1
                        else: 
                            if alcohol<10.3:
                                if alcohol<10.2:
                                    if alcohol<10.1:
                                        if alcohol<10:
                                            if alcohol<9.9:
                                                if alcohol<9.8:
                                                    if alcohol<9.7:
                                                        if alcohol<9.4:
                                                            if alcohol<9.2:
                                                                return 1
                                                            else: 
                                                                if sulphates<1.18:
                                                                    if sulphates<1.08:
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
                                                        return 1
                                                else: 
                                                    if sulphates<1.36:
                                                        return 1
                                                    else: 
                                                        return 1
                                            else: 
                                                return 1
                                        else: 
                                            if sulphates<0.9:
                                                if sulphates<0.82:
                                                    return 1
                                                else: 
                                                    return 1
                                            else: 
                                                return 1
                                    else: 
                                        if sulphates<0.97:
                                            if sulphates<0.76:
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
                    if alcohol<9.6:
                        if sulphates<1.06:
                            return -1
                        else: 
                            return -1
                    else: 
                        return -1
        else: 
            if sulphates<0.7:
                if total_sulfur_dioxide<99:
                    if volatile_acidity<0.655:
                        if volatile_acidity<0.52:
                            if chlorides<0.213:
                                if sulphates<0.68:
                                    if density<0.9968:
                                        if pH<3.47:
                                            if fixed_acidity<8:
                                                if alcohol<10:
                                                    if alcohol<9.7:
                                                        if alcohol<9.6:
                                                            if alcohol<9.5:
                                                                if alcohol<9.4:
                                                                    return -1
                                                                else: 
                                                                    if sulphates<0.58:
                                                                        return -1
                                                                    else: 
                                                                        return -1
                                                            else: 
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
                                                if alcohol<10.3:
                                                    if alcohol<10.2:
                                                        return 1
                                                    else: 
                                                        return 1
                                                else: 
                                                    return -1
                                        else: 
                                            if sulphates<0.6:
                                                return 1
                                            else: 
                                                return 1
                                    else: 
                                        if alcohol<10.3:
                                            if alcohol<10.2:
                                                if alcohol<10:
                                                    if alcohol<9.8:
                                                        if alcohol<9.7:
                                                            if alcohol<9.6:
                                                                if alcohol<9.5:
                                                                    if alcohol<9.4:
                                                                        if alcohol<9.2:
                                                                            if alcohol<9.1:
                                                                                if alcohol<9:
                                                                                    return -1
                                                                                else: 
                                                                                    if sulphates<0.61:
                                                                                        return -1
                                                                                    else: 
                                                                                        return -1
                                                                            else: 
                                                                                return -1
                                                                        else: 
                                                                            if sulphates<0.64:
                                                                                if sulphates<0.55:
                                                                                    return -1
                                                                                else: 
                                                                                    return -1
                                                                            else: 
                                                                                return -1
                                                                    else: 
                                                                        return -1
                                                                else: 
                                                                    if sulphates<0.64:
                                                                        if sulphates<0.61:
                                                                            if sulphates<0.55:
                                                                                return -1
                                                                            else: 
                                                                                return -1
                                                                        else: 
                                                                            return -1
                                                                    else: 
                                                                        if pH<3.4:
                                                                            return -1
                                                                        else: 
                                                                            return -1
                                                            else: 
                                                                return -1
                                                        else: 
                                                            return -1
                                                    else: 
                                                        if sulphates<0.65:
                                                            if sulphates<0.59:
                                                                if sulphates<0.58:
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
                                    return 1
                            else: 
                                if sulphates<0.63:
                                    return 1
                                else: 
                                    return 1
                        else: 
                            if sulphates<0.54:
                                if total_sulfur_dioxide<89:
                                    if chlorides<0.069:
                                        if sulphates<0.47:
                                            return 1
                                        else: 
                                            return 1
                                    else: 
                                        if density<0.997:
                                            if alcohol<10.3:
                                                if alcohol<9.9:
                                                    if alcohol<9.8:
                                                        if alcohol<9.5:
                                                            if alcohol<9.4:
                                                                if sulphates<0.51:
                                                                    if sulphates<0.48:
                                                                        if sulphates<0.47:
                                                                            return -1
                                                                        else: 
                                                                            return -1
                                                                    else: 
                                                                        return -1
                                                                else: 
                                                                    return -1
                                                            else: 
                                                                if sulphates<0.52:
                                                                    return -1
                                                                else: 
                                                                    return -1
                                                        else: 
                                                            return -1
                                                    else: 
                                                        if sulphates<0.53:
                                                            if sulphates<0.48:
                                                                return -1
                                                            else: 
                                                                return -1
                                                        else: 
                                                            if pH<3.3:
                                                                return -1
                                                            else: 
                                                                return -1
                                                else: 
                                                    return -1
                                            else: 
                                                return -1
                                        else: 
                                            if sulphates<0.5:
                                                if alcohol<9.6:
                                                    return -1
                                                else: 
                                                    return -1
                                            else: 
                                                if sulphates<0.53:
                                                    if alcohol<10:
                                                        return 1
                                                    else: 
                                                        return 1
                                                else: 
                                                    return -1
                                else: 
                                    if alcohol<9.7:
                                        return 1
                                    else: 
                                        return 1
                            else: 
                                if free_sulfur_dioxide<6:
                                    if alcohol<10.1:
                                        if alcohol<10:
                                            if alcohol<9.9:
                                                if alcohol<9.8:
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
                                    if volatile_acidity<0.55:
                                        if sulphates<0.59:
                                            if sulphates<0.57:
                                                return 1
                                            else: 
                                                return -1
                                        else: 
                                            if alcohol<10:
                                                if alcohol<9.4:
                                                    if alcohol<9.3:
                                                        return 1
                                                    else: 
                                                        if sulphates<0.6:
                                                            return 1
                                                        else: 
                                                            return 1
                                                else: 
                                                    return 1
                                            else: 
                                                if sulphates<0.64:
                                                    return 1
                                                else: 
                                                    return 1
                                    else: 
                                        if free_sulfur_dioxide<8:
                                            if alcohol<10.3:
                                                if alcohol<10.2:
                                                    if alcohol<10.1:
                                                        if alcohol<9.9:
                                                            if alcohol<9.7:
                                                                if alcohol<9.5:
                                                                    if sulphates<0.63:
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
                                            if alcohol<9.3:
                                                if sulphates<0.65:
                                                    if sulphates<0.63:
                                                        return -1
                                                    else: 
                                                        return -1
                                                else: 
                                                    return -1
                                            else: 
                                                if residual_sugar<2.9:
                                                    if pH<3.55:
                                                        if citric_acid<0.44:
                                                            if total_sulfur_dioxide<46:
                                                                if total_sulfur_dioxide<39:
                                                                    if residual_sugar<2:
                                                                        if alcohol<9.6:
                                                                            return -1
                                                                        else: 
                                                                            return -1
                                                                    else: 
                                                                        if alcohol<10.3:
                                                                            if alcohol<10:
                                                                                if alcohol<9.7:
                                                                                    if alcohol<9.5:
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
                                                                    if alcohol<10.1:
                                                                        if alcohol<9.5:
                                                                            return -1
                                                                        else: 
                                                                            return -1
                                                                    else: 
                                                                        return -1
                                                            else: 
                                                                if alcohol<10.3:
                                                                    if alcohol<10.1:
                                                                        if alcohol<9.8:
                                                                            if alcohol<9.6:
                                                                                if alcohol<9.5:
                                                                                    if sulphates<0.65:
                                                                                        return 1
                                                                                    else: 
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
                                                                        return 1
                                                                else: 
                                                                    return 1
                                                        else: 
                                                            if alcohol<9.7:
                                                                return -1
                                                            else: 
                                                                return -1
                                                    else: 
                                                        if sulphates<0.66:
                                                            return -1
                                                        else: 
                                                            return -1
                                                else: 
                                                    if alcohol<10.1:
                                                        if alcohol<9.7:
                                                            return -1
                                                        else: 
                                                            return -1
                                                    else: 
                                                        return -1
                    else: 
                        if alcohol<9.1:
                            if sulphates<0.6:
                                return 1
                            else: 
                                return 1
                        else: 
                            if total_sulfur_dioxide<98:
                                if free_sulfur_dioxide<42:
                                    if volatile_acidity<1.04:
                                        if chlorides<0.114:
                                            if density<0.99888:
                                                if total_sulfur_dioxide<81:
                                                    if alcohol<10.2:
                                                        if alcohol<10.1:
                                                            if alcohol<10:
                                                                if alcohol<9.95:
                                                                    if alcohol<9.9:
                                                                        if alcohol<9.8:
                                                                            if alcohol<9.7:
                                                                                if alcohol<9.6:
                                                                                    if alcohol<9.55:
                                                                                        if alcohol<9.5:
                                                                                            if alcohol<9.4:
                                                                                                if alcohol<9.3:
                                                                                                    if alcohol<9.2:
                                                                                                        return -1
                                                                                                    else: 
                                                                                                        if sulphates<0.56:
                                                                                                            if sulphates<0.54:
                                                                                                                if sulphates<0.53:
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
                                                                                                if sulphates<0.6:
                                                                                                    if sulphates<0.54:
                                                                                                        if sulphates<0.53:
                                                                                                            return -1
                                                                                                        else: 
                                                                                                            return -1
                                                                                                    else: 
                                                                                                        return -1
                                                                                                else: 
                                                                                                    if pH<3.41:
                                                                                                        return -1
                                                                                                    else: 
                                                                                                        return -1
                                                                                        else: 
                                                                                            if sulphates<0.53:
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
                                                                                        return -1
                                                                                else: 
                                                                                    if sulphates<0.56:
                                                                                        if sulphates<0.54:
                                                                                            if sulphates<0.53:
                                                                                                if sulphates<0.51:
                                                                                                    return -1
                                                                                                else: 
                                                                                                    return -1
                                                                                            else: 
                                                                                                return -1
                                                                                        else: 
                                                                                            return -1
                                                                                    else: 
                                                                                        if pH<3.48:
                                                                                            return -1
                                                                                        else: 
                                                                                            return -1
                                                                            else: 
                                                                                if sulphates<0.6:
                                                                                    return -1
                                                                                else: 
                                                                                    return -1
                                                                        else: 
                                                                            if sulphates<0.68:
                                                                                if sulphates<0.65:
                                                                                    if sulphates<0.58:
                                                                                        if sulphates<0.57:
                                                                                            if sulphates<0.51:
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
                                                                        if sulphates<0.68:
                                                                            if sulphates<0.59:
                                                                                if sulphates<0.52:
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
                                                                if sulphates<0.62:
                                                                    if sulphates<0.48:
                                                                        if sulphates<0.47:
                                                                            return -1
                                                                        else: 
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
                                                            if sulphates<0.63:
                                                                if sulphates<0.54:
                                                                    return -1
                                                                else: 
                                                                    return -1
                                                            else: 
                                                                return -1
                                                    else: 
                                                        if sulphates<0.67:
                                                            if sulphates<0.58:
                                                                return -1
                                                            else: 
                                                                return -1
                                                        else: 
                                                            return -1
                                                else: 
                                                    if total_sulfur_dioxide<85:
                                                        return 1
                                                    else: 
                                                        if alcohol<10.1:
                                                            return -1
                                                        else: 
                                                            return -1
                                            else: 
                                                if density<0.99892:
                                                    return 1
                                                else: 
                                                    if alcohol<9.8:
                                                        return -1
                                                    else: 
                                                        return -1
                                        else: 
                                            if alcohol<10.3:
                                                return 1
                                            else: 
                                                return -1
                                    else: 
                                        return 1
                                else: 
                                    return 1
                            else: 
                                return 1
                else: 
                    if chlorides<0.069:
                        return 1
                    else: 
                        if alcohol<10.1:
                            if alcohol<9.9:
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
                                                        if sulphates<0.61:
                                                            if sulphates<0.58:
                                                                return -1
                                                            else: 
                                                                return -1
                                                        else: 
                                                            return -1
                                                else: 
                                                    if sulphates<0.69:
                                                        if sulphates<0.68:
                                                            if sulphates<0.59:
                                                                if sulphates<0.57:
                                                                    if sulphates<0.53:
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
                                                    if sulphates<0.62:
                                                        if sulphates<0.56:
                                                            if sulphates<0.55:
                                                                if sulphates<0.54:
                                                                    if sulphates<0.53:
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
                                            if sulphates<0.64:
                                                if sulphates<0.61:
                                                    if sulphates<0.6:
                                                        if sulphates<0.55:
                                                            if sulphates<0.54:
                                                                if pH<3.33:
                                                                    return -1
                                                                else: 
                                                                    return -1
                                                            else: 
                                                                if pH<3.33:
                                                                    return -1
                                                                else: 
                                                                    return -1
                                                        else: 
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
                                        if sulphates<0.59:
                                            if sulphates<0.57:
                                                return -1
                                            else: 
                                                return -1
                                        else: 
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
                                if sulphates<0.52:
                                    if sulphates<0.51:
                                        if sulphates<0.49:
                                            return -1
                                        else: 
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
                if alcohol<9.8:
                    if residual_sugar<2.6:
                        if total_sulfur_dioxide<45:
                            if sulphates<0.8:
                                if alcohol<9.6:
                                    return 1
                                else: 
                                    return 1
                            else: 
                                if total_sulfur_dioxide<44:
                                    if alcohol<9.6:
                                        if alcohol<9.5:
                                            if alcohol<9.4:
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
                            if sulphates<1.61:
                                if alcohol<9.7:
                                    if alcohol<9.6:
                                        if alcohol<9.5:
                                            if alcohol<9.4:
                                                if alcohol<9.3:
                                                    if alcohol<9.2:
                                                        if alcohol<9.1:
                                                            return -1
                                                        else: 
                                                            return -1
                                                    else: 
                                                        if sulphates<1.34:
                                                            return -1
                                                        else: 
                                                            return -1
                                                else: 
                                                    if sulphates<1.15:
                                                        if sulphates<1.09:
                                                            if sulphates<1.03:
                                                                return -1
                                                            else: 
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
                                            if sulphates<1.22:
                                                if sulphates<0.78:
                                                    return -1
                                                else: 
                                                    return -1
                                            else: 
                                                return -1
                                    else: 
                                        if sulphates<0.82:
                                            return -1
                                        else: 
                                            return -1
                                else: 
                                    return -1
                            else: 
                                return 1
                    else: 
                        if sulphates<1.07:
                            if alcohol<9.6:
                                if alcohol<9.4:
                                    if alcohol<9.25:
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
                    if free_sulfur_dioxide<32:
                        if chlorides<0.122:
                            if volatile_acidity<0.705:
                                if alcohol<10.3:
                                    if alcohol<10.2:
                                        if alcohol<10.1:
                                            if alcohol<10:
                                                if alcohol<9.9:
                                                    return 1
                                                else: 
                                                    if sulphates<1.95:
                                                        if sulphates<0.96:
                                                            return 1
                                                        else: 
                                                            return 1
                                                    else: 
                                                        return 1
                                            else: 
                                                if sulphates<0.8:
                                                    if sulphates<0.78:
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
                                    if sulphates<0.83:
                                        if sulphates<0.76:
                                            return 1
                                        else: 
                                            return 1
                                    else: 
                                        return 1
                            else: 
                                if alcohol<10:
                                    return 1
                                else: 
                                    return -1
                        else: 
                            if density<0.99752:
                                if alcohol<10.2:
                                    return 1
                                else: 
                                    return 1
                            else: 
                                if alcohol<10.2:
                                    return -1
                                else: 
                                    if sulphates<1.18:
                                        return -1
                                    else: 
                                        return -1
                    else: 
                        if alcohol<10.2:
                            if sulphates<0.86:
                                return -1
                            else: 
                                return -1
                        else: 
                            return -1
    else: 
        if volatile_acidity<0.78:
            if total_sulfur_dioxide<67:
                if sulphates<0.59:
                    if chlorides<0.059:
                        if chlorides<0.048:
                            if alcohol<12.4:
                                return 1
                            else: 
                                return 1
                        else: 
                            if alcohol<13:
                                if alcohol<12.1:
                                    if alcohol<11.95:
                                        if alcohol<11.8:
                                            if alcohol<11.7:
                                                if alcohol<11.4:
                                                    return -1
                                                else: 
                                                    if sulphates<0.56:
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
                        if density<0.9962:
                            if free_sulfur_dioxide<36:
                                if fixed_acidity<9.8:
                                    if free_sulfur_dioxide<18:
                                        if alcohol<13.3:
                                            if alcohol<12.8:
                                                if alcohol<12.7:
                                                    if alcohol<12.4:
                                                        if alcohol<12.2:
                                                            if alcohol<11.9:
                                                                if alcohol<11.8:
                                                                    if alcohol<11.6:
                                                                        if alcohol<11.5:
                                                                            if alcohol<11.3:
                                                                                if alcohol<11:
                                                                                    if alcohol<10.9:
                                                                                        if alcohol<10.8:
                                                                                            if alcohol<10.5:
                                                                                                if sulphates<0.58:
                                                                                                    return 1
                                                                                                else: 
                                                                                                    return 1
                                                                                            else: 
                                                                                                if sulphates<0.56:
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
                                                    return 1
                                            else: 
                                                if sulphates<0.55:
                                                    return 1
                                                else: 
                                                    return 1
                                        else: 
                                            return 1
                                    else: 
                                        if sulphates<0.57:
                                            return -1
                                        else: 
                                            if alcohol<11.8:
                                                if alcohol<11.4:
                                                    if alcohol<10.7:
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
                                return -1
                        else: 
                            if alcohol<11.7:
                                if chlorides<0.088:
                                    if alcohol<11.4:
                                        if alcohol<11:
                                            if alcohol<10.9:
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
                                        return -1
                                else: 
                                    if alcohol<10.7:
                                        return -1
                                    else: 
                                        if alcohol<10.8:
                                            return 1
                                        else: 
                                            return 1
                            else: 
                                if alcohol<12:
                                    if alcohol<11.9:
                                        return 1
                                    else: 
                                        return 1
                                else: 
                                    return 1
                else: 
                    if alcohol<10.8:
                        if density<0.9965:
                            if density<0.99605:
                                if alcohol<10.7:
                                    if alcohol<10.6:
                                        return 1
                                    else: 
                                        if sulphates<1.16:
                                            return 1
                                        else: 
                                            return 1
                                else: 
                                    return -1
                            else: 
                                if alcohol<10.7:
                                    if alcohol<10.6:
                                        if sulphates<0.67:
                                            return -1
                                        else: 
                                            return -1
                                    else: 
                                        return -1
                                else: 
                                    return -1
                        else: 
                            if total_sulfur_dioxide<12:
                                return -1
                            else: 
                                if volatile_acidity<0.75:
                                    if alcohol<10.7:
                                        if alcohol<10.6:
                                            if alcohol<10.5:
                                                if sulphates<0.81:
                                                    if sulphates<0.68:
                                                        return 1
                                                    else: 
                                                        return 1
                                                else: 
                                                    return 1
                                            else: 
                                                if sulphates<0.8:
                                                    if sulphates<0.74:
                                                        if sulphates<0.67:
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
                                            if sulphates<1.04:
                                                if sulphates<0.86:
                                                    if sulphates<0.72:
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
                                    return -1
                    else: 
                        if pH<3.01:
                            return -1
                        else: 
                            if fixed_acidity<6.3:
                                if fixed_acidity<6.2:
                                    if alcohol<14:
                                        if alcohol<12.8:
                                            if alcohol<12.5:
                                                return 1
                                            else: 
                                                if sulphates<0.84:
                                                    if sulphates<0.61:
                                                        if pH<4.01:
                                                            return 1
                                                        else: 
                                                            return 1
                                                    else: 
                                                        return 1
                                                else: 
                                                    return 1
                                        else: 
                                            if sulphates<0.63:
                                                return 1
                                            else: 
                                                return 1
                                    else: 
                                        if sulphates<0.75:
                                            return 1
                                        else: 
                                            return 1
                                else: 
                                    if alcohol<11.3:
                                        return 1
                                    else: 
                                        if alcohol<12:
                                            return -1
                                        else: 
                                            return -1
                            else: 
                                if density<0.99818:
                                    if volatile_acidity<0.2:
                                        if alcohol<11.2:
                                            return -1
                                        else: 
                                            if alcohol<11.9:
                                                if alcohol<11.8:
                                                    return 1
                                                else: 
                                                    return 1
                                            else: 
                                                return 1
                                    else: 
                                        if alcohol<14:
                                            if alcohol<13.4:
                                                if alcohol<13.1:
                                                    if alcohol<12.8:
                                                        if alcohol<12.7:
                                                            if alcohol<12.6:
                                                                if alcohol<12.5:
                                                                    if alcohol<12.4:
                                                                        if alcohol<12.2:
                                                                            if alcohol<12.1:
                                                                                if alcohol<12:
                                                                                    if alcohol<11.9:
                                                                                        if alcohol<11.8:
                                                                                            if alcohol<11.7:
                                                                                                if alcohol<11.6:
                                                                                                    if alcohol<11.5:
                                                                                                        if alcohol<11.4:
                                                                                                            if alcohol<11.3:
                                                                                                                if alcohol<11.2:
                                                                                                                    if alcohol<11.1:
                                                                                                                        if alcohol<11:
                                                                                                                            if alcohol<10.9:
                                                                                                                                if sulphates<0.78:
                                                                                                                                    if sulphates<0.69:
                                                                                                                                        if sulphates<0.62:
                                                                                                                                            if pH<3.43:
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
                                                                                                                                    if sulphates<0.83:
                                                                                                                                        if sulphates<0.78:
                                                                                                                                            if sulphates<0.76:
                                                                                                                                                if sulphates<0.75:
                                                                                                                                                    if sulphates<0.73:
                                                                                                                                                        if sulphates<0.68:
                                                                                                                                                            if sulphates<0.64:
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
                                                                                                                                    return 1
                                                                                                                        else: 
                                                                                                                            if sulphates<0.86:
                                                                                                                                if sulphates<0.85:
                                                                                                                                    if sulphates<0.82:
                                                                                                                                        if sulphates<0.81:
                                                                                                                                            if sulphates<0.75:
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
                                                                                                                        if sulphates<0.89:
                                                                                                                            if sulphates<0.85:
                                                                                                                                if sulphates<0.79:
                                                                                                                                    if sulphates<0.75:
                                                                                                                                        if pH<3.42:
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
                                                                                                                    if sulphates<0.8:
                                                                                                                        if sulphates<0.69:
                                                                                                                            if pH<3.37:
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
                                                                                                                        if sulphates<0.71:
                                                                                                                            if sulphates<0.67:
                                                                                                                                if sulphates<0.62:
                                                                                                                                    if sulphates<0.6:
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
                                                                                                            if sulphates<0.87:
                                                                                                                if sulphates<0.85:
                                                                                                                    if sulphates<0.76:
                                                                                                                        if sulphates<0.71:
                                                                                                                            if sulphates<0.68:
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
                                                                                                        if sulphates<0.84:
                                                                                                            if sulphates<0.77:
                                                                                                                if sulphates<0.72:
                                                                                                                    if sulphates<0.68:
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
                                                                                                            return 1
                                                                                                else: 
                                                                                                    if sulphates<0.82:
                                                                                                        if sulphates<0.76:
                                                                                                            return 1
                                                                                                        else: 
                                                                                                            return 1
                                                                                                    else: 
                                                                                                        return 1
                                                                                            else: 
                                                                                                if sulphates<0.85:
                                                                                                    if sulphates<0.84:
                                                                                                        if sulphates<0.74:
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
                                                                                            if sulphates<0.89:
                                                                                                if sulphates<0.74:
                                                                                                    return 1
                                                                                                else: 
                                                                                                    return 1
                                                                                            else: 
                                                                                                return 1
                                                                                    else: 
                                                                                        if sulphates<0.8:
                                                                                            return 1
                                                                                        else: 
                                                                                            return 1
                                                                                else: 
                                                                                    return 1
                                                                            else: 
                                                                                if sulphates<0.96:
                                                                                    if sulphates<0.77:
                                                                                        if sulphates<0.71:
                                                                                            if sulphates<0.69:
                                                                                                if sulphates<0.64:
                                                                                                    return 1
                                                                                                else: 
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
                                                                            if sulphates<0.64:
                                                                                return 1
                                                                            else: 
                                                                                return 1
                                                                    else: 
                                                                        if sulphates<1.01:
                                                                            if sulphates<0.8:
                                                                                if sulphates<0.66:
                                                                                    return 1
                                                                                else: 
                                                                                    return 1
                                                                            else: 
                                                                                return 1
                                                                        else: 
                                                                            return 1
                                                                else: 
                                                                    if sulphates<0.81:
                                                                        if sulphates<0.78:
                                                                            if sulphates<0.7:
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
                                                                if sulphates<0.82:
                                                                    return 1
                                                                else: 
                                                                    return 1
                                                        else: 
                                                            return 1
                                                    else: 
                                                        if sulphates<0.7:
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
                                    if density<0.9982:
                                        return -1
                                    else: 
                                        if total_sulfur_dioxide<55:
                                            if alcohol<13.4:
                                                if alcohol<13:
                                                    if alcohol<12.7:
                                                        if alcohol<11.7:
                                                            if alcohol<11.5:
                                                                if alcohol<11.4:
                                                                    if alcohol<11.3:
                                                                        if alcohol<11.2:
                                                                            if alcohol<11:
                                                                                if alcohol<10.9:
                                                                                    return 1
                                                                                else: 
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
                if residual_sugar<2.6:
                    if free_sulfur_dioxide<38:
                        if alcohol<14:
                            if alcohol<12.9:
                                if alcohol<12.7:
                                    if alcohol<12.2:
                                        if alcohol<11.8:
                                            if alcohol<11.5:
                                                if alcohol<11.4:
                                                    if sulphates<1.18:
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
                        if alcohol<11.3:
                            return -1
                        else: 
                            return -1
                else: 
                    if alcohol<14.9:
                        if alcohol<13:
                            if alcohol<11:
                                if sulphates<0.83:
                                    if sulphates<0.8:
                                        if sulphates<0.76:
                                            return -1
                                        else: 
                                            return -1
                                    else: 
                                        return -1
                                else: 
                                    return -1
                            else: 
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
                if residual_sugar<2:
                    if alcohol<10.6:
                        return -1
                    else: 
                        if alcohol<11.9:
                            return 1
                        else: 
                            return 1
                else: 
                    if alcohol<12.2:
                        if alcohol<11.6:
                            if alcohol<11.5:
                                if alcohol<11.4:
                                    if alcohol<11.3:
                                        if alcohol<11:
                                            if alcohol<10.9:
                                                if fixed_acidity<6.5:
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
                if volatile_acidity<0.915:
                    if alcohol<13:
                        if alcohol<12.9:
                            if alcohol<11:
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
                        if alcohol<11.5:
                            if alcohol<11.4:
                                return -1
                            else: 
                                return -1
                        else: 
                            return -1
