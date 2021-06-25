import unittest
from app import dal, get_orders_by_customers, prep_db


class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dal.db_init('sqlite:///:memory:')
        prep_db()

    def test_orders_by_customer_blank(self):
        expected_results = [(u'wlk001', u'cookiemon', u'111-111-1111')]
        results = get_orders_by_customers('cookiemon')
        self.assertEqual(results, expected_results)

    def test_orders_by_customer_blank_shipped(self):
        result = get_orders_by_customers('cookiemon', True)
        self.assertEqual(result, [])

    def test_orders_by_customer_blank_notshipped(self):
        expected_results = [(u'wlk001', u'cookiemon', u'111-111-1111')]
        result = get_orders_by_customers('cookiemon', False)
        self.assertEqual(result, expected_results)

    def test_orders_by_customer_blank_details(self):
        expected_results = [
            (u'wlk001', u'cookiemon', u'111-111-1111', u'dark chocolate chip',
             2, str(float('1.00'))),
            (u'wlk001', u'cookiemon', u'111-111-1111', u'oatmeal raisin',
             12, str(float('3.00')))
        ]
        result = get_orders_by_customers('cookiemon', details=True)
        self.assertEqual(result, expected_results)

    def test_orders_by_customer_blank_shipped_details(self):
        result = get_orders_by_customers('cookiemon', True, True)
        self.assertEqual(result, [])

    def test_orders_by_customer_blank_notshipped_details(self):
        expected_results = [
            (u'wlk001', u'cookiemon', u'111-111-1111', u'dark chocolate chip',
             2, str(float('1.00'))),
            (u'wlk001', u'cookiemon', u'111-111-1111', u'oatmeal raisin',
             12, str(float('3.00')))
        ]
        result = get_orders_by_customers('cookiemon', False, True)
        self.assertEqual(result, expected_results)
