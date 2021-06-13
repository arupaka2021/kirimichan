import cv2

##### img = cv2.imread("C:/Users/Owner/Downloads/shiru1.jpeg")
# 「upload_img.html」から受け取った画像データ「food_img」を読み込み、img変数に格納
img = cv2.imread("food_img")

# img変数に格納した画像データを指定したディレクトリに出力
cv2.imwrite("image/shiru1.jpeg", img)