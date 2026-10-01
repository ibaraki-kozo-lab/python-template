"""単純はりに集中荷重を掛けたときの，たわみを計算する．

テンプレートの例なので，自分の計算に置き換える．
"""

import numpy as np
from numpy.typing import ArrayLike, NDArray


def deflection(
    x: ArrayLike, p: float, a: float, length: float, e: float, inertia: float
) -> float | NDArray[np.float64]:
    """左端から x [mm] の位置のたわみ [mm]（下向きを正）を返す．

    長さ length [mm] のはりの，左端から a [mm] の位置に荷重 p [N] を掛ける．
    e はヤング率 [N/mm2]，inertia は断面二次モーメント [mm4]．
    x は1つの数でも配列でもよい．配列なら，同じ形の配列で返す．
    """
    x = np.asarray(x, dtype=np.float64)
    b = length - a
    left = p * b * x * (length**2 - b**2 - x**2)  # 荷重より左の点の式
    right = p * a * (length - x) * (2 * length * x - x**2 - a**2)  # 荷重より右の点の式
    # np.where は，x <= a の点では left を，それ以外の点では right を選ぶ
    return np.where(x <= a, left, right) / (6 * e * inertia * length)
