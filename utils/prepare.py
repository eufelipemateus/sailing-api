def prepare(doc):
    # Alias to _id
    doc['id'] = str(doc['_id'])
    # Delete _id key
    del doc['_id']
    # Return doc
    return doc

def prepareImage(doc):
    doc['id'] = str(doc['_id'])
    doc['image_id'] = str(doc['image_id'])
    doc['boat_id'] = str(doc['boat_id'])
    # Delete _id key
    del doc['_id']
    # Return doc
    return doc
