import importlib.util
from pathlib import Path


def _load_remaining_fraction():
    repo_root = Path(__file__).resolve().parents[1]
    calc_path = repo_root / 'scripts' / 'decay_calculator.py'
    spec = importlib.util.spec_from_file_location('decay_calculator', str(calc_path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.remaining_fraction


def test_remaining_at_t0():
    remaining_fraction = _load_remaining_fraction()
    assert abs(remaining_fraction(0, 30) - 1.0) < 1e-9


def test_remaining_at_half_life():
    remaining_fraction = _load_remaining_fraction()
    assert abs(remaining_fraction(30, 30) - 0.5) < 1e-6
