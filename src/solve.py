from dataclasses import dataclass
from itertools import batched
from typing import IO
from pathlib import Path

import typer

NUCLEOTIDE_MAP = {0: "A", 64: "C", 128: "G", 192: "T"}

BITS = [128, 64, 32, 16, 8, 4, 2, 1]

EXCLAMATION_MARK_CODE = 33


@dataclass
class Nucleotide:
    nucleotide: str
    confidence: int

    @property
    def confidence_symbol(self) -> str:
        return chr(self.confidence + EXCLAMATION_MARK_CODE)


def str_to_bytes(binary_representation: str) -> bytes:
    number = int(binary_representation, 2)
    size = len(binary_representation) // 8
    return number.to_bytes(size)


def solve(data: IO, length: int) -> str:
    nucleotides: list[Nucleotide] = []
    while byte := data.read(1):
        nucleotide_code = byte[0] & sum(BITS[:2])
        nucleotide = NUCLEOTIDE_MAP[nucleotide_code]
        confidence = byte[0] & sum(BITS[2:])
        nucleotides.append(Nucleotide(nucleotide=nucleotide, confidence=confidence))
    fastaq = []
    for i, group in enumerate(batched(nucleotides, length), start=1):
        fastaq.append(f"@READ_{i}")
        fastaq.append("".join([nucleotide.nucleotide for nucleotide in group]))
        fastaq.append(f"+READ_{i}")
        fastaq.append("".join([nucleotide.confidence_symbol for nucleotide in group]))
    return "\n".join(fastaq)


def main(input_file: Path, lenght: int):
    with input_file.open("r+b") as opened_file:
        print(solve(opened_file, lenght))


if __name__ == "__main__":
    typer.run(main)
