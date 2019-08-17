from unittest import TestCase
from src.to_do.sequential.task import task_01


class TestSequentialList(TestCase):
    def test_mark_task_as_completed(self):
        task_01.status = 'test'

        task_01.mark_task_as_completed()

        self.assertEqual('completed', task_01.status)
