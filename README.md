
# SolarCalc - Solar Energy Calculator

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

SolarCalc is a comprehensive solar energy calculator designed to help homeowners, businesses, and solar installers estimate solar power system requirements with precision.

## 📱 Overview

SolarCalc provides an intuitive web interface for calculating solar system components, estimating costs, and generating detailed bills of materials. Whether you're a homeowner exploring solar options or a professional installer preparing quotes, SolarCalc streamlines the entire estimation process.

## ✨ Key Features

- ⚡ Quick System Size Estimator
- 🔧 Detailed PV System Calculator
- 📋 Bill of Materials Generator
- 📊 Real-time Calculations
- 📱 Responsive Design
- 📄 Print-Friendly Reports
- 🔒 Privacy-Focused (Client-side calculations only)

## 🏗️ System Architecture

```text
Frontend (HTML/CSS/JS)
        │
        ▼
     Flask Backend
        │
        ▼
   Jinja2 Templates
        │
        ▼
 Static Assets (CSS/Images)
```

# 🚀 Quick Start

## Prerequisites

- Python 3.7+
- pip

### Clone the Repository

```bash
git clone https://github.com/imtona44/solarcalc.git
cd solarcalc
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python Solar.py
```

Application: **http://localhost:5000**

## 🎯 Usage Guide

### Quick System Size Estimator

1. Enter monthly electricity bill.
2. Enter monthly energy consumption (kWh).
3. Click **Calculate System Size**.
4. Review recommended PV system size.

### Detailed PV Calculator

Configure:

- System Voltage
- PV Module Rating
- PV Module Isc
- Advanced Settings
- Device Loads

Results include:

- Energy Consumption
- Solar Panels
- Battery Bank
- Inverter
- Charge Controller

### Bill of Materials

Generate and print a complete component list after calculation.

## 📁 Project Structure

```text
solarcalc/
├── Solar.py
├── requirements.txt
├── LICENSE
├── README.md
├── templates/
├── static/
└── docs/
```

## 🔧 API Endpoints

| Route | Method | Description |
|------|------|-------------|
| / | GET | Home |
| /system-size | GET | Quick estimator |
| /detailed-calculator | GET | Detailed calculator |
| /materials | GET | Materials |
| /about | GET | About |
| /privacy | GET | Privacy |
| /api/calculate-system-size | POST | Quick calculation |
| /api/calculate-detailed-system | POST | Full calculation |

## 📊 Calculation Methodology

```python
Daily Consumption = Monthly Consumption / 30
System Size = Daily Consumption / (24 * PanelEfficiency)

TotalWh = Σ(DeviceWatts * DeviceHours)
RequiredWh = TotalWh * SystemLossFactor
Panels = ceil(TotalWp / PanelRating)
BatteryAh = (TotalWh * DaysAutonomy) / (Derating * DOD * Voltage)
Inverter = TotalDeviceWatts * 1.25
Controller = ceil(Panels * Isc * 1.3)
```

## ⚙️ Default Parameters

| Parameter | Value |
|-----------|------:|
| System Loss Factor | 1.3 |
| Panel Generation Factor | 3.43 |
| Days of Autonomy | 3 |
| Derating Factor | 0.85 |
| Depth of Discharge | 0.6 |
| Panel Efficiency | 0.16 |

## 📦 Installation Options

### Standard

```bash
pip install -r requirements.txt
```

### Development

```bash
python -m venv venv
pip install -r requirements-dev.txt
python Solar.py
```

### Production

```bash
gunicorn -w 4 Solar:app
```

or

```bash
waitress-serve --port=5000 Solar:app
```

## 🧪 Testing

```bash
python -m pytest tests/
python -m pytest --cov=. tests/
```

## 🐛 Troubleshooting

| Issue | Solution |
|------|----------|
| Port already in use | Change port |
| Missing dependencies | Install requirements |
| Template missing | Verify templates folder |
| Static files missing | Check static folder |

## 🤝 Contributing

1. Fork repository
2. Create feature branch
3. Commit changes
4. Push branch
5. Open Pull Request

## 📄 License

Educational project using the MIT License.

## ⚠️ Disclaimer

Results are estimates only. Consult a certified solar engineer before installation.

## 📞 Support

- **Email:** region2@tesda.gov.ph
- **Telephone:** (078) 846-1618
- **Address:** TESDA Region II, Tuguegarao, Cagayan

## 🙏 Acknowledgments

- LEONICS Solar PV System Design
- TESDA Region II
- Font Awesome
- Community Contributors

## ⭐ Star the Project

If you found this project useful, please consider giving it a ⭐ on GitHub.

Built with ❤️ for the renewable energy community.
