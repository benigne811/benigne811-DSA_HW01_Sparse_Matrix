class SparseMatrix:
    def __init__(self, matrixFilePath=None, numRows=0, numCols=0):
        self.rows = numRows
        self.cols = numCols
        # Store non-zero elements as list of (row, col, value) tuples
        self.elements = []
        
        if matrixFilePath:
            self._load_from_file(matrixFilePath)

    def _load_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = [line.strip() for line in file if line.strip()]  # Ignore empty lines
                
                if len(lines) < 2:
                    raise ValueError("Input file has wrong format")
                
                # Parse rows
                if not lines[0].startswith("rows="):
                    raise ValueError("Input file has wrong format")
                try:
                    self.rows = int(lines[0].split("=")[1])
                except (IndexError, ValueError):
                    raise ValueError("Input file has wrong format")
                
                # Parse columns
                if not lines[1].startswith("cols="):
                    raise ValueError("Input file has wrong format")
                try:
                    self.cols = int(lines[1].split("=")[1])
                except (IndexError, ValueError):
                    raise ValueError("Input file has wrong format")
                
                # Parse matrix entries
                for line in lines[2:]:
                    # Check for correct format: (row, col, value)
                    if not (line.startswith("(") and line.endswith(")")):
                        raise ValueError("Input file has wrong format")
                    
                    # Remove parentheses and split
                    try:
                        entry = line[1:-1].split(",")
                        if len(entry) != 3:
                            raise ValueError("Input file has wrong format")
                        
                        row = int(entry[0].strip())
                        col = int(entry[1].strip())
                        value = int(entry[2].strip())  # Only integers allowed
                        
                        if row >= self.rows or col >= self.cols or row < 0 or col < 0:
                            raise ValueError("Input file has wrong format")
                            
                        self.elements.append((row, col, value))
                    except ValueError:
                        raise ValueError("Input file has wrong format")
                        
        except FileNotFoundError:
            raise FileNotFoundError(f"File {file_path} not found")

    def getElement(self, currRow, currCol):
        for row, col, value in self.elements:
            if row == currRow and col == currCol:
                return value
        return 0  # Default value for sparse matrix

    def setElement(self, currRow, currCol, value):
        if currRow >= self.rows or currCol >= self.cols or currRow < 0 or currCol < 0:
            raise ValueError("Invalid row or column index")
            
        # Remove existing element if present
        self.elements = [(r, c, v) for r, c, v in self.elements if not (r == currRow and c == currCol)]
        
        if value != 0:  # Only store non-zero elements
            self.elements.append((currRow, currCol, value))

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for addition")
            
        result = SparseMatrix(numRows=self.rows, numCols=self.cols)
        
        # Add all elements from self
        for row, col, value in self.elements:
            result.setElement(row, col, value)
            
        # Add elements from other matrix
        for row, col, value in other.elements:
            new_value = result.getElement(row, col) + value
            result.setElement(row, col, new_value)
            
        return result

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for subtraction")
            
        result = SparseMatrix(numRows=self.rows, numCols=self.cols)
        
        # Add all elements from self
        for row, col, value in self.elements:
            result.setElement(row, col, value)
            
        # Subtract elements from other matrix
        for row, col, value in other.elements:
            new_value = result.getElement(row, col) - value
            result.setElement(row, col, new_value)
            
        return result

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns in first matrix must equal number of rows in second matrix")
            
        result = SparseMatrix(numRows=self.rows, numCols=other.cols)
        
        # For each non-zero element in self
        for row1, col1, val1 in self.elements:
            # For each non-zero element in other
            for row2, col2, val2 in other.elements:
                if col1 == row2:
                    # Multiply and add to result
                    curr_val = result.getElement(row1, col2)
                    result.setElement(row1, col2, curr_val + val1 * val2)
                    
        return result

    def save_to_file(self, file_path):
        with open(file_path, 'w') as file:
            file.write(f"rows={self.rows}\n")
            file.write(f"cols={self.cols}\n")
            for row, col, value in sorted(self.elements):  # Sort for consistent output
                file.write(f"({row}, {col}, {value})\n")

def main():
    while True:
        print("\nSparse Matrix Operations")
        print("1. Add matrices")
        print("2. Subtract matrices")
        print("3. Multiply matrices")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '4':
            break
            
        if choice not in ['1', '2', '3']:
            print("Invalid choice. Please try again.")
            continue
            
        file1 = input("Enter first matrix file path: ")
        file2 = input("Enter second matrix file path: ")
        output_file = input("Enter output file path: ")
        
        try:
            matrix1 = SparseMatrix(file1)
            matrix2 = SparseMatrix(file2)
            
            if choice == '1':
                result = matrix1.add(matrix2)
            elif choice == '2':
                result = matrix1.subtract(matrix2)
            else:  # choice == '3'
                result = matrix1.multiply(matrix2)
                
            result.save_to_file(output_file)
            print(f"Result saved to {output_file}")
            
        except (ValueError, FileNotFoundError) as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()