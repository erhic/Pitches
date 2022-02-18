import unittest
from app.models import Pitches


class TestPitch(unittest.TestCase):
    def setUp(self):
        """
        Method that will run before every test
        """
        self.new_pitches = Pitches(
            user_id=1,
            title="Test Title",
            post="Test Pitch",
            
        )

    def test_instance(self):
        """
        Test to check if the pitches object is an instance of the Pitches class
        """
        self.assertTrue(isinstance(self.new_pitches, Pitches))

    def test_save_pitches(self):
        """
        Test to save a pitches
        """
        self.new_pitches.save_pitches()
        self.assertTrue(len(Pitches.query.all()) > 0)

    def test_get_pitches_by_id(self):
        """
        Test to check if the get pitches by id method is working
        """
        self.new_pitches.save_pitches()
        got_pitches = Pitches.get_pitches(1)
        self.assertTrue(got_pitches is not None)