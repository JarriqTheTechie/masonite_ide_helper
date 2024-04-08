# Masonite IDE Helper

Masonite IDE Helper is a utility for generating Python type hinting stub files (.pyi) for Masonite ORM models. It automates the process of extracting relevant information such as class names, properties, and methods with their return types from model files.

## Installation

You can install the Masonite IDE Helper via pip:

```bash
pip install masonite-ide-helper
```

## Usage

To use the Masonite IDE Helper, follow these steps:

1. Import the library:

    ```python
    from masonite_ide_helper import IdeHelper
    ```

2. Instantiate the `IdeHelper` class:

    ```python
    ide_helper = IdeHelper(models_dir="path/to/models")
    ```

    If the `models_dir` parameter is not provided, it defaults to the "application/models" directory.

3. Call the `make_pyi_files` method:

    ```python
    ide_helper.make_pyi_files()
    ```

    This will generate .pyi files for the models located in the specified directory.

## Example

```python
from masonite_ide_helper import IdeHelper

# Instantiate IdeHelper with optional models directory parameter
ide_helper = IdeHelper(models_dir="path/to/models")

# Generate .pyi files for the models
ide_helper.make_pyi_files()
```

## Documentation

### `IdeHelper` class

#### `__init__(self, models_dir: str | None = None)`

Initializes an instance of IdeHelper.

- `models_dir` (str | None): The directory path containing the model files. If not provided, defaults to the "application/models" directory.

#### `make_pyi_files(self)`

Generates Python type hinting stub files (.pyi) for the models located in the specified directory.

#### `get_models(self)`

Retrieves the list of model files from the specified directory and extracts relevant information such as class name, module path, properties, and methods with their return types.

## Notes

- This library assumes a standard Masonite project structure where models reside in the "application/models" directory. If your project structure differs, you may need to adjust the `models_dir` parameter accordingly.
- If any error occurs during the generation of stubs for a model, the error message will be printed, and the process will continue for other models.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contribution

Contributions are welcome! If you find any issues or want to improve the library, feel free to open a pull request or create an issue in the repository.