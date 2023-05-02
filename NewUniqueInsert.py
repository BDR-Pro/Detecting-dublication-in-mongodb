
def UniqueInsert(collection,list_,index,value):        #function to insert the data
    if(inmongo(collection,list_,index,value)==False) :
        try:
            collection.insert_one(list_)
        except Exception:
            collection = db[list_["Series"]] #create collection if not exist
            UniqueInsert(collection,list_,index,value) #insert the data
        return True
    return False    
    
def inmongo(collection,list_,index,value):             #function to check if the data is already in the database
    try:
        search=collection.find_one({index: list_[value]})
    except:
        return search is None
    return search
