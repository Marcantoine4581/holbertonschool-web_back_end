# ES6_Basics

## Learning Objectives

- What ES6 is
- New features introduced in ES6
- The difference between a constant and a variable
- Block-scoped variables
- Arrow functions and function parameters default to them
- Rest and spread function parameters
- String templating in ES6
- Object creation and their properties in ES6
- Iterators and for-of loops

## Requirements

- All your files will be executed on Ubuntu 18.04 LTS using NodeJS 12.11.x
- Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `js` extension
- Your code will be tested using the [Jest Testing Framework](https://jestjs.io/ "Jest Testing Framework")
- Your code will be analyzed using the linter [ESLint](https://eslint.org/ "ESLint") along with specific rules that we’ll provide
- All of your functions must be exported

## Setup

### Install NodeJS 12.11.x

(in your home directory):

```
curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
```

```
$ nodejs -v
v12.11.1
$ npm -v
6.11.3
```

### Install Jest, Babel, and ESLint

in your project directory:

- Install Jest using: `npm install --save-dev jest`
- Install Babel using: `npm install --save-dev babel-jest @babel/core @babel/preset-env`
- Install ESLint using: `npm install --save-dev eslint`

## Configuration files

### `package.json`

### `babel.config.js`

### `.eslintrc.js`


### Finally…

Don’t forget to run `npm install` from the terminal of your project folder to install all necessary project dependencies.

## Files

| Tasks                                                       | Files                                       |
| ----------------------------------------------------------- | ------------------------------------------- |
| Const or let?                                               | **0-main.js, 0-constants.js**               |
| Block Scope                                                 | **1-main.js, 1-block-scoped.js**            |
| Arrow functions                                             | **2-main.js, 2-arrow.js**                   |
| Parameter defaults                                          | **3-main.js, 3-default-parameter.js**       |
| Rest parameter syntax for functions                         | **4-main.js, 4-rest-parameter.js**          |
| The wonders of spread syntax                                | **5-main.js, 5-spread-operator.js**         |
| Take advantage of template literals                         | **6-main.js, 6-string-interpolation.js**    |
| Object property value shorthand syntax                      | **7-main.js, 7-getBudgetObject.js**         |
| No need to create empty objects before adding in properties | **8-main.js, 8-getBudgetCurrentYear.js**    |
| ES6 method properties                                       | **9-main.js, 9-getFullBudget.js**           |
| For...of Loops                                              | **10-main.js, 10-loops.js**                 |
| Iterator                                                    | **11-main.js, 11-createEmployeesObject.js** |
| Let's create a report object                                | **12-main.js, 12-createReportObject.js**    |

## Authors
Marc-Antoine VANNIER