from util_methods import *
import psycopg2
import argparse


class DB:
    def __init__(self, movies: list, rating: float | None):
        self._movies = movies
        self._rating = rating
        self._params = get_config()
        self._conn = psycopg2.connect(**self._params)
        self._curs = self._conn.cursor()

    def retrieve_all_movies(self):
        with self._conn as conn:
            with self._curs as curs:
                curs.execute("SELECT * FROM imdb_top")
                result = curs.fetchall()
        conn.close()
        return result

    def retrieve_rating_specific_movies(self):
        with self._conn as conn:
            with self._curs as curs:
                curs.execute(f"SELECT * FROM imdb_top WHERE rating > {self._rating}")
                result = curs.fetchall()
        conn.close()
        return result

    def check_movie_name(self):
        results = []
        for movie in self._movies:
            with self._conn as conn:
                with self._curs as curs:
                    query = "SELECT exists (SELECT movie_name FROM imdb_top WHERE movie_name ILIKE %s);"
                    curs.execute(query, (f"%{movie}%", ))
                    results.append(curs.fetchone())
            conn.close()
        return results


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="IMDB DB CLI",
                                     description="Check movies db")

    parser.add_argument('-m', '--movies',
                        nargs='*',
                        help='check if a movie name exists in top 250 IMDB db')
    parser.add_argument('-r', '--rating',
                        help='display all movies with rating > value',
                        default=None)

    args = parser.parse_args(['-m', 'the godfather'])

    # SQL injection:
    # args = parser.parse_args(['-m', "godfather'); CREATE TABLE test (test int, test2 int); "
    #                                 "SELECT * from imdb_top WHERE "
    #                                 "movie_name = ('"])

    db = DB(movies=args.movies, rating=args.rating)

    if args.movies:
        print(db.check_movie_name())

    if args.rating:
        print(db.retrieve_rating_specific_movies())

    if args.movies == args.rating is None:
        print(db.retrieve_all_movies())
