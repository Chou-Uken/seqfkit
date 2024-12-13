import pytest
from seqfkit.utils import read_fasta
import os
from seqfkit.utils import read_first_fasta

@pytest.fixture
def fasta_file():
    fasta_content = ">seq1\nATGCGTA\n>seq2\nCGTACGTAGCTA\n>seq3\nGCTAGCTAGCTA"
    fasta_file_path = '/tmp/test.fasta'
    with open(fasta_file_path, 'w') as f:
        f.write(fasta_content)
    yield fasta_file_path
    os.remove(fasta_file_path)

@pytest.fixture
def empty_file():
    empty_file_path = '/tmp/empty.fasta'
    with open(empty_file_path, 'w') as f:
        f.write('')
    yield empty_file_path
    os.remove(empty_file_path)

@pytest.fixture
def no_seq_file():
    no_seq_content = ">seq1\n>seq2\n>seq3"
    no_seq_file_path = '/tmp/no_seq.fasta'
    with open(no_seq_file_path, 'w') as f:
        f.write(no_seq_content)
    yield no_seq_file_path
    os.remove(no_seq_file_path)

def test_read_fasta(fasta_file):
    expected_output = {
        'seq1': 'ATGCGTA',
        'seq2': 'CGTACGTAGCTA',
        'seq3': 'GCTAGCTAGCTA'
    }
    result = read_fasta(fasta_file)
    assert result == expected_output

def test_read_fasta_empty_file(empty_file):
    result = read_fasta(empty_file)
    assert result == {}

def test_read_fasta_no_sequences(no_seq_file):
    expected_output = {'seq1': '', 'seq2': '', 'seq3': ''}
    result = read_fasta(no_seq_file)
    assert result == expected_output

def test_read_first_fasta(fasta_file):
    expected_output = 'ATGCGTA'
    result = read_first_fasta(fasta_file)
    assert result == expected_output

def test_read_first_fasta_empty_file(empty_file):
    result = read_first_fasta(empty_file)
    assert result == ''

def test_read_first_fasta_no_sequences(no_seq_file):
    result = read_first_fasta(no_seq_file)
    assert result == ''
