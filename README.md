# Dive In

Dive In is a blog based on scuba diving, travel, and the lifestyle that comes with it. Users can view blogs, comment, share and add to the conversation.

Unfortunately I ran out of time with this project and did not receive any reply to my request for an extension when applied for with detailed reasons.

![Logo](static/images/diveinlogo.png)

## Table of Contents

...


## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

Provide an overview of your project, explaining its purpose and goals. Include any relevant background information.


## Features

The key features of the Dive In Blog Project are designed to empower users and create an immersive experience. Here's a rundown of the core functionalities:

- **User Authentication and**: We've implemented a robust user authentication system to ensure secure access to the platform and enable users to create and interact with content safely.

- **Blog Post Management**: Our database models facilitate seamless creation, management, and display of compelling blog, enabling users to share their stories and experiences effortlessly.

- **Comments Functionality**: An interactive comment section allows users to engage in meaningful discussions share feedback, and cultivate a vibrant community within the platform.

## Features


| Feature | Description |
|---------|-------------|
| Feature 1 | Description of feature 1 |
| Feature 2 | Description of feature 2 |
| Feature 3 | Description of feature 3 |

## Installation

We've curated a step-by-step installation process to streamline the setup of the Dive In Blog Project. Here's how you can get started:

1. **Clone the Repository**: Begin cloning the project repository from GitHub to access the source code and files.

2. **Install Dependencies**: Utilize the `pip` package manager to install the dependencies listed in the `requirements.txt` file, ensuring a smooth and efficient setup process.

3. **Database Configuration**: Customize the database settings in `settings.py` to align with your specific environment, enabling seamless interaction with the underlying database.


## Usage

Explain how to use your Django blog project. Provide examples and code snippets if necessary. Include any configuration options or settings that need to be modified.

# Project Planning

With a major time constraint in getting the project together, by using the MoSCoW method, I could prioritize the project requirements, focus on the must-haves and should-haves to deliver key functionalities, and then consider the could-haves based on available resources and time.

## Must-haves:

* User authentication and authorization for logging in, creating posts, and comments.
* Database models for blog posts, comments, and travel-related content.
* Basic UI for displaying blog posts, travel content, and user profiles.

## Should-haves:

* Enhanced user profile management with additional information such as profile picture, bio, etc.
* HTML/CSS styling for the UI to improve the overall look and feel.
* Comment moderation functionality to manage and moderate user comments.

## Could-haves:

* Rich text editing for creating and editing blog posts.
* Integration with a third-party API for fetching travel-related information or images.
* User notification system for new comments, likes, etc.

## Won't-haves:

* Advanced features like real-time chat functionality.
* Social media integration for sharing blog posts or travel content.
* Implementing a comprehensive search functionality.

# ERD's

## Post Model:


## About Model: 

| About        |                | Blog       | 
|--------------|----------------|------------|
| id           |                | id         |
| title        |                | title      |
| content      |                | content    |
| created_at   |                | created_at |
| updated_at   |                | updated_at |
| blog_id (FK) | 1:1            |            |



# BUGS

Page not loading css styling when DEBUG is set to False. Can't figure out why.

## Project Details

### Technologies

The Dive In Blog Project leverages a range of technologies to deliver a seamless and immersive experience. Our technology stack includes Django, HTML, CSS, Bootstrap, Tailwind and additional libraries and frameworks tailored to enrich the user experience.

### Deployment

Detailed information on deploying the Dive Blog Project from GitHub to platforms like Heroku will be provided in the project documentation, ensuring a smooth and efficient deployment process for interested users.

### Credits

Acknowledging the invaluable contributions of all, contributors, and external resources forms an integral part of the project. We express our gratitude to all individuals and entities who have been instrumental in bringing Dive In to fruition.

Utilized code institutes "I think Therefore I Blog" tutorial in setting up my Django model as I learn a lot better with doing than reading. From the base of the blog walkthrough I morphed and changed the models and details to create my own Dive Blog.


Thanks to Viola my fellow coder for keeping me motivated through difficult slumps throughout a long few months and a fury of overwhelming information.



### Site Information

The Dive In Blog Project seeks to captivate a diverse audience of scuba diving and travel enthusiasts, providing a platform for them to share their experiences, connect with like-minded individuals, and immerse themselves in compelling narratives and conversations.
```bash

## Project Planning
