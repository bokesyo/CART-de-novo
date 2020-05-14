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
        if volatile_acidity<0.36:
            if density<0.9974:
                return 7.0
            else: 
                if alcohol<10.2:
                    if alcohol<10.1:
                        if alcohol<9.4:
                            return 6.0
                        else: 
                            return 6.0
                    else: 
                        return 6.0
                else: 
                    return 6.0
        else: 
            if total_sulfur_dioxide<13:
                if alcohol<9.95:
                    if alcohol<9.8:
                        return 5.0
                    else: 
                        return 5.0
                else: 
                    return 3.0
            else: 
                if alcohol<9.8:
                    if pH<3.47:
                        if sulphates<1.61:
                            if alcohol<9.2:
                                if sulphates<0.62:
                                    if alcohol<9.1:
                                        return 5.0
                                    else: 
                                        return 5.0
                                else: 
                                    return 6.0
                            else: 
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
                            return 6.0
                    else: 
                        if alcohol<9.7:
                            return 6.0
                        else: 
                            return 6.0
                else: 
                    if citric_acid<0.12:
                        if volatile_acidity<1.04:
                            if alcohol<10.2:
                                if alcohol<10.1:
                                    if alcohol<10:
                                        if alcohol<9.9:
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
                        if free_sulfur_dioxide<12:
                            if volatile_acidity<0.67:
                                if alcohol<10.4:
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
                                return 5.0
                        else: 
                            if sulphates<0.58:
                                return 6.0
                            else: 
                                if alcohol<10.4:
                                    if alcohol<10.3:
                                        if alcohol<10.1:
                                            return 5.0
                                        else: 
                                            return 5.0
                                    else: 
                                        return 5.0
                                else: 
                                    return 5.0
    else: 
        if sulphates<0.58:
            if citric_acid<0.44:
                if alcohol<12.8:
                    if alcohol<12.2:
                        if alcohol<12.1:
                            if alcohol<11.5:
                                if alcohol<11.4:
                                    if alcohol<11.3:
                                        if alcohol<10.9:
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
                if alcohol<12.4:
                    return 6.0
                else: 
                    return 6.0
        else: 
            if free_sulfur_dioxide<14:
                if alcohol<12.9:
                    if volatile_acidity<0.44:
                        if volatile_acidity<0.35:
                            if alcohol<12.5:
                                if alcohol<12.4:
                                    if alcohol<12.1:
                                        if alcohol<11.9:
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
                            if alcohol<11.7:
                                return 8.0
                            else: 
                                return 8.0
                    else: 
                        if pH<3.57:
                            if residual_sugar<6:
                                if alcohol<12.7:
                                    if alcohol<11.4:
                                        if alcohol<11.1:
                                            if alcohol<11:
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
                                return 7.0
                        else: 
                            if alcohol<12.8:
                                return 7.0
                            else: 
                                return 7.0
                else: 
                    if alcohol<13.1:
                        return 8.0
                    else: 
                        return 8.0
            else: 
                if density<0.99084:
                    return 8.0
                else: 
                    if fixed_acidity<6.7:
                        if alcohol<12.5:
                            if alcohol<12:
                                if alcohol<11.3:
                                    return 5.0
                                else: 
                                    return 5.0
                            else: 
                                return 5.0
                        else: 
                            if alcohol<14:
                                return 6.0
                            else: 
                                return 6.0
                    else: 
                        if total_sulfur_dioxide<106:
                            if sulphates<0.75:
                                if alcohol<12.8:
                                    if alcohol<12.1:
                                        if alcohol<11.8:
                                            if alcohol<11.5:
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
                                        return 6.0
                                else: 
                                    return 6.0
                            else: 
                                if volatile_acidity<0.38:
                                    if alcohol<11.3:
                                        if alcohol<11:
                                            return 7.0
                                        else: 
                                            return 7.0
                                    else: 
                                        return 7.0
                                else: 
                                    if alcohol<11.8:
                                        if alcohol<11.5:
                                            if alcohol<11.4:
                                                return 6.0
                                            else: 
                                                return 6.0
                                        else: 
                                            return 6.0
                                    else: 
                                        return 6.0
                        else: 
                            return 5.0
