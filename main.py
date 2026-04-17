import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    active_passcards = Passcard.objects.filter(is_active=True)
    print('Количество активных пропусков:', len(active_passcards))

    # some_passcard = passcards[0]
    # print(f"owner_name: {some_passcard.owner_name}\n"
    #       f"passcode: {some_passcard.passcode}\n"
    #       f"created_at: {some_passcard.created_at}\n"
    #       f"is_active: {some_passcard.is_active}")
