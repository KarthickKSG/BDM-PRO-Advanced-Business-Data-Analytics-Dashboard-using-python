    
# 📊 BDM-PRO: Advanced Business Data Analytics Dashboard

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)

**BDM-PRO** is a high-performance, interactive data visualization platform built with Python. It is specifically designed to handle complex financial transaction logs, providing business owners and analysts with real-time insights through a modern, blue glassmorphism interface.

## 🌟 Visual Previews
| Revenue Trends | Peak Hour Analytics |
|---|---|
| ![Revenue](https://github.com/KarthickKSG/BDM-PRO-Advanced-Business-Data-Analytics-Dashboard-using-python/blob/main/Screenshot%202026-01-03%20at%2023-47-21%20BDM%20Pro%20Analytics.png?raw=true) | ![Hourly](https://github.com/KarthickKSG/BDM-PRO-Advanced-Business-Data-Analytics-Dashboard-using-python/blob/main/Screenshot%202026-01-03%20at%2023-47-42%20BDM%20Pro%20Analytics.png?raw=true) |

## ✨ Core Features

*   **⚡ Real-Time CSV Processing**: Instant cleaning and formatting of raw data.
*   **💎 Glassmorphism UI**: Premium dark-blue professional theme with CSS animations.
*   **📈 Smart KPIs**: Track GMV, Success Rate, Average Ticket Size, and Unique Customers.
*   **🕒 Activity Heatmaps**: Identify peak transaction hours to optimize business operations.
*   **💳 Payment Insights**: Sunburst and Pie charts for Payment Mode and Status correlation.
*   **🔍 Multi-Layer Filtering**: Drill down by Date Range, Transaction Status, and Payment Methods.
*   **📥 Data Export**: Export filtered data directly to a clean CSV report.

---

## 🚀 Setup & Installation Guide

### Prerequisites
- Python 3.8 or higher installed on your system.

### 🪟 Windows Installation
1. **Clone the Repo:**
   ```bash
   git clone https://github.com/KarthickKSG/BDM-PRO-Advanced-Business-Data-Analytics-Dashboard-using-python.git
   cd BDM-PRO-Advanced-Business-Data-Analytics-Dashboard-using-python

  

    Create Virtual Environment:
    code Bash

    
python -m venv venv
venv\Scripts\activate

  

Install Dependencies:
code Bash

    
pip install -r requirements.txt

  

Launch App:
code Bash

        
    streamlit run app.py

      

🐧 Linux Installation

    Clone the Repo:
    code Bash

    
git clone https://github.com/KarthickKSG/BDM-PRO-Advanced-Business-Data-Analytics-Dashboard-using-python.git
cd BDM-PRO-Advanced-Business-Data-Analytics-Dashboard-using-python

  

Setup Environment:
code Bash

    
python3 -m venv venv
source venv/bin/activate

  

Install Dependencies:
code Bash

    
pip install -r requirements.txt

  

Launch App:
code Bash

        
    streamlit run app.py

      

📖 Application Manual
1. Data Upload

    Click on "Browse files" in the left sidebar.

    Upload your transaction CSV (the app is optimized for standard payment gateway formats).

2. Analysis & Filtering

    Date Filter: Select a specific range to see revenue growth over time.

    Status Filter: Toggle between SUCCESS and FAILURE to analyze drop-off rates.

    Payment Mode: Compare UPI vs Credit Card performance.

3. Interpreting Charts

    Revenue Timeline: Hover over the area chart to see specific daily earnings.

    Peak Hours: Check the bar chart to see which hours (0-23) have the most traffic.

    Sunburst Chart: Click segments to see the success/failure breakdown per payment method.

4. Exporting Reports

    Once you have applied your desired filters, use the "Download Filtered Report" button to save the specific data to your computer.

🛠️ Built With

    Streamlit - The web framework for Data Apps.

    Pandas - Data manipulation and analysis.

    Plotly - Interactive graphing library.

    Matplotlib - Advanced table styling.

👤 Developer

Karthick KSG

    GitHub: @KarthickKSG

Built with ❤️ for Data-Driven Businesses.
code Code

    
---

### 3. Professional Setup Script (`setup.sh`)
To make it very easy for Linux users, you can also add this `setup.sh` file:

```bash
#!/bin/bash

echo "🚀 Starting BDM-PRO Setup..."

# Update and install python venv if not present
sudo apt-get update
sudo apt-get install python3-venv -y

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Setup Complete!"
echo "👉 To run the app, type: streamlit run app.py"

  
