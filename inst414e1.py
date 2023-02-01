import json
from statistics import mean

with open("imdb_movies_1985to2022.json", 'r')  as f:
    averages = []
    for line in f:
        movies = json.loads(line)
        for actor in movies['actors']:
            if actor[1] == "Hugh Jackman":
                averages.append(movies['rating']['avg'])
    # print(averages)
    avg = mean(averages)
    print(round(avg, 2))