# Permite burlarse (hacer mocking) del comportamiento de la función
# get_database de Django.
# Simulará que la base de datos esta disponible o no mientras se
# prueba el comando.
from unittest.mock import patch

from django.core.management import call_command

# Error operacional que Django arroja cuando la BD no está disponible.
# Se utilizará para simular que la BD está disponible o no cuando se
# ejecute el comando.
from django.db.utils import OperationalError

from django.test import TestCase


class CommandTests(TestCase):

    def test_wait_for_db_ready(self):
        """Test waiting for db when db is available"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """Test waiting for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
