from ..database.database import engine
from . import blog,user

def run_migration():
    blog.Base.metadata.create_all(engine)
    user.Base.metadata.create_all(engine)   