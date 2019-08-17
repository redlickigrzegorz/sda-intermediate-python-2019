from unittest import TestCase

from src.to_do.sequential import SequentialList
from src.to_do.sequential.task import task_01, task_02, task_03


class TestSequentialList(TestCase):
    def test_add_three_task(self):
        my_list = SequentialList()

        my_list.add_task(task_01)
        my_list.add_task(task_02)
        my_list.add_task(task_03)

        self.assertIn(task_01, my_list.tasks)
        self.assertIn(task_02, my_list.tasks)
        self.assertIn(task_03, my_list.tasks)

    def test_get_task(self):
        my_list = SequentialList()
        my_list.add_task(task_01)
        my_list.add_task(task_02)
        my_list.add_task(task_03)

        task = my_list.get_task()

        self.assertEqual(task_01, task)
        self.assertNotIn(task_01, my_list.tasks)


    def test_get_task_from_empty_list(self):
        my_list = SequentialList()

        task = my_list.get_task()

        self.assertEqual(None, task)

    def test_remove_task(self):
        my_list = SequentialList()
        my_list.add_task(task_01)
        my_list.add_task(task_02)
        my_list.add_task(task_03)

        my_list.remove_task(task_02)

        self.assertNotIn(task_02, my_list.tasks)
        self.assertEqual(2, len(my_list.tasks))

