import pytest
import math
from gameplay import hit_reaction_direction as mod

CASES = [
    ("rel", 'm.relative_dir((1, 1), (0, 0)) == (1, 1)'),
    ("world", 'm.world_dir((1, 0), 90) == approx((0, 1))'),
    ("bucket", 'm.angle_bucket(45, 8) == 1'),
    ("strongest", 'm.strongest([10, 30, 20]) == 30'),
    ("stagger", 'm.stagger(10, 0.03) == approx(0.3)'),
    ("knock", 'm.knockback(10, 2) == 5'),
    ("flatten", 'm.flatten((1, 2, 3)) == (1, 0, 3)'),
    ("sync", 'm.sync_dir((1, 0)) == (1, 0)'),
    ("armor", 'm.armor_blocks("super") is True'),
    ("camera", 'm.camera_dir((1, 0)) == (1, 0)'),
    ("angle", 'm.attack_angle(1, 1, 0, 0) == approx(45)'),
    ("flank", 'm.is_flank(90) is True'),
    ("total", 'm.total_damage([10, 20]) == 30'),
    ("key", 'm.hit_key(7) == "h:7"'),
    ("clamp", 'm.clamp_angle(-10) == 0')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
