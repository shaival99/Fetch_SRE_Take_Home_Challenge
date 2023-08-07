# Fetch_SRE_Take_Home_Challenge


This is a Python program that monitors the health of a set of HTTP endpoints and calculates availability percentages for each domain. It reads input from a YAML configuration file, tests the health of endpoints every 15 seconds, and logs cumulative availability percentages for each domain.

## Getting Started

### Prerequisites

Make sure you have Python installed on your system. You can download it from the official Python website: [Python Downloads](https://www.python.org/downloads/)

### Installation

1. Clone this repository to your local machine:

```
git clone https://github.com/your-username/http-endpoint-health-checker.git
```

### Navigate to the repository directory
Change the directory name to wherever your file is located
```
cd http-endpoint-health-checker
```

### Install the required Python packages:
```
pip install requests pyyaml
```

### Usage

Run the program by providing the path to your YAML configuration file as a command-line argument:

```
python health_checker.py path/to/config.yaml
```
Replace path/to/config.yaml with the actual path to your configuration file.

The program will continuously test the health of the endpoints every 15 seconds and display the availability percentage for each domain. You can manually exit the program using Ctrl+C.


