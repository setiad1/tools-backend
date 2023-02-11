"""empty message

Revision ID: 5dba5ccba0e7
Revises: 019fd68d90b0
Create Date: 2023-02-11 09:40:50.446851

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5dba5ccba0e7'
down_revision = '019fd68d90b0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ref_user_group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('group_name', sa.String(length=50), nullable=False),
    sa.Column('group_description', sa.String(length=225), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ref_user_group_group_name'), 'ref_user_group', ['group_name'], unique=True)
    op.create_index(op.f('ix_ref_user_group_id'), 'ref_user_group', ['id'], unique=False)
    op.create_table('ref_user_id_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_type', sa.String(length=50), nullable=False),
    sa.Column('id_description', sa.String(length=225), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ref_user_id_type_id'), 'ref_user_id_type', ['id'], unique=False)
    op.create_index(op.f('ix_ref_user_id_type_id_type'), 'ref_user_id_type', ['id_type'], unique=True)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('group_id', sa.Integer(), server_default='4', nullable=True),
    sa.Column('id_type', sa.Integer(), nullable=True),
    sa.Column('id_number', sa.String(length=50), nullable=True),
    sa.Column('phone', sa.String(length=15), nullable=True),
    sa.Column('address', sa.TEXT(), nullable=True),
    sa.Column('status', sa.Enum('enabled', 'disabled'), server_default='disabled', nullable=False),
    sa.Column('creator', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('editor', sa.Integer(), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['ref_user_group.id'], ),
    sa.ForeignKeyConstraint(['id_type'], ['ref_user_id_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_group_id'), 'user', ['group_id'], unique=False)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_index(op.f('ix_user_id_number'), 'user', ['id_number'], unique=False)
    op.create_index(op.f('ix_user_id_type'), 'user', ['id_type'], unique=False)
    op.create_index(op.f('ix_user_name'), 'user', ['name'], unique=False)
    op.create_index(op.f('ix_user_status'), 'user', ['status'], unique=False)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('user_activation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('acticode', sa.String(length=255), nullable=False),
    sa.Column('expired', sa.DateTime(timezone=True), nullable=True),
    sa.Column('activated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('status', sa.Enum('activated', 'inactivated'), server_default='inactivated', nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('acticode')
    )
    op.create_index(op.f('ix_user_activation_id'), 'user_activation', ['id'], unique=False)
    op.create_index(op.f('ix_user_activation_user_id'), 'user_activation', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_activation_user_id'), table_name='user_activation')
    op.drop_index(op.f('ix_user_activation_id'), table_name='user_activation')
    op.drop_table('user_activation')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_status'), table_name='user')
    op.drop_index(op.f('ix_user_name'), table_name='user')
    op.drop_index(op.f('ix_user_id_type'), table_name='user')
    op.drop_index(op.f('ix_user_id_number'), table_name='user')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_group_id'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_ref_user_id_type_id_type'), table_name='ref_user_id_type')
    op.drop_index(op.f('ix_ref_user_id_type_id'), table_name='ref_user_id_type')
    op.drop_table('ref_user_id_type')
    op.drop_index(op.f('ix_ref_user_group_id'), table_name='ref_user_group')
    op.drop_index(op.f('ix_ref_user_group_group_name'), table_name='ref_user_group')
    op.drop_table('ref_user_group')
    # ### end Alembic commands ###
