# Logic and Reasoning Android App

This is an Android application developed using Python and Kivy, designed to test and enhance the user's logic and reasoning skills. The app includes 6 chapters, each containing 4-6 questions. Users can switch between questions and answers within each chapter, providing an interactive learning experience.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Features

- Interactive questions and answers for 6 chapters.
- Smooth navigation between questions and answers.
- User-friendly interface with a consistent theme.
- Developed using Python and Kivy.

## Installation

### Prerequisites

- Python 3.6 or later
- Kivy 2.2.1 or later
- Buildozer (for building the Android APK)

### Clone the Repository

```bash
git clone https://github.com/yourusername/logic-and-reasoning-app.git
cd logic-and-reasoning-app
```

### Install Dependencies

```bash
pip install kivy
```

### Building the APK

Note: The APK file is already provided in the repository. However, if you want to build it yourself, follow these steps:

1. Ensure you have Buildozer installed and configured. [This](https://buildozer.readthedocs.io/) is the official buildozer instructions to convert into APK files.
2. Run the following command to build the APK:

```bash
buildozer -v android debug
```

## Usage

1. Install the provided APK file on your Android device.

2. Navigate through the app to test the logic and reasoning questions.

3. If you want to run the application locally:

```bash
python main.py
```

## File Structure

```
logic-and-reasoning-app/
│
├── Chapter-001/
│   ├── Answers/
│   │   ├── A-001-01.png
│   │   ├── A-001-02.png
│   └── Questions/
│       ├── Q-001-01.png
│       ├── Q-001-02.png
│
├── Chapter-002/
│   ├── Answers/
│   │   ├── A-002-01.png
│   │   ├── A-002-02.png
│   └── Questions/
│       ├── Q-002-01.png
│       ├── Q-002-02.png
│
├── Chapter-003/
│   ├── Answers/
│   │   ├── A-003-01.png
│   │   ├── A-003-02.png
│   └── Questions/
│       ├── Q-003-01.png
│       ├── Q-003-02.png
│
├── Chapter-004/
│   ├── Answers/
│   │   ├── A-004-01.png
│   │   ├── A-004-02.png
│   └── Questions/
│       ├── Q-004-01.png
│       ├── Q-004-02.png
│
├── Chapter-005/
│   ├── Answers/
│   │   ├── A-005-01.png
│   │   ├── A-005-02.png
│   └── Questions/
│       ├── Q-005-01.png
│       ├── Q-005-02.png
│
├── Chapter-006/
│   ├── Answers/
│   │   ├── A-006-01.png
│   │   ├── A-006-02.png
│   └── Questions/
│       ├── Q-006-01.png
│       ├── Q-006-02.png
│
├── main.py
├── main_kv.kv
├── logic_and_reasoning_app.apk
└── README.md
```

## Screenshots

![brainstormie_home](https://github.com/user-attachments/assets/5b306dcf-6bf4-43f7-9937-335c2ba0874e)
![BS_terms2](https://github.com/user-attachments/assets/78d07033-58f5-4567-861e-d5412fa6f033)
![BS_index](https://github.com/user-attachments/assets/c178319d-d739-4c8b-a143-ec0780c9d4cd)
![BS_q](https://github.com/user-attachments/assets/e781b5b3-92f8-45e2-9b82-924e0e557697)
![BS_ans1](https://github.com/user-attachments/assets/e74a6ed1-9158-48e6-8c82-7b203a513ef6)
![bs_ans2](https://github.com/user-attachments/assets/ff66f4ed-5c13-4d10-8231-b6f664cefef8)

## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request. If you want to build the APK yourself, follow the [Building the APK](#building-the-apk) instructions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
