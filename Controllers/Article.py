from Models import Article as artModel
from Views import Article as artView, Functions as viewFunc
from Controllers import Functions as ctrlFunc
def new_article():
    title,content = artView.input_article()
    if ctrlFunc.check_length("titre", title, 3, 100) == False:
        return
    if ctrlFunc.check_length("contenu", content, 10, 500) == False:
        return
    created_at = ctrlFunc.get_current_date()
    state = 0
    user = "Breukh"
    tags = artView.input_tag()
    for tag in tags:
        if ctrlFunc.check_length("tag", tag, 3, 15) == False:
            return
    views = 0
    article_id = ctrlFunc.generate_id()

    # Ajouter l'article dans la liste des articles
    artModel.add_article(article_id,created_at,state)
    # Creer le fichier ou se trouve les details de l'article:
    artModel.creer_article_file(article_id,title,content,user,tags,views)
    viewFunc.success_message("Article créé avec succès")
    

def print_article():
    article_id = input("Entrer l'ID de l'article : ")
    if ctrlFunc.check_length("id", article_id,14,14) == False:
        return
    if artModel.article_exists(article_id) == False:
        viewFunc.error_message("Article introuvable")
        return
    article = artModel.get_article_by_id(article_id)
    if article == None:
        viewFunc.error_message("Erreur lors de la récupération des données de l'article")
        return
    artView.print_article(article)
    artModel.increment_article_view(article_id)