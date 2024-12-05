def add_article(article_id,created_at,state=0):
    with open(f"./DB/articles.txt", "a") as f:
        f.write(f"{article_id}::{created_at}::{state}\n")

    
def creer_article_file(article_id,title,content,user,tags,views=0):
    with open(f"./DB/articles/{article_id}.txt", "w") as f:
        tags = ",".join(tags)
        f.write(f"{title}::{content}::{user}::{tags}::{views}\n")
        
def article_exists(article_id):
    with open("./DB/articles.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            # id, _, _ = line.strip().split("::")
            id= line.strip().split("::")[0]
            if id == article_id:
                return True
    return False

def get_article_by_id(article_id):
    article = None
    with open(f"./DB/articles/{article_id}.txt", "r") as f:
        lines = f.readlines()
        article = lines[0].strip().split("::")
    return article

def increment_article_view(article_id):
    with open(f"./DB/articles/{article_id}.txt", "r") as f:
        lines = f.readlines()
        article = lines[0].strip().split("::")
        views = int(article[-1]) + 1
        article[-1] = str(views)
    with open(f"./DB/articles/{article_id}.txt", "w") as f:
        f.write("::".join(article))