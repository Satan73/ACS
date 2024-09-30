from flask_sqlalchemy import SQLAlchemy

# Initialize the database object
db = SQLAlchemy()

class Role(db.Model):
    """
    Role model represents the role table in the database.
    It stores the different roles that users can have, like admin or user.
    """
    __tablename__ = 'roles'  # Define the name of the table

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each role
    name = db.Column(db.String(50), unique=True, nullable=False)  # Role name (must be unique)

    # Define relationship with User
    users = db.relationship('User', backref='role', lazy=True)

    def __repr__(self):
        return f"Role('{self.name}')"

    def __str__(self):
        return self.name
