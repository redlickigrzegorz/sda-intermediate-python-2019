from unittest import TestCase

from src.to_do.backlog import Backlog
from src.to_do.backlog.task import task_01, task_02, task_03


class TestBacklog(TestCase):
    def test_should_add_one_task(self) -> None:
        # Given
        backlog = Backlog()

        # When
        backlog.add_task(task_03)

        # Then
        self.assertListEqual([task_03], backlog.tasks)

    def test_should_add_three_task(self) -> None:
        # Given
        backlog = Backlog()

        # When
        backlog.add_task(task_03)
        backlog.add_task(task_01)
        backlog.add_task(task_02)

        # Then
        self.assertListEqual([task_03, task_01, task_02], backlog.tasks)

    def test_should_get_task(self) -> None:
        # Given
        backlog = Backlog()
        backlog.add_task(task_03)
        backlog.add_task(task_01)
        backlog.add_task(task_02)
        # When
        actual_task = backlog.get_task()
        # Then
        self.assertEqual(task_02, actual_task)

    def test_get_task_from_empty_list(self) -> None:
        # Given
        backlog = Backlog()

        # When
        actual_task = backlog.get_task()

        # Then
        self.assertEqual(None, actual_task)
