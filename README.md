# Difference Calculator (gendiff)

### Hexlet tests and linter status:
[![Actions Status](https://github.com/GrScode404/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/GrScode404/python-project-50/actions)
### SonarQube:
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=GrScode404_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=GrScode404_python-project-50)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=GrScode404_python-project-50&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=GrScode404_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=GrScode404_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=GrScode404_python-project-50)

### 🔍Description
___
Gendiff — a command-line tool that compares two configuration files and shows the difference.
It supports JSON and YAML formats and provides several output styles:

🪶 stylish — hierarchical diff (default)

✏️ plain — human-readable text format

⚙️ json — structured machine-readable format

### 🛠 Installation
___
1. Clone the repository and install dependencies:
```bash
git clone https://github.com/GrScode404/python-project-50.git
```
2. Navigate to the project directory:
```bash
cd python-project-50
```
3. Install the dependencies
```bash
make install
```
### Supported file types
___
- .json
- .yml
- .yaml

### Usage
___
Compare two configuration files:
```bash
gendiff <path_to_file1> <path_to_file2>
```
### Examples
Stylish (default):
```bash
gendiff tests/test_data/file1.json tests/test_data/file2.json
```
Plain format:
```bash
gendiff --format plain tests/test_data/file1.json tests/test_data/file2.json
```
JSON format:
```bash
gendiff --format json tests/test_data/file1.yml tests/test_data/file2.yml
```






