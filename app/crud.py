from . import models

def create_contact(db, contact_data):
    contact = models.Contact(**contact_data.dict())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact

def create_newsletter(db, email):
    entry = models.Newsletter(email=email.email)
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry

def create_blog(db, data):
    blog = models.Blog(**data.dict())
    db.add(blog)
    db.commit()
    return blog

def create_comment(db, data):
    comment = models.Comment(**data.dict())
    db.add(comment)
    db.commit()
    return comment
