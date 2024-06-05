"""add load balancing

Revision ID: 4e99a8df00ff
Revises: 47cc7df8c4f3
Create Date: 2024-05-10 12:08:09.812736

"""
import sqlalchemy as sa
from alembic import op

import models as models

# revision identifiers, used by Alembic.
revision = '4e99a8df00ff'
down_revision = '64a70a7aab8b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('load_balancing_model_configs',
    sa.Column('id', models.StringUUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('tenant_id', models.StringUUID(), nullable=False),
    sa.Column('provider_name', sa.String(length=255), nullable=False),
    sa.Column('model_name', sa.String(length=255), nullable=False),
    sa.Column('model_type', sa.String(length=40), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('encrypted_config', sa.Text(), nullable=True),
    sa.Column('enabled', sa.Boolean(), server_default=sa.text('true'), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP(0)'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP(0)'), nullable=False),
    sa.PrimaryKeyConstraint('id', name='load_balancing_model_config_pkey')
    )
    with op.batch_alter_table('load_balancing_model_configs', schema=None) as batch_op:
        batch_op.create_index('load_balancing_model_config_tenant_provider_model_idx', ['tenant_id', 'provider_name', 'model_type'], unique=False)

    op.create_table('provider_model_settings',
    sa.Column('id', models.StringUUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('tenant_id', models.StringUUID(), nullable=False),
    sa.Column('provider_name', sa.String(length=255), nullable=False),
    sa.Column('model_name', sa.String(length=255), nullable=False),
    sa.Column('model_type', sa.String(length=40), nullable=False),
    sa.Column('enabled', sa.Boolean(), server_default=sa.text('true'), nullable=False),
    sa.Column('load_balancing_enabled', sa.Boolean(), server_default=sa.text('false'), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP(0)'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP(0)'), nullable=False),
    sa.PrimaryKeyConstraint('id', name='provider_model_setting_pkey')
    )
    with op.batch_alter_table('provider_model_settings', schema=None) as batch_op:
        batch_op.create_index('provider_model_setting_tenant_provider_model_idx', ['tenant_id', 'provider_name', 'model_type'], unique=False)

    with op.batch_alter_table('provider_models', schema=None) as batch_op:
        batch_op.alter_column('provider_name',
               existing_type=sa.VARCHAR(length=40),
               type_=sa.String(length=255),
               existing_nullable=False)

    with op.batch_alter_table('provider_orders', schema=None) as batch_op:
        batch_op.alter_column('provider_name',
               existing_type=sa.VARCHAR(length=40),
               type_=sa.String(length=255),
               existing_nullable=False)

    with op.batch_alter_table('providers', schema=None) as batch_op:
        batch_op.alter_column('provider_name',
               existing_type=sa.VARCHAR(length=40),
               type_=sa.String(length=255),
               existing_nullable=False)

    with op.batch_alter_table('tenant_default_models', schema=None) as batch_op:
        batch_op.alter_column('provider_name',
               existing_type=sa.VARCHAR(length=40),
               type_=sa.String(length=255),
               existing_nullable=False)

    with op.batch_alter_table('tenant_preferred_model_providers', schema=None) as batch_op:
        batch_op.alter_column('provider_name',
               existing_type=sa.VARCHAR(length=40),
               type_=sa.String(length=255),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tenant_preferred_model_providers', schema=None) as batch_op:
        batch_op.alter_column('provider_name',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=40),
               existing_nullable=False)

    with op.batch_alter_table('tenant_default_models', schema=None) as batch_op:
        batch_op.alter_column('provider_name',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=40),
               existing_nullable=False)

    with op.batch_alter_table('providers', schema=None) as batch_op:
        batch_op.alter_column('provider_name',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=40),
               existing_nullable=False)

    with op.batch_alter_table('provider_orders', schema=None) as batch_op:
        batch_op.alter_column('provider_name',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=40),
               existing_nullable=False)

    with op.batch_alter_table('provider_models', schema=None) as batch_op:
        batch_op.alter_column('provider_name',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=40),
               existing_nullable=False)

    with op.batch_alter_table('provider_model_settings', schema=None) as batch_op:
        batch_op.drop_index('provider_model_setting_tenant_provider_model_idx')

    op.drop_table('provider_model_settings')
    with op.batch_alter_table('load_balancing_model_configs', schema=None) as batch_op:
        batch_op.drop_index('load_balancing_model_config_tenant_provider_model_idx')

    op.drop_table('load_balancing_model_configs')
    # ### end Alembic commands ###