# unittest.mock позволяет заменить любой объект на магический "всемогутор". Все есть Mock и вернется Mock.
# Не показывает как работают реальные внешние сервисы.
from unittest.mock import Mock

email_service = Mock
email_service.send_email('alice@example.com', 'hello')
