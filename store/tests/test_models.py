from unittest.mock import patch
from django.test import TestCase
from django.contrib.auth import get_user_model

from store.models import Category, Product, product_image


class TestCategoriesModel(TestCase):
    def setUp(self) -> None:
        self.data1 = Category.objects.create(name="Django", slug="django")

    def test_category_model_entry(self):
        """
        Test Category model data insert/ type/ field attibs
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_return(self):
        """
        Test Category model return
        """
        data = self.data1
        self.assertEqual(str(data), "Django")


class TestProductModels(TestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(name="Django", slug="django")
        self.user = get_user_model().objects.create(username="admin")
        self.data1 = Product.objects.create(
            category=self.category,
            title="Django Beginners",
            created_by=self.user,
            slug="django-beginners",
            price="20.00",
            image="django",
        )

    def test_category_model_entry(self):
        """
        Test Product model data insert/ type/ field attibs
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), "Django Beginners")

    @patch("uuid.uuid4")
    def test_product_image_file_name_uuid(self, mock_uuid):
        """Test that image is saved in correct location"""
        uuid = "test-uuid"
        mock_uuid.return_value = uuid
        file_path = product_image(None, "myimage.jpg")
        exp_path = f"images/product/{uuid}.jpg"

        self.assertEqual(file_path, exp_path)
