# fatsecretAPIを使用して食べ物のカロリーを取得する関数
def get_calorie(food="banana"):
    import re
    import get_food_data as dat

    # APIから結果を取得
    foods = dat.fs.foods_search(food)
    
    # 取得したデータをリストに格納
    food_list = []

    for food in foods:
        food_list.append([food['food_description']])

    # リストに格納した情報のうち、カロリーのみ取得
    res1 = re.sub(r".*Calories", "Calories", food_list[0][0]) #グラム情報の削除
    res2s = res1.split('|') #'|'で区切られた文字列を要素とするリストの作成
    res3s = re.sub(r'\D', '', res2s[0]) #カロリーのみ抽出

    return res3s