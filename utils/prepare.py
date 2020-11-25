def prepare(doc):
    # Alias to _id
    doc['id'] = str(doc['_id'])
    # Delete _id key
    del doc['_id']
    # Return doc
    return doc