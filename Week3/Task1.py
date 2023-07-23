import json
import csv
import urllib.request

# 定義輸出的檔案名稱
attraction_file = 'attraction.csv'
mrt_file = 'mrt.csv'

# 取得網路上的資料
url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'
response = urllib.request.urlopen(url)
data = json.loads(response.read().decode('utf-8'))

# 將景點資料輸出到 attraction.csv 檔案
with open(attraction_file, 'w', encoding='utf-8-sig', newline='') as csvfile:
    writer = csv.writer(csvfile)
# 創建格式欄位
    writer.writerow(['景點名稱', '區域', '經度', '緯度', '第一張圖檔網址'])

# 取得原始json檔案的資料
    for item in data['result']['results']:
        name = item['stitle']
        # 以切片方式取得區域部分
        address = item['address'].split('區')[0] + '區'  
        address = address.replace('臺北市 ', '')

        longitude = item['longitude']
        latitude = item['latitude']
        image_url = item['file']

        # 找到第一個 "http" 和 ".jpg" 的位置
        # 發現jpg字串會抓不到JPG結尾的圖檔, 先將網址都轉為小寫
        image_url_lower = image_url.lower()
        start_index = image_url_lower.find('http')
        end_index = image_url_lower.find('.jpg', start_index)

        # 取得第一個 "http" 到 ".jpg" 的內容, 將.jpg四個字元的位置向後推算
        result = image_url_lower[start_index:end_index + 4]

        writer.writerow([name, address, longitude, latitude, result])

# 建立一個字典來按捷運站名稱分群景點名稱
# 景點數量不一致, 無法先創建格式欄位
mrt_data = {}
for attraction in data["result"]["results"]:
    mrt_station = attraction["MRT"]
    attraction_name = attraction["stitle"]

    if mrt_station in mrt_data:
        mrt_data[mrt_station].append(attraction_name)
    else:
        mrt_data[mrt_station] = [attraction_name]

# 將資料寫入CSV檔案
with open(mrt_file, "w", newline="", encoding="utf-8-sig") as csvfile:  # 使用utf-8-sig來解決CSV的亂碼問題
    writer = csv.writer(csvfile)
    
    # 寫入每一行的內容
    for mrt_station, attractions in mrt_data.items():
        # 在每一行的第一欄位先印出MRT名稱, 接著印景點名稱
        writer.writerow([mrt_station] + attractions)

#陽明山國家公園 MRT為null值