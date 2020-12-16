import pdb

if __name__ == "__main__":
    with open("2020_12_06.input") as f:
        input_file = f.read()
        pdb.set_trace()
        grps = input_file.split("\n\n")
        grps_fst = ["".join(x.strip() for x in grp.split("\n")) for grp in grps]
    set_grps = [set(grp) for grp in grps_fst]
    n = sum((len(set_g) for set_g in set_grps))
    print(n)

    grps_snd = []
    for grp in grps:
        aux = None
        for x in grp.split("\n"):
            if aux is None:
                aux = set(x)
            else:
                aux &= set(x)
        grps_snd.append(aux)
    pdb.set_trace()
    m = sum((len(set_g) for set_g in grps_snd))
    print(m)

        
