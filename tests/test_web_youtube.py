"""Tests for YouTube-related utilities."""

import re
import pytest
from unittest.mock import patch, MagicMock
import time

from psykickai_tools.web.youtube import fetch_transcript

@pytest.fixture
def mock_transcript():
    return [
        {'text': 'First line', 'start': 0.0, 'duration': 1.5},
        {'text': 'Second line', 'start': 1.5, 'duration': 2.0}
    ]

def test_fetch_transcript_without_timestamp(mock_transcript):
    """Test fetching transcript without timestamps."""
    with patch('youtube_transcript_api.YouTubeTranscriptApi.get_transcript') as mock_get:
        mock_get.return_value = mock_transcript
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        
        result = fetch_transcript(url)
        assert isinstance(result, str)
        assert result == "First line Second line"

def test_fetch_transcript_with_timestamp(mock_transcript):
    """Test fetching transcript with timestamps."""
    with patch('youtube_transcript_api.YouTubeTranscriptApi.get_transcript') as mock_get:
        mock_get.return_value = mock_transcript
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        
        result = fetch_transcript(url, with_timestamp=True)
        assert isinstance(result, list)
        assert len(result) == 2
        assert result == mock_transcript

def test_fetch_transcript_invalid_url():
    """Test fetching transcript with invalid URL."""
    url = "https://www.youtube.com/invalid"
    with pytest.raises(ValueError, match="Could not extract video ID from URL"):
        fetch_transcript(url)

def test_fetch_transcript_api_error():
    """Test handling of API errors."""
    with patch('youtube_transcript_api.YouTubeTranscriptApi.get_transcript') as mock_get:
        mock_get.side_effect = Exception("API Error")
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        
        with pytest.raises(ValueError, match=re.escape(f"Could not fetch transcript for {url}: API Error")):
            fetch_transcript(url)

def test_fetch_transcript_list_without_timestamp(mock_transcript):
    """Test fetching transcripts for multiple URLs without timestamps."""
    with patch('youtube_transcript_api.YouTubeTranscriptApi.get_transcript') as mock_get:
        mock_get.return_value = mock_transcript
        urls = [
            "https://www.youtube.com/watch?v=video1",
            "https://www.youtube.com/watch?v=video2"
        ]
        
        result = fetch_transcript(urls)
        assert isinstance(result, list)
        assert len(result) == 2
        assert all(isinstance(r, str) for r in result)
        assert result == ["First line Second line", "First line Second line"]

def test_fetch_transcript_list_with_timestamp(mock_transcript):
    """Test fetching transcripts for multiple URLs with timestamps."""
    with patch('youtube_transcript_api.YouTubeTranscriptApi.get_transcript') as mock_get:
        mock_get.return_value = mock_transcript
        urls = [
            "https://www.youtube.com/watch?v=video1",
            "https://www.youtube.com/watch?v=video2"
        ]
        
        result = fetch_transcript(urls, with_timestamp=True)
        assert isinstance(result, list)
        assert len(result) == 2
        assert all(isinstance(r, list) for r in result)
        assert result == [mock_transcript, mock_transcript]

def test_fetch_transcript_empty_list():
    """Test fetching transcripts with empty list."""
    result = fetch_transcript([])
    assert isinstance(result, list)
    assert len(result) == 0

def test_fetch_transcript_list_with_invalid_url(mock_transcript):
    """Test fetching transcripts with a list containing an invalid URL."""
    with patch('youtube_transcript_api.YouTubeTranscriptApi.get_transcript') as mock_get:
        mock_get.return_value = mock_transcript
        urls = [
            "https://www.youtube.com/watch?v=video1",
            "https://www.youtube.com/invalid",
            "https://www.youtube.com/watch?v=video3"
        ]
        
        with pytest.raises(ValueError, match="Could not extract video ID from URL"):
            fetch_transcript(urls)

def test_fetch_transcript_delay_between_requests(mock_transcript):
    """Test that there is a delay between fetching multiple transcripts."""
    with patch('youtube_transcript_api.YouTubeTranscriptApi.get_transcript') as mock_get, \
         patch('time.sleep') as mock_sleep:
        mock_get.return_value = mock_transcript
        urls = [
            "https://www.youtube.com/watch?v=video1",
            "https://www.youtube.com/watch?v=video2",
            "https://www.youtube.com/watch?v=video3"
        ]
        
        fetch_transcript(urls)
        
        # Check that sleep was called twice (between the three requests)
        assert mock_sleep.call_count == 2
        assert all(call.args[0] == 3 for call in mock_sleep.call_args_list) 