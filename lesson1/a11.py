# movie_len = int(input("What's the movie length in minutes? "))
# print(f"Easy movie length: {movie_len // 60}:{movie_len % 60}")

movie_len_s = int(input("What's the movie length in seconds? "))
print(f"Easy movie length: {movie_len_s // 3600}:{(movie_len_s % 3600) // 60}:{(movie_len_s % 3600) % 60 }")
