from app import db
from app.models import User

#jpc=User(username="Jean-Pierre")
#db.session.add(jpc)
#db.session.commit()
users = db.session.query(User).all()
for user in users:
    print(user)
