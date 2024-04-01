def productEntity(doc)->dict:
    return{
        "id":str(doc["_id"]),
        "product_name":doc['product_name'],
        "product_price":doc['product_price'],
       "usecase":doc['usecase'],
    }

def productsEntity(docs)->list:
    return [productEntity(doc) for doc in docs]