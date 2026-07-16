
# Post-Vote

A full-stack social network built with FastAPI, PostgreSQL and React. The project focuses on production-oriented backend architecture, authentication, friendships, posts, image uploads, Docker and cloud deployment.

## Features

- JWT authentication
- Cookie-based authentication
- User profiles
- Friend requests
- Friendships
- Posts
- Image uploads
- Likes
- Comments
- Docker
- Testing

## Tech Stack

### Backend

- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL
- Pydantic
- argon2
- python-jose

### Frontend

- React
- TypeScript
- Vite

### Tools

- Docker
- pytest

## Project Structure
```shell
┗━━📁Post-Vote/
    ┣━━ 📁 backend/
    ┃   ┣━━ 📁 alembic/ # Generated via alembic init
    ┃   ┃   ┣━━ 📁 versions/ # Alembic DB version control
    ┃   ┃   ┣━━ 🐍 env.py # Alembic automigration
    ┃   ┃   ┗━━ 📄 script.py.mako # Generated via alembic
    ┃   ┣━━ 📁 app/
    ┃   ┃   ┣━━ 📁 api/ # CRUD operations
    ┃   ┃   ┃   ┣━━ 🐍 comment.py
    ┃   ┃   ┃   ┣━━ 🐍 authentication.py
    ┃   ┃   ┃   ┣━━ 🐍 friendship.py
    ┃   ┃   ┃   ┣━━ 🐍 post.py
    ┃   ┃   ┃   ┗━━ 🐍 user.py
    ┃   ┃   ┣━━ 📁 core/ # Core operations
    ┃   ┃   ┃   ┣━━ 📁 security/ # Security operation
    ┃   ┃   ┃   ┃   ┣━━ 🐍 authorization.py # JWT creation and verification
    ┃   ┃   ┃   ┃   ┣━━ 🐍 cookies.py # Set JWT token data into cookies
    ┃   ┃   ┃   ┃   ┗━━ 🐍 hash.py # Password hashing with argon2
    ┃   ┃   ┃   ┣━━ 🐍 config.py # Creating Settings to initialize with .env file data 
    ┃   ┃   ┃   ┗━━ 🐍 dependencies.py # Dependencies for FastAPI's "Depends" 
    ┃   ┃   ┣━━ 📁 db/ # Database connection
    ┃   ┃   ┃   ┣━━ 🐍 base.py # The DeclarativeBase initialization
    ┃   ┃   ┃   ┣━━ 🐍 database.py # Database connection with SQLAlchemy
    ┃   ┃   ┃   ┗━━ 🐍 session.py # Session maker  
    ┃   ┃   ┣━━ 📁 models/ # SQLAlchemy models 
    ┃   ┃   ┃   ┣━━ 🐍 comment.py
    ┃   ┃   ┃   ┣━━ 🐍 friendship.py
    ┃   ┃   ┃   ┣━━ 🐍 post.py
    ┃   ┃   ┃   ┗━━ 🐍 user.py
    ┃   ┃   ┣━━ 📁 repository/ # Database queries
    ┃   ┃   ┃   ┣━━ 🐍 comment.py
    ┃   ┃   ┃   ┣━━ 🐍 friendship.py
    ┃   ┃   ┃   ┣━━ 🐍 post.py
    ┃   ┃   ┃   ┗━━ 🐍 user.py
    ┃   ┃   ┣━━ 📁 schemas/ # Pydantic BaseModels
    ┃   ┃   ┃   ┣━━ 🐍 comment.py
    ┃   ┃   ┃   ┣━━ 🐍 friendship.py
    ┃   ┃   ┃   ┣━━ 🐍 post.py
    ┃   ┃   ┃   ┣━━ 🐍 token.py
    ┃   ┃   ┃   ┗━━ 🐍 user.py
    ┃   ┃   ┣━━ 📁 services/ # Services for API's CRUD opearions
    ┃   ┃   ┃   ┣━━ 🐍 authentication.py
    ┃   ┃   ┃   ┣━━ 🐍 comment.py
    ┃   ┃   ┃   ┣━━ 🐍 user.py
    ┃   ┃   ┃   ┣━━ 🐍 post.py
    ┃   ┃   ┃   ┗━━ 🐍 friendship.py
    ┃   ┃   ┣━━ 📁 utils/
    ┃   ┃   ┃   ┗━━ 📁 exceptions/
    ┃   ┃   ┃       ┗━━ 📁 http/
    ┃   ┃   ┃           ┣━━ 🐍 exc_401.py # Exceptions with status 401
    ┃   ┃   ┃           ┣━━ 🐍 exc_403.py # Exceptions with status 403
    ┃   ┃   ┃           ┣━━ 🐍 exc_404.py # Exceptions with status 404
    ┃   ┃   ┃           ┗━━ 🐍 exc_409.py # Exceptions with status 409
    ┃   ┃   ┗━━ 📁 messages/
    ┃   ┃       ┗━━ 🐍 exc_details.py # Exception messages
    ┃   ┣━━ 📁 tests/ # Application testing with pytest
    ┃   ┃   ┣━━ 🐍 conftest.py
    ┃   ┃   ┣━━ 🐍 test_auth.py
    ┃   ┃   ┗━━ 🐍 test_user.py
    ┃   ┣━━ 📄 .env.example # Example of .env file
    ┃   ┣━━ 📄 .gitignore # A file that list files to be excluded when commiting into git
    ┃   ┣━━ 📄 alembic.ini  # Automatic database migration configuration
    ┃   ┗━━ 📄 requirements.txt # Packages installed for backend app
    ┣━━ 📁frontend # IN DEVELOPMENT
    ┣━━ 📄 LICENSE # License for this project
    ┣━━ 📄 pyproject.toml # Linter and test main configuration file
    ┗━━ 📝 README.md # The main documentation file for this template repository
```
## Installation
```shell
git clone https://github.com/futsu37/post-vote.git

cd backend

python -m venv venv

pip install -r requirements.txt
```

## Environment variables
All environment variables are included in .env.example file. Simply change .env.example to .env

## API
### user.py
```shell
POST "/users" # Create new user
POST "/users/current" # Get logined user
```
### authentication.py
```shell
POST "/login" # log user into session
```
### friendship.py
```shell
GET "/friendships/friends" # Get friends
POST "/friendships/send{receiver_id}" # Send friend request to user
DELETE "/friendships/remove{friend_id}" # remove a friend
```
### post.py
```shell
GET "/posts/all" # Get friends of the logined user
POST "/posts" # Create post
PUT "/posts/{post_id}" # Edit post
DELETE "/posts/{post_id}" # Delete post
```
### comment.py
```shell
GET "/comments/all/{post_id}" # Get all comments from a post
GET "/comments/{comment_id}" # Get comment
POST "/comments" # Create comment
PATCH "/comments/{comment_id}" # Edit comment
DELETE "/comments/{comment_id}" # Delete comment
```
---
More & detailed requests are autogenerated by fast api in "/docs"

## Future improvements
- Imagine uploading system
- Docker
- CI/CD
- AWS
- Code refactoring
- Add frontend

## Progress
- [x] Authentication
- [x] Authorization
- [x] Friend requests
- [x] Posts
- [x] Comments
- [ ] Likes
- [ ] User profile
- [ ] Docker
- [ ] Frontend part
- [ ] Image uploads
- [ ] AWS deployment

## The purpose of the project
Learn how to create readable and scalable backend applications, enhance and polish my current skills. Connect with a developer communnity. Show my dedication and learning abilities.

## Contributions
If you want to help me with this learning journey, I will appreciate your recommendations and/or critique. For the more direct connections, I have all the info pinned on my github profile. Thanks to everyone who decided to help me!

## Current me
I have little to no knowledge on how to write scalable backend applications, never worked in a team with other people, have faith in kind developers that can navigate me on my journey, so I can follow the right path.  I believe that connecting with people is the main way to achieve all of that.