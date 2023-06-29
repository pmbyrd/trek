"""
This is the user_seed module.
Intended to contain all user-related functionality for the Trek project user blueprint.
Populates the database with users made from a csv file of phony user data.
"""
import csv
import random
import requests
from faker import Faker
from werkzeug.security import generate_password_hash
from datetime import datetime
import string

fake = Faker()


USERS_CSV_HEADERS = ['email', 'username', 'avatar', 'password', 'bio', 'first_name', 'last_name', 'location']
NUM_USERS = 1000

def generate_bio():
    bio = fake.paragraph(nb_sentences=10)
    return bio

def generate_users_csv(file_path):
    image_urls = [
        f"https://randomuser.me/api/portraits/{kind}/{i}.jpg"
        for kind, count in [("lego", 10), ("men", 100), ("women", 100)]
        for i in range(count)
    ]

    with open(file_path, 'w') as users_csv:
        users_writer = csv.DictWriter(users_csv, fieldnames=USERS_CSV_HEADERS)
        users_writer.writeheader()

        for i in range(NUM_USERS):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            password_hash = generate_password_hash('password')

            users_writer.writerow(dict(
                email=email,
                username=fake.user_name(),
                avatar=random.choice(image_urls),
                password=password_hash,
                bio=' '.join([generate_bio() for _ in range(5)]),
                first_name=first_name,
                last_name=last_name,
                location=fake.city()
            ))

if __name__ == '__main__':
    generate_users_csv('app/seed/users.csv')

            

# NOTE - Need to clean the code below
# import os
# import csv
# import random
# import requests
# from faker import Faker
# from werkzeug.security import generate_password_hash
# from datetime import datetime, timedelta
# import string
# # from app.extensions import db
# from app.models import User, DEFAULT_IMAGE_URL

# fake = Faker()

# # Number of fake users to generate
# num_users = 1000

# # Output file path
# output_file = os.path.join(os.path.dirname(__file__), 'fake_users.csv')



# # Generate fake users and save them to a CSV file
# def generate_fake_users(num_users, output_file):
    
#     start_date = datetime(2022, 1, 1)  # Define the start date
#     end_date = datetime(2023, 12, 31)  # Define the end date
#     delta = end_date - start_date
#     with open(output_file, 'w', newline='') as csvfile:
#         fieldnames = ['username', 'first_name', 'last_name', 'email', 'password', 'bio', 'location', 'created_at']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#         users = []
#         for _ in range(num_users):
#             username = ''.join(random.choices(string.ascii_lowercase, k=8))
#             first_name = fake.first_name()
#             last_name = fake.last_name()
#             email = f'{username}@example.com'
#             password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
#             bio = generate_bio()
#             location = fake.city()
#             created_at = start_date + random.random() * delta
#             users.append({
#                 'username': username,
#                 'first_name': first_name,
#                 'last_name': last_name,
#                 'email': email,
#                 'password': password,
#                 'bio': bio,
#                 'location': location,
#                 'created_at': created_at
#             })
#             writer.writerow({
#                 'username': username,
#                 'first_name': first_name,
#                 'last_name': last_name,
#                 'email': email,
#                 'password': password,
#                 'bio': bio,
#                 'location': location,
#                 'created_at': created_at
#             })
#         print(f'{num_users} fake users generated and saved to {output_file}')
#         return users

# # Seed users from CSV file
# # def seed_users(users):
# #     for user_data in users:
# #         username = user_data['username']
# #         email = user_data['email']
# #         password = user_data['password']
# #         if User.query.filter_by(email=email).first() is not None:
# #             print(f"Skipping user {username} with email {email}: email already exists")
# #         elif User.query.filter_by(username=username).first() is not None:
# #             print(f"Skipping user {username} with email {email}: username already exists")
# #         else:
# #             user = User(
# #                 username=username,
# #                 first_name=user_data['first_name'],
# #                 last_name=user_data['last_name'],
# #                 email=email,
# #                 password=password,
# #                 bio=user_data['bio'],
# #                 location=user_data['location'],
# #                 created_at=user_data['created_at']
# #             )
# #             db.session.add(user)
# #             print(f"Added user {username} with email {email}")
# #     db.session.commit()

# # Main function
# if __name__ == "__main__":
#     generate_fake_users(num_users, output_file)
