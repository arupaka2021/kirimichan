import re
import get_food_data as dat

food = "uiuii"

# APIから結果を取得
try:
    foods = dat.fs.foods_search(food)
except:
    foods = dat.fs.foods_search("banana")

# 取得したデータをリストに格納
food_list = []

try:
    for food in foods:
        food_list.append([food['food_description']])
except:
    food_list.append(['Per 100g - Calories: 0kcal | Fat: 0g | Carbs: 0g | Protein: 0g'])

# food_list.append([foods['food_description']])

# リストに格納した情報のうち、カロリーのみ取得
res1 = re.sub(r".*Calories", "Calories", food_list[0][0]) #グラム情報の削除
res2s = res1.split('|') #'|'で区切られた文字列を要素とするリストの作成
res3s = re.sub(r'\D', '', res2s[0]) #カロリーのみ抽出

print(res3s)