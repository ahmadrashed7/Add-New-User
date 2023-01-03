from faker import Faker

fake = Faker(locale='en_CA')
moodle_url = 'http://52.33.5.136/'
moodle_login_url = 'http://52.33.5.136/login/index.php'
moodle_username = 'admin'
moodle_password = 'Moodle$erver002!#'
moodle_dashboard_url = 'http://52.33.5.136/my/'
new_username = fake.user_name()
new_password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
email = fake.email()
moodle_net_profile = f'https://moodle.net/{new_username}'
city = fake.city()
country = fake.country()
description = fake.text(200)
pic_description = fake.sentence(nb_words=3)
phonetic_name = fake.first_name()
phonetic_last = fake.last_name()
phonetic_middle = fake.first_name()
phonetic_alternate = fake.last_name()
list_of_interests = [fake.city(), fake.country(), fake.name()]
id_numbers = fake.random_int()
institution = fake.random_number(7)
department = fake.job()
phone = fake.phone_number()
address = fake.address().replace("\n","")
moodle_users_main_page = 'http://52.33.5.136/admin/user.php'
full_name = f'{first_name} {last_name}'
second_log_in_page = 'http://52.33.5.136/login/change_password.php'
