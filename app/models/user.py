from conects import conect

class User(conect.Model):
    __tablename__ = "Users"
    username = conect.Column(conect.String(80), unique=True,primary_key=True)
    pw_hash = conect.Column(conect.String(80))

    def __init__ (self,username,pw_hash):
        self.username=username
        self.pw_hash=pw_hash

