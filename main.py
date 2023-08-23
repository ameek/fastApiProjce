from fastapi import FastAPI
from models import Todo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello world"}


todos = []

# get all todo
@app.get("/todos")
async def get_todos():
    return{"todos":todos}

# get a single todo
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return({"todo":todo})
    return{"message":"not found"} 

# create a todo
@app.post("/todos")
async def create_todos(todo: Todo):
    todos.append(todo)
    return {"message": "item added"}


# update a todo
@app.put("/todos/{todo_id}") 
async def update_todo(todo_id: int, todo_body: Todo ):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo.id
            todo.item = todo_body.item
            return({"todo":todo,
                    "message": "update sucesssfull"})
    return{"message":"not found"}


# delete a todo
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return{"message":"delete successful"}
    return{"message":"not found"}


# mark done a todo