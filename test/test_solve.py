from io import BytesIO
from pathlib import Path

import pytest

from dna_nexus.solve import solve, str_to_bytes

INPUT = "00000000111000001100000101111111"
SOLUTION = """@READ_1
AT
+READ_1
!A
@READ_2
TC
+READ_2
"`"""


def test_solve_on_example() -> None:
    stream = BytesIO(str_to_bytes(INPUT))
    assert solve(stream, 2) == SOLUTION


@pytest.mark.parametrize("length", [7, 15, 80])
def test_solve(length: int) -> None:
    assert (
        solve((Path(__file__).parent / "input").open("rb"), length).split()
        == (Path(__file__).parent / f"output{length}").read_text().split()
    )
