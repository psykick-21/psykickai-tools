# psykickai-tools

A collection of reusable Python tools and utilities (logging, etc.) designed to streamline project setup and provide out-of-the-box functionality for common development needs.

## Available functionalities

### Logger

The logger provides a pre-configured logging system with both console and file output. It offers:
- Console output for INFO level and above with a concise format showing time, level, and message
- Daily rotating file logs with detailed format including file path and line numbers
- Debug level logging in files for comprehensive debugging
- Automatic log directory creation

#### Example Usage

```python
from psykickai_tools.utils import logger

# Different logging levels
logger.debug("Detailed debug information")  # Only appears in log file
logger.info("General information")          # Appears in both console and file
logger.warning("Warning message")           # Appears in both console and file
logger.error("Error message")              # Appears in both console and file
logger.critical("Critical error")          # Appears in both console and file
```

Console output will show:
```
14:30:45 | INFO     | General information
14:30:45 | WARNING  | Warning message
```

Log file (`logs/app_YYYYMMDD.log`) will contain:
```
2024-01-27 14:30:45 | DEBUG    | /path/to/your/file.py:10 | Detailed debug information
2024-01-27 14:30:45 | INFO     | /path/to/your/file.py:11 | General information
2024-01-27 14:30:45 | WARNING  | /path/to/your/file.py:12 | Warning message
```