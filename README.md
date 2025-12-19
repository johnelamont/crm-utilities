# CRM Utilities

A serverless function application built with Zoho Catalyst for CRM utility operations.

## Overview

This project contains utility functions for CRM operations, deployed as serverless functions using the Zoho Catalyst platform.

## Project Structure

```
crm-utilities/
├── functions/
│   └── crm_utilities_function/
│       ├── main.py                  # Main handler with endpoints
│       ├── no_auth_processes.py     # Non-authenticated utility functions
│       ├── requirements.txt         # Python dependencies
│       └── catalyst-config.json     # Function configuration
├── catalyst.json                    # Project configuration
└── README.md
```

## Prerequisites

- Python 3.x
- Zoho Catalyst SDK
- Flask

## Installation

1. Install the Catalyst SDK globally for code suggestions:
   ```bash
   python3 -m pip install zcatalyst-sdk
   ```

2. Install project dependencies:
   ```bash
   cd functions/crm_utilities_function
   pip install -r requirements.txt
   ```

## Available Endpoints

### GET /
Default endpoint that returns a welcome message.

**Response:**
```json
{
  "status": "success",
  "message": "Hello from main.py"
}
```

### GET /cache
Demonstrates cache operations using Catalyst's cache segment.

**Response:**
```json
{
  "key": "Name",
  "value": "DefaultName"
}
```

### GET /wait
Runs a timer for a specified number of seconds (no authentication required).

**Query Parameters:**
- `seconds` (required): Number of seconds to wait

**Example Request:**
```
GET /wait?seconds=5
```

**Success Response:**
```json
{
  "status": "success",
  "message": "Timer completed successfully after 5 seconds"
}
```

**Error Response:**
```json
{
  "status": "error",
  "message": "Missing required parameter: seconds"
}
```

## Module: no_auth_processes.py

Contains utility functions that don't require authentication.

### run_timer(seconds)
Executes a timer for the specified number of seconds.

**Parameters:**
- `seconds` (int): Number of seconds to wait

**Returns:**
- Dictionary with status and message

## Deployment

Deploy to Zoho Catalyst using the Catalyst CLI:

```bash
catalyst deploy
```

## Development

To add new endpoints:

1. For authenticated operations: Add a new `elif` block in `main.py` handler
2. For non-authenticated operations: Add functions to `no_auth_processes.py`

## License

Proprietary
