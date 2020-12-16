def urlSpaceEncoder(url):
    url = list(url)
    while url[-1] == ' ':
        del url[-1]

    for i in range(0, len(url)):
        if url[i] == ' ':
            url[i] = '%20'

    url = ''.join(url)
    return url

url = str(input())
space_encoded_url = urlSpaceEncoder(url)

print('Space Encoded URL: ' + space_encoded_url)