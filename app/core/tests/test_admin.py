from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse



class AdminSiteTests(TestCase):

    # Función de configuración que se ejecuta antes de la prueba
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@tests.com',
            password='password123'
        ) # Usuario administrador
        # force_login es una función de ayuda de Client que le permite iniciar sesión
        # a un usuario con Django autentication
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@gmail.com',
            password='password123',
            name='Test user full name'
        ) # Usuario común


    def test_users_listed(self):
        """Test that users are listed on user page"""

        # Reverse crea una url para la página de lista de usuario
        # Reverse actualizará la url si ésta cambia en el futuro evitando así cambiarla manualmente
        url = reverse('admin:core_user_changelist')
        # Realiza un http get de la url
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
        # esta función además de verificar que en la respuesta viene el name y email
        # tambien verifica que el status de la respuesta sea 200


    def test_user_change_page(self):
        """Test that the user edit page works"""

        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)


    def test_create_user_page(self):
        """Test that the create user page works"""

        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)


