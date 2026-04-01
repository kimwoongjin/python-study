def get_web(url):
    '''URL 을 넣으면 페이지 내용을 올려주는 함수'''
    import urllib.request
    response = urllib.request.urlopen(url)
    data = response.read()
    decoded = data.decode('utf-8')
    return decoded

url = input('input URL ::: ')
content = get_web(url)
print(content)