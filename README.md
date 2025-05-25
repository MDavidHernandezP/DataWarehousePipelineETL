[![Python](https://img.shields.io/badge/python-3.12.1-red.svg)](https://www.python.org/)

# Data Warehouse creation ETL Pipeline

This project aims to create an entire functional ETL Pipeline for building an entire system of a Data Warehouse to use it for Data Analysis purposes. In this case, beginning from constructing the workflow by desinging the Pipeline orchestrated with Airflow and Data Modeling the structure of the Database (By now using just MSSQLServer but it can be expanded to other DBMS).

By now there's not much about the new and fixed project, but the files of the original one are in the folder: Original Project Files, there are some others folders to contain the scripts of the querys for the database in the future and the diagram of the new expected Database.

### First steps of Project

### ETL Data Architecting

### Data Modeling

### 

# Index
- [Content Overview](#content-overview)
- [Installation](#installation)
- [Usage](#usage)
- [placeholder](#placeholder)
- [Contributions](#contributions)
- [Credits](#credits)
- [License](#license)

## Content Overview

### 1. `dags/`

placeholder.

### 2. `documentation/`

placeholder.

#### 2.1 `Original Project Files/`

placeholder.

#### 2.2 `SuperMarket's DB ER diagram.pdf`

placeholder.

### 3. `scripts/`

placeholder.

#### 3.1 `db/`

Python scripts with the clients of each Database engine, mssqlserver, mysql, oracle, postgresql and sqlite.

#### 3.2 `dataGenerator.py`

placeholder.

#### 3.3 `dataIngestor.py`

placeholder.

#### 3.4 `dataWarehouse.py`

placeholder.

#### 3.5 `schemaGenerator.py`

placeholder.

#### 3.6 `scriptExecutor.py`

placeholder.

#### 3.7 `tableExtractor.py`

placeholder.

### 4. `sql/`

placeholder.

#### 4.1 `DDL/`

placeholder.

#### 4.2 `DML/`

placeholder.

#### 4.3 `DQL/`

placeholder.

### 5. `sqlite_db/`

placeholder.

### 6. `config.py`

placeholder.

### 7. `docker-compose.yml`

placeholder.

### 8. `Dockerfile`

placeholder.

### 9. `requirements.txt`

placeholder.

## Installation

1. Clone the repository:

    ```bash
    git clone -b master git@github.com:MDavidHernandezP/DataWarehousePipelineETL.git
    cd "the project directory"
    ```
    
    OR:

    ```bash
    git clone https://github.com/MDavidHernandezP/DataWarehousePipelineETL.git
    cd "the project directory"
    ```

2. Build and run the Docker containers:

    ```bash
    docker-compose up --build
    ```

## Usage

Placeholder:

## Contributions

Any contribution is accepted for this project we align with the MIT License for open source. If you are interested in contributing directly with us or just copy our code for an own project, you're completly free to do it. You can contact us by this email in case of doubts or contributions: `mdavidhernandezp@gmail.com`.

- **Steps for contributing:**
1. Fork the project.
2. Create a branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -am 'adding new feature'`).
4. Push the branch (`git push origin feature/new-feature`).
5. Open a pull request.

## Credits

This project was originally created by a group team of Data Engineering Students for the subject Data Preprocessing.

1. MARIO DAVID HERNÁNDEZ PANTOJA
2. LUIS ARTURO MICHEL PEREZ
3. GERARDO HERNÁNDEZ WIDMAN
4. OSCAR MARTINEZ ESTEVEZ
5. MOISES JESUS CARRILLO ALONZO

Then it was reinvented for its improvement and is being maintained by:

1. MARIO DAVID HERNÁNDEZ PANTOJA

## License

This project is licensed under the MIT License

MIT License

Copyright (c) 2024 Mario David Hernández Pantoja

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---