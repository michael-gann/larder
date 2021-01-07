from flask import Blueprint, jsonify, request
from app.models import PantryIngredient, db
from sqlalchemy.orm import selectinload
from app.forms import PantryItemsForm


pantry_routes = Blueprint('pantries', __name__)


@pantry_routes.route("user-pantry", methods=["GET"])  # get a users pantry
def pantry():

    userId = request.args.get("userId")

    pantry_ingredients = PantryIngredient.query.filter_by(
        user_id=userId).options(
        selectinload(PantryIngredient.ingredients),
        selectinload(PantryIngredient.measurements)).all()

    return jsonify([{**ingredient.to_dict()}
                    for ingredient in pantry_ingredients])


# submit a new item to pantry or update existing
@pantry_routes.route("add-to-pantry", methods=["PUT"])
def post_pantry():
    form = PantryItemsForm()

    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():

        ingredient_quantities = {}

        for pantry_ingredient in form.pantry_ingredients.entries:

            db_pantry_ingredient = PantryIngredient.query.filter_by(
                user_id=pantry_ingredient.user_id.data,
                ingredient_id=pantry_ingredient.ingredient_id.data).first()

            if db_pantry_ingredient is None:

                # query for data, if none, add it, if there, update? maybe frontend check post vs put
                db_pantry_ingredient = PantryIngredient(
                    user_id=pantry_ingredient.user_id.data,
                    ingredient_id=pantry_ingredient.ingredient_id.data,
                    measurement_id=pantry_ingredient.measurement_id.data,
                    quantity=pantry_ingredient.quantity.data
                )
                ingredient_quantities[pantry_ingredient.ingredient_id.data] = pantry_ingredient.quantity.data
                db.session.add(db_pantry_ingredient)
            else:
                db_pantry_ingredient.quantity += pantry_ingredient.quantity.data
                ingredient_quantities[pantry_ingredient.ingredient_id.data] = db_pantry_ingredient.quantity
            db.session.commit()

        return ingredient_quantities
        # send list of added pantry_ingredients and ingredients that need to be updated
    return {'errors': ['Internal Server Error']}, 500


# @ pantry_routes.route("update-pantry", methods=["PUT"])
# def put_pantry():

#     form = PantryIngredientForm()

#     form['csrf_token'].data = request.cookies['csrf_token']

#     if form.validate_on_submit():
#         pantry_update = PantryIngredient(
#             user_id=form.user_id.data,
#             ingredient_id=form.ingredient_id.data,
#             measurement_id=form.measurement_id.data,
#             quantity=form.quantity.data
#         )

#         db.session.add(pantry_update)
#         db.session.commit()

#         return pantry_update.to_dict()
#     return {'errors': ['Internal Server Error']}, 500