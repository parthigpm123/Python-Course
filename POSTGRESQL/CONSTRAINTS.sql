what is constraints in sql?

1.primery key

2.foreign key
3.unique key
4.not null
5.check
6.default


⚡ In short:

PRIMARY KEY → unique + not null (table identity)

FOREIGN KEY → links tables

UNIQUE → no duplicates allowed

NOT NULL → must always have a value

CHECK → apply conditions

NULL → allows missing values

DEFAULT - DEFAULT "Unassigned"-> if no value is provided, "Unassigned" will be used manually
⚡ Example:
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY AUTO INCREMENT,          -- Primery Key
    FirstName VARCHAR(50) NOT NULL,      -- Not Null
    LastName VARCHAR(50) NOT NULL,       -- Not Null
    Email VARCHAR(100) UNIQUE,           -- Unique Key
    DepartmentID INT,
    Salary DECIMAL(10, 2) CHECK (Salary > 0), -- Check Constraint
    HireDate DATE DEFAULT CURRENT_DATE,  -- Default Value
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID) -- Foreign Key
