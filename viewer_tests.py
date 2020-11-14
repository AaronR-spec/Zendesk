import unittest
from viewer import Viewer


class TestViewer(unittest.TestCase):

    def setUp(self):
        user = 'd00222467@student.dkit.ie'
        pwd = 'aaronreihillzendesk'
        self._ticket_viewer = Viewer(user, pwd)

    def test_init(self):
        self.assertGreater(len(self._ticket_viewer._tickets), 0)

    def test_get_ticket(self):
        self.assertFalse(self._ticket_viewer.get_ticket(2222222222222222222222))
        self.assertFalse(self._ticket_viewer.get_ticket(""))
        self.assertFalse(self._ticket_viewer.get_ticket("safasfasf2222"))
        self.assertFalse(self._ticket_viewer.get_ticket(-5))
        self.assertTrue(self._ticket_viewer.get_ticket(5))

    def test_display(self):
        self.assertTrue(self._ticket_viewer.display())


if __name__ == "__main__":
    unittest.main()
