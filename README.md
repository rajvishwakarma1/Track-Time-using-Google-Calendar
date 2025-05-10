# Track Time Using Google Calendar

**Track Time Using Google Calendar** is a Python automation script designed to help you monitor and analyze your time spent on various activities by leveraging the Google Calendar API.

## 📌 Features

* **Automated Time Tracking**: Fetches events from your Google Calendar to calculate the time spent on each activity.
* **Customizable Analysis**: Modify the script to analyze specific calendars or time frames according to your needs.
* **Simple and Lightweight**: A straightforward script without unnecessary complexities.

## 💠 Technologies Used

* **Programming Language**: Python
* **APIs**: Google Calendar API

## 🚀 Getting Started

### Prerequisites

* Python 3.x installed on your system.
* Google Calendar account with API access enabled.
* Google API credentials (credentials.json file).

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/rajvishwakarma1/Track-Time-using-Google-Calendar.git
   cd Track-Time-using-Google-Calendar
   ```

2. **Install required Python packages**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Google Calendar API credentials**:

   * Follow the instructions to create a project in the [Google Developers Console](https://console.developers.google.com/).
   * Enable the Google Calendar API for your project.
   * Create credentials and download the `credentials.json` file.
   * Place the `credentials.json` file in the project directory.

## 📈 Usage

1. **Run the script**:

   ```bash
   python google_calendar_time_tracker.py
   ```

2. The script will authenticate with your Google account and fetch events from your calendar.

3. It will then calculate and display the time spent on each event.

## 📁 Project Structure

```
Track-Time-using-Google-Calendar/
├── google_calendar_time_tracker.py  # Main script
├── credentials.json                 # Google API credentials
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation
```

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*Developed by [Raj Vishwakarma](https://github.com/rajvishwakarma1).*
