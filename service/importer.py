#ce fichier fait le lien entre le fichier qui récupère les infos API 
# et celui qui construit la base de données.

#le fichier qui permet de récupérer toutes les infos des films via l'API
from service.api_client import discover_movies
from service.api_client import get_movie_details

#le fichier qui permet de gérer la base de données SQLite
from service.database import connect
from service.database import create_tables
from service.database import insert_movie


def ask_update_database():
    """
    Demande à l'utilisateur s'il souhaite mettre à jour la base de données.

    Retourne :
        True si oui
        False si non
    """

    while True:
        answer = input("Souhaitez-vous mettre à jour la base de données de films ? Cela peut prendre plusieurs minutes.(o/n) : ").strip().lower()

        if answer in ("o", "oui", "y", "yes"):
            return True

        elif answer in ("n", "non", "no"):
            return False

        print("Réponse invalide. Veuillez répondre par 'o' ou 'n'.")


def import_movies():

    connection = connect()

    create_tables(connection)

    NUMBER_OF_PAGES = 100

    for page in range(1, NUMBER_OF_PAGES + 1):

        print(f"Téléchargement page {page}")

        movies = discover_movies(page)

        for movie in movies["results"]:

            details = get_movie_details(movie["id"])

            insert_movie(connection, details)

    connection.close()

    print("Import terminé.")




if __name__ == "__main__":

    import_movies()



