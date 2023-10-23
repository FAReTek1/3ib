import requests
data = {
    'url': r'https://2016.filemail.com/api/file/get?filekey=MO5z7tQoY9P45Km2SgyjUFKqhdOZ03Ub1g9AFDoSCK-o-0yFxsBZ9tpdYZYBC60KXWI871qEXOgMDAuR&pk_vid=588068b070a02cd41697905181181e85',
    'return': 'youtube',
    'api_token': '07c708cae47b23720bc1d4df050e6492'
}
result = requests.post('https://api.audd.io/', data=data)
print(result.text)