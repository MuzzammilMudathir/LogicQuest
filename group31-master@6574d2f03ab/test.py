import unittest
from unittest.mock import patch
import lightningMode
import Sign_In
import instructorMode
import Leaderboard
import addQuestion
import developerMode


class TestLightningMode(unittest.TestCase):

    @patch('lightningMode.read_questions')
    def test_read_questions(self, mock_read):
        mock_data = lightningMode.get_question_text()
        data = "1.if p then r"
        self.assertEqual(mock_data, data)

class TestSignIn(unittest.TestCase):

    @patch('Sign_In.read_users')
    def test_read_users(self, mock_read):
        mock_data = Sign_In.get_user_data()
        data = "1. user1"
        self.assertEqual(mock_data, data)

class TestinstructorMode(unittest.TestCase):

    @patch('instructorMode.read_questions')
    def test_read_questions(self, mock_read):
        mock_data = instructorMode.get_question_text()
        data = "1.if p then r"
        self.assertEqual(mock_data, data)

    @patch('instructorMode.read_questions')
    def test_read_questions(self, mock_read):
        mock_data = instructorMode.get_question_text()
        data = "1.if p then r"
        self.assertEqual(mock_data, data)

class TestLeaderboard(unittest.TestCase):

    @patch('Leaderboard.read_leaderboard')
    def test_read_leaderboard(self, mock_read):
        mock_data = Leaderboard.get_leaderboard_data()
        data = "1. user1"
        self.assertEqual(mock_data, data)

    @patch('Leaderboard.read_leaderboard')
    def test_read_leaderboard(self, mock_read):
        mock_data = Leaderboard.get_leaderboard_data()
        data = "1. user1"
        self.assertEqual(mock_data, data)

class TestAddQuestion(unittest.TestCase):

    @patch('AddQuestion.read_questions')
    def test_read_questions(self, mock_read):
        mock_data = addQuestion.get_question_text()
        data = "1.if p then r"
        self.assertEqual(mock_data, data)

    @patch('AddQuestion.read_questions')
    def test_read_questions(self, mock_read):
        mock_data = addQuestion.get_question_text()
        data = "1.if p then r"
        self.assertEqual(mock_data, data)
    
    @patch('AddQuestion.read_questions')
    def test_read_questions(self, mock_read):
        mock_data = addQuestion.get_question_text()
        data = "1.if p then r"
        self.assertEqual(mock_data, data)

class TestDeveloperMode(unittest.TestCase):

    @patch('DeveloperMode.read_questions')
    def test_read_questions(self, mock_read):
        mock_data = developerMode.get_question_text()
        data = "1.if p then r"
        self.assertEqual(mock_data, data)

    @patch('DeveloperMode.read_questions')
    def test_read_questions(self, mock_read):
        mock_data = developerMode.get_question_text()
        data = "1.if q then p"
        self.assertEqual(mock_data, data)

    @patch('DeveloperMode.read_questions')
    def test_read_questions(self, mock_read):
        mock_data = developerMode.get_question_text()
        data = "1.if q then r"
        self.assertEqual(mock_data, data)

if __name__ == '__main__':
    unittest.main()