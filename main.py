from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()



class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
    

my_posts = [{'title': 'title of the post 1', 'content': 'content of the post 1', 'id': 1}, {'title': 'title of the post 2', 'content': 'content of the post 2', 'id': 2}]

@app.post('/posts')
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(1, 1000000)
    my_posts.append(post_dict)
    return {"data" : my_posts}




@app.post('/n_posts')
def create_post(post: Post):
    # print(new_post)
    # print(new_post.published)
    print(post.rating)
    print(post.dict())
    return {'data': post}

# request Get method url: "/"

@app.get("/")
def read_root():
    message = {
        'name' : "Md Al Amin",
        'age' : 22
    }
    return {"messages" : message}

@app.get('/posts')
def get_posts(): # path operation Function
    return {'data' : my_posts}


"""
# get request simply do: its request to retrive data form api-server
get <------------------------------------ api-server

post request sand the data to api server
post{conten} ------------------------------> api-server
"""

# @app.post('/createposts')
# def create_post(payLoad : dict = Body(...)): # path operation Function
#     print(payLoad)
#     # return {'post' : 'Alhamdulilla successfully create a post'}
#     return f'''
# This is the post content form backend and the 
# title: {payLoad['title']} 
# and the content is
# {payLoad['content']}


# '''

