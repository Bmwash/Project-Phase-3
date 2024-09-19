import click
from stock_monitoring.db import SessionLocal
from stock_monitoring.models import Item, Stock
from sqlalchemy.orm.exc import NoResultFound
from contextlib import contextmanager

@click.group()
def cli():
    """Stock Monitoring CLI Application."""
    pass

@contextmanager
def get_session():
    """Create a new database session."""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@cli.command()
@click.argument('name')
@click.argument('category')
def add_item(name, category):
    """Add a new item to the stock."""
    with get_session() as session:
        item = Item(name=name, category=category)
        session.add(item)
        session.commit()
        click.echo(f"Item '{name}' added to the database.")

@cli.command()
@click.argument('item_name')
@click.argument('quantity', type=int)
def add_stock(item_name, quantity):
    """Add stock for an item."""
    with get_session() as session:
        try:
            item = session.query(Item).filter_by(name=item_name).one()
            # Create a Stock instance without the 'notes' field
            stock = Stock(item_id=item.id, quantity=quantity, status="Available")
            session.add(stock)
            session.commit()
            click.echo(f"Added {quantity} units of '{item_name}' to stock.")
        except NoResultFound:
            click.echo(f"Item '{item_name}' does not exist in the database.")

@cli.command()
@click.argument('item_name')
def remove_item(item_name):
    """Remove an item from the stock."""
    with get_session() as session:
        try:
            item = session.query(Item).filter_by(name=item_name).one()
            session.delete(item)
            session.commit()
            click.echo(f"Item '{item_name}' has been removed from the database.")
        except NoResultFound:
            click.echo(f"Item '{item_name}' not found in the database.")

@cli.command()
@click.argument('item_name')
def check_stock(item_name):
    """Check the stock level of an item."""
    with get_session() as session:
        try:
            item = session.query(Item).filter_by(name=item_name).one()
            stock = session.query(Stock).filter_by(item_id=item.id).all()
            total_quantity = sum(s.quantity for s in stock)
            click.echo(f"Total stock for '{item_name}': {total_quantity} units.")
        except NoResultFound:
            click.echo(f"Item '{item_name}' not found in the database.")

@cli.command()
def list_items():
    """List all items in the database."""
    with get_session() as session:
        items = session.query(Item).all()
        if items:
            click.echo("Items in stock:")
            for item in items:
                click.echo(f"- {item.name} (Category: {item.category})")
        else:
            click.echo("No items found in the database.")

if __name__ == "__main__":
    cli()
