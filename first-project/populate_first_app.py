import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

django.setup()

# FAKE POP SCRIPT
import random
from first_app.models import Topic, WebPage, AccessRecord
from faker import Faker

fake_generator = Faker()
fake_generator.random.seed(7)

topics = ['Search', 'News', 'Sport', 'Health']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(n=5):
    for entry in range(n):
        # get topic
        top = add_topic()

        # create data for that entry
        fake_url = fake_generator.url()
        fake_date = fake_generator.date()
        fake_name = fake_generator.company()

        # create a new web page entry
        webpg = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # create a fake access record
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)


if __name__ == '__main__':
    print("Populating script!")
    populate(20)
    print("Populating complete")
