# Shared ORM Library


Overview

The **Shared ORM Library** is a Django package that provides reusable ORM models and database configurations. This library is intended for integration into Django projects to maintain consistent database schemas and settings.

## Project Structure

- **`shared_orm_library`**: Contains the Django project with ORM models and configurations.

## Setup and Installation

### Prerequisites

- Python 3.x
- PostgreSQL (or any other supported database)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/opengits/shared-orm-library.git
   cd shared-orm-library
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   Install the required Python packages listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Database**

   Edit `shared_orm_library/settings.py` to set up your database connection. Example configuration for PostgreSQL:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'my-account',
           'USER': 'your-username',
           'PASSWORD': 'your-password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

5. **Build and Package the Library**

   To prepare the library for use in other projects, build and package it:

   ```bash
   python setup.py sdist bdist_wheel
   ```

   The built package will be available in the `dist/` directory.

## Usage

To use this library in a Django project:

1. **Install the Shared ORM Library**

   Install the built package from the `dist/` directory:

   ```bash
   pip install dist/shared_orm_library-<version>.tar.gz
   ```

2. **Add the Library to Your Django Project**

   In your Django project's `settings.py`, add the library to the `INSTALLED_APPS`:

   ```python
   INSTALLED_APPS = [
       ...
       'sharedorm',
       ...
   ]
   ```

3. **Update and Rebuild**

   If you need to update the library or its configurations:

   - Make necessary changes.
   - Rebuild and repackage the library:

     ```bash
     python setup.py sdist bdist_wheel
     ```

   - Reinstall the updated package in your Django project:

     ```bash
     pip install --upgrade dist/shared_orm_library-<version>.tar.gz
     ```



## Contributing

1. **Fork the Repository**
2. **Create a New Branch**
3. **Make Your Changes**
4. **Submit a Pull Request**

## License

This project is licensed under the MIT License.

## Contact

For any questions or issues, please contact [Kamal Sharma](mailto:kamalsharma.git@gmail.com).
```

### Summary of Changes:

- Added **Build and Package** section under Installation for preparing the library for distribution.
- Updated **Usage** section to include instructions for installing from the built package and for updating/rebuilding the library.
- Added a note to **Update and Rebuild** if changes are made.

This approach ensures that users are aware of the need to rebuild and repackage the library when configuration changes occur.
