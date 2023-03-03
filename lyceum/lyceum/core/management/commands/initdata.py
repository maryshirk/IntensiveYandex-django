from django.core.management import BaseCommand, call_command
from dotenv import load_dotenv
import os

load_dotenv()

user_email = os.environ.get("ADMIN_EMAIL")


class Command(BaseCommand):
    help = "Check migrations, loaddata and createsuperuser in one command"

    def handle(self, *args, **options):
        if options["fixture_file"] and self.check_migrations():
            call_command("loaddata", options["fixture_file"][0])
            if user_email is not None:
                call_command("createsuperuser", email=user_email)
            else:
                call_command("createsuperuser")
        else:
            raise

    def add_arguments(self, parser):
        parser.add_argument(
            "fixture_file", nargs=1, help="File to load fixture"
        )

    def check_migrations(self):
        print("checking some migrations")
        for address, dirs, files in os.walk("lyceum\catalog"):
            if dirs:
                if os.path.basename(address) == "migrations":
                    if os.listdir(address):
                        print("checked")
                        return True
                    else:
                        return False
