import logging
from typing import Optional, Callable
from rclpy.node import Node
from std_msgs.msg import Bool

class Tower(Node):
    def __init__(self):
        super().__init__("Tower")
        self._topicName = "/tower_move"
        self._publisher = self.create_publisher(Bool, self._topicName, 10)

    def throw_ball(self) -> None:
        msg = Bool()
        msg.data = True
        self._publisher.publish(msg)
        logging.info(f"[TOWER] throwed the ball")
