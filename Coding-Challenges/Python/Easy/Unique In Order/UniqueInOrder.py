def unique_in_order(iterable):
    if iterable == "":
        return []
    a = []
    for i in range(len(iterable)-1):
        if iterable[i] == iterable[i+1]:
            print("")
        else:
            a.append(iterable[i])
    a.append(iterable[-1])
    return a