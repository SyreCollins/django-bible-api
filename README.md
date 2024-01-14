# django-bible-api
A King James Version Translated Bible API built using Django's rest framework.
# Bible API Project

## Table of Contents
1. Introduction
2. Installation
3. Usage
4. Contributing
5. License

## Introduction
Welcome to the Bible API project. This project is a RESTful API built with Django and Django REST Framework. It provides access to the text of each book, chapter, and verse in the Bible.

## Installation
Before you start, make sure you have Python and pip installed on your system. If not, you can download Python here and pip will be installed with it.

1. **Clone the repository**: Clone this repository to your local machine using `git clone https://github.com/SyreCollins/django-bible-api.git`.

2. **Install Django and Django REST Framework**: Navigate to the project directory and install Django and Django REST Framework using pip:
    ```bash
    pip install django djangorestframework
    ```

3. **Run the server**: Start the Django server:
    ```bash
    python manage.py runserver
    ```

Now, your server should be running at `http://localhost:8000`.

## Usage
You can access the text of a specific book, chapter, or verse in the Bible by making a GET request to the following endpoints:

- **Book**: `http://localhost:8000/api/book_name/`
- **Chapter**: `http://localhost:8000/api/book_name/chapter_number/`
- **Verse**: `http://localhost:8000/api/book_name/chapter_number/verse_number/`

Replace `book_name`, `chapter_number`, and `verse_number` with the actual name of the book, number of the chapter, and number of the verse you want to access.

## Contributing
Contributions are welcome!

## License
This project is licensed under the terms of the MIT license. See the LICENSE file for details.
