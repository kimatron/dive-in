# Dive In

Dive In is a dynamic blog platform dedicated to scuba diving, travel, and the lifestyle that accompanies these adventures. The site provides a vibrant community where users can read engaging blog posts, share their own experiences, participate in discussions, and connect with other diving enthusiasts.

![Logo](static/images/divinlogolight.png)

## Live Site

Explore the live site here: [Dive In Blog](https://dive-inn-c4449bc967b4.herokuapp.com/)

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

Dive In is a comprehensive blog platform aimed at scuba diving and travel enthusiasts. It allows users to:

- **Discover**: Read and explore a variety of blog posts related to scuba diving and travel.
- **Engage**: Comment on posts, share insights, and interact with a community of like-minded individuals.
- **Contribute**: Create and manage blog posts, providing a space for users to share their diving experiences and travel stories.

This project integrates a user-friendly interface with powerful backend functionalities, making it a robust platform for sharing and discovering diving and travel content.

## Detailed Planning Steps

### 1. Define Blog Objectives
- **Mission and Vision**: Establish the overarching goals and purpose of the Dive In blog. This includes defining the blog’s unique value proposition and target audience.
- **Key Goals**:
  - **User Engagement**: Develop strategies to increase interaction, such as comments, shares, and user contributions.
  - **Content Sharing**: Implement features that encourage users to share content on social media and other platforms.
  - **Community Building**: Create features that foster a sense of community among users, such as forums or discussion boards.

### 2. Gather User Requirements
- **Collect Requirements**: Engage with potential users to understand their needs and expectations for the blog. This can be done through surveys, interviews, or focus groups.
- **Essential Features**:
  - **User Authentication**: Secure login and registration system.
  - **Blog Post Management**: Tools for creating, editing, and managing blog posts.
  - **Comments Functionality**: Interactive commenting system for user feedback and discussion.

### 3. Design Layout & UI
- **Layout Development**: Create the layout for various pages, including:
  - **Home Page**: Overview of recent posts and featured content.
  - **Post Details Page**: Detailed view of individual blog posts.
  - **User Profiles**: Pages displaying user information and their posts.
- **UI Design**: Utilize frameworks like [Bootstrap](https://getbootstrap.com/) and [Tailwind CSS](https://tailwindcss.com/) to ensure a modern, responsive design.

### 4. Create Data Models
- **Django Models**: Develop the necessary models in Django to represent:
  - **Post**: Blog posts with fields like title, content, and author.
  - **Comment**: User comments on posts with fields for content and approval status.
  - **Category**: Categories to organize posts.
  - **UserProfile**: Extended user profiles including profile pictures and bios.
- **Data Relationships**: Define how these models relate to each other, such as foreign keys linking comments to posts and posts to categories.

### 5. Feature Planning
- **Prioritization**: Use the MoSCoW method (Must-have, Should-have, Could-have, Won’t-have) to prioritize features based on importance and feasibility.
- **Features to Include**:
  - **User Authentication**: Secure login and registration.
  - **Post Creation**: Interface for users to create and manage their posts.
  - **Commenting**: Functionality for users to leave comments on posts.

### 6. Develop Wireframes
- **Wireframes**: Design wireframes for key pages to visualize layout and functionality. Tools like [CodePen](https://codepen.io/) and [Universe](https://universe.com/) can be used for creating and sharing wireframes.
- **Stakeholder Validation**: Present wireframes to stakeholders for feedback and adjust designs as needed.

### 7. User Feedback & Revisions
- **Gather Feedback**: Collect feedback on wireframes and initial designs from potential users and stakeholders.
- **Revisions**: Make necessary changes based on feedback to ensure the final design meets user needs and expectations.

### 8. Implement Features
- **Development**: Begin coding and integrating prioritized features into the application.
- **Integration**: Ensure seamless integration with Django models and user interface elements.

### 9. Testing Phase
- **Testing**: Conduct comprehensive testing, including:
  - **Functionality**: Verify that all features work as intended.
  - **Usability**: Ensure the application is user-friendly and intuitive.
  - **Security**: Test for vulnerabilities and ensure data protection.
- **Documentation**: Document testing procedures and results. Make necessary improvements based on test outcomes.

### 10. Deployment
- **Deployment**: Deploy the blog to a live environment, such as [Heroku](https://www.heroku.com/).
- **Configuration**: Ensure all settings and configurations are correctly set for a smooth and successful launch.

![Flowchart](static/images/documentation/diveinflowchart.png)

## Future Features

Several enhancements are planned for future versions of the Dive In blog to further improve user experience and functionality:

- **User Profiles**: Allow users to create and customize their profiles, including adding profile pictures, bios, and other personal information directly from the UI.
- **Saving Favourites**: Enable users to save their favorite blog posts and easily access them later.
- **Featured Posts**: Highlight popular or recommended blog posts on the home page or in a dedicated section.
- **Related Posts**: Display related blog posts on individual post pages to encourage further reading.
- **Images in Blogs**: Incorporate images within blog posts to enhance visual appeal and content engagement.

## Features Not Implemented

Due to time constraints, the following features were not implemented in the initial release but are planned for future updates:

- **User Profiles**: Full implementation of user profiles with customizable options.
- **Saving Favourites**: Functionality for users to bookmark and save their favorite posts.
- **Personal Bios and Info**: Ability for users to add and edit their bios and information from the front end.
- **Featured and Related Posts**: Systems for showcasing featured posts and displaying related content within blog posts.
- **Images in Blog Posts**: Support for embedding and displaying images within blog content.

## Features

Dive In offers a range of features designed to enhance user experience and foster community interaction:

- **User Authentication**: A secure system for user registration and login. Users can register, log in, and manage their profiles with ease.
- **Blog Post Management**: Users can create, edit, and publish blog posts. Posts can include rich text, images, and other media.
- **Comments Functionality**: An interactive comment section where users can engage in discussions, provide feedback, and connect with other readers.
- **Author Profiles**: Each post features an author's profile picture and bio, adding a personal touch to the content and allowing readers to learn more about the writers.

### Detailed Features

| Feature                | Description                                                                                                 |
|------------------------|-------------------------------------------------------------------------------------------------------------|
| User Authentication    | Secure login and registration system with optional social authentication through Django Allauth.          |
| Blog Post Management   | Comprehensive management system for creating, editing, and displaying blog posts with rich text and media support. |
| Comments Functionality | Interactive comment section supporting threaded discussions and moderation for community engagement.       |
| Author Profiles        | Displays profile pictures and bios of authors, enhancing personalization and connection with readers.       |

## Installation

To set up Dive In locally, follow these steps:

1. **Clone the Repository**: Clone the project repository from GitHub:
    ```bash
    git clone https://github.com/kimatron/dive-in.git
    ```
2. **Install Dependencies**: Install the required dependencies using `pip`:
    ```bash
    pip install -r requirements.txt
    ```
3. **Database Configuration**: Configure your database settings in `settings.py`. For example, set up PostgreSQL or SQLite depending on your preference:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'dive_in_db',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```
4. **Run Migrations**: Apply database migrations to set up your database schema:
    ```bash
    python manage.py migrate
    ```
5. **Create a Superuser**: Create a superuser to access the Django admin interface:
    ```bash
    python manage.py createsuperuser
    ```
6. **Run the Server**: Start the Django development server:
    ```bash
    python manage.py runserver
    ```

## Models Overview

Dive In utilizes several key models to structure and manage the content on the site.

### Post Model

The `Post` model represents a blog post with the following fields:

- **title**: `CharField` with a maximum length of 200 characters, unique for each post.
- **slug**: `SlugField` for creating URL-friendly versions of the title.
- **author**: `ForeignKey` linking to the `User` model, representing the post's author.
- **content**: `TextField` for the main content of the post.
- **created_on**: `DateTimeField` that records the creation time of the post.
- **status**: `IntegerField` with choices (`Draft`, `Published`) indicating the post's publication status.
- **excerpt**: `TextField` for a summary of the post.
- **updated_on**: `DateTimeField` that updates automatically when the post is modified.

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


![Logo](static/images/documentation/authorbio.png)
### Testing

Testing for the Dive In Blog Project ensures that the application functions correctly and meets user expectations. Testing is conducted through both manual and automated procedures:

- **Unit Tests**: Automated tests to validate individual components and functions of the application.
- **Integration Tests**: Tests to verify that different components of the application work together as expected.
- **User Acceptance Testing (UAT)**: Manual testing to ensure that the application meets the needs of its users and is easy to navigate.
- **Cross-Browser Testing**: Ensuring the site functions correctly across different web browsers.
- **Responsive Design Testing**: Verifying that the application is usable on various devices and screen sizes.

Detailed testing procedures and results are documented in [TESTING.md](TESTING.md).

## Project Planning

The planning of the Dive In Blog Project followed the MoSCoW method to prioritize features and deliverables:

- **Must-haves**: Essential features such as user authentication, blog post management, and commenting functionality.
- **Should-haves**: Important features including author profiles and enhanced UI elements.
- **Could-haves**: Additional enhancements like advanced search and filtering options.
- **Won't-haves**: Features not included in the initial release, such as multi-language support.

This structured approach ensured that critical functionalities were developed first while providing flexibility for future enhancements.


## WireFrames

![Index Page](static/images/documentation/wireframeindex.png)

![Post Detail](static/images/documentation/wireframepost.png)

![Profile](static/images/documentation/wireframeprofile.png)

![About Page](static/images/documentation/wireframeabout.png)

## Technologies Used

Dive In is built with a modern technology stack to ensure a robust and user-friendly experience:

- **[Django](https://www.djangoproject.com/)**: A high-level Python web framework for building the backend.
- **[HTML](https://html.spec.whatwg.org/) / [CSS](https://www.w3.org/Style/CSS/)**: For structuring and styling web pages.
- **[Bootstrap](https://getbootstrap.com/)** & **[Tailwind CSS](https://tailwindcss.com/)**: Frontend frameworks for responsive design and modern UI elements.
- **[Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)**: Enhances Django forms for improved rendering and user experience.
- **[Django Allauth](https://django-allauth.readthedocs.io/en/latest/)**: Provides comprehensive authentication features including social login options.
- **[CodePen](https://codepen.io/)**: For experimenting with and showcasing front-end code snippets and styles.
- **[Universe](https://universe.com/)**: For inspiration and ideas related to web design and user experience.

## Deployment

Dive In is deployed on Heroku, a cloud platform that enables easy deployment and scaling of web applications. The deployment process involves:

1. **Connecting to Heroku**: Link the GitHub repository to Heroku for continuous integration and deployment.
2. **Configuring Environment Variables**: Set up environment variables such as database credentials and secret keys in the Heroku dashboard.
3. **Setting Up the Database**: Configure PostgreSQL or another supported database for production use.
4. **Running Migrations**: Apply database migrations to ensure the schema is up-to-date on Heroku.
5. **Deploying Updates**: Push changes from GitHub to Heroku to keep the live site updated with the latest features and fixes.

For more detailed deployment instructions, refer to the [Heroku Deployment Documentation](https://devcenter.heroku.com/articles/deploying-python).

## Credits

Special thanks to the following resources and individuals for their contributions and inspiration:

- **[Code Institute](https://codeinstitute.net/)**: The "I Think Therefore I Blog" tutorial was essential for understanding Django's ORM and setting up initial models.
- **[Django Documentation](https://docs.djangoproject.com/)**: Official documentation guided implementation of Django features and best practices.
- **[CodePen](https://codepen.io/)**: Provided valuable front-end code snippets and design ideas.
- **[Uiverse](https://uiverse.io/)**: Offered inspiration for web design and user experience improvements.
- **[Bootstrap](https://getbootstrap.com/)**: Used for creating a responsive and modern layout.
- **[Canva](https://canva.com/)**: Helped in styling the Dive In logo.
- **[Viola](https://github.com/violaberg)**: A fellow coder who provided support and motivation throughout the development process, helping to overcome challenging phases and stay focused.

### Social Media

Stay connected and follow updates on our Facebook page: [Dive In Blog Facebook Page](https://www.facebook.com/blogdivein)


### Site Information

Dive In aims to create an engaging and interactive platform for scuba diving and travel enthusiasts. By offering a space for users to share experiences, connect with others, and explore captivating content, Dive In fosters a sense of community and adventure among its users.

