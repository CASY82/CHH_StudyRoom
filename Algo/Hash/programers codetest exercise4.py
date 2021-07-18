#해시 4 베스트 앨범

    # for i in genres:
    #     try: count[i] += 1
    #     except: count[i] = 1
    #
    # sorted(count.items(), key=lambda x: x)
    # keys = list(count.keys())
    #
    # for i in range(len(keys)):
    #     for j in range(len(genres)):
    #         if genres[j] == keys[i]:
    #             answer.append(j)
    #             print(plays[j], end=' ')
    #
    #
    # return answer



genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def solution(genres, plays):
    # count = {}
    # answer = []
    # element = list(set(genres))
    # numbering = [i for i in range(len(genres))]
    #
    # 필요한 로직을 적어보자
    # 속한 노래가 많이 재생된 장르를 먼저 수록 --> 재생 횟수로 정렬 후, 해당 장르를 우선 배치
    # 장르 내에서 많이 재생된 노래를 먼저 수록 --> 단 넣어주는 시점에서 plays수가 많은 2곡을 넣으면 된다
    # 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록 --> 고유 번호 순서만 넣어주면 될듯
    #
    # dic_total = {plays[i]:genres[i] for i in range(len(genres))}
    # dic_gen = {i:genres[i] for i in range(len(genres))}
    # dic_play = {i:plays[i] for i in range(len(plays))}
    # sort_dic_play = dict(sorted(dic_play.items(), key=lambda x: x[1], reverse=True))
    #
    # return answer

    answer = []
    genre_total_play = {}
    genre_dic = {}
    for i in range(len(genres)):
        if genres[i] not in genre_dic.keys():
            genre_dic[genres[i]] = [(plays[i], i)]
            genre_total_play[genres[i]] = plays[i]
        else:
            genre_dic[genres[i]].append((plays[i], i))
            genre_total_play[genres[i]] = genre_total_play[genres[i]] + plays[i]
    sorted_total_play = sorted(genre_total_play.items(), key=lambda x: x[1], reverse=True)
    print(sorted_total_play)

    for key in sorted_total_play:
        play_list = genre_dic[key[0]]

        play_list = sorted(play_list, key = lambda x : (-x[0], x[1]))

        for i in range(len(play_list)):
            if i == 2:
                break
            answer.append(play_list[i][1])

    return answer

print(solution(genres, plays))