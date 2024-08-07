from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

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
    return {'data' : 'This is my data post method'}


"""
# get request simply do: its request to retrive data form api-server
get <------------------------------------ api-server

post request sand the data to api server
post{conten} ------------------------------> api-server
"""

@app.post('/createposts')
def create_post(payLoad : dict = Body(...)): # path operation Function
    print(payLoad)
    # return {'post' : 'Alhamdulilla successfully create a post'}
    return f'''
This is the post content form backend and the 
title: {payLoad['title']} 
and the content is
{payLoad['content']}

'''