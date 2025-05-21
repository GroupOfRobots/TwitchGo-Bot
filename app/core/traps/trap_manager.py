import yaml
import os
from app.core.traps.trap import Trap
from typing import Dict
import random
import rclpy

class TrapManager:
    def __init__(self):
        self._init_ros()
        self.traps: Dict[str, Trap] = {}
        self._load_traps()
        self.current_running_trap = None
    
    def _init_ros(self):
        if not rclpy.ok():
            rclpy.init()

    def _load_traps(self):
        config_path = os.path.join("app", "config", "traps.yaml")
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)
            for trap_data in config.get("traps", []):
                name = trap_data["name"]
                topic = trap_data["ros_topic"]
                label = trap_data["label"]
                self.traps[name] = Trap(name=name, label=label, topicName=topic)

    def add_vote(self, trap_name: str, username: str):
        if trap_name in self.traps:
            self.traps[trap_name].add_vote(username)

    def clear_votes(self):
        for trap in self.traps.values():
            trap.clear_votes()

    def get_votes(self):
        return self.traps

    def get_winning_trap(self) -> Trap:
        max_votes = 1 # co najmniej jeden głos aby aktywować przeszkode
        winners = []
        for trap in self.traps.values():
            votes = trap.count_votes()
            if votes > max_votes:
                max_votes = votes
                winners = [trap]
            elif votes == max_votes:
                winners.append(trap)
        return random.choice(winners) if winners else None

    def next_choicing_round(self):
        if self.current_running_trap:
            self.current_running_trap.stop() 

        self.current_running_trap = self.get_winning_trap()
        self.clear_votes()
        if self.current_running_trap:
            self.current_running_trap.run()
       
    def current_voiting_state(self) -> str:
        StringBuilder = []
        for trap in self.traps.values():
            StringBuilder.append(str(trap))

        return ", ".join(StringBuilder)