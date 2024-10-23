from dataclasses import dataclass

EXCLAMATION_MARK_CODE = 33


@dataclass
class Nucleotide:
    nucleotide: str
    confidence: int

    @property
    def confidence_symbol(self) -> str:
        return chr(self.confidence + EXCLAMATION_MARK_CODE)
