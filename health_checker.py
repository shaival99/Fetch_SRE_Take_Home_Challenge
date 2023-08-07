import sys
import time
import requests
import yaml

# Define the user agent for HTTP requests
USER_AGENT = "fetch-synthetic-monitor"

# Function to test endpoint health
def test_endpoint(endpoint):
    try:
        start_time = time.time()
        response = requests.request(
            method=endpoint.get("method", "GET"),
            url=endpoint["url"],
            headers=endpoint.get("headers", {"User-Agent": USER_AGENT}),
            data=endpoint.get("body"),
        )
        latency = time.time() - start_time

        if (
            response.status_code >= 200
            and response.status_code < 300
            and latency < 0.5
        ):
            return "UP"
        else:
            return "DOWN"
    except Exception:
        return "DOWN"

# Function to calculate availability percentage
def calculate_availability(up_count, total_count):
    if total_count == 0:
        return 0
    return round((up_count / total_count) * 100)

# Main function
def main(config_file_path):
    try:
        with open(config_file_path, "r") as file:
            domains = {}  # Dictionary to store domain names and endpoint statuses
            endpoints = yaml.safe_load(file)

            # Initialize the domains dictionary with domain names
            for endpoint in endpoints:
                domain = endpoint["url"].split("//")[-1].split("/")[0]
                if domain not in domains:
                    domains[domain] = {"up": 0, "total": 0}
            while True:
                for domain in domains:
                    domain_stats = domains[domain]

                    # Iterate through endpoints and update statistics for the domain
                    for endpoint in endpoints:
                        endpoint_domain = endpoint["url"].split("//")[-1].split("/")[0]
                        if endpoint_domain == domain:
                            domain_stats["total"] += 1
                            if test_endpoint(endpoint) == "UP":
                                domain_stats["up"] += 1

                # Display availability percentages for each domain
                for domain, stats in domains.items():
                    availability_percentage = calculate_availability(stats["up"], stats["total"])
                    print(f"{domain} has {availability_percentage:.2f}% availability percentage")

                time.sleep(15)

    except KeyboardInterrupt:
        print("Exiting the program.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python program.py <config_file_path>")
    else:
        config_file_path = sys.argv[1]
        main(config_file_path)
