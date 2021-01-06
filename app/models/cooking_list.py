from .db import db


class Cooking_List(db.Model):
    __tablename__ = 'cooking_lists'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey(
        "recipes.id"), nullable=False)

    users = db.relationship("User", back_populates="cooking_lists")
    recipes = db.relationship("Recipe", back_populates="cooking_lists")
