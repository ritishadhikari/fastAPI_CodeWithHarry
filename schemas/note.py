def noteEntity(item:dict) -> dict:
    return {
        "id": str(item["_id"]),
        "title":str(item["title"]),
        "description":str(item["description"]),
        "important":str(item["important"])
    }

def notesEntity(items) -> list:
    return [noteEntity(item) for item in items]