from unittest import TestCase

from src.to_do.backlog import Backlog
from src.to_do.backlog.task import backlog_task_03, backlog_task_01, backlog_task_02
from src.to_do.value_objects import TaskStatus


class TestBacklog(TestCase):
    def test_should_add_one_task(self) -> None:
        backlog = Backlog()
        expected_tasks = [backlog_task_03]

        backlog.add_task(backlog_task_03)

        self.assertListEqual(expected_tasks, backlog.tasks)
        self.assertEqual(TaskStatus.PENDING, backlog_task_03.status)

    def test_should_add_three_task(self) -> None:
        backlog = Backlog()
        expected_tasks = [backlog_task_03, backlog_task_01, backlog_task_02]

        backlog.add_task(backlog_task_03)
        backlog.add_task(backlog_task_01)
        backlog.add_task(backlog_task_02)

        self.assertListEqual(expected_tasks, backlog.tasks)

    def test_should_get_task(self) -> None:
        backlog = Backlog()
        backlog.add_task(backlog_task_03)
        backlog.add_task(backlog_task_01)
        backlog.add_task(backlog_task_02)

        actual_task = backlog.get_task()

        self.assertEqual(backlog_task_02, actual_task)
        self.assertEqual(TaskStatus.STARTED, actual_task.status)

    def test_get_task_from_empty_list(self) -> None:
        backlog = Backlog()

        actual_task = backlog.get_task()

        self.assertEqual(None, actual_task)

    def test_complete_task(self) -> None:
        backlog = Backlog()
        backlog.add_task(backlog_task_03)
        task = backlog.get_task()
        expected_completed_tasks = [task]

        backlog.complete_task(task)

        self.assertListEqual(expected_completed_tasks, backlog.completed_tasks)
        self.assertEqual(TaskStatus.COMPLETED, task.status)
