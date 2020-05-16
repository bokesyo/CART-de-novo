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
        if sulphates<0.54:
            if volatile_acidity<0.815:
                return 1.5681225772491416 + 1.763051530845388 * sulphates + 0.28017473047970043 * alcohol
            else: 
                if fixed_acidity<7.2:
                    return -8.5 + 8.5 * fixed_acidity + -79.0 * volatile_acidity + 304.0 * citric_acid + -1.0 * residual_sugar + 0.0 * chlorides + -0.4375 * free_sulfur_dioxide + 0.28125 * total_sulfur_dioxide + -40.0 * density + 6.421875 * pH + -24.0 * sulphates + 4.75 * alcohol
                else: 
                    return 20.87301550230586 + -0.0016497196245666146 * fixed_acidity + -1.1555297193552292 * citric_acid + 5.890023040668893 * chlorides + -0.009832589330940777 * free_sulfur_dioxide + -3.288219173338291 * pH + 4.566147725306109 * sulphates + -0.8007257222249109 * alcohol
        else: 
            if alcohol<9.9:
                if fixed_acidity<12.5:
                    return 5.88817311194953 + -0.6079581399795373 * volatile_acidity + -0.003224685729383836 * free_sulfur_dioxide + -0.0031064911151206798 * total_sulfur_dioxide
                else: 
                    return 49.0 + 1.125 * fixed_acidity + 95.5 * volatile_acidity + 52.0 * citric_acid + 0.5 * residual_sugar + -2240.0 * chlorides + -3.375 * free_sulfur_dioxide + 0.6875 * total_sulfur_dioxide + 24.0 * density + 7.0 * sulphates + 2.5 * alcohol
            else: 
                if pH<3.54:
                    if volatile_acidity<0.66:
                        return 5.903782208569027 + -3.7883576437805004 * chlorides + -0.006495817383012137 * total_sulfur_dioxide + 0.7855253669761169 * sulphates
                    else: 
                        return -34.72879124575002 + -0.13136372649951866 * fixed_acidity + 1.112626981895282 * volatile_acidity + -1.6438754031990186 * citric_acid + -0.2178024309487263 * residual_sugar + -13.188780905051772 * chlorides + 0.0006783438761825966 * free_sulfur_dioxide + 0.009260608736105236 * total_sulfur_dioxide + 41.28238814843053 * density + 1.2413974255164248 * sulphates
                else: 
                    if sulphates<0.66:
                        return 3.5
                    else: 
                        return 307.0 + -27.1875 * fixed_acidity + -73.125 * volatile_acidity + 250.0 * residual_sugar + -672.0 * chlorides + -0.46875 * free_sulfur_dioxide + 0.2421875 * total_sulfur_dioxide + -11.0 * density + -1.0 * sulphates + -2.375 * alcohol
    else: 
        if sulphates<0.59:
            if volatile_acidity<1.02:
                if volatile_acidity<0.46:
                    return 82.64799969980959 + 0.14390484488920663 * fixed_acidity + 0.7177207973998065 * volatile_acidity + 0.03792799035939254 * residual_sugar + -4.338341847819265 * chlorides + -0.008095497364438486 * free_sulfur_dioxide + 0.0041854662852358615 * total_sulfur_dioxide + -84.46563213481568 * density + 1.6396692136746935 * pH + -2.805441194924697 * sulphates + 0.18929978617836696 * alcohol
                else: 
                    return 4.396238935955575 + 0.9798713543765949 * volatile_acidity + 0.13923299060645888 * citric_acid + -0.0807111050201672 * residual_sugar + 3.961316049701068 * chlorides + 0.028950899111668704 * free_sulfur_dioxide + -0.005758161277995111 * total_sulfur_dioxide
            else: 
                return 1.9375 + -2.5 * fixed_acidity + 13.5 * volatile_acidity + 208.0 * citric_acid + -2.125 * residual_sugar + 232.0 * chlorides + -1.125 * free_sulfur_dioxide + 8.0 * density + -4.875 * pH + 14.0 * sulphates
        else: 
            if alcohol<11.6:
                if total_sulfur_dioxide<55:
                    if volatile_acidity<0.38:
                        if pH<3.26:
                            return -14.720299221924506 + 0.4940550856408663 * fixed_acidity + 6.422086147301343 * volatile_acidity + -3.1290798481477395 * citric_acid + -0.07712060301230395 * residual_sugar + -4.963257077410162 * chlorides + -0.03057972073656856 * free_sulfur_dioxide + -12.498113242094405 * density + 4.387679207116889 * pH + 0.10781780456909473 * sulphates + 1.4271503887921426 * alcohol
                        else: 
                            return -12.68906348231394 + -0.25019297431396126 * fixed_acidity + -0.7234586488500554 * citric_acid + 0.28326023928609345 * residual_sugar + 0.0027382231274124536 * free_sulfur_dioxide + -0.01545657428391678 * total_sulfur_dioxide + 4.475124300927746 * sulphates + 1.6049673127349706 * alcohol
                    else: 
                        return -4.236062106268946 + -0.05408783686741003 * fixed_acidity + 0.7221522043211337 * citric_acid + 0.13395266322367405 * residual_sugar + -1.4069493993206947 * chlorides + 8.340577452880098 * density + 1.116494350998778 * pH + -0.15476116380705207 * alcohol
                else: 
                    return 7.196577898793578 + 0.05416209487658552 * fixed_acidity + 0.7651791603613844 * volatile_acidity + 0.6538425309478839 * citric_acid + 0.029222245144605807 * free_sulfur_dioxide + -0.0139626238163163 * total_sulfur_dioxide + -0.7630103104745274 * pH + 0.19497984794679724 * sulphates
            else: 
                if total_sulfur_dioxide<20:
                    return 5.216518852124409 + 0.1462270953322502 * residual_sugar + 0.08861092142137039 * free_sulfur_dioxide + -0.9685478328301258 * sulphates + 0.12528164428664468 * alcohol
                else: 
                    if sulphates<0.74:
                        return 6.7005862515197805 + 0.15319069110728734 * residual_sugar + 0.0058511023999503475 * total_sulfur_dioxide + -1.874860231932871 * sulphates + -0.006750903786212348 * alcohol
                    else: 
                        if fixed_acidity<13.5:
                            return 90.39404745897627 + 0.02827002724879435 * fixed_acidity + 0.3010972811858892 * citric_acid + -4.951521290083747 * chlorides + -0.023998343231249386 * free_sulfur_dioxide + 0.0054902153483578076 * total_sulfur_dioxide + -80.78902610848309 * density + -1.9228342602273187 * pH + -1.348419731081833 * sulphates + 0.3746813872016901 * alcohol
                        else: 
                            return 5.0
