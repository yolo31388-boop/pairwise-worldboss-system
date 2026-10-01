"""世界BOSS测试"""
import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.engine import WorldBossSystem, Boss

class TestAggro:
    def test_taunt_matters(self):
        wbs = WorldBossSystem()
        a1 = wbs.get_aggro(100, 0, 10)
        a2 = wbs.get_aggro(50, 100, 5)
        assert a2 > a1, "嘲讽不影响仇恨"

class TestReward:
    def test_reward_tiers(self):
        wbs = WorldBossSystem()
        r3 = wbs.get_reward(3)
        r4 = wbs.get_reward(4)
        r50 = wbs.get_reward(50)
        assert r4 != r50, "4名和50名奖励一样"
