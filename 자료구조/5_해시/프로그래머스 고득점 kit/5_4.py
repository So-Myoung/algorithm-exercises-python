
# 프로그래머스 알고리즘 고득점 kit
# 해시 - 베스트앨범 : Level 3

# genres_dic : {'classic': [(0, 500), (2, 150), (3, 800)], 'pop': [(1, 600), (4, 2500)]}
# plays_dic : {'classic': 1450, 'pop': 3100}

def solution(genres, plays):
    res = []
    genres_dic = {}
    plays_dic = {}

    for i in range(len(genres)):
        genre, play = genres[i], plays[i]

        if genre not in genres_dic:
            genres_dic[genre] = []
            plays_dic[genre] = 0
        genres_dic[genre].append((i, play))
        plays_dic[genre] += play

    sorted_genres = sorted(plays_dic.items(), key=lambda x: x[1], reverse=True)

    for genre, _ in sorted_genres:
        best_songs = sorted(genres_dic[genre], key=lambda x: (-x[1],x[0]))
        res.extend([i for i, _ in best_songs[:2]])

    return res




def main():
    # 테스트 케이스 1
    print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))


if __name__ == "__main__":
    main()
