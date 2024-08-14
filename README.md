# Dive In

Dive In is a blog based on scuba diving, travel, and the lifestyle that comes with it. Users can view blogs, comment, share and add to the conversation.





![Logo](static/images/diveinlogolight.png)

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

# Models

## Overview

This document provides an overview of the key models used in the blog application. Each model represents a core entity within the system, and this section explains their purpose and key attributes.

## Models

### Post

The `Post` model represents a blog post. It contains the following fields:

- **title**: A `CharField` with a maximum length of 200 characters and a unique constraint to ensure that each post has a distinct title.
- **slug**: A `SlugField` used to generate URL-friendly versions of the title. Unique for each post.
- **author**: A `ForeignKey` linking to the `User` model, representing the author of the post. Uses `related_name` to reference blog posts by the user.
- **content**: A `TextField` containing the main content of the post.
- **created_on**: A `DateTimeField` that records when the post was created.
- **status**: An `IntegerField` with choices (`Draft`, `Published`) indicating the publication status of the post.
- **excerpt**: A `TextField` for a brief summary or excerpt of the post, which can be left blank.
- **updated_on**: A `DateTimeField` that updates automatically with the current time whenever the post is modified.

**Meta Information:**
- **ordering**: Orders posts by creation date in descending order.

**String Representation:**
```python
def __str__(self):
    return f"{self.title} | scribed by {self.author}"
```
## Comment Model

The `Comment` model represents user comments on blog posts and includes the following fields:

- **post** (`ForeignKey` to `Post`): The blog post that the comment is associated with.
- **author** (`ForeignKey` to `User`): The user who wrote the comment.
- **body** (`TextField`): The content of the comment.
- **approved** (`BooleanField`): Indicates whether the comment has been approved.
- **created_on** (`DateTimeField`): The date and time when the comment was created.

**Meta Information:**

- **ordering**: Orders comments by creation date in ascending order.

**String Representation:**

```python
def __str__(self):
    return f"Comment {self.body} by {self.author}"
```

## Category Model

The `Category` model helps organize blog posts into categories. It includes the following fields:

- **name** (`CharField`): The name of the category, limited to 100 characters.
- **description** (`TextField`): A description of the category.

**String Representation:**

```python
def __str__(self):
    return self.name
```

# Author Profile Picture Feature

## Overview

The Author Profile Picture feature allows displaying an author's profile image and bio on blog posts. This enhancement provides a more personalized and engaging experience for readers by showcasing the author alongside their content.

## Key Changes

### 1. Model Update
- **UserProfile Model**: Added a `profile_picture` field to the `UserProfile` model to support profile images.

  ```python
  from django.db import models
  from django.contrib.auth.models import User
  
  class UserProfile(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
      bio = models.TextField(max_length=500, blank=True)
  
      def __str__(self):
          return self.user.username```

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
