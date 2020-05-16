

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

    a = 1 * 140.82971915672533 + fixed_acidity * 0.331140924451347 + volatile_acidity * 3.708134600444282 + citric_acid * -2.83168624396194 + residual_sugar * -0.24057021849233706 + chlorides * 13.773210860548716 + free_sulfur_dioxide * 0.01674923953530083 + total_sulfur_dioxide * -0.008420173733650671 + density * -142.17330442531966 + pH * 1.2553122583640288 + sulphates * 0.8147788260259858 + alcohol * -0.11848622474826698
    b = 1 * -31.58047807731782 + fixed_acidity * -0.0017139313135317025 + volatile_acidity * -0.6258515469431813 + citric_acid * -0.3902393936516546 + residual_sugar * 0.050064603824672815 + chlorides * 0.5115696335035196 + free_sulfur_dioxide * -0.006236387584144243 + total_sulfur_dioxide * -0.0017447501751078343 + density * 35.29131409333786 + pH * 0.2986092983605886 + sulphates * 0.21331855581448167 + alcohol * 0.10891241256581452
    c = 1 * -74.20194581122996 + fixed_acidity * -0.0993269987548171 + volatile_acidity * -0.23347531296400348 + citric_acid * -1.2001842941535301 + residual_sugar * 0.06961736256233308 + chlorides * -6.596262368131647 + free_sulfur_dioxide * 0.016339285798199654 + total_sulfur_dioxide * -0.01064551502062372 + density * 92.70396539683134 + pH * -2.6796589876815418 + sulphates * -0.9008090285637991 + alcohol * -0.15352000080019934
    d = 1 * 532.5437304982916 + fixed_acidity * 0.8790576288220109 + volatile_acidity * -3.188155940035358 + citric_acid * -11.953823498697602 + residual_sugar * 0.25325164531119526 + chlorides * -44.73740381380776 + free_sulfur_dioxide * -0.1466177724141744 + total_sulfur_dioxide * 0.045174418978490394 + density * -480.05843803845346 + pH * -6.072100219593267 + sulphates * -4.901800255562648 + alcohol * -2.2130301238794345
    e = 1 * 170.0 + fixed_acidity * -3.25 + volatile_acidity * -6.25 + citric_acid * 41.5 + residual_sugar * -41.0 + chlorides * 0.0 + free_sulfur_dioxide * 0.65625 + total_sulfur_dioxide * -0.75 + density * 4.0 + pH * -2.0 + sulphates * 12.0 + alcohol * -4.5
    f = 1 * -208.8673781619582 + fixed_acidity * -0.11331971427037502 + volatile_acidity * -0.16092397562924532 + citric_acid * -0.4117445005866216 + residual_sugar * -0.14570905097635034 + chlorides * 0.43372060615445207 + free_sulfur_dioxide * 0.012581193694065074 + total_sulfur_dioxide * -0.00045747010716073316 + density * 223.1068371303263 + pH * -1.9187684441761803 + sulphates * -0.26725027666338974 + alcohol * -0.08349363648483177
    g = 1 * -14.611084736985504 + fixed_acidity * -0.4796826729520234 + volatile_acidity * 0.31350106960633184 + citric_acid * 0.06467596470253056 + residual_sugar * -0.278108182185953 + chlorides * 17.63099787377695 + free_sulfur_dioxide * -0.021287261296320192 + total_sulfur_dioxide * -0.005342124521299674 + density * 33.67731921249651 + pH * -3.9982821980229915 + sulphates * 5.551706100487166 + alcohol * 0.05377247448785738
    h = 1 * -25.759498439147137 + fixed_acidity * -0.024289114178941418 + volatile_acidity * 0.7087566573147228 + citric_acid * 1.7958965024629379 + residual_sugar * -0.12420203249720885 + chlorides * 0.5949098840628722 + free_sulfur_dioxide * 0.03527963459233874 + total_sulfur_dioxide * -0.004088724443967351 + density * 27.664969406556338 + pH * 0.2295902028299679 + sulphates * -1.9955102400133455 + alcohol * 0.2874571090876543
    i = 1 * 3520.0 + fixed_acidity * 54.0 + volatile_acidity * 352.0 + citric_acid * 5888.0 + residual_sugar * -240.0 + chlorides * -7168.0 + free_sulfur_dioxide * -4.625 + total_sulfur_dioxide * 1.625 + density * 131.0 + pH * 50.0 + sulphates * 26.0 + alcohol * -14.0
    j = 1 * -285.0 + fixed_acidity * -0.609375 + volatile_acidity * -78.0 + citric_acid * 0.125 + residual_sugar * 2.375 + chlorides * -18.5 + free_sulfur_dioxide * -0.375 + total_sulfur_dioxide * 0.130859375 + density * 418.25 + pH * 39.5 + sulphates * 14.5 + alcohol * 1.96875
    k = 1 * 356.0 + fixed_acidity * -0.015625 + volatile_acidity * 3.0 + citric_acid * 13.75 + residual_sugar * -0.125 + chlorides * 56.0 + free_sulfur_dioxide * 0.0390625 + total_sulfur_dioxide * -0.01171875 + density * -608.0 + pH * 8.125 + sulphates * -4.0 + alcohol * 0.1875
    l = 1 * -296.77233119437005 + fixed_acidity * -0.264589463335966 + volatile_acidity * -2.2516085457791633 + citric_acid * -1.8006685096945603 + residual_sugar * -0.16681936310902756 + chlorides * 5.219539635297679 + free_sulfur_dioxide * -0.012382850282484092 + total_sulfur_dioxide * 0.0025366285564543123 + density * 295.1524180023116 + pH * 0.6880901376624706 + sulphates * 1.323793638079394 + alcohol * 0.8422742641671448
    m = 1 * -692.0 + fixed_acidity * 127.75 + volatile_acidity * 912.0 + citric_acid * 420.0 + residual_sugar * -76.0 + chlorides * -160.0 + free_sulfur_dioxide * -1.0 + total_sulfur_dioxide * -5.59375 + density * 5.0 + pH * -8.0 + sulphates * 176.0 + alcohol * -23.125
    n = 1 * 688.9644929250062 + fixed_acidity * 0.20761977797516806 + volatile_acidity * 1.8998177652525783 + citric_acid * 1.5397651495909486 + residual_sugar * 0.08784484142331195 + chlorides * 32.2943884981496 + free_sulfur_dioxide * 0.010719547739264534 + total_sulfur_dioxide * -0.00688281206697372 + density * -675.0609732176526 + pH * -2.5874238173287267 + sulphates * 1.091397172174993 + alcohol * -0.7638215427082287
    o = 1 * 279.81848003440246 + fixed_acidity * 0.18192924135161093 + volatile_acidity * 1.949217620514787 + citric_acid * 1.8275572590322327 + residual_sugar * 0.16675591169961024 + chlorides * -2.084806104950445 + free_sulfur_dioxide * -0.030620290100578984 + total_sulfur_dioxide * -0.00376721579572159 + density * -279.37515362520935 + pH * 1.8618131162393183 + sulphates * 2.1866028415372014 + alcohol * -0.45126792854989617
    p = 1 * 10.577810475238948 + fixed_acidity * -0.4186104066239409 + volatile_acidity * 1.777654557576966 + citric_acid * 1.7086524504795548 + residual_sugar * 0.019219348498339173 + chlorides * -14.540100500074914 + free_sulfur_dioxide * -0.008439358050116641 + total_sulfur_dioxide * 0.00653782340537945 + density * 4.0946524778119056 + pH * -2.894118289957987 + sulphates * 1.4525692595948954 + alcohol * 0.2631059450543489

    if alcohol<10.5:
        if volatile_acidity<0.32:
            return a
        else: 
            if volatile_acidity<0.67:
                if alcohol<9.9:
                    return b
                else: 
                    if sulphates<0.69:
                        return c
                    else: 
                        if free_sulfur_dioxide<32:
                            return d
                        else: 
                            return e
            else: 
                return f
    else: 
        if sulphates<0.59:
            if volatile_acidity<1.02:
                if pH<3.37:
                    return g
                else: 
                    return h
            else: 
                return i
        else: 
            if alcohol<11.6:
                if total_sulfur_dioxide<58:
                    if residual_sugar<5.5:
                        if pH<3.2:
                            if volatile_acidity<0.4:
                                return j
                            else: 
                                return k
                        else: 
                            return l
                    else: 
                        return m
                else: 
                    return n
            else: 
                if free_sulfur_dioxide<15:
                    return o
                else: 
                    return p
