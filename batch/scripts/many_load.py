import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, State, Iso, Region, Site

def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()
    Site.objects.all().delete()

    # Format
    # name, description, justification, year, longitude, latitude, area_hectares, category, state, region, iso

    for row in reader:
        # print(row[5])
        try:
            a = float(row[6])
        except ValueError:
            a = 0

        c, created = Category.objects.get_or_create(name=row[7])
        s, created = State.objects.get_or_create(name=row[8])
        r, created = Region.objects.get_or_create(name=row[9])
        i, created = Iso.objects.get_or_create(name=row[10])

        site = Site(name=row[0], description=row[1], justification=row[2],
                    year=row[3], longitude=row[4], latitude=row[5],
                    area_hectares=a, category=c, state=s,
                    region=r, iso=i)
        site.save()


        # r = Site.LEARNER
        # if row[1] == 'I':
        #     r = Membership.INSTRUCTOR
        # m = Membership(role=r, person=p, course=c)
        # m.save()