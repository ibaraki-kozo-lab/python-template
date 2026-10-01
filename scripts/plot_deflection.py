"""data/beams.csv の条件ごとのたわみを，1枚の図に描く（テンプレートの例）．

リポジトリの一番上で uv run python scripts/plot_deflection.py と実行する．
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from my_package import deflection


def main() -> None:
    # 1行目（列の名前）を飛ばし，「,」で区切った数を読む．
    # ndmin=2 は，条件が1行だけでも，1行に1つの条件が並んだ2次元の配列にする指定
    beams = np.loadtxt("data/beams.csv", delimiter=",", skiprows=1, ndmin=2)

    fig, ax = plt.subplots()
    for p, a, length, e, inertia in beams:
        x = np.linspace(0.0, length, 101)
        ax.plot(x, deflection(x, p, a, length, e, inertia), label=f"a = {a:.0f} mm")
    ax.invert_yaxis()  # 下向きのたわみが下に描かれるように，縦軸の上下を逆にする
    ax.set_xlabel("x [mm]")
    ax.set_ylabel("deflection [mm]")
    ax.legend()

    out = Path("results")
    out.mkdir(exist_ok=True)
    fig.savefig(out / "deflection.png", dpi=150)
    print(f"wrote {out / 'deflection.png'}")


if __name__ == "__main__":
    main()
