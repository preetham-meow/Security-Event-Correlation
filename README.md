# Security Event Correlation System

A security event correlation system that connects multiple independent security events into a meaningful security incident, detects suspicious sequences, assigns severity, and recommends a response.

## Problem Statement

Develop a security event correlation system capable of connecting multiple seemingly independent events into a meaningful security incident.

**Example sequence:** Failed Login → Successful Login → Unusual File Access

## Features

- Ingests security events (user, event type, timestamp)
- Correlates related events per user
- Identifies suspicious event sequences occurring in order
- Assigns incident severity (Medium / High) based on failed login count
- Generates alerts with a recommended response

## How It Works

1. Events are grouped by user
2. Events are sorted chronologically
3. The system checks whether the sequence `failed_login → successful_login → unusual_file_access` occurs in order
4. If detected, severity is calculated:
   - **High** — 3 or more failed logins before success
   - **Medium** — fewer than 3 failed logins
5. An alert is generated with the matched events and a recommended response

## Example Output
