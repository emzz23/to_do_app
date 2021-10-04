from fastapi import FastAPI
from enum import Enum
from typing import Optional
from fastapi.param_functions import Query
from pydantic import BaseModel


to_do_list=[]

app=FastAPI()



class Item(BaseModel):
    ind:int
    text: str=None
    status:str="undone"

@app.get("/")
def hello():
    return {"message":"Hello, let's do something!"}

@app.get("/get-all-items")
def get_items():
    return to_do_list

@app.post("/create-item{item_text}")
def create_item(item_text:str,item: Item):   
    if to_do_list==[]:
        item.ind=1
    else :
        item.ind=to_do_list[-1].ind+1  

    item.text=item_text
    to_do_list.append(item)

    return {"message":"Item added!"}


@app.put("/mark-as-done{item_ind}")
def update_item_status(item_ind:int):

    if item_ind>len(to_do_list) or item_ind<1:
        return {"message":"Invalid item index"}

    elif to_do_list[item_ind-1].status=="done":
        return {"message":"It's already done, relax."}

    else:
        to_do_list[item_ind-1].status="done"

    return {"message":"Change saved!"}

@app.put("/update-item{item_ind}/update-txt{update_txt}")
def update_item_text(item_ind:int,update_txt:str):

    if item_ind>len(to_do_list) or item_ind<1:
        return {"message":"Invalid item index"}
    else:
        to_do_list[item_ind-1].text=update_txt

    return {"message":"Change saved!"}


@app.delete("/delete-item{item_ind}")
def delete_item(item_ind:int):
    if item_ind>len(to_do_list) or item_ind<1:
        return {"message":"Invalid item index"}

    if item_ind==len(to_do_list):
        del to_do_list[item_ind-1]
        return {"message":"Item deleted!"}

    for i in range(item_ind,len(to_do_list)):
        to_do_list[i].ind=to_do_list[i].ind-1

    del to_do_list[item_ind-1]
    return {"message":"Item deleted!"}



