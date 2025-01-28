"""Tests for the file operations module."""

import pytest
from pathlib import Path
from psykickai_tools.io.file_ops import (
    read_file_content,
    write_file_content,
    append_file_content,
)

@pytest.fixture
def temp_file(tmp_path):
    """Create a temporary file for testing."""
    file_path = tmp_path / "test.txt"
    return file_path

def test_write_and_read_file(temp_file):
    """Test writing content to a file and reading it back."""
    content = "Hello, World!"
    write_file_content(temp_file, content)
    assert temp_file.exists()
    
    read_content = read_file_content(temp_file)
    assert read_content == content

def test_append_file_content(temp_file):
    """Test appending content to a file."""
    initial_content = "First line"
    append_content = "Second line"
    
    write_file_content(temp_file, initial_content)
    append_file_content(temp_file, append_content)
    
    content = read_file_content(temp_file)
    assert content == f"{initial_content}\n{append_content}"

def test_read_nonexistent_file():
    """Test reading a file that doesn't exist raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        read_file_content("nonexistent.txt")

def test_write_to_nested_directory(tmp_path):
    """Test writing to a file in a nested directory structure."""
    nested_path = tmp_path / "deep" / "nested" / "dir" / "test.txt"
    content = "Test content"
    
    write_file_content(nested_path, content, create_dirs=True)
    assert nested_path.exists()
    assert read_file_content(nested_path) == content

def test_append_without_newline(temp_file):
    """Test appending content without adding a newline."""
    initial_content = "First"
    append_content = "Second"
    
    write_file_content(temp_file, initial_content)
    append_file_content(temp_file, append_content, add_newline=False)
    
    content = read_file_content(temp_file)
    assert content == f"{initial_content}{append_content}"