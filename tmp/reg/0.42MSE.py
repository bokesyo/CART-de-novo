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
            return 7.750143099419802 + -0.6285198207973508 * volatile_acidity + -6.25970028077063 * chlorides + -0.5450312756004223 * pH
        else: 
            return 4.084613785142665 + 0.03354798436563344 * fixed_acidity + -0.8718583981253119 * volatile_acidity + -0.7716999201550152 * chlorides + 0.0020211470002418075 * free_sulfur_dioxide + -0.0038222290180742746 * total_sulfur_dioxide + 0.18782676297848866 * alcohol
    else: 
        if sulphates<0.59:
            return 67.35923346963682 + -0.8546006826934827 * volatile_acidity + 0.5286783247509277 * citric_acid + 5.121280238102258 * chlorides + 0.01571653152547503 * free_sulfur_dioxide + 0.0005222358814349071 * total_sulfur_dioxide + -63.9877584760834 * density + -0.18186532584732618 * pH + 0.19901631951768195 * alcohol
        else: 
            return 32.6012181905935 + -0.5146255903668937 * volatile_acidity + -3.095921260462319 * chlorides + -0.0016548993713505489 * free_sulfur_dioxide + -0.006877825926877357 * total_sulfur_dioxide + -29.217425669870863 * density + 0.881130839935695 * sulphates + 0.2482027203785151 * alcohol
