def domain_name(url):
    if url.find('//') != -1:
        url = url.split("//")[1]
    second_arr = url.split('.')
    test = second_arr[0] if second_arr[0] != 'www' else second_arr[1]
    print(second_arr)
    return test