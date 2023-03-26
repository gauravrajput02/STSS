import requests
input_text = "Ray Serve eases the pain of model serving"
json_data = {
    "image_left": "https://dm0qx8t0i9gc9.cloudfront.net/thumbnails/video/N_-wj6-wx/bangkok-thailand-march-2016-early-morning-traffic-in-bangkok-no-traffic-jam_hxxfzhqqa_thumbnail-1080_01.png",
    "image_right": "https://c8.alamy.com/comp/FXY4EC/buses-cars-in-traffic-jam-baclaran-manila-philippines-05-may-2015-FXY4EC.jpg"
}
result = requests.post(
    "http://127.0.0.1:8000/CustomDesploy", json=json_data).json()
print("Result for '{}': {}".format(input_text, result))
