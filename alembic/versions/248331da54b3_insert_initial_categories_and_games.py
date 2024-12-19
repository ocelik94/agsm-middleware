"""Insert initial categories and games

Revision ID: 248331da54b3
Revises: b46278e60d4b
Create Date: 2024-12-19 15:06:25.927035

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '248331da54b3'
down_revision: Union[str, None] = 'b46278e60d4b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Insert categories
    op.execute("""
    INSERT INTO categories (name) VALUES 
        ('game'),
        ('voice'),
        ('website')
    ON CONFLICT DO NOTHING;
    """)

    # Insert games
    op.execute("""
    INSERT INTO games (name, image, tag, category) VALUES 
        ('minecraft', 'placeholder', 'placeholder', 'game'),
        ('ark survival ascended', 'placeholder', 'placeholder', 'game')
    ON CONFLICT DO NOTHING;
    """)


def downgrade():
    # Delete games
    op.execute("""
    DELETE FROM games WHERE name IN ('minecraft', 'ark survival ascended');
    """)

    # Delete categories
    op.execute("""
    DELETE FROM categories WHERE name IN ('game', 'voice', 'website');
    """)