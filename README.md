# Dive In

Dive In is a blog based on scuba diving, travel, and the lifestyle that comes with it. Users can view blogs, comment, share and add to the conversation.

Unfortunately I ran out of time with this project to get everything I needed done, I learned a lot and it was a lot of information to get through. I look forward to finishing it in the near future!



![Logo](static/images/diveinlogo.png)

## Table of Contents

...





## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Models Overview](#models-overview)
- [Testing](#testing)
- [Project Planning](#project-planning)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
- [Credits](#credits)

## Project Overview

Dive In is a scuba diving and travel-oriented blog project that aims to provide users with a platform to explore narratives, engage in discussions, and share experiences related to scuba diving adventures. The project is designed to incorporate various features to enhance user interaction and create a vibrant community around scuba diving and travel lifestyle.

## Features

Dive In Blog Project encapsulates several key features tailored to enrich the user experience and foster community engagement:

- **User Authentication**: Implementing a secure login and registration system for users to access and interact with the blog.
- **Blog Post Management**: Utilizing database models to create, edit, and display blog posts, enabling users to share their stories.
- **Comments Functionality**: Enabling an interactive comments section for users to engage, share feedback, and build a vibrant community.

### Detailed Features

| Feature                | Description                                                                                                 |
|------------------------|-------------------------------------------------------------------------------------------------------------|
| User Authentication     | Robust user authentication system ensuring secure access and interaction within the platform.            |
| Blog Post Management    | Database models facilitate seamless creation, management, and display of captivating blog posts.          |
| Comments Functionality  | Interactive comment section allows users to participate in discussions and provide feedback.

## Installation

To set up the Dive In Blog Project, follow these steps:

1. **Clone the Repository**: Clone the project repository from GitHub to access the source code.
2. **Install Dependencies**: Use the `pip` package manager to install dependencies listed in the `requirements.txt` file.
3. **Database Configuration**: Customize database settings in `settings.py` for seamless interaction with the database.

## Models Overview

### Post Model

**Fields**:
- Title (CharField)
- Slug (SlugField)
- Author (ForeignKey to User)
- Content (TextField)
- Created On (DateTimeField)
- Status (Draft or Published)
- Excerpt (TextField)
- Updated On (DateTimeField)

### Comment Model

**Fields**:
- Post (ForeignKey to Post)
- Author (ForeignKey to User)
- Body (TextField)
- Approved (Boolean)
- Created On (DateTimeField)

### About Model

**Fields**:
- Company Name (CharField)
- Founding Date (DateField)
- Mission (TextField)
- Offerings (TextField)
- Updated On (DateTimeField)
- Content (TextField)

#### Additional Models

- Category
- Tag
- Subscriber
- FeaturedPost

## Testing

The Dive In Blog Project employs manual and/or automated procedures for assessing functionality, usability, and data management within the web application. Testing processes are documented for reference.

## Project Planning

Utilizing the MoSCoW method, project requirements were prioritized into Must-haves, Should-haves, Could-haves, and Won't-haves to deliver key functionalities efficiently within time constraints.

## Technologies Used

The technology stack includes Django, HTML, CSS, Bootstrap, Tailwind, Crispy Forms, and Allauth aimed at delivering an immersive and user-friendly blogging experience.

## Deployment

Detailed deployment procedures from GitHub to platforms like Heroku are documented to facilitate a seamless deployment process, ensuring a secure and efficient live version of the blog.

## Credits


Utilized code institutes "I think Therefore I Blog" tutorial in setting up my Django model as I learn a lot better with doing than reading. From the base of the blog walkthrough I morphed and changed the models and details to create my own Dive Blog.


Thanks to Viola my fellow coder for keeping me motivated through difficult slumps throughout a long few months and a fury of overwhelming information.



### Site Information

The Dive In Blog Project seeks to captivate a diverse audience of scuba diving and travel enthusiasts, providing a platform for them to share their experiences, connect with like-minded individuals, and immerse themselves in compelling narratives and conversations.
```bash

## Project Planning
