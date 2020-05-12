def deepGenerate(in_dict):
    keys = list(in_dict.keys())
    out_dict = {}
    for i in keys:
        value = in_dict[i]
        out_dict[i] = value
    return out_dict
