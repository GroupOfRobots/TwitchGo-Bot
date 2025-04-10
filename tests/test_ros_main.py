# tests/test_ros_main.py

import unittest
from unittest.mock import patch, MagicMock
from app.ros.obstacle_activator import ObstacleActivator  # Poprawiony import


class TestObstacleActivator(unittest.TestCase):
    @patch('app.ros.obstacle_activator.Node')
    def test_obstacle_activator_initialization(self, mock_node):
        obstacle_names = ["adx", "jjj"]
        activator = ObstacleActivator(obstacle_names)

        # Sprawdzenie, czy publisherzy zostali utworzeni
        self.assertEqual(len(activator._obstacles_pub), 2)
        mock_node_instance = mock_node.return_value
        mock_node_instance.create_publisher.assert_any_call(MagicMock(spec=[]), 'adx_topic', 10)
        mock_node_instance.create_publisher.assert_any_call(MagicMock(spec=[]), 'jjj_topic', 10)
        self.assertIn("adx", activator._obstacles_pub)
        self.assertIn("jjj", activator._obstacles_pub)

    @patch('app.ros.obstacle_activator.Node')
    def test_start_obstacle(self, mock_node):
        mock_publisher = MagicMock()
        mock_node_instance = mock_node.return_value
        mock_node_instance.create_publisher.return_value = mock_publisher

        obstacle_names = ["adx"]
        activator = ObstacleActivator(obstacle_names)
        activator.start_obstacle("adx")

        mock_publisher.publish.assert_called_with(MagicMock(data=True))

    @patch('app.ros.obstacle_activator.Node')
    def test_stop_obstacle(self, mock_node):
        mock_publisher = MagicMock()
        mock_node_instance = mock_node.return_value
        mock_node_instance.create_publisher.return_value = mock_publisher

        obstacle_names = ["adx"]
        activator = ObstacleActivator(obstacle_names)
        activator.stop_obstacle("adx")

        mock_publisher.publish.assert_called_with(MagicMock(data=False))

    @patch('app.ros.obstacle_activator.Node')
    def test_append_obstacle(self, mock_node):
        mock_publisher = MagicMock()
        mock_node_instance = mock_node.return_value
        mock_node_instance.create_publisher.return_value = mock_publisher

        obstacle_names = ["adx"]
        activator = ObstacleActivator(obstacle_names)
        activator.append("new_obstacle")

        self.assertIn("new_obstacle", activator._obstacles_pub)
        mock_node_instance.create_publisher.assert_called_with(MagicMock(spec=[]), 'new_obstacle_topic', 10)

    @patch('app.ros.obstacle_activator.Node')
    def test_publish_message_invalid_obstacle(self, mock_node):
        mock_publisher = MagicMock()
        mock_node_instance = mock_node.return_value
        mock_node_instance.create_publisher.return_value = mock_publisher
        mock_logger = mock_node_instance.get_logger.return_value

        obstacle_names = ["adx"]
        activator = ObstacleActivator(obstacle_names)
        activator._publish_message(MagicMock(data=True), "invalid_obstacle")

        mock_logger.warning.assert_called_with("Obstacle invalid_obstacle not found.")


if __name__ == '__main__':
    unittest.main()
