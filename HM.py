import requests
import pandas as pd
import json💥
                                                  💕🤩🤩🤩🤩🤩🤩💕
url = "http://www2.hm.com/it_it/donna/acquista-per-prodotto/abiti/_jcr_content/main/productlisting.display.json"

res =[]
querystring = {"sort":"stock","image-size":"small","image":"model","offset":"36","page-size":"36"}

payload = ""  😏😏
headers = {
    'accept-encoding': 'gzip, deflate, br',
    'cookie': "ak_bmsc=C52FF7F49B1069D0B59EE97AAD7B23CD~000000000000000000000000000000~YAAQLjArF5OaUZSAAQAA4Sczvg9GqpP8vynubQBsUjP+P39sInBYc04ZAtY0CQryWS+51x+li4KcrSkN5DyXcIaBuGYIMVhqmmwt7jIzbTEaGA/YpIWBUx8QUktvNF3IABoEgCCZOKsuATALa0e4VgDcCbKRiroH+Sgpw0eOo4MnChXmwO/GFVWqwMZ46sKVRL7JJX96Etjx9fD7tA9wuo77NudNQhnIepO0Vn/YEa0wmIyf6R5q4WJGUvpMmIIBW0a07fUVMxMKW+SJalQ0JumgUVtubs3GdIueL8ND3epQBwS+daGN8pPl3t3ssGQ3YZUp3uM5JSuxMK/mhh92/sZS246yVVTAmEnAf7ja4RAgWftCsmxeQeeUVC9MWmumYUefXoHvOIKGX8+OgyFH/qp+2zYSCSSca9NWFHMyBgned0yl65k3lFOUwM9pbtedZYp8u5wyo88+wXpb0uSENQM+oU+qmgALVutdWOTjfLeCwrTKZDGL8Q==; HMCORP_locale=it_IT; HMCOUNTRY_name=Italy; AKA_A2=A; bm_sz=8A10CF4C14CDC3CFCED3AB55D17B6B01~YAAQJp4qF8i7vZaAAQAA9I4zvg/K3SRbNIKllMLs3qxyRPOfCp3XLa0R4wQCcxVP8hsBkksacQcEq+d4PnEzScO8TOTEsWqh8Xxcjp+R9Zoev2gx8cldJos9QhuJldJqrWMVZ4epFrmH3J+kuMO6lj1lZYZUPYmb2G+7Q7sZUl+3QCKA2/IZ00sfDj4nKRcasuTW/7e1DM/JAatB5Ti7ytAlhk2AgUmWrH2Q49Pkc8Y8aOp9xHIOVrgYThhQ/9tqFRHb4liJEQR0T0I6vRBp3WclygSdbhFbr7yOQFBwLg==~3556162~3617589; akainst=EU5; INGRESSCOOKIE=1652458495.073.59994.6891^|690fb80ac6d9f7009fc04fa34f769148; _abck=DA5E4AEDA9B01CC41A26EB80D50ACF01~0~YAAQJp4qF9C7vZaAAQAAJZwzvgfBsyOF4jZlk0lt7fzhv32p/DGjVtXS4k9nE0ByWAAIanw08L/sbhd551h9yjw25PirxagagNi1dtfFQ4rSvTYLTVKc4Esb5OVZriaA08MafkYCQRWu4l2wudm012m55yByuw14D4zERWgxEnTfgfEPLLNpTVnYGa52jkdMrjRdvxODexdg9r8S4sH1y6SqrcDib54u673/6RHxMY1v20hU+m6aNKRaw2ynq4hQ7jB3cbfTNMiovZim2LbqY+sOAS5Jztc8fdEvU2UlJXkOqpX93cryOSJNqEU5F2+ab9raOOY9/JNXcFWdCb+pBvwQIzqUac/hLTS26ia1QjgiYX7n8oROQxK+coTN+3Hfa8/StK79o0vgqgRd0Zg/QSUEGFI=~-1~-1~-1; hmid=C2210A63-5C66-434F-90A6-5E3066BF917E; agCookie=c85487bb-70e3-4ff5-a6fe-6b9f977c8e23; JSESSIONID=CE05FEAD90C59A76B4AB729808230DA6D846483F8C9F314813BDF4BD303477443DA03746AF917619E3D53874D0558062D7C7A3B2ACC444B51FEB169EDD9CC965.hybris-ecm-web-6b48766999-w42mk; userCookie=^#^#eyJjYXJ0Q291bnQiOjB9^#^#; hm-italy-favourites=^\^^^; _ga=GA1.2.1279744047.1652458496; OptanonAlertBoxClosed=2022-05-13T16:15:01.580Z; _gid=GA1.2.425570851.1652458507; optimizelyEndUserId=269e2a176c1300000f847e62320100001f360100; AMCVS_32B2238B555215F50A4C98A4^%^40AdobeOrg=1; s_ecid=MCMID^%^7C62185666592463493300951615798332208980; AMCV_32B2238B555215F50A4C98A4^%^40AdobeOrg=359503849^%^7CMCIDTS^%^7C19126^%^7CMCMID^%^7C62185666592463493300951615798332208980^%^7CMCAAMLH-1653063313^%^7C3^%^7CMCAAMB-1653063313^%^7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y^%^7CMCOPTOUT-1652465713s^%^7CNONE^%^7CMCAID^%^7CNONE^%^7CMCCIDH^%^7C1201993770^%^7CvVersion^%^7C5.0.1; _gcl_au=1.1.1091233972.1652458532; _scid=d6f642d9-11f5-43ba-b28c-a8a4993ae4f1; _fbp=fb.1.1652458534604.2067893031; _sctr=1^|1652382000000; _clck=mabbv3^|1^|f1f^|0; _tt_enable_cookie=1; _ttp=698c6853-6b33-4aa0-b50e-3af745dbee0f; _pin_unauth=dWlkPVlXWXlOemxtTnpFdE16ZGhOaTAwTkROaExXRm1ZbUl0TXpBMFlURTJaVEl4WVRnMQ; akavpau_www2_it_it=1652459901~id=c20f82135d16d7a1cfd65f4270e4130b; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+13+2022+21^%^3A33^%^3A20+GMT^%^2B0500+(Pakistan+Standard+Time)&version=6.31.0&isIABGlobal=false&hosts=&consentId=3cf017e3-746e-4690-aad3-96ddf0827bdb&interactionCount=1&landingPath=NotLandingPage&groups=C0001^%^3A1^%^2CC0002^%^3A1^%^2CC0003^%^3A1^%^2CC0004^%^3A1&geolocation=PK^%^3BKP&AwaitingReconsent=false; akamref=; _ga_Z1370GPB5L=GS1.2.1652458495.1.1.1652459602.0; bm_sv=CEF1BF2F87D8B27350EEC04B680E35DD~YAAQBWswF35BzLqAAQAAsodEvg/dd+kRCCVyiWTmEnTKj/Z30q4Hu3tLBhjOxqhtELNbe5eXZSg/BrCpWM34Y1UazQPfBgqv3hjrhDQ8hjPBPdV3K3XLY7TYqjeDEVw5ptVyUd6DqvfTtR+lVamXJGshxnKL5wSqotVUyKZ5zoP0+RnNJy81JBKFeNZOWZhcPSn2qwz3IFj48VtpA8Q6geg2H6nqq8m2P/7cEu2s+vTaaM0/I9ulVBIRLymM~1; RT=^\^z=1",
    'authority': "www2.hm.com",
    'accept': "application/json, text/javascript, */*; q=0.01",
    'accept-language': "en-US,en;q=0.9",
    'referer': "https://www2.hm.com/it_it/donna/acquista-per-prodotto/abiti.html?sort=stock&image-size=small&image=model&offset=0&page-size=36",
    'sec-ch-ua': "^\^",
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
jsondata = json.loads(response.text)                💘💘💢🧡💛💚❤️‍🔥

print(response.text)

api_data = response.json()          🎈🎈🖋️🖋️🖋️

for data in api_data['products']:
    title = data['title']
    categories = data['category']
    price = data['price']
    color = data['swatches'][0]['colorName']
    brandName = data['brandName']
    image = data['image'][0]['src']

    hm_dict ={
        'Product Name': title,
        'Product Categories': categories,
        'Price': price,
        'Color': color,
        'BrandName': brandName,
        'Image': image
    }

    res.append(hm_dict)

df = pd.json_normalize(res)
df.to_csv('hm.csv')

                                            ❌ ❌ ❌ ❌ ❌ ❌