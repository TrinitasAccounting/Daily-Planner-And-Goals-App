#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, ToDos

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!

    # Delete Data from the tables first
        ToDos.query.delete()
        db.session.commit()

    # Add initial Todos 
        t1 = ToDos(title='Pick up Trash', description='close the bag and take out the trash')
        t2 = ToDos(title='Sweep', description='grab broom and sweep floor')
        t3 = ToDos(title='watch show', description='at 8pm the new episode will come on')
        t4 = ToDos(title='drink water', description='you sleep better when you drink plenty of water')

        db.session.add_all([t1, t2, t3, t4])
        db.session.commit()



        print("Completed Seeding")
