# 베스트 앨범엔 장르 별로 가장 많이 재생된 노래 2개 수록
# 1. 많이 재생된 장르 순대로 수록
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록
# 3. 장르 내에서 재생횟수가 같은 노래 중에서는 고유번호가 낮은 노래를 먼저 수록

# infos
# {
#   "classic": {
#       "cnt": XXX,
#       "priorities": [{"cnt": XX, "id": XX}, {"cnt": XX, "id": XX} , ...]
#   }
# }

def solution(genres, plays):
    answer = []
    plays_by_genre = dict()
    
    for i in range(len(genres)):
        current_genre = genres[i]
        played_times = plays[i]
        if current_genre in plays_by_genre:
            plays_by_genre[current_genre]["cnt"] += played_times
            plays_by_genre[current_genre]["priorities"].append({"cnt": played_times, "id": i})
        else:
            plays_by_genre[current_genre] = dict()
            plays_by_genre[current_genre]["cnt"] = played_times
            plays_by_genre[current_genre]["priorities"] = [{"cnt": played_times, "id": i}]
    
    for genre_name, val in plays_by_genre.items():
        val["priorities"].sort(key=lambda x: [-x["cnt"], x["id"]])
    
    # 가장 많이 재생된 장르 순서 정렬
    desc_most_played_genres = sorted(plays_by_genre, key=lambda x: -plays_by_genre[x]["cnt"])
    
    for genre_name in desc_most_played_genres:
        songs_list = plays_by_genre[genre_name]["priorities"]
        best_song_id = songs_list[0]["id"]
        answer.append(best_song_id)
        if len(songs_list) >= 2:
            secondary_song_id = songs_list[1]["id"]
            answer.append(secondary_song_id)
    
    
    return answer