from unittest import TestCase

from src.to_do.prioritized_list import PrioritizedList
from src.to_do.prioritized_list.task import task_01, task_02, task_03


class TestPrioritizedList(TestCase):
    def test_add_three_task(self):
        my_list = PrioritizedList()

        my_list.add_task(task_01)
        my_list.add_task(task_02)
        my_list.add_task(task_03)

        self.assertListEqual([task_03, task_01, task_02], my_list.tasks)

    def test_add_one_task(self):
        my_list = PrioritizedList()

        my_list.add_task(task_01)

        self.assertListEqual([task_01], my_list.tasks)

    def test_get_task(self):
        my_list = PrioritizedList()
        my_list.add_task(task_01)
        my_list.add_task(task_02)
        my_list.add_task(task_03)

        task = my_list.get_task()

        self.assertEqual(task_03, task)

    def test_get_task_from_empty_list(self):
        my_list = PrioritizedList()

        task = my_list.get_task()

        self.assertEqual(None, task)

