import unittest
from app.models import Comments


class CommentTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Comment class model.
    """

    def setUp(self):
        """
        Set up method that will run before every Test to create a comment instance.
        """
        self.comment= Comments(comment_itself = 'I am testing comment class')


    def tearDown(self):
        Comments.query.delete()


    def test_instance(self):
        self.assertTrue(isinstance(self.comment, Comments))


    def test_check_instance_variables(self):
        self.assertEquals(self.comment.opinion,'I am testing comment class')