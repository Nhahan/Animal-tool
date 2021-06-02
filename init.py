from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

# 파일 첫 실행 때 돌려주세요!

db.visitorCounter.insert_one({'Counts': 0})
db.visitorsToday.insert_one({'today date': "2021-05-30"})
db.todayCounter.insert_one({'todayCounts': 0})
db.visitorIP.insert_one({'IP': 0})
db.visitorIP.remove()
db.final_result.insert_one({"type": "반들반들 청결 펭귄형", "counts": 0})
db.final_result.insert_one({"type": "영타 500타 원숭이형", "counts": 0})
db.final_result.insert_one({"type": "수다쟁이 앵무새형", "counts": 0})
db.final_result.insert_one({"type": "워라밸 판다형", "counts": 0})
db.final_result.insert_one({"type": "사무실 마이홈 코알라형", "counts": 0})
db.final_result.insert_one({"type": "유아독존 고양이형", "counts": 0})
db.final_result.insert_one({"type": "탕비실 지박령 다람쥐형", "counts": 0})
db.final_result.insert_one({"type": "충혈된 카멜레온형", "counts": 0})
db.final_result.insert_one({"type": "빡! 집중 고슴도치형", "counts": 0})
db.final_result.insert_one({"type": "호기심 많은 미어캣형", "counts": 0})
db.final_result.insert_one({"type": "안마의자 마니아 캥거루형", "counts": 0})
db.final_result.insert_one({"type": "근면성실 꿀벌형", "counts": 0})
db.final_result.insert_one({"type": "야근요정 부엉이형", "counts": 0})
db.final_result.insert_one({"type": "금강산도 식후경 돼지형", "counts": 0})
db.total_count.insert_one({"total_count": 0})