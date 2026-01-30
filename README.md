# AI-Based PPE Compliance & Safety Surveillance System

## Problem Statement
Manual PPE monitoring in construction sites is reactive, inconsistent, and does not scale
across large and dynamic environments, leading to preventable safety incidents.

## Proposed Solution
This project proposes a real-time computer vision system that automatically detects
PPE compliance (helmet, vest, gloves, boots, harness) using deep learning models
on live CCTV or camera feeds.

## Key Features
- Real-time multi-PPE detection
- YOLO-based object detection
- Instant alerts for safety violations
- Scalable architecture for multi-camera sites

## System Architecture
Camera Feed → Frame Processing → PPE Detection Model → Compliance Logic → Alerts & Dashboard

## Tech Stack
- Python
- YOLOv8
- OpenCV
- Flask / Streamlit (for dashboard)

## Project Status
This repository currently contains the project design, architecture, and documentation.
Model training and deployment will be implemented in the next phase.

## Future Enhancements
- Unsafe action detection
- PPE compliance confidence scoring
- Mobile alerts and access control integration## Architecture Diagram
Refer to docs/architecture.png for the system architecture.

## Architecture Diagram
Refer to docs/architecture.png for the system architecture.

## Code Status
Current code represents a prototype inference pipeline.
Model training and optimization will be completed in the next phase.


