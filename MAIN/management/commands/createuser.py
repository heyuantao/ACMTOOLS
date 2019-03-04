from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Create User ! # createuser --username abc --password 123  --type admin # type should be in admin or user"
    def add_arguments(self, parser):
        parser.add_argument("-u","--username", type=str, help="username")
        parser.add_argument("-p", "--password", type=str, help="password")
        parser.add_argument("-t", "--type", type=str, help="admin or user")  #admin or user

    def handle(self, *args, **options):
        username = options["username"]
        password = options["password"]
        type = options["type"]

        if username.find("@")==-1:
            self.stdout.write(self.style.ERROR("Username Should In Email Format !".format(username)))
            return

        try:
            user_query_set = User.objects.filter(is_superuser=True)
            if user_query_set:
                superuser_instance = user_query_set[0]
                self.stdout.write(self.style.ERROR("Super User {} Exist!".format(superuser_instance.username)))
                return

            user_query_set = User.objects.filter(username = username)
            if user_query_set:
                self.stdout.write(self.style.ERROR("User with {} Exist!".format(username)))
                return
            user_instance = User.objects.create(username=username,email=username)
            user_instance.set_password(password)
            user_instance.save()

            if type=="admin":
                user_instance.is_superuser=True
                user_instance.is_staff = True
            else:
                user_instance.is_superuser=False
                user_instance.is_staff = False
            user_instance.save()

            self.stdout.write(self.style.SUCCESS("Successfully Create User !".format(username)))
            self.stdout.write(self.style.SUCCESS("{}:{}".format(username, type)))
        except Exception:
            self.stdout.write(self.style.ERROR("Error Happen !".format(username)))