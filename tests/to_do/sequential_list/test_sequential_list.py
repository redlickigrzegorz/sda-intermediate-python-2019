from collections import deque
from unittest import TestCase

from src.to_do.sequential_list import SequentialList
from src.to_do.sequential_list.task import sequential_task_01, sequential_task_02, sequential_task_03
from src.to_do.value_objects import TaskStatus


class TestSequentialList(TestCase):
    def test_should_add_one_task(self):
        sequential_list = SequentialList()
        expected_tasks = deque([sequential_task_03])

        sequential_list.add_task(sequential_task_03)

        self.assertEqual(expected_tasks, sequential_list.tasks)
        self.assertEqual(TaskStatus.PENDING, sequential_task_03.status)

    def test_should_add_three_task(self):
        sequential_list = SequentialList()
        expected_tasks = deque([sequential_task_03, sequential_task_02, sequential_task_01])

        sequential_list.add_task(sequential_task_03)
        sequential_list.add_task(sequential_task_02)
        sequential_list.add_task(sequential_task_01)

        self.assertEqual(expected_tasks, sequential_list.tasks)

    def test_should_get_task(self):
        sequential_list = SequentialList()
        sequential_list.add_task(sequential_task_03)
        sequential_list.add_task(sequential_task_02)
        sequential_list.add_task(sequential_task_01)

        actual_task = sequential_list.get_task()

        self.assertEqual(sequential_task_03, actual_task)
        self.assertEqual(TaskStatus.STARTED, actual_task.status)

    def test_get_task_from_empty_list(self):
        sequential_list = SequentialList()

        actual_task = sequential_list.get_task()

        self.assertEqual(None, actual_task)

    def test_complete_task(self) -> None:
        sequential_list = SequentialList()
        sequential_list.add_task(sequential_task_03)
        task = sequential_list.get_task()
        expected_completed_tasks = [task]

        sequential_list.complete_task(task)

        self.assertListEqual(expected_completed_tasks, sequential_list.completed_tasks)
        self.assertEqual(TaskStatus.COMPLETED, task.status)
