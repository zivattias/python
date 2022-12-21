# Given a string that represents DNA, check whether a given DNA string contain a TATA-box-like pattern.
#
# TATA-box-like pattern has the following structure: “TATAA” followed by 3 nucleotides and ends with “TT”
# Nucleotide is one of: [A, C, G, T]

# Examples of TATA-box-like DNA:
# "ACGACGTTTACACGGATATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAA" - True
# "ACGACGTTTACACGGAAATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAA" - False

import re


def match_tata(seq: str) -> bool:
    match = re.match('.*TATAA[ACGT]{3}TT.*', seq)
    if match is not None:
        return True
    return False


def search_tata(seq: str) -> re.Match | None:
    search = re.search('TATAA[ACGT]{3}TT', seq)
    return search


if __name__ == '__main__':
    seq_1 = "ACGACGTTTACACGGATATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAA"
    seq_2 = "ACGACGTTTACACGGAAATAAGGGTTACGCGCTGTATAATTTCAGCTGATTCGAA"
    print(match_tata(seq_1))
    print(match_tata(seq_2))
    print(search_tata(seq_1))
    print(search_tata(seq_2))
