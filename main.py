from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
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

def getSinglePost(id):
    for p in my_posts:
        if p['id'] == id:
            return p
        
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

@app.get("/")
def read_root():
    message = {
        'name' : "Md Al Amin",
        'age' : 22
    }
    return {"messages" : message}

@app.post('/posts', status_code=status.HTTP_201_CREATED)
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



@app.get('/posts')
def get_posts(): # path operation Function
    return {'data' : my_posts}

@app.get('/posts/latest')
def get_latest_post():
    post = my_posts[len(my_posts) - 1]
    return post

@app.get('/posts/{id}')
def get_post(id: int, response: Response):
    post = getSinglePost(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")

    return {'post_detail': post}


@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not not exists")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put('/posts/{id}')
def post_update(id: int, post: Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not not exists")
    
    post_dict = post.dict()
    post_dict['id'] = id
    # post_dict['title'] = post.title
    # post_dict['content'] = post.content
    my_posts[index] = post_dict
    
    return {'data' : post_dict}

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

