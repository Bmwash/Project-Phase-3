# import click
# from stock_monitoring.db import SessionLocal
# from stock_monitoring.models import Item, Stock, User
# from sqlalchemy.orm.exc import NoResultFound
# from contextlib import contextmanager

# @click.group()
# def cli():
#     """Stock Monitoring CLI Application."""
#     pass

# @contextmanager
# def get_session():
#     """Create a new database session."""
#     session = SessionLocal()
#     try:
#         yield session
#     finally:
#         session.close()

# # Item Commands
# @cli.command()
# @click.argument('name')
# @click.argument('category')
# def add_item(name, category):
#     """Add a new item to the stock."""
#     with get_session() as session:
#         item = Item(name=name, category=category)
#         session.add(item)
#         session.commit()
#         click.echo(f"Item '{name}' added to the database.")

# # @cli.command()
# # @click.argument('item_name')
# # @click.argument('quantity', type=int)
# # @click.argument('status')
# # def add_stock(item_name, quantity, status):
# #     """Add stock for an item with a given status."""
# #     # Define valid statuses
# #     valid_statuses = ["available", "damaged", "out_of_stock"]
# #     status = input("Enter status (available, damaged, out_of_stock): ")

# #     if status.lower() not in valid_statuses:
# #         click.echo(f"Invalid status '{status}'. Valid options are: {', '.join(valid_statuses)}.")
# #         return
    
# #     with get_session() as session:
# #         try:
# #             item = session.query(Item).filter_by(name=item_name).one()
# #             stock = Stock(item_id=item.id, quantity=quantity, status=status)
# #             session.add(stock)
# #             session.commit()
# #             click.echo(f"Added {quantity} units of '{item_name}' to stock with status '{status}'.")
# #         except NoResultFound:
# #             click.echo(f"Item '{item_name}' does not exist in the database.")@cli.command()


# @click.argument('item_name')
# @click.argument('quantity', type=int)
# @click.argument('status')
# def add_stock(item_name, quantity, status):
#     """Add stock for an item with a given status."""
#     valid_statuses = ["available", "damaged", "out_of_stock"]

#     if status.lower() not in valid_statuses:
#         click.echo(f"Invalid status '{status}'. Valid options are: {', '.join(valid_statuses)}.")
#         return

#     if not isinstance(quantity, int) or quantity < 0:
#         click.echo("Quantity must be a non-negative integer.")
#         return
    
#     with get_session() as session:
#         try:
#             item = session.query(Item).filter_by(name=item_name).one()
#             stock = Stock(item_id=item.id, quantity=quantity, status=status)
#             session.add(stock)
#             session.commit()
#             click.echo(f"Added {quantity} units of '{item_name}' to stock with status '{status}'.")
#         except NoResultFound:
#             click.echo(f"Item '{item_name}' does not exist in the database.")


# @cli.command()
# @click.argument('item_name')
# def remove_item(item_name):
#     """Remove an item from the stock."""
#     with get_session() as session:
#         try:
#             item = session.query(Item).filter_by(name=item_name).one()
#             session.delete(item)
#             session.commit()
#             click.echo(f"Item '{item_name}' has been removed from the database.")
#         except NoResultFound:
#             click.echo(f"Item '{item_name}' not found in the database.")

# @cli.command()
# @click.argument('item_name')
# def check_stock(item_name):
#     """Check the stock level of an item."""
#     with get_session() as session:
#         items = session.query(Item).filter_by(name=item_name).all()
#         if not items:
#             click.echo(f"Item '{item_name}' not found in the database.")
#         else:
#             click.echo(f"Stock levels for items named '{item_name}':")
#             for item in items:
#                 stock = session.query(Stock).filter_by(item_id=item.id).all()
#                 total_quantity = sum(s.quantity for s in stock)
#                 click.echo(f"- {item.name} (Category: {item.category}): {total_quantity} units.")

# @cli.command()
# def list_items():
#     """List all items in the database."""
#     with get_session() as session:
#         items = session.query(Item).all()
#         if items:
#             click.echo("Items in stock:")
#             for item in items:
#                 click.echo(f"- {item.name} (Category: {item.category})")
#         else:
#             click.echo("No items found in the database.")

# # User Commands
# @cli.command()
# @click.argument('name')
# @click.argument('role')
# def create_user(name, role):
#     """Create a new user account."""
#     with get_session() as session:
#         user = User(name=name, role=role)
#         session.add(user)
#         session.commit()
#         click.echo(f"User '{name}' with role '{role}' created successfully.")

# @cli.command()
# @click.argument('user_id', type=int)
# def remove_user(user_id):
#     """Remove a user from the database."""
#     with get_session() as session:
#         try:
#             user = session.query(User).get(user_id)
#             if user:
#                 session.delete(user)
#                 session.commit()
#                 click.echo(f"User '{user_id}' has been removed from the database.")
#             else:
#                 click.echo(f"User '{user_id}' not found in the database.")
#         except NoResultFound:
#             click.echo(f"User '{user_id}' not found in the database.")

# @cli.command()
# def list_users():
#     """List all users in the database."""
#     with get_session() as session:
#         users = session.query(User).all()
#         if users:
#             click.echo("Users in the database:")
#             for user in users:
#                 click.echo(f"- ID: {user.id}, Name: {user.name}, Role: {user.role}")
#         else:
#             click.echo("No users found in the database.")

# if __name__ == "__main__":
#     cli()


import click
from stock_monitoring.db import SessionLocal
from stock_monitoring.models import Item, Stock, User
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

# Item Commands
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

# @cli.command()
# @click.argument('item_name')
# @click.argument('quantity', type=int)
# @click.argument('status')
# def add_stock(item_name, quantity, status):
#     """Add stock for an item with a given status."""
#     valid_statuses = ["available", "damaged", "out_of_stock"]

#     if status.lower() not in valid_statuses:
#         click.echo(f"Invalid status '{status}'. Valid options are: {', '.join(valid_statuses)}.")
#         return

#     if quantity < 0:
#         click.echo("Quantity must be a non-negative integer.")
#         return
    
#     with get_session() as session:
#         try:
#             item = session.query(Item).filter_by(name=item_name).one()
#             stock = Stock(item_id=item.id, quantity=quantity, status=status)
#             session.add(stock)
#             session.commit()
#             click.echo(f"Added {quantity} units of '{item_name}' to stock with status '{status}'.")
#         except NoResultFound:
#             click.echo(f"Item '{item_name}' does not exist in the database.")

@cli.command()
@click.argument('item_name')
@click.argument('quantity', type=int)
@click.argument('status')
def add_stock(item_name, quantity, status):
    """Add stock for an item with a given status."""
    valid_statuses = [status.lower() for status in StockStatus._value2member_map_]

    status = status.lower()

    if status not in valid_statuses:
        click.echo(f"Invalid status '{status}'. Valid options are: {', '.join(valid_statuses)}.")
        return

    if quantity < 0:
        click.echo("Quantity must be a non-negative integer.")
        return
    
    with get_session() as session:
        try:
            item = session.query(Item).filter_by(name=item_name).one()
            stock = Stock(item_id=item.id, quantity=quantity, status=status)
            session.add(stock)
            session.commit()
            click.echo(f"Added {quantity} units of '{item_name}' to stock with status '{status}'.")
        except NoResultFound:
            click.echo(f"Item '{item_name}' does not exist in the database.")


# @cli.command()
# @click.argument('item_name')
# def remove_item(item_name):
#     """Remove an item from the stock."""
#     with get_session() as session:
#         try:
#             item = session.query(Item).filter_by(name=item_name).all()
#             session.delete(item)
#             session.commit()
#             click.echo(f"Item '{item_name}' has been removed from the database.")
#         except NoResultFound:
#             click.echo(f"Item '{item_name}' not found in the database.")

@cli.command()
@click.argument('item_name')
def remove_item(item_name):
    """Remove an item from the stock."""
    with get_session() as session:
        items = session.query(Item).filter_by(name=item_name).all()
        if not items:
            click.echo(f"Item '{item_name}' not found in the database.")
        else:
            for item in items:
                session.delete(item)
            session.commit()
            click.echo(f"Item(s) with name '{item_name}' have been removed from the database.")


@cli.command()
@click.argument('item_name')
def check_stock(item_name):
    """Check the stock level of an item."""
    with get_session() as session:
        items = session.query(Item).filter_by(name=item_name).all()
        if not items:
            click.echo(f"Item '{item_name}' not found in the database.")
        else:
            click.echo(f"Stock levels for items named '{item_name}':")
            for item in items:
                stock = session.query(Stock).filter_by(item_id=item.id).all()
                total_quantity = sum(s.quantity for s in stock)
                click.echo(f"- {item.name} (Category: {item.category}): {total_quantity} units.")

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

# User Commands
@cli.command()
@click.argument('name')
@click.argument('role')
def create_user(name, role):
    """Create a new user account."""
    with get_session() as session:
        user = User(name=name, role=role)
        session.add(user)
        session.commit()
        click.echo(f"User '{name}' with role '{role}' created successfully.")

@cli.command()
@click.argument('user_id', type=int)
def remove_user(user_id):
    """Remove a user from the database."""
    with get_session() as session:
        try:
            user = session.query(User).get(user_id)
            if user:
                session.delete(user)
                session.commit()
                click.echo(f"User '{user_id}' has been removed from the database.")
            else:
                click.echo(f"User '{user_id}' not found in the database.")
        except NoResultFound:
            click.echo(f"User '{user_id}' not found in the database.")

@cli.command()
def list_users():
    """List all users in the database."""
    with get_session() as session:
        users = session.query(User).all()
        if users:
            click.echo("Users in the database:")
            for user in users:
                click.echo(f"- ID: {user.id}, Name: {user.name}, Role: {user.role}")
        else:
            click.echo("No users found in the database.")

if __name__ == "__main__":
    cli()
