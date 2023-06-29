"""
This is the user_seed module.
Intended to contain all user-related functionality for the Trek project user blueprint.
Populates the database with users made from a csv file of phony user data.
"""
import os
import csv
import random
import string
from app import create_app, db
from app.models import User

# Number of fake users to generate
num_users = 1000

# Output file path
output_file = os.path.join(os.path.dirname(__file__), 'fake_users.csv')

# Generate fake users and save them to a CSV file
def generate_fake_users(num_users, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['username', 'email', 'password']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for _ in range(num_users):
            username = ''.join(random.choices(string.ascii_lowercase, k=8))
            email = f'{username}@example.com'
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
            writer.writerow({'username': username, 'email': email, 'password': password})
    print(f'{num_users} fake users generated and saved to {output_file}')

# Seed users from CSV file
def seed_users_from_csv(csv_file):
    with open(csv_file, newline='') as users:
        reader = csv.DictReader(users)
        for row in reader:
            username = row['username']
            email = row['email']
            password = row['password']
            if User.query.filter_by(email=email).first() is not None:
                print(f"Skipping user {username} with email {email}: email already exists")
            elif User.query.filter_by(username=username).first() is not None:
                print(f"Skipping user {username} with email {email}: username already exists")
            else:
                user = User(username=username, email=email, password=password)
                db.session.add(user)
                print(f"Added user {username} with email {email}")
        db.session.commit()

# Main function
if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
        generate_fake_users(num_users, output_file)
        seed_users_from_csv(output_file)
