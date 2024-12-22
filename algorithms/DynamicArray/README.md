# Dynamic Array in Python

This project implements a `DynamicArray` class in Python, which mimics the behavior of dynamic arrays (such as `ArrayList` in Java or `std::vector` in C++). The implementation includes various methods for adding, removing, sorting, and accessing elements, along with some basic sorting algorithms like insertion sort, selection sort, and bubble sort.

## Features

- **Dynamic resizing**: Automatically resizes when the array's capacity is exceeded.
- **Basic operations**: Add, remove, set, and get elements by index.
- **Sorting algorithms**: Includes Insertion Sort, Selection Sort, and Bubble Sort.
- **Iteration**: Supports iteration with Python's `for` loop.
- **Contains and index**: Check if an object exists in the array and retrieve its index.

## Prerequisites

Before running the code or tests, ensure you have Python 3.x installed on your machine.

## Project Structure

```
├── DynamicArray.py       # Main DynamicArray class implementation
├── DynamicArrayUnittest.py  # Unit tests for DynamicArray class
├── README.md              # Project overview and instructions
```

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/naveenairani/PythonDSA.git
   cd PythonDSA
   ```

## Running the Main Code

The `DynamicArray.py` file contains the main implementation of the `DynamicArray` class. You can modify it or import it into your own projects.

## Unit Testing

This project includes unit tests to ensure that the `DynamicArray` class functions as expected. The tests are located in the `DynamicArrayUnittest.py` file and are built using Python's `unittest` module.

### Running the Unit Tests

1. Navigate to the project directory.
2. Run the tests using the following command:
   ```bash
   python -m unittest DynamicArrayUnittest.py
   ```

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is open source and available under the [BSD 3-Clause](LICENSE).

## Contact

If you have any questions or suggestions, please open an issue in the GitHub repository.