

def UniqueInsert(collection, list_, index):
    if not inmongo(collection, list_, index):
        try:
            collection.insert_one(list_)
            print(f"inserted {list_}")
        except Exception:
            collection = db[list_["Series"]]
            UniqueInsert(collection, list_)
        return True
    return False


def inmongo(collection, list_, index):
    try:
        search = collection.find_one({index: list_[index]})
    except:
        return False
    if search is not None:
        print(f"found {search}")
        return True
    return False
