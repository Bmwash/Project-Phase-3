from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a70bcc0dc905'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create 'transactions' table
    op.create_table('transactions',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('stock_id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('action', sa.String(), nullable=False),
        sa.Column('timestamp', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
        sa.ForeignKeyConstraint(['stock_id'], ['stock.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )

    # Since SQLite doesn't support ALTER COLUMN, we ensure that these columns are created properly
    # from the beginning, during table creation.

    # Modify the 'stock' table schema
    op.create_table('new_stock',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('item_id', sa.Integer(), nullable=False),
        sa.Column('quantity', sa.Integer(), nullable=False),
        sa.Column('status', sa.Enum('available', 'damaged', 'out_of_stock', name='stockstatus')),
        sa.ForeignKeyConstraint(['item_id'], ['items.id'])
    )
    op.execute('INSERT INTO new_stock SELECT id, item_id, quantity, status FROM stock')
    op.drop_table('stock')
    op.rename_table('new_stock', 'stock')

    # Modify the 'items' table schema
    op.create_table('new_items',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('category', sa.String(), nullable=False)
    )
    op.execute('INSERT INTO new_items SELECT id, name, category FROM items')
    op.drop_table('items')
    op.rename_table('new_items', 'items')

    # Modify the 'users' table schema
    op.create_table('new_users',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('role', sa.String(), nullable=False)
    )
    op.execute('INSERT INTO new_users SELECT id, name, role FROM users')
    op.drop_table('users')
    op.rename_table('new_users', 'users')

def downgrade() -> None:
    # Recreate the original tables in the downgrade section
    op.create_table('stock',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('item_id', sa.Integer(), nullable=True),
        sa.Column('quantity', sa.Integer(), nullable=True),
        sa.Column('status', sa.Integer())
    )
    op.execute('INSERT INTO stock SELECT id, item_id, quantity, status FROM new_stock')
    op.drop_table('new_stock')

    op.create_table('items',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.Numeric(), nullable=True),
        sa.Column('category', sa.Numeric(), nullable=True)
    )
    op.execute('INSERT INTO items SELECT id, name, category FROM new_items')
    op.drop_table('new_items')

    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.Numeric(), nullable=True),
        sa.Column('role', sa.NullType(), nullable=True),
        sa.Column('STRING', sa.NullType(), nullable=True)
    )
    op.execute('INSERT INTO users SELECT id, name, role FROM new_users')
    op.drop_table('new_users')

    # Drop the transactions table
    op.drop_table('transactions')
