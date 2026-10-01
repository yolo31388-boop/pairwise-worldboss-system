"""世界BOSS - 带8个bug"""
from dataclasses import dataclass, field
import random, time

@dataclass
class Boss:
    bid: str
    name: str
    hp: float
    max_hp: float
    phase: int
    debuffs: list

class WorldBossSystem:
    def __init__(self):
        self.bosses: dict[str, Boss] = {}
        self.damage = {}  # player_id -> total damage
        self.claimed = {}
        self.refresh_time = 0

    def refresh(self, server_id):
        # bug1: 全局固定时间
        self.refresh_time = time.time() + 3600

    def get_aggro(self, damage, taunt, distance):
        # bug2: 只看伤害
        return damage

    def switch_phase(self, bid):
        boss = self.bosses[bid]
        boss.phase += 1
        # bug3: 不清debuff
        boss.hp = boss.max_hp

    def get_ranking(self):
        # bug4: 只看总伤害
        return sorted(self.damage.items(), key=lambda x: x[1], reverse=True)

    def get_reward(self, rank):
        # bug5: 第4名以后都一样
        if rank <= 3:
            return {"gold": 10000}
        return {"gold": 100}

    def can_participate(self, player_id, damage_dealt):
        # bug7: 无最低伤害门槛
        return True

    def claim_reward(self, player_id, kill_id):
        # bug8: 无幂等
        return {"gold": 1000}
