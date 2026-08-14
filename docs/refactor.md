 # Refactoring

## Why am I refactoring?

While working on this project, I've dealt with different kind of problems. This time my problem is the code that I've written. When trying to establish connection between backend and frontend, I've noticed that the more I do the less readable it becomes. The structure that I use doesn't look right. Because of my poor decisions in the past(due to the lack of knowledge), I wrote code that I can't conveniently work with.

## What is going to be refactored?

### pyproject.toml instead of requirements.txt

I am going to make this change because pyproject.toml provides more information than the default requirements.txt. It is more common nowadays to see pyproject.toml instead of requirements.txt.

### Implementing SQLModel

This solution will affect my models and schemas. I will be using SQLModel for both building a schema and models for my data base. SQLModel provides more readability and consistency. Using separately pydantic for schemas and declarative base for models - requires more effort and increases complexity.

### Core changes

* config.py - Will be refactored to add more clarity. 
* db.py - Removing declarative base.
* security.py - Improving password hashing by using both Argon2 and Bcrypt.

### Special thanks
Thanks to the official full-stack fastapi template for providing new information to learn and to implement in my project. It would've been impossible without their template and excellent code writing. I am going to continue learning their code to improve my skills and make this project as real-looking as possible. Link: https://github.com/fastapi/full-stack-fastapi-template

### Misc
Creating new branch "refactoring".
