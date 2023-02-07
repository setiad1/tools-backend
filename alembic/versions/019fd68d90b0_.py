"""empty message

Revision ID: 019fd68d90b0
Revises: 
Create Date: 2023-02-07 09:22:53.453829

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '019fd68d90b0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ques_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=255), nullable=False),
    sa.Column('category_description', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ques_category_category'), 'ques_category', ['category'], unique=False)
    op.create_index(op.f('ix_ques_category_id'), 'ques_category', ['id'], unique=False)
    op.create_table('ques_session',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('session', sa.String(length=500), nullable=False),
    sa.Column('session_description', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ques_session_id'), 'ques_session', ['id'], unique=False)
    op.create_index(op.f('ix_ques_session_session'), 'ques_session', ['session'], unique=False)
    op.create_table('ques_question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('question', sa.String(length=500), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['ques_category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ques_question_category_id'), 'ques_question', ['category_id'], unique=False)
    op.create_index(op.f('ix_ques_question_id'), 'ques_question', ['id'], unique=False)
    op.create_index(op.f('ix_ques_question_question'), 'ques_question', ['question'], unique=False)
    op.create_table('ques',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('session_id', sa.Integer(), nullable=True),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('question_status', sa.Enum('enabled', 'disabled'), server_default='enabled', nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['ques_question.id'], ),
    sa.ForeignKeyConstraint(['session_id'], ['ques_session.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ques_id'), 'ques', ['id'], unique=False)
    op.create_index(op.f('ix_ques_question_id'), 'ques', ['question_id'], unique=False)
    op.create_index(op.f('ix_ques_session_id'), 'ques', ['session_id'], unique=False)
    op.create_table('ques_option',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('option', sa.String(length=500), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['ques_question.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ques_option_id'), 'ques_option', ['id'], unique=False)
    op.create_index(op.f('ix_ques_option_option'), 'ques_option', ['option'], unique=False)
    op.create_index(op.f('ix_ques_option_question_id'), 'ques_option', ['question_id'], unique=False)
    op.create_table('ques_answer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('answer', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['answer'], ['ques_option.id'], ),
    sa.ForeignKeyConstraint(['question_id'], ['ques_question.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ques_answer_answer'), 'ques_answer', ['answer'], unique=False)
    op.create_index(op.f('ix_ques_answer_id'), 'ques_answer', ['id'], unique=False)
    op.create_index(op.f('ix_ques_answer_question_id'), 'ques_answer', ['question_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_ques_answer_question_id'), table_name='ques_answer')
    op.drop_index(op.f('ix_ques_answer_id'), table_name='ques_answer')
    op.drop_index(op.f('ix_ques_answer_answer'), table_name='ques_answer')
    op.drop_table('ques_answer')
    op.drop_index(op.f('ix_ques_option_question_id'), table_name='ques_option')
    op.drop_index(op.f('ix_ques_option_option'), table_name='ques_option')
    op.drop_index(op.f('ix_ques_option_id'), table_name='ques_option')
    op.drop_table('ques_option')
    op.drop_index(op.f('ix_ques_session_id'), table_name='ques')
    op.drop_index(op.f('ix_ques_question_id'), table_name='ques')
    op.drop_index(op.f('ix_ques_id'), table_name='ques')
    op.drop_table('ques')
    op.drop_index(op.f('ix_ques_question_question'), table_name='ques_question')
    op.drop_index(op.f('ix_ques_question_id'), table_name='ques_question')
    op.drop_index(op.f('ix_ques_question_category_id'), table_name='ques_question')
    op.drop_table('ques_question')
    op.drop_index(op.f('ix_ques_session_session'), table_name='ques_session')
    op.drop_index(op.f('ix_ques_session_id'), table_name='ques_session')
    op.drop_table('ques_session')
    op.drop_index(op.f('ix_ques_category_id'), table_name='ques_category')
    op.drop_index(op.f('ix_ques_category_category'), table_name='ques_category')
    op.drop_table('ques_category')
    # ### end Alembic commands ###