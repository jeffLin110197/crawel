import json
import requests
import os
if not os.path.exists("./poya_1"):
    os.mkdir("./poya_1")
# print(os.getcwd())

url = """
https://www.poyabuy.com.tw/webapi/SearchV2/GetShopSalePageBySearch?keyword=%22%E6%B4%97%E9%AB%AE%E7%B2%BE%22&order=Correlation&minPrice=&maxPrice=&shippingType=&payType=&startIndex={}&maxCount=50&displayScore=false&shopCategoryId=0&scoreThreshold=0.8&isResearch=true&locationId=0&tags=&showMoreTagKeys=true&scoreThreshold=0.8&shopId=40916&lang=zh-TW
"""


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

index = 0


for j in range(0, 9):
    res = requests.get(url.format(index), headers=headers)
    jsonStr = res.text
    json_data = json.loads(jsonStr)
    name = json_data["Data"]["SalePageList"]
    for i in name:
        name = i['Title']
        product = "https:" + i['PicUrl']
        # print(product)
        res_url = requests.get(url=product, headers=headers)
        # print(res_url)
        with open("C:/python_class/pythonProject_20220702/poya_1/{}.jpg".format(name.replace("/", "-").replace("*", "")), 'wb') as f:
                                                        #./poya_1/{}.jpg
                                                        # 檔案目錄/檔名
            f.write(res_url.content)
    index = index + 50

