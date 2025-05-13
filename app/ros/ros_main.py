# app/ros/ros_main.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
from typing import List
import queue
import logging

TIME_OUT = 30.0  # seconds 

class ObstacleActivator(Node):

    def __init__(self, obstacle_names: List[str]):
        super().__init__("Obstacles")
        logging.info('Obstacles node initialized')
        self._obstacles_pub = {}
        for obstac in obstacle_names:
            self._obstacles_pub[obstac] = self.create_publisher(Bool, f'{obstac}_topic', 10)

    def start_obstacle(self, obstacle_name: str):
        msg = Bool()
        msg.data = True
        self._publish_message(msg, obstacle_name)

    def stop_obstacle(self, obstacle_name: str):  #
        msg = Bool()
        msg.data = False
        self._publish_message(msg, obstacle_name)

    def append(self, obstacle_name: str):
        self._obstacles_pub[obstacle_name] = self.create_publisher(Bool, f'{obstacle_name}_topic', 10)
        logging.info(f'Current obstacle list: {list(self._obstacles_pub.keys())}')

    def _publish_message(self, msg: Bool, obstacle_name: str):
        if obstacle_name in self._obstacles_pub:
            self._obstacles_pub[obstacle_name].publish(msg)
            logging.info(f"Published message to {obstacle_name}_topic: {msg.data}")
        else:
            logging.warning(f"Obstacle {obstacle_name} not found.")

def main(args=None, command_queue=None):
    rclpy.init(args=args)
    node = ObstacleActivator(["adx", "jjj"])
    while True:
        try:
            command, obstacle = command_queue.get(timeout=TIME_OUT)
            rclpy.spin_once(node, timeout_sec=1.0)

            if command == 'start':
                node.start_obstacle(obstacle)
            elif command == 'stop':
                node.stop_obstacle(obstacle)
            else:
                logging.warning(f"Unknown command: {command}")

        except queue.Empty:
            continue
        except KeyboardInterrupt:
            break
    
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
