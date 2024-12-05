def input_article():
    title = input("Entrer le titre de l'article : ")
    content = input("Entrer le contenu de l'article : ")
    return title, content


def input_tag():
    tags = []
    i = 0
    while True:
        i += 1
        tag = input(f"Entrer un tag {i} ['Entree' pour arreter] : ")
        if tag == "":
            break
        tags.append(tag)
    return tags

def print_article(article):
    title, content, user, tags, views = article
    print(f"Titre : {title}")
    print(f"Contenu : {content}")
    print(f"Créé par : {user}")
    print(f"Tags : {tags}")
    print(f"Vues : {views}")
    