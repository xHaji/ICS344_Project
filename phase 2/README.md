# Phase 2: SIEM (Splunk) Attack Log Analysis and Visualization

Having accomplished the first stage of service compromise, the following step is to analyze and visualize attack information using a Security Information and Event Management (SIEM) system). Splunk was previously stated as the chosen SIEM platform due to its predominant position in the industry for its unparalleled data indexing, searching, and visulazation capabilities. In this phase, all generated attack data was first uploaded into Splunk and analyzed using pre-defined custom dashboards and visualizations tailored specifically for identifying the types and frequencies of attacks.

---

## Splunk Setup and Installation

Splunk was installed directly on the attacker machine (Kali Linux 2024) to serve as the central log analysis platform.

### Installation Steps:

1. Download Splunk from the official site:
   - File: splunk-8.2.6-a6fe1ee8894b-linux-2.6-amd64.deb

2. Install the .deb package using:
   sudo dpkg -i splunk-8.2.6-a6fe1ee8894b-linux-2.6-amd64.deb

3. Start Splunk:
   sudo /opt/splunk/bin/splunk start --accept-license

![Starting Splunk CLI](./screenshots/splunk_startup_cli.png)

4. Access the Splunk Web Interface at:
   https://localhost:8000

![Splunk Web Dashboard](./screenshots/splunk_dashboard_home.png)

---

## Attack Data Collection

At this stage, active reconnaissance and vulnerability scanning techniques were applied on the victim machine to generate attack data. To obtain advanced information regarding the HTTP service running on the target machine, three different approaches were applied:

### 1. Nmap Scan
Command:
nmap -sV -p 80 192.168.56.109 -oN http_nmap_scan.txt

### 2. Nikto Web Server Vulnerability Scan
Command:
nikto -h http://192.168.56.109 -o http_nikto_scan.txt

### 3. Custom Python HTTP Banner Script
Command:
python3 http_script.py > http_custom_scan.txt

![Prepared Log Files](./screenshots/log_files_and_script.png)

---

## Data Ingestion into Splunk

The three log files were uploaded using Splunk's "Add Data" feature:
- http_nmap_scan.txt
- http_nikto_scan.txt
- http_custom_scan.txt

Each file was uploaded with source type: Automatic detection, and assigned to index: main.

![Upload Success](./screenshots/splunk_upload_success.png)
![Log Source Count](./screenshots/log_sources_count.png)

---

## Searching Attack Events

To verify ingestion, a search was run using the query:
index="main"

This returned results from all three sources:
- Nmap scan
- Nikto scan
- Custom Python script

![Search Query Results](./screenshots/splunk_search_index_main.png)
![Nmap Event Detail](./screenshots/splunk_event_nmap_detail.png)
![Nikto Event Detail](./screenshots/splunk_event_nikto_detail.png)
![Python Script Event](./screenshots/splunk_event_http_script.png)

---

## Dashboard Creation and Visualization

A dashboard titled "HTTP Attack Dashboard" was created in Splunk with the following panels:

### Pie Chart Panel
A pie chart was created that showed how each source of attack contributed to the total number of attacks. Namely, it illustrated what proportion of the attacks came from Nmap, Nikot, and the custom Python script developed from the provided .txt files.

![Pie Chart](./screenshots/dashboard_pie_chart.png)

### Bar Chart Panel
A histogram was added to track the number of events from each source: http_nmap_scan.txt, http_nikto_scan.txt, and http_script_output.txt. This enabled him to analyze the traffic or log entries for each type of attack and repurpose the data for easier comparison.

![Bar Chart](./screenshots/dashboard_bar_chart.png)

### Single Value Panel
A custom data panel was created which showed the total number of attack events registered as a single value. This enhanced monitoring efforts by providing a quick figure summary.

![Single Value Panel](./screenshots/dashboard_single_value_panel.png)

---

## Summary

In this phase, attack data was successfully generated using multiple tools, ingested into Splunk, and visualized using a custom dashboard. This process highlighted how SIEM platforms can transform raw log data into meaningful insights for monitoring, threat detection, and analysis.
