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
    if alcohol < 10.55:
        if volatile_acidity < 0.655:
            if alcohol < 9.9:
                if fixed_acidity < 12.5:
                    if total_sulfur_dioxide < 42:
                        if sulphates < 0.57:
                            if volatile_acidity < 0.29:
                                return 4.0
                            else: 
                                if chlorides < 0.07:
                                    if sulphates < 0.48:
                                        return 5.0
                                    else: 
                                        if alcohol < 9.8:
                                            if alcohol < 9.5:
                                                return 6.0
                                            else: 
                                                return 6.0
                                        else: 
                                            return 6.0
                                else: 
                                    if pH < 3.35:
                                        if pH < 3.13:
                                            return 6.0
                                        else: 
                                            if volatile_acidity < 0.585:
                                                if alcohol < 9.8:
                                                    if alcohol < 9.7:
                                                        if alcohol < 9.6:
                                                            if alcohol < 9.5:
                                                                if alcohol < 9.4:
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
                                                if volatile_acidity < 0.6:
                                                    return 6.0
                                                else: 
                                                    if alcohol < 9.8:
                                                        return 5.0
                                                    else: 
                                                        return 5.0
                                    else: 
                                        if alcohol < 9.4:
                                            return 5.0
                                        else: 
                                            if alcohol < 9.8:
                                                return 6.0
                                            else: 
                                                return 6.0
                        else: 
                            if fixed_acidity < 6.6:
                                if alcohol < 9.8:
                                    if alcohol < 9.5:
                                        if alcohol < 9.4:
                                            return 5.0
                                        else: 
                                            return 5.0
                                    else: 
                                        return 5.0
                                else: 
                                    return 5.0
                            else: 
                                if citric_acid < 0.52:
                                    if total_sulfur_dioxide < 29:
                                        if chlorides < 0.088:
                                            if sulphates < 0.59:
                                                return 7.0
                                            else: 
                                                if sulphates < 0.65:
                                                    if chlorides < 0.079:
                                                        if fixed_acidity < 10.7:
                                                            if alcohol < 9.5:
                                                                if alcohol < 9.4:
                                                                    if alcohol < 9.3:
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
                                                        if alcohol < 9.5:
                                                            return 5.0
                                                        else: 
                                                            return 5.0
                                                else: 
                                                    if alcohol < 9.8:
                                                        if alcohol < 9.6:
                                                            if alcohol < 9.5:
                                                                if alcohol < 9.4:
                                                                    if alcohol < 9.3:
                                                                        if alcohol < 9.2:
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
                                            if chlorides < 0.118:
                                                if alcohol < 9.7:
                                                    if alcohol < 9.6:
                                                        if alcohol < 9.5:
                                                            return 5.0
                                                        else: 
                                                            return 5.0
                                                    else: 
                                                        return 5.0
                                                else: 
                                                    return 5.0
                                            else: 
                                                if sulphates < 1.05:
                                                    if alcohol < 9.8:
                                                        if alcohol < 9.5:
                                                            return 6.0
                                                        else: 
                                                            return 6.0
                                                    else: 
                                                        return 6.0
                                                else: 
                                                    return 5.0
                                    else: 
                                        if density < 0.99855:
                                            if pH < 3.27:
                                                if alcohol < 9.8:
                                                    if alcohol < 9.5:
                                                        if alcohol < 9.4:
                                                            return 5.0
                                                        else: 
                                                            return 5.0
                                                    else: 
                                                        return 5.0
                                                else: 
                                                    return 5.0
                                            else: 
                                                if chlorides < 0.08:
                                                    if residual_sugar < 2.2:
                                                        if sulphates < 0.72:
                                                            if alcohol < 9.7:
                                                                if alcohol < 9.6:
                                                                    return 5.0
                                                                else: 
                                                                    return 5.0
                                                            else: 
                                                                return 5.0
                                                        else: 
                                                            if alcohol < 9.8:
                                                                if alcohol < 9.6:
                                                                    return 6.0
                                                                else: 
                                                                    return 6.0
                                                            else: 
                                                                return 5.0
                                                    else: 
                                                        if alcohol < 9.7:
                                                            return 6.0
                                                        else: 
                                                            return 6.0
                                                else: 
                                                    if alcohol < 9.7:
                                                        if alcohol < 9.6:
                                                            if alcohol < 9.3:
                                                                if alcohol < 9.2:
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
                                            if alcohol < 9.7:
                                                if alcohol < 9.6:
                                                    if alcohol < 9.4:
                                                        return 5.0
                                                    else: 
                                                        return 5.0
                                                else: 
                                                    return 5.0
                                            else: 
                                                return 5.0
                                else: 
                                    if alcohol < 9.4:
                                        return 6.0
                                    else: 
                                        if alcohol < 9.6:
                                            if alcohol < 9.5:
                                                return 5.0
                                            else: 
                                                return 5.0
                                        else: 
                                            return 5.0
                    else: 
                        if pH < 3.41:
                            if citric_acid < 0.66:
                                if sulphates < 0.62:
                                    if total_sulfur_dioxide < 89:
                                        if density < 0.9991:
                                            if alcohol < 9.8:
                                                if alcohol < 9.7:
                                                    if alcohol < 9.6:
                                                        if alcohol < 9.5:
                                                            if alcohol < 9.4:
                                                                if alcohol < 9.3:
                                                                    if alcohol < 9.2:
                                                                        if alcohol < 9.1:
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
                                            if alcohol < 9.6:
                                                return 5.0
                                            else: 
                                                return 4.0
                                    else: 
                                        if total_sulfur_dioxide < 96:
                                            if alcohol < 9.5:
                                                if alcohol < 9.2:
                                                    return 5.0
                                                else: 
                                                    return 5.0
                                            else: 
                                                if alcohol < 9.8:
                                                    if alcohol < 9.6:
                                                        return 6.0
                                                    else: 
                                                        return 6.0
                                                else: 
                                                    return 6.0
                                        else: 
                                            if density < 0.9962:
                                                if volatile_acidity < 0.53:
                                                    if alcohol < 9.7:
                                                        if alcohol < 9.5:
                                                            return 5.0
                                                        else: 
                                                            return 5.0
                                                    else: 
                                                        return 5.0
                                                else: 
                                                    if alcohol < 9.8:
                                                        return 6.0
                                                    else: 
                                                        return 6.0
                                            else: 
                                                if chlorides < 0.069:
                                                    return 6.0
                                                else: 
                                                    if alcohol < 9.8:
                                                        if alcohol < 9.7:
                                                            if alcohol < 9.5:
                                                                if alcohol < 9.4:
                                                                    if alcohol < 9.3:
                                                                        if alcohol < 9.2:
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
                                    if total_sulfur_dioxide < 108:
                                        if residual_sugar < 1.8:
                                            if alcohol < 9.5:
                                                if alcohol < 9.3:
                                                    if alcohol < 9.2:
                                                        if alcohol < 9:
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
                                            if citric_acid < 0.27:
                                                if alcohol < 9.2:
                                                    return 6.0
                                                else: 
                                                    if alcohol < 9.6:
                                                        if alcohol < 9.5:
                                                            if alcohol < 9.4:
                                                                if alcohol < 9.3:
                                                                    return 5.0
                                                                else: 
                                                                    return 5.0
                                                            else: 
                                                                return 5.0
                                                        else: 
                                                            return 5.0
                                                    else: 
                                                        if free_sulfur_dioxide < 20:
                                                            return 6.0
                                                        else: 
                                                            if alcohol < 9.8:
                                                                if alcohol < 9.7:
                                                                    return 5.0
                                                                else: 
                                                                    return 5.0
                                                            else: 
                                                                return 5.0
                                            else: 
                                                if volatile_acidity < 0.54:
                                                    if total_sulfur_dioxide < 62:
                                                        if alcohol < 9.7:
                                                            if alcohol < 9.5:
                                                                if alcohol < 9.2:
                                                                    return 6.0
                                                                else: 
                                                                    return 6.0
                                                            else: 
                                                                return 6.0
                                                        else: 
                                                            return 6.0
                                                    else: 
                                                        if pH < 3.32:
                                                            if alcohol < 9.6:
                                                                if alcohol < 9.4:
                                                                    if alcohol < 9:
                                                                        return 5.0
                                                                    else: 
                                                                        return 5.0
                                                                else: 
                                                                    return 5.0
                                                            else: 
                                                                return 5.0
                                                        else: 
                                                            if chlorides < 0.082:
                                                                if alcohol < 9.8:
                                                                    return 5.0
                                                                else: 
                                                                    return 5.0
                                                            else: 
                                                                if alcohol < 9.7:
                                                                    if alcohol < 9.6:
                                                                        return 6.0
                                                                    else: 
                                                                        return 6.0
                                                                else: 
                                                                    return 6.0
                                                else: 
                                                    if alcohol < 9.5:
                                                        if alcohol < 9.1:
                                                            return 6.0
                                                        else: 
                                                            return 6.0
                                                    else: 
                                                        return 6.0
                                    else: 
                                        if alcohol < 9.2:
                                            return 4.0
                                        else: 
                                            if alcohol < 9.8:
                                                if alcohol < 9.5:
                                                    if alcohol < 9.4:
                                                        if alcohol < 9.3:
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
                                if density < 0.9996:
                                    return 5.0
                                else: 
                                    if alcohol < 9.4:
                                        return 3.0
                                    else: 
                                        return 4.0
                        else: 
                            if citric_acid < 0.33:
                                if citric_acid < 0.12:
                                    if chlorides < 0.08:
                                        if alcohol < 9.8:
                                            if alcohol < 9.7:
                                                return 5.0
                                            else: 
                                                return 5.0
                                        else: 
                                            return 5.0
                                    else: 
                                        if alcohol < 9.8:
                                            if alcohol < 9.7:
                                                return 6.0
                                            else: 
                                                return 6.0
                                        else: 
                                            return 6.0
                                else: 
                                    if chlorides < 0.08:
                                        if alcohol < 9.8:
                                            if alcohol < 9.7:
                                                if alcohol < 9.5:
                                                    if alcohol < 9.4:
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
                                        if pH < 3.44:
                                            if alcohol < 9.5:
                                                return 6.0
                                            else: 
                                                return 6.0
                                        else: 
                                            if alcohol < 9.4:
                                                return 5.0
                                            else: 
                                                return 5.0
                            else: 
                                if alcohol < 9.7:
                                    if alcohol < 9.5:
                                        if alcohol < 9.2:
                                            if alcohol < 9.1:
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
                    if sulphates < 0.84:
                        if alcohol < 9.8:
                            if alcohol < 9.5:
                                if alcohol < 9.3:
                                    return 6.0
                                else: 
                                    return 6.0
                            else: 
                                return 6.0
                        else: 
                            return 6.0
                    else: 
                        if alcohol < 9.8:
                            return 7.0
                        else: 
                            return 7.0
            else: 
                if sulphates < 0.69:
                    if sulphates < 0.53:
                        if residual_sugar < 1.6:
                            return 7.0
                        else: 
                            if density < 0.99787:
                                if sulphates < 0.44:
                                    return 4.0
                                else: 
                                    if sulphates < 0.51:
                                        if alcohol < 10.5:
                                            if alcohol < 10.3:
                                                if alcohol < 10.2:
                                                    if alcohol < 10.1:
                                                        if alcohol < 10:
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
                                        if total_sulfur_dioxide < 59:
                                            if alcohol < 10.4:
                                                return 6.0
                                            else: 
                                                return 6.0
                                        else: 
                                            return 5.0
                            else: 
                                return 6.0
                    else: 
                        if chlorides < 0.063:
                            if total_sulfur_dioxide < 54:
                                if alcohol < 10.5:
                                    if alcohol < 10.4:
                                        if alcohol < 10.2:
                                            if alcohol < 10.1:
                                                if alcohol < 10:
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
                                if alcohol < 10.4:
                                    return 7.0
                                else: 
                                    return 6.0
                        else: 
                            if citric_acid < 0.02:
                                if alcohol < 10.5:
                                    return 6.0
                                else: 
                                    return 7.0
                            else: 
                                if pH < 3.66:
                                    if density < 0.99575:
                                        if total_sulfur_dioxide < 99:
                                            if alcohol < 10.5:
                                                if alcohol < 10.4:
                                                    if alcohol < 10.3:
                                                        if alcohol < 10.2:
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
                                        if pH < 3.03:
                                            return 7.0
                                        else: 
                                            if volatile_acidity < 0.475:
                                                if residual_sugar < 2.1:
                                                    if alcohol < 10.5:
                                                        if alcohol < 10.4:
                                                            if alcohol < 10.3:
                                                                if alcohol < 10.2:
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
                                                    if density < 0.9984:
                                                        if density < 0.99834:
                                                            if alcohol < 10.1:
                                                                return 5.0
                                                            else: 
                                                                if density < 0.9974:
                                                                    if pH < 3.43:
                                                                        if chlorides < 0.114:
                                                                            if alcohol < 10.5:
                                                                                if alcohol < 10.3:
                                                                                    if alcohol < 10.2:
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
                                                                        return 5.0
                                                                else: 
                                                                    if alcohol < 10.4:
                                                                        return 5.0
                                                                    else: 
                                                                        return 5.0
                                                        else: 
                                                            return 7.0
                                                    else: 
                                                        if alcohol < 10.5:
                                                            if alcohol < 10.3:
                                                                if alcohol < 10.2:
                                                                    return 5.0
                                                                else: 
                                                                    return 5.0
                                                            else: 
                                                                return 5.0
                                                        else: 
                                                            return 5.0
                                            else: 
                                                if fixed_acidity < 7.6:
                                                    if chlorides < 0.083:
                                                        if alcohol < 10.5:
                                                            if alcohol < 10.4:
                                                                if alcohol < 10.3:
                                                                    if alcohol < 10.2:
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
                                                        if alcohol < 10.3:
                                                            if alcohol < 10.2:
                                                                return 6.0
                                                            else: 
                                                                return 7.0
                                                        else: 
                                                            return 5.0
                                                else: 
                                                    if free_sulfur_dioxide < 29:
                                                        if pH < 3.34:
                                                            if pH < 3.07:
                                                                return 5.0
                                                            else: 
                                                                if alcohol < 10.5:
                                                                    if alcohol < 10.4:
                                                                        if alcohol < 10.3:
                                                                            if alcohol < 10.2:
                                                                                if alcohol < 10.1:
                                                                                    if alcohol < 10.03333333:
                                                                                        if alcohol < 10:
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
                                                            if pH < 3.39:
                                                                if alcohol < 10.3:
                                                                    return 5.0
                                                                else: 
                                                                    return 5.0
                                                            else: 
                                                                if alcohol < 10.2:
                                                                    if alcohol < 10.1:
                                                                        return 6.0
                                                                    else: 
                                                                        return 6.0
                                                                else: 
                                                                    return 6.0
                                                    else: 
                                                        if alcohol < 10.1:
                                                            return 5.0
                                                        else: 
                                                            return 5.0
                                else: 
                                    return 4.0
                else: 
                    if volatile_acidity < 0.43:
                        if residual_sugar < 1.8:
                            if sulphates < 1.1:
                                if chlorides < 0.066:
                                    if alcohol < 10.3:
                                        if alcohol < 10.1:
                                            return 6.0
                                        else: 
                                            return 6.0
                                    else: 
                                        return 7.0
                                else: 
                                    if alcohol < 10:
                                        return 7.0
                                    else: 
                                        return 7.0
                            else: 
                                return 8.0
                        else: 
                            if fixed_acidity < 10.4:
                                if chlorides < 0.085:
                                    if sulphates < 0.75:
                                        if alcohol < 10.5:
                                            return 7.0
                                        else: 
                                            return 7.0
                                    else: 
                                        if alcohol < 10:
                                            return 5.0
                                        else: 
                                            if total_sulfur_dioxide < 67:
                                                if alcohol < 10.5:
                                                    if alcohol < 10.4:
                                                        if alcohol < 10.3:
                                                            if alcohol < 10.2:
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
                                                if sulphates < 0.9:
                                                    return 7.0
                                                else: 
                                                    return 6.0
                                else: 
                                    if pH < 3.42:
                                        if density < 0.9969:
                                            return 6.0
                                        else: 
                                            if alcohol < 10.5:
                                                if alcohol < 10:
                                                    return 7.0
                                                else: 
                                                    return 7.0
                                            else: 
                                                return 7.0
                                    else: 
                                        return 6.0
                            else: 
                                if alcohol < 10.5:
                                    if density < 0.9981:
                                        return 7.0
                                    else: 
                                        if alcohol < 10.4:
                                            if alcohol < 10.1:
                                                if alcohol < 10:
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
                        if citric_acid < 0.66:
                            if citric_acid < 0.36:
                                if pH < 3.57:
                                    if density < 0.9984:
                                        if free_sulfur_dioxide < 8:
                                            return 5.0
                                        else: 
                                            if alcohol < 10.5:
                                                if alcohol < 10.3:
                                                    if alcohol < 10:
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
                                    if alcohol < 10.5:
                                        return 5.0
                                    else: 
                                        return 5.0
                            else: 
                                if alcohol < 10.2:
                                    return 4.0
                                else: 
                                    if residual_sugar < 2.7:
                                        if sulphates < 0.87:
                                            if alcohol < 10.3:
                                                return 6.0
                                            else: 
                                                return 6.0
                                        else: 
                                            return 5.0
                                    else: 
                                        if alcohol < 10.5:
                                            return 5.0
                                        else: 
                                            return 5.0
                        else: 
                            if alcohol < 10.4:
                                return 7.0
                            else: 
                                return 7.0
        else: 
            if volatile_acidity < 0.815:
                if density < 0.9983:
                    if pH < 3.55:
                        if residual_sugar < 1.4:
                            return 4.0
                        else: 
                            if sulphates < 0.5:
                                if citric_acid < 0.03:
                                    if alcohol < 9.6:
                                        return 5.0
                                    else: 
                                        if alcohol < 9.7:
                                            return 4.0
                                        else: 
                                            return 4.0
                                else: 
                                    if alcohol < 10:
                                        if alcohol < 9.9:
                                            if alcohol < 9.7:
                                                if alcohol < 9.6:
                                                    if alcohol < 9.5:
                                                        if alcohol < 9.4:
                                                            if alcohol < 9.3:
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
                                if pH < 3:
                                    if alcohol < 10.2:
                                        return 6.0
                                    else: 
                                        return 6.0
                                else: 
                                    if alcohol < 9.5:
                                        if density < 0.99623:
                                            return 6.0
                                        else: 
                                            if sulphates < 0.54:
                                                if fixed_acidity < 8.3:
                                                    if alcohol < 9.3:
                                                        if alcohol < 9.2:
                                                            return 5.0
                                                        else: 
                                                            return 5.0
                                                    else: 
                                                        return 5.0
                                                else: 
                                                    return 4.0
                                            else: 
                                                if alcohol < 9.4:
                                                    if alcohol < 9.3:
                                                        if alcohol < 9.2:
                                                            return 5.0
                                                        else: 
                                                            return 5.0
                                                    else: 
                                                        return 5.0
                                                else: 
                                                    return 5.0
                                    else: 
                                        if residual_sugar < 5.2:
                                            if total_sulfur_dioxide < 11:
                                                return 6.0
                                            else: 
                                                if free_sulfur_dioxide < 42:
                                                    if fixed_acidity < 7.4:
                                                        if pH < 3.24:
                                                            if sulphates < 0.59:
                                                                return 5.0
                                                            else: 
                                                                return 6.0
                                                        else: 
                                                            if alcohol < 10.3:
                                                                if alcohol < 10.2:
                                                                    if alcohol < 10.1:
                                                                        if alcohol < 10:
                                                                            if alcohol < 9.8:
                                                                                if alcohol < 9.7:
                                                                                    if alcohol < 9.6:
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
                                                        if fixed_acidity < 8.1:
                                                            if alcohol < 9.8:
                                                                if chlorides < 0.076:
                                                                    return 6.0
                                                                else: 
                                                                    if alcohol < 9.6:
                                                                        return 5.0
                                                                    else: 
                                                                        return 5.0
                                                            else: 
                                                                if pH < 3.27:
                                                                    if sulphates < 0.71:
                                                                        if alcohol < 9.9:
                                                                            return 5.0
                                                                        else: 
                                                                            return 5.0
                                                                    else: 
                                                                        return 6.0
                                                                else: 
                                                                    if alcohol < 10.5:
                                                                        if alcohol < 10:
                                                                            if alcohol < 9.9:
                                                                                return 6.0
                                                                            else: 
                                                                                return 6.0
                                                                        else: 
                                                                            return 6.0
                                                                    else: 
                                                                        return 6.0
                                                        else: 
                                                            if citric_acid < 0.1:
                                                                return 6.0
                                                            else: 
                                                                if sulphates < 0.55:
                                                                    if sulphates < 0.54:
                                                                        if alcohol < 9.8:
                                                                            if alcohol < 9.6:
                                                                                return 5.0
                                                                            else: 
                                                                                return 5.0
                                                                        else: 
                                                                            return 5.0
                                                                    else: 
                                                                        return 6.0
                                                                else: 
                                                                    if alcohol < 10.5:
                                                                        if alcohol < 10.4:
                                                                            if alcohol < 10.3:
                                                                                if alcohol < 10.1:
                                                                                    if alcohol < 10:
                                                                                        if alcohol < 9.9:
                                                                                            if alcohol < 9.8:
                                                                                                if alcohol < 9.6:
                                                                                                    if alcohol < 9.55:
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
                                                    return 6.0
                                        else: 
                                            if alcohol < 9.6:
                                                return 6.0
                                            else: 
                                                return 6.0
                    else: 
                        if alcohol < 9.95:
                            return 5.0
                        else: 
                            return 3.0
                else: 
                    if residual_sugar < 3.2:
                        if pH < 3.17:
                            return 5.0
                        else: 
                            if pH < 3.35:
                                if alcohol < 10.4:
                                    if alcohol < 10.1:
                                        if alcohol < 9.9:
                                            if alcohol < 9.5:
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
                                if sulphates < 0.86:
                                    if alcohol < 10:
                                        return 5.0
                                    else: 
                                        return 5.0
                                else: 
                                    if alcohol < 9.9:
                                        return 6.0
                                    else: 
                                        return 6.0
                    else: 
                        if alcohol < 10.2:
                            if alcohol < 9.9:
                                if alcohol < 9.6:
                                    if alcohol < 9.4:
                                        if alcohol < 9.3:
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
                if fixed_acidity < 7.4:
                    if alcohol < 9.7:
                        if sulphates < 0.72:
                            if sulphates < 0.6:
                                if alcohol < 9.6:
                                    return 5.0
                                else: 
                                    return 5.0
                            else: 
                                return 4.0
                        else: 
                            return 6.0
                    else: 
                        if sulphates < 0.51:
                            if sulphates < 0.48:
                                return 5.0
                            else: 
                                if alcohol < 10.5:
                                    return 4.0
                                else: 
                                    return 4.0
                        else: 
                            if alcohol < 10.2:
                                if alcohol < 9.8:
                                    return 3.0
                                else: 
                                    return 3.0
                            else: 
                                return 3.0
                else: 
                    if volatile_acidity < 1:
                        if alcohol < 9.2:
                            return 6.0
                        else: 
                            if sulphates < 0.5:
                                if sulphates < 0.47:
                                    if sulphates < 0.46:
                                        return 4.0
                                    else: 
                                        if alcohol < 10:
                                            return 5.0
                                        else: 
                                            return 5.0
                                else: 
                                    if alcohol < 10:
                                        return 4.0
                                    else: 
                                        return 4.0
                            else: 
                                if pH < 3.6:
                                    if alcohol < 10.2:
                                        if alcohol < 10:
                                            if alcohol < 9.9:
                                                if alcohol < 9.8:
                                                    if alcohol < 9.6:
                                                        if alcohol < 9.5:
                                                            if alcohol < 9.4:
                                                                if alcohol < 9.3:
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
                        if sulphates < 0.55:
                            if alcohol < 10:
                                return 5.0
                            else: 
                                return 5.0
                        else: 
                            if alcohol < 10.1:
                                if alcohol < 9.9:
                                    return 6.0
                                else: 
                                    return 6.0
                            else: 
                                return 6.0
    else: 
        if volatile_acidity < 0.875:
            if sulphates < 0.64:
                if alcohol < 11.7:
                    if free_sulfur_dioxide < 9:
                        if volatile_acidity < 0.39:
                            if alcohol < 11.3:
                                if pH < 3.27:
                                    if alcohol < 10.9:
                                        return 6.0
                                    else: 
                                        return 6.0
                                else: 
                                    if alcohol < 11:
                                        return 5.0
                                    else: 
                                        return 5.0
                            else: 
                                if pH < 3.29:
                                    return 7.0
                                else: 
                                    if alcohol < 11.5:
                                        if alcohol < 11.4:
                                            return 6.0
                                        else: 
                                            return 6.0
                                    else: 
                                        return 6.0
                        else: 
                            if density < 0.99517:
                                if alcohol < 11.5:
                                    if alcohol < 11.4:
                                        return 5.0
                                    else: 
                                        return 5.0
                                else: 
                                    return 6.0
                            else: 
                                if alcohol < 10.7:
                                    return 6.0
                                else: 
                                    if total_sulfur_dioxide < 15:
                                        if residual_sugar < 2.6:
                                            if pH < 3.38:
                                                return 5.0
                                            else: 
                                                if alcohol < 11.5:
                                                    return 4.0
                                                else: 
                                                    return 4.0
                                        else: 
                                            if alcohol < 10.9:
                                                return 5.0
                                            else: 
                                                return 5.0
                                    else: 
                                        if alcohol < 11.4:
                                            if alcohol < 11.3:
                                                if alcohol < 11.2:
                                                    if alcohol < 11:
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
                        if total_sulfur_dioxide < 31:
                            if density < 0.99394:
                                return 5.0
                            else: 
                                if free_sulfur_dioxide < 14:
                                    if density < 0.99655:
                                        if pH < 3.43:
                                            if alcohol < 11.5:
                                                if alcohol < 11.3:
                                                    if alcohol < 11:
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
                                        return 6.0
                                else: 
                                    if alcohol < 11.6:
                                        if alcohol < 11.3:
                                            if alcohol < 11:
                                                return 6.0
                                            else: 
                                                return 6.0
                                        else: 
                                            return 6.0
                                    else: 
                                        return 6.0
                        else: 
                            if sulphates < 0.58:
                                if total_sulfur_dioxide < 64:
                                    if chlorides < 0.065:
                                        if sulphates < 0.57:
                                            if alcohol < 11.4:
                                                if alcohol < 10.8:
                                                    return 6.0
                                                else: 
                                                    return 6.0
                                            else: 
                                                return 6.0
                                        else: 
                                            return 5.0
                                    else: 
                                        if volatile_acidity < 0.63:
                                            if alcohol < 11.2:
                                                if alcohol < 11:
                                                    if alcohol < 10.9:
                                                        if alcohol < 10.8:
                                                            if alcohol < 10.7:
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
                                            if alcohol < 11:
                                                if alcohol < 10.8:
                                                    return 6.0
                                                else: 
                                                    return 6.0
                                            else: 
                                                if alcohol < 11.6:
                                                    return 5.0
                                                else: 
                                                    return 5.0
                                else: 
                                    if alcohol < 11.5:
                                        return 6.0
                                    else: 
                                        return 6.0
                            else: 
                                if density < 0.99438:
                                    return 5.0
                                else: 
                                    if total_sulfur_dioxide < 90:
                                        if residual_sugar < 2.8:
                                            if alcohol < 11.4:
                                                if alcohol < 11.1:
                                                    if alcohol < 10.9:
                                                        if alcohol < 10.8:
                                                            if alcohol < 10.7:
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
                                            if total_sulfur_dioxide < 52:
                                                if alcohol < 11.6:
                                                    return 6.0
                                                else: 
                                                    return 6.0
                                            else: 
                                                return 5.0
                                    else: 
                                        return 5.0
                else: 
                    if volatile_acidity < 0.49:
                        if residual_sugar < 4:
                            if citric_acid < 0.68:
                                if sulphates < 0.44:
                                    return 7.0
                                else: 
                                    if total_sulfur_dioxide < 17:
                                        if density < 0.99538:
                                            if alcohol < 12.8:
                                                return 7.0
                                            else: 
                                                return 7.0
                                        else: 
                                            if sulphates < 0.58:
                                                if alcohol < 13.2:
                                                    if alcohol < 12.2:
                                                        return 6.0
                                                    else: 
                                                        return 6.0
                                                else: 
                                                    return 6.0
                                            else: 
                                                return 7.0
                                    else: 
                                        if volatile_acidity < 0.48:
                                            if alcohol < 13.3:
                                                if alcohol < 12.8:
                                                    if alcohol < 12.7:
                                                        if alcohol < 12.5:
                                                            if alcohol < 12.4:
                                                                if alcohol < 12.2:
                                                                    if alcohol < 12:
                                                                        if alcohol < 11.9:
                                                                            if alcohol < 11.8:
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
                                            return 7.0
                            else: 
                                return 5.0
                        else: 
                            if alcohol < 12.5:
                                if alcohol < 12.3:
                                    if alcohol < 12.1:
                                        return 7.0
                                    else: 
                                        return 7.0
                                else: 
                                    return 7.0
                            else: 
                                if alcohol < 13:
                                    return 6.0
                                else: 
                                    return 7.0
                    else: 
                        if chlorides < 0.059:
                            if pH < 3.85:
                                if density < 0.99488:
                                    if alcohol < 13:
                                        if alcohol < 12.1:
                                            if alcohol < 11.95:
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
                                if alcohol < 12.9:
                                    return 6.0
                                else: 
                                    return 6.0
                        else: 
                            if residual_sugar < 2.5:
                                if free_sulfur_dioxide < 5:
                                    return 7.0
                                else: 
                                    if alcohol < 11.8:
                                        return 7.0
                                    else: 
                                        if alcohol < 12.8:
                                            if alcohol < 12.5:
                                                if alcohol < 12.2:
                                                    if alcohol < 12.1:
                                                        if alcohol < 12:
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
                                if total_sulfur_dioxide < 17:
                                    if alcohol < 12.9:
                                        if alcohol < 12.6:
                                            return 5.0
                                        else: 
                                            return 5.0
                                    else: 
                                        return 5.0
                                else: 
                                    if sulphates < 0.63:
                                        if alcohol < 12.8:
                                            if alcohol < 12.7:
                                                if alcohol < 11.9:
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
                if alcohol < 11.6:
                    if volatile_acidity < 0.4:
                        if pH < 3.26:
                            if volatile_acidity < 0.28:
                                if density < 0.9978:
                                    if alcohol < 11.2:
                                        if alcohol < 10.9:
                                            return 6.0
                                        else: 
                                            return 6.0
                                    else: 
                                        return 6.0
                                else: 
                                    return 7.0
                            else: 
                                if citric_acid < 0.32:
                                    if alcohol < 11.4:
                                        return 8.0
                                    else: 
                                        return 8.0
                                else: 
                                    if sulphates < 0.67:
                                        if alcohol < 11:
                                            return 7.0
                                        else: 
                                            return 8.0
                                    else: 
                                        if total_sulfur_dioxide < 10:
                                            return 6.0
                                        else: 
                                            if free_sulfur_dioxide < 25:
                                                if alcohol < 11.4:
                                                    if alcohol < 11.3:
                                                        if alcohol < 11.2:
                                                            if alcohol < 11.1:
                                                                if alcohol < 11:
                                                                    if alcohol < 10.9:
                                                                        if alcohol < 10.8:
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
                            if alcohol < 10.7:
                                if pH < 3.39:
                                    if pH < 3.32:
                                        return 5.0
                                    else: 
                                        return 6.0
                                else: 
                                    return 5.0
                            else: 
                                if pH < 3.4:
                                    if residual_sugar < 2.7:
                                        if total_sulfur_dioxide < 65:
                                            if sulphates < 0.69:
                                                return 7.0
                                            else: 
                                                if sulphates < 0.71:
                                                    if alcohol < 11.2:
                                                        return 5.0
                                                    else: 
                                                        return 6.0
                                                else: 
                                                    if alcohol < 11.5:
                                                        if alcohol < 11.4:
                                                            if alcohol < 11.2:
                                                                if alcohol < 11.1:
                                                                    if alcohol < 11:
                                                                        if alcohol < 10.9:
                                                                            if alcohol < 10.8:
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
                                            if volatile_acidity < 0.38:
                                                if pH < 3.33:
                                                    if alcohol < 11:
                                                        return 5.0
                                                    else: 
                                                        return 6.0
                                                else: 
                                                    if alcohol < 11.3:
                                                        if alcohol < 11.2:
                                                            return 5.0
                                                        else: 
                                                            return 5.0
                                                    else: 
                                                        return 5.0
                                            else: 
                                                if alcohol < 11.4:
                                                    return 6.0
                                                else: 
                                                    return 6.0
                                    else: 
                                        if chlorides < 0.081:
                                            if alcohol < 11:
                                                return 7.0
                                            else: 
                                                return 6.0
                                        else: 
                                            if alcohol < 11.2:
                                                if alcohol < 11:
                                                    if alcohol < 10.8:
                                                        return 7.0
                                                    else: 
                                                        return 7.0
                                                else: 
                                                    return 7.0
                                            else: 
                                                return 7.0
                                else: 
                                    if chlorides < 0.08:
                                        if alcohol < 11.3:
                                            if alcohol < 11:
                                                return 7.0
                                            else: 
                                                return 7.0
                                        else: 
                                            return 7.0
                                    else: 
                                        return 6.0
                    else: 
                        if pH < 3.29:
                            if chlorides < 0.095:
                                if density < 0.99518:
                                    return 5.0
                                else: 
                                    if total_sulfur_dioxide < 55:
                                        if density < 0.996:
                                            if sulphates < 0.85:
                                                return 7.0
                                            else: 
                                                return 6.0
                                        else: 
                                            if alcohol < 11.5:
                                                if alcohol < 11.4:
                                                    if alcohol < 11.3:
                                                        if alcohol < 11.2:
                                                            if alcohol < 11:
                                                                if alcohol < 10.9:
                                                                    if alcohol < 10.8:
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
                                if citric_acid < 0.54:
                                    if total_sulfur_dioxide < 68:
                                        if alcohol < 11.5:
                                            if alcohol < 11.2:
                                                if alcohol < 11.1:
                                                    if alcohol < 10.9:
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
                                    if alcohol < 11.3:
                                        return 7.0
                                    else: 
                                        if alcohol < 11.5:
                                            return 6.0
                                        else: 
                                            return 6.0
                        else: 
                            if density < 0.99684:
                                if total_sulfur_dioxide < 78:
                                    if chlorides < 0.12:
                                        if alcohol < 10.6:
                                            return 7.0
                                        else: 
                                            if alcohol < 11.5:
                                                if alcohol < 11.4:
                                                    if alcohol < 11.3:
                                                        if alcohol < 11.2:
                                                            if alcohol < 11.1:
                                                                if alcohol < 11:
                                                                    if alcohol < 10.9:
                                                                        if alcohol < 10.8:
                                                                            if alcohol < 10.7:
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
                                                if sulphates < 0.72:
                                                    return 6.0
                                                else: 
                                                    return 7.0
                                    else: 
                                        return 7.0
                                else: 
                                    if alcohol < 11.1:
                                        if alcohol < 11:
                                            return 5.0
                                        else: 
                                            return 5.0
                                    else: 
                                        return 6.0
                            else: 
                                if chlorides < 0.084:
                                    if alcohol < 11.5:
                                        return 7.0
                                    else: 
                                        return 7.0
                                else: 
                                    if density < 0.9979:
                                        if total_sulfur_dioxide < 18:
                                            return 6.0
                                        else: 
                                            if alcohol < 11.2:
                                                return 7.0
                                            else: 
                                                return 7.0
                                    else: 
                                        if alcohol < 11.1:
                                            if alcohol < 10.8:
                                                return 6.0
                                            else: 
                                                return 6.0
                                        else: 
                                            return 6.0
                else: 
                    if fixed_acidity < 13.5:
                        if total_sulfur_dioxide < 20:
                            if density < 0.9976:
                                if residual_sugar < 1.9:
                                    if sulphates < 0.74:
                                        if alcohol < 12.5:
                                            return 8.0
                                        else: 
                                            return 8.0
                                    else: 
                                        if alcohol < 11.9:
                                            return 7.0
                                        else: 
                                            return 7.0
                                else: 
                                    if density < 0.99318:
                                        return 8.0
                                    else: 
                                        if volatile_acidity < 0.42:
                                            if total_sulfur_dioxide < 9:
                                                return 6.0
                                            else: 
                                                if alcohol < 12.8:
                                                    if alcohol < 12.5:
                                                        if alcohol < 12.2:
                                                            if alcohol < 12.1:
                                                                if alcohol < 12:
                                                                    if alcohol < 11.8:
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
                                            if sulphates < 0.74:
                                                if total_sulfur_dioxide < 16:
                                                    if alcohol < 12.7:
                                                        if alcohol < 11.8:
                                                            return 7.0
                                                        else: 
                                                            return 7.0
                                                    else: 
                                                        return 7.0
                                                else: 
                                                    return 6.0
                                            else: 
                                                if alcohol < 14:
                                                    if alcohol < 12.3:
                                                        return 6.0
                                                    else: 
                                                        return 6.0
                                                else: 
                                                    return 6.0
                            else: 
                                if alcohol < 12.6:
                                    return 7.0
                                else: 
                                    if alcohol < 13.4:
                                        return 8.0
                                    else: 
                                        return 8.0
                        else: 
                            if sulphates < 0.74:
                                if sulphates < 0.65:
                                    return 7.0
                                else: 
                                    if free_sulfur_dioxide < 6:
                                        return 7.0
                                    else: 
                                        if pH < 3.4:
                                            if alcohol < 13.4:
                                                if alcohol < 12.8:
                                                    if alcohol < 12.7:
                                                        if alcohol < 12.5:
                                                            if alcohol < 12.4:
                                                                if alcohol < 11.9:
                                                                    if alcohol < 11.8:
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
                                            if alcohol < 12.1:
                                                return 5.0
                                            else: 
                                                if alcohol < 12.5:
                                                    return 6.0
                                                else: 
                                                    return 6.0
                            else: 
                                if chlorides < 0.066:
                                    if volatile_acidity < 0.42:
                                        if pH < 3.44:
                                            if alcohol < 13.4:
                                                if alcohol < 13.3:
                                                    if alcohol < 12.4:
                                                        if alcohol < 12.1:
                                                            if alcohol < 11.7:
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
                                            if chlorides < 0.063:
                                                if alcohol < 14:
                                                    return 6.0
                                                else: 
                                                    return 6.0
                                            else: 
                                                return 7.0
                                    else: 
                                        if sulphates < 0.84:
                                            if total_sulfur_dioxide < 50:
                                                return 7.0
                                            else: 
                                                if alcohol < 14:
                                                    return 8.0
                                                else: 
                                                    return 8.0
                                        else: 
                                            if alcohol < 13:
                                                if alcohol < 12.9:
                                                    return 7.0
                                                else: 
                                                    return 7.0
                                            else: 
                                                return 7.0
                                else: 
                                    if fixed_acidity < 8.9:
                                        if citric_acid < 0.12:
                                            if alcohol < 12.3:
                                                return 7.0
                                            else: 
                                                return 7.0
                                        else: 
                                            if residual_sugar < 6.2:
                                                if alcohol < 12.9:
                                                    if alcohol < 12.8:
                                                        if alcohol < 12.4:
                                                            if alcohol < 12.1:
                                                                if alcohol < 12:
                                                                    if alcohol < 11.8:
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
                                        if free_sulfur_dioxide < 10:
                                            if alcohol < 12.1:
                                                if alcohol < 12:
                                                    return 6.0
                                                else: 
                                                    return 6.0
                                            else: 
                                                return 7.0
                                        else: 
                                            if alcohol < 12.5:
                                                if alcohol < 12.1:
                                                    if alcohol < 12:
                                                        if alcohol < 11.9:
                                                            if alcohol < 11.7:
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
                        if alcohol < 14.9:
                            return 5.0
                        else: 
                            return 5.0
        else: 
            if volatile_acidity < 1.02:
                if density < 0.9955:
                    if sulphates < 0.73:
                        if alcohol < 11.9:
                            if alcohol < 11.5:
                                if alcohol < 11.2:
                                    if alcohol < 10.9:
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
                    if sulphates < 0.64:
                        if sulphates < 0.58:
                            if alcohol < 11.5:
                                if alcohol < 10.9:
                                    return 5.0
                                else: 
                                    return 5.0
                            else: 
                                return 5.0
                        else: 
                            return 6.0
                    else: 
                        if sulphates < 0.67:
                            if alcohol < 11.3:
                                return 4.0
                            else: 
                                return 4.0
                        else: 
                            return 5.0
            else: 
                if residual_sugar < 2.1:
                    if alcohol < 11.5:
                        return 5.0
                    else: 
                        return 5.0
                else: 
                    if citric_acid < 0.06:
                        if alcohol < 11:
                            if alcohol < 10.9:
                                return 3.0
                            else: 
                                return 3.0
                        else: 
                            return 3.0
                    else: 
                        if alcohol < 11.4:
                            if alcohol < 11.2:
                                return 4.0
                            else: 
                                return 4.0
                        else: 
                            return 4.0
