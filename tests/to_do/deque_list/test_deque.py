from collections import deque
from unittest import TestCase

from src.to_do.deque_list import DequeList
from src.to_do.deque_list.task import task_03, task_01, task_02, DequeTask


class TestBacklog(TestCase):
    def test_should_add_one_task(self):
        # Given
        deque_list = DequeList()

        # When
        deque_list.add_task(task_03)

        # Then
        self.assertEqual(deque([task_03]), deque_list.tasks)

    def test_should_add_three_task(self):
        # Given
        deque_list = DequeList()

        # When
        deque_list.add_task(task_01)
        deque_list.add_task(task_02)
        deque_list.add_task(task_03)

        # Then
        self.assertEqual(deque([task_01, task_02, task_03]), deque_list.tasks)

    def test_should_get_task(self):
        # Given
        deque_list = DequeList()
        deque_list.add_task(task_03)
        deque_list.add_task(task_01)
        deque_list.add_task(task_02)
        # When
        actual_task = deque_list.get_task()
        # Then
        self.assertEqual(task_03, actual_task) # FIFO - The first task entered to the deque is task_03 and this is removed (.popleft)

    def test_get_task_from_empty_dequelist(self):
        # Given
        deque_list = DequeList()

        # When
        actual_task = deque_list.get_task()

        # Then
        self.assertEqual(None, actual_task)

    def test_remove_any_task_from_dequelist(self):
        # Given
        deque_list = DequeList()
        deque_list.add_task(task_03)
        deque_list.add_task(task_01)
        deque_list.add_task(task_02)
        # When
        deque_list.remove_task(task_01)
        # Then
        self.assertEqual(deque([task_03, task_02]), deque_list.tasks)

    def test_check_new_task_status(self):
        # Given
        task_1 = DequeTask('Task1', 'Description')

        # When
        expect_status = 'NEW'

        # Then
        self.assertEqual(task_1.status, expect_status)

    def test_check_add_status(self):
        # Given
        deque_list = DequeList()
        self.assertEqual(task_03.status, 'NEW')

        # When
        deque_list.add_task(task_03)
        expect_status = 'PENDING'

        # Then
        self.assertEqual(task_03.status, expect_status)

    def test_check_get_status(self):
        # Given
        deque_list = DequeList()
        deque_list.add_task(task_03)
        self.assertEqual(task_03.status, 'PENDING')

        # When
        deque_list.get_task()
        expect_status = 'TAKEN'

        # Then
        self.assertEqual(task_03.status, expect_status)

    def test_check_mark_status(self):
        # Given
        deque_list = DequeList()
        deque_list.add_task(task_03)
        self.assertEqual(task_03.status, 'PENDING')

        # When
        deque_list.mark_task_as_completed(task_03)
        expect_status = 'DONE'

        # Then
        self.assertEqual(task_03.status, expect_status)

    def test_mark_for_empty_dequelist(self):
        # Given
        deque_list = DequeList()

        # When
        actual_task = deque_list.remove_task(task_03)

        # Then
        self.assertEqual(None, actual_task)

    def test_mark_status_for_noexisting_task_at_dequelist(self):
        # Given
        deque_list = DequeList()
        deque_list.add_task(task_03)
        self.assertEqual(task_03.status, 'PENDING')

        # When
        deque_list.mark_task_as_completed(task_02)
        expect_status = 'DONE'

        # Then
        self.assertNotEqual(task_02.status, expect_status)


