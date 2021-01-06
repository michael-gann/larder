"""create_recipe_ingredients_table

Revision ID: bb4bb5e1857e
Revises: 5ec3d62ade65
Create Date: 2021-01-05 20:33:57.959720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb4bb5e1857e'
down_revision = '5ec3d62ade65'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recipe_ingredients',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('recipe_id', sa.Integer(), nullable=False),
                    sa.Column('ingredient_id', sa.Integer(), nullable=False),
                    sa.Column('measurement_id', sa.Integer(), nullable=False),
                    sa.Column('quantity', sa.Integer(), nullable=False),
                    sa.Column('created_at', sa.DateTime(),
                              server_default=sa.text('now()'), nullable=True),
                    sa.Column('updated_at', sa.DateTime(),
                              server_default=sa.text('now()'), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['ingredient_id'], ['ingredients.id'], ),
                    sa.ForeignKeyConstraint(['measurement_id'], [
                                            'measurements.id'], ),
                    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipe_ingredients')
    # ### end Alembic commands ###