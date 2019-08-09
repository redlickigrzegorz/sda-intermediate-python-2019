from unittest import TestCase

from src.to_do.prioritized_list import PrioritizedList
from src.to_do.prioritized_list.task import prioritized_task_01, prioritized_task_02, prioritized_task_03
from src.to_do.value_objects import TaskStatus


class TestPrioritizedList(TestCase):
    def test_add_one_task(self):
        prioritized_list = PrioritizedList()
        expected_tasks = [prioritized_task_01]

        prioritized_list.add_task(prioritized_task_01)

        self.assertListEqual(expected_tasks, prioritized_list.tasks)
        self.assertEqual(TaskStatus.PENDING, prioritized_task_01.status)

    def test_add_three_task(self):
        prioritized_list = PrioritizedList()
        expected_tasks = [prioritized_task_03, prioritized_task_01, prioritized_task_02]

        prioritized_list.add_task(prioritized_task_01)
        prioritized_list.add_task(prioritized_task_02)
        prioritized_list.add_task(prioritized_task_03)

        self.assertListEqual(expected_tasks, prioritized_list.tasks)

    def test_get_task(self):
        prioritized_list = PrioritizedList()
        prioritized_list.add_task(prioritized_task_01)
        prioritized_list.add_task(prioritized_task_02)
        prioritized_list.add_task(prioritized_task_03)

        actual_task = prioritized_list.get_task()

        self.assertEqual(prioritized_task_03, actual_task)
        self.assertEqual(TaskStatus.STARTED, actual_task.status)

    def test_get_task_from_empty_list(self):
        prioritized_list = PrioritizedList()

        actual_task = prioritized_list.get_task()

        self.assertEqual(None, actual_task)

    def test_complete_task(self) -> None:
        prioritized_list = PrioritizedList()
        prioritized_list.add_task(prioritized_task_03)
        task = prioritized_list.get_task()
        expected_completed_tasks = [task]

        prioritized_list.complete_task(task)

        self.assertListEqual(expected_completed_tasks, prioritized_list.completed_tasks)
        self.assertEqual(TaskStatus.COMPLETED, task.status)
