"""create_recipe_steps_table

Revision ID: 27ca2257c283
Revises: 5ce46692a2e2
Create Date: 2021-01-05 19:56:01.917494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27ca2257c283'
down_revision = '5ce46692a2e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recipe_steps',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('recipe_id', sa.Integer(), nullable=False),
                    sa.Column('step_number', sa.Integer(), nullable=False),
                    sa.Column('content', sa.String(), nullable=True),
                    sa.Column('created_at', sa.DateTime(),
                              server_default=sa.text('now()'), nullable=True),
                    sa.Column('updated_at', sa.DateTime(),
                              server_default=sa.text('now()'), nullable=True),
                    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipe_steps')
    # ### end Alembic commands ###
