# MA-Metier_auto-pilot

## Description

This repository contains the code and resources for the MA-Metier_auto-pilot project, which focuses on developing an autonomous pilot system for a miniature glider with a simulator.

## Getting Started

### Prerequisites

- Python 3.14 or higher
- Microsoft Flight Simulator

### Installation

Install the required Python packages using pip:

```bash
# use Virtual Environment 
python3 -m venv env 

# on windows
env\Scripts\Activate.ps1

# on Linux and MacOS
source env/bin/activate

pip install -r requirements.txt
```

## Usage

### Available Commands

The program uses a command system. Here are the available commands:

#### List all commands

```bash
python main.py
```

#### Start the HTTP server

```bash
python main.py http
```

This command starts the web server with the API to control the aircraft.

#### Format code

```bash
python main.py format
```

This command automatically formats all Python files in the project.

#### Check formatting

```bash
python main.py check_format
```

This command checks if Python files are correctly formatted without modifying them.

### Usage Example

An autopilot example using api is available in [examples/go_straight_in_line.py](examples/go_straight_in_line.py).

#### Steps to use the program

1. **Start Microsoft Flight Simulator in a flight session**

2. **Start the HTTP server**

    ```bash
    python main.py http
    ```

    The server will start and be accessible at `http://localhost:8000`

3. **Run an autopilot script**

     ```bash
     python main.py auto_pilot
     ```

    This script uses the API to control the aircraft and maintain a heading of 90°.

### API Endpoints

Once the HTTP server is running, the API is available with the following endpoints:

- `GET /api/aircraft` - Get glider telemetry data
- `POST /api/aircraft` - Send glider control commands
- Web interface available at `/`

## Authors

- Leticia Dépierraz
- Ethann Schneider
- Amael Rochat
- Cédric Jankiewicz

## License

[MIT License](LICENSE)