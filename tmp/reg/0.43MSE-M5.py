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
            return 7.837398813878281 + -0.6532827477424377 * volatile_acidity + -6.302732562202095 * chlorides + -0.5645772277764536 * pH
        else: 
            return 4.041868053202961 + 0.038111925327427354 * fixed_acidity + -0.8605596685183201 * volatile_acidity + -0.7796251537303078 * chlorides + 0.001275924239937054 * free_sulfur_dioxide + -0.0037602032467864976 * total_sulfur_dioxide + 0.18847556959843814 * alcohol
    else: 
        if sulphates<0.59:
            return 39.364243497337156 + -0.8667080524269734 * volatile_acidity + 0.5010441532136554 * citric_acid + 0.015034490633167419 * free_sulfur_dioxide + 0.0006993162967562777 * total_sulfur_dioxide + -35.28261115560599 * density + -0.11866196474171176 * pH + 0.16403410270740437 * alcohol
        else: 
            return 33.69352500215609 + -0.6378668970062336 * volatile_acidity + -2.5850764140672027 * chlorides + -0.0020238269308903156 * free_sulfur_dioxide + -0.005995713807091629 * total_sulfur_dioxide + -29.567956152444822 * density + 0.2400634349100983 * alcohol
