"""beam の関数を，答えの分かる問題で確かめる．"""

import pytest

from my_package import deflection

P, LENGTH, E, INERTIA = 10_000.0, 1_000.0, 205_000.0, 8.0e6


def test_midspan_load_gives_pl3_over_48ei():
    expected = P * LENGTH**3 / (48 * E * INERTIA)
    assert deflection(LENGTH / 2, P, LENGTH / 2, LENGTH, E, INERTIA) == pytest.approx(
        expected
    )


def test_supports_do_not_move():
    v = deflection([0.0, LENGTH], P, 300.0, LENGTH, E, INERTIA)
    assert v == pytest.approx([0.0, 0.0])


def test_reciprocal_theorem():
    # 300 mm の点に荷重を掛けたときの 700 mm の点のたわみは，700 mm の点に掛けたときの
    # 300 mm の点のたわみと等しい（マクスウェルの相反定理）．荷重より右の点の式も確かめる
    v_at_700 = deflection(700.0, P, 300.0, LENGTH, E, INERTIA)
    v_at_300 = deflection(300.0, P, 700.0, LENGTH, E, INERTIA)
    assert v_at_700 == pytest.approx(v_at_300)
