#!/usr/bin/env python
import os
from flask.cli import FlaskGroup
from app import create_app, db
from app.models.user import User
from app.models.article import Article

app = create_app()
cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    """Creates the database tables."""
    db.create_all()
    print("Database tables created!")

@cli.command("drop_db")
def drop_db():
    """Drops the database tables."""
    db.drop_all()
    print("Database tables dropped!")

@cli.command("seed_db")
def seed_db():
    """Seeds the database with initial data."""
    # Create admin user
    admin = User(
        email='admin@cirec.net',
        username='admin',
        first_name='Admin',
        last_name='User',
        is_admin=True
    )
    admin.set_password('admin123')
    db.session.add(admin)
    db.session.commit()
    print("Database seeded with initial data!")

if __name__ == '__main__':
    cli()
