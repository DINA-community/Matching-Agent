#!/bin/bash
set -e

echo "Setting up NetBox..."

# Create superuser if it doesn't exist
python /opt/netbox/netbox/manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='${NETBOX_SUPERUSER_NAME}').exists():
    User.objects.create_superuser(
        '${NETBOX_SUPERUSER_NAME}',
        '${NETBOX_SUPERUSER_EMAIL}',
        '${DJANGO_SUPERUSER_PASSWORD}'
    )
    print('Superuser created.')
else:
    print('Superuser already exists.')
END

# Create API token if it doesn't exist
python /opt/netbox/netbox/manage.py shell << END
from users.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()
user = User.objects.get(username='${NETBOX_SUPERUSER_NAME}')

# Check if token already exists for this user
if not Token.objects.filter(user=user).exists():
    token = Token.objects.create(user=user, write_enabled=True)
    print(f'API Token created: {token.key}')
    # Optionally save to a file
    with open('/tmp/netbox_token.txt', 'w') as f:
        f.write(token.key)
else:
    token = Token.objects.filter(user=user).first()
    print(f'API Token already exists: {token.key}')
END

echo "NetBox setup complete!"