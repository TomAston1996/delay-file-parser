[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

# 📄 Train Delay File Parser

A simple application for parsing train delay data text files. Simply specify the directory you would like the parser to search through and it will read all text files for delay data.
The output of the application is one excel file with all delay data combined, grouped and sorted by timestamp. The GUI allows you to select which event types you'd like to filter by.

## 🧑‍💻 Tech Stack

![Python]
![Pandas]

## 🔧 Setup

### 📋 Dependencies
Run the command ```pip install -r requirements.txt``` to install dependencies or ```uv sync``` if using uv package manager.

### Run Locally
``` python ./DelayFileParser.py``` will run the GUI via the terminal or a .exe file is provided in the ```dist``` directory.
### Build
To build the app for distribution run ```python build.py```. The ```.exe``` file will be created in your ```dist``` directory.


## 🧑‍🤝‍🧑 Developers 

| Name           | Email                      |
| -------------- | -------------------------- |
| Tom Aston      | mailto:mail@tomaston.dev     |

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/TomAston1996/delay-file-parser.svg?style=for-the-badge
[contributors-url]: https://github.com/TomAston1996/delay-file-parser/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/TomAston1996/delay-file-parser.svg?style=for-the-badge
[forks-url]: https://github.com/TomAston1996/delay-file-parser/network/members
[stars-shield]: https://img.shields.io/github/stars/TomAston1996/delay-file-parser.svg?style=for-the-badge
[stars-url]: https://github.com/TomAston1996/delay-file-parser/stargazers
[issues-shield]: https://img.shields.io/github/issues/TomAston1996/delay-file-parser.svg?style=for-the-badge
[issues-url]: https://github.com/TomAston1996/delay-file-parser/issues
[license-shield]: https://img.shields.io/github/license/TomAston1996/delay-file-parser.svg?style=for-the-badge
[license-url]: https://github.com/TomAston1996/delay-file-parser/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/tomaston96
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Pandas]: https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white
