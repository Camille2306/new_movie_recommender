from dotenv import load_dotenv
from service.questionnaire import Questionnaire
from service.importer import ask_update_database
from service.importer import import_movies
from recommender import score_database
from recommender import save_scores
from service.database import connect
from service.database import get_top_movies





DATABASE = "data/movies.db"



update=ask_update_database()
if update==True:
    import_movies()

testquestionnaire = Questionnaire()

answers = testquestionnaire.run()
user = testquestionnaire.build_profile()

print("\nRéponses de l'utilisateur :")

for key, value in answers.items():
    print(f"{key} : {value}")


print("\nProfil de l'utilisateur :")

for key, value in user.__dict__.items():
    print(f"{key} : {value}")


results = score_database(DATABASE, user)

print(f"\n{len(results)} films évalués.")

save_scores(DATABASE, results)

print("\nScores enregistrés dans la table 'scores'.")



connection = connect()

top_movies = get_top_movies(connection)

print("\nVoici les films que nous vous recommandons.")

for movie_id, title, score in top_movies:
    print(f"{title} : {score:.3f}")