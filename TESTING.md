# TESTING.md

## Overview

This document details the testing process, methodologies, and results for the Full-Stack Web application. The goal is to ensure that the application meets the specified requirements, is fully functional, and provides a smooth and secure user experience.

### Learning Outcomes Addressed

- **LO1**: Application designed and developed using Agile methodology and MVC framework.
- **LO2**: Implementation of a data model, application features, and business logic.
- **LO3**: Application of authentication, authorization, and permission features.
- **LO4**: Creation of manual and automated tests.
- **LO5**: Use of version control with Git and GitHub.
- **LO6**: Deployment of the application to a cloud-based platform.
- **LO7**: Understanding and use of object-based software concepts.

## Testing Strategy

### Manual Testing

Manual testing was conducted to validate user interactions, data handling, and overall application behavior. Each feature and user story was manually tested to ensure it met the acceptance criteria.

**Tools Used:**

- **Agile Tool**: For tracking user stories and testing progress.
- **Django Admin**: For backend testing of models and admin actions.
- **Browser Developer Tools**: For inspecting frontend elements and console errors.

### Automated Testing

Automated tests were written using Django's testing framework and other relevant tools. These tests focused on verifying the functionality, usability, and data management processes of the application.

**Python Tests:**

- **Unit Tests**: Testing individual components such as models, views, and forms.
- **Integration Tests**: Ensuring that components work together as expected.
- **End-to-End Tests**: Validating the complete user workflow from start to finish.

### Browser and Device Compatibility Testing

The application was tested across multiple browsers and devices to ensure consistent performance and responsiveness.

**Browsers Tested:**

- Google Chrome
- Mozilla Firefox
- Microsoft Edge
- Safari

**Devices Tested:**

- Desktop (Windows, macOS)
- Tablet (iOS, Android)
- Mobile (iOS, Android)

## Test Scenarios

### Post Model

| Test Scenario                              | Expected Outcome                                                       | Pass/Fail    |
|--------------------------------------------|-------------------------------------------------------------------------|--------------|
| Test creating a new post                   | A new post should be created successfully                               | Pass         |
| Test setting post status as "Published"    | Post status should be updated to "Published"                            | Pass         |
| Test setting post status as "Draft"        | Post status should be updated to "Draft"                                | Pass         |
| Test creating a post without an author     | The system should not allow creating a post without specifying an author | Pass         |
| Test slug generation                       | Slugs should be correctly generated based on the post title             | Pass         |
| Test displaying featured posts on homepage | Featured posts should be displayed correctly on the homepage            | Pass         |

### Comment Model

| Test Scenario                                   | Expected Outcome                                                                 | Pass/Fail    |
|-------------------------------------------------|-----------------------------------------------------------------------------------|--------------|
| Test adding a new comment                       | A comment should be added successfully                                            | Pass         |
| Test editing an existing comment                | Users should be able to edit their own comments, and it should be marked as "Pending" | Pass     |
| Test deleting a comment                         | Users should be able to delete their own comments                                 | Pass         |
| Test comment approval process                   | Comments should only be visible after admin approval                              | Pass         |
| Test viewing pending comments as author         | Authors should be able to see their own comments marked as "Pending approval"     | Pass         |
| Test viewing comments of other users            | Users should not see unapproved comments from other users                         | Pass         |
| Test admin comment approval actions             | Admins should be able to approve comments via the admin panel                     | Pass         |

### Category and Tag Models

| Test Scenario                                   | Expected Outcome                                                                 | Pass/Fail    |
|-------------------------------------------------|-----------------------------------------------------------------------------------|--------------|
| Test creating a new category                    | A new category should be created successfully                                     | Pass         |
| Test creating a new tag                         | A new tag should be created successfully                                          | Pass         |
| Test associating categories with posts          | Categories should be successfully associated with posts                           | Pass         |
| Test associating tags with posts                | Tags should be successfully associated with posts                                 | Pass         |
| Test displaying posts by category               | Posts should be filtered and displayed by category on the frontend                | Pass         |
| Test displaying posts by tag                    | Posts should be filtered and displayed by tag on the frontend                     | Pass         |

### User Authentication and Profile

| Test Scenario                                   | Expected Outcome                                                                 | Pass/Fail    |
|-------------------------------------------------|-----------------------------------------------------------------------------------|--------------|
| Test user registration                          | Users should be able to register successfully                                     | Pass         |
| Test user login                                 | Users should be able to log in successfully                                       | Pass         |
| Test user logout                                | Users should be able to log out successfully                                      | Pass         |
| Test viewing user profile                       | Users should be able to view their own profile                                    | Pass         |
| Test updating user profile                      | Users should be able to update their profile information                          | Pass         |
| Test uploading profile picture                  | Users should be able to upload and update their profile picture                   | Pass         |
| Test restricted access to admin panel           | Non-admin users should not be able to access the admin panel                      | Pass         |

### Admin Actions

| Test Scenario                                   | Expected Outcome                                                                 | Pass/Fail    |
|-------------------------------------------------|-----------------------------------------------------------------------------------|--------------|
| Test accessing the admin panel                  | Only staff members should be able to access the admin panel                       | Pass         |
| Test managing posts in the admin panel          | Admins should be able to create, edit, and delete posts                           | Pass         |
| Test managing comments in the admin panel       | Admins should be able to approve, edit, and delete comments                       | Pass         |
| Test managing categories in the admin panel     | Admins should be able to create, edit, and delete categories                      | Pass         |
| Test managing tags in the admin panel           | Admins should be able to create, edit, and delete tags                            | Pass         |
| Test managing users in the admin panel          | Admins should be able to manage user accounts                                     | Pass         |
| Test approval of pending comments               | Admins should be able to see and approve pending comments                         | Pass         |

## Bugs Identified

### List of Bugs

1. **Comment Approval Visibility**
   - **Description**: Unapproved comments were temporarily visible to other users due to a caching issue.
   - **Steps to Reproduce**:
     1. Add a new comment on a post.
     2. Check the post as another user.
   - **Expected Outcome**: Unapproved comments should not be visible to other users.
   - **Actual Outcome**: Unapproved comments were visible until the cache refreshed.
   - **Status**: Fixed by adjusting cache settings.

2. **Profile Picture Upload**
   - **Description**: Profile picture uploads failed on Safari due to file type handling.
   - **Steps to Reproduce**:
     1. Attempt to upload a profile picture using Safari.
   - **Expected Outcome**: The profile picture should upload successfully.
   - **Actual Outcome**: The upload failed with a file type error.
   - **Status**: Fixed by updating the allowed file types.

3. **Post Slug Collision**
   - **Description**: Duplicate slugs were generated when creating posts with similar titles.
   - **Steps to Reproduce**:
     1. Create a post titled "My Post."
     2. Create another post titled "My Post."
   - **Expected Outcome**: A unique slug should be generated for the second post.
   - **Actual Outcome**: The second post had the same slug, causing a collision.
   - **Status**: Fixed by appending a unique identifier to duplicate slugs.

## Screenshots and Logs

Below are the screenshots and logs captured during the testing process. These visual aids help to contextualize the test results and provide evidence of the testing procedures.

### Screenshots

- **New Post Creation**: ![New Post Creation](screenshots/new_post_creation.png)
- **Comment Approval Notice**: ![Comment Approval Notice](screenshots/comment_approval_notice.png)
- **Category Filtering**: ![Category Filtering](screenshots/category_filtering.png)
- **Admin Panel Access**: ![Admin Panel Access](screenshots/admin_panel_access.png)

### Logs

- **Error Logs**: Relevant logs capturing errors encountered during testing are stored in the `logs/error.log` file.
- **Test Execution Logs**: Logs of automated test execution can be found in the `logs/test_execution.log` file.

## Future Testing Considerations

1. **Performance Testing**: Evaluate the application under heavy load to ensure it scales effectively.
2. **Security Testing**: Conduct penetration testing to identify potential security vulnerabilities.
3. **Accessibility Testing**: Ensure the application meets accessibility standards for users with disabilities.
4. **Continuous Integration**: Implement a CI pipeline to automate the testing process for future updates.

## Round Up

The testing process for this Full-Stack Web application was comprehensive, covering manual, automated, and compatibility testing across various browsers and devices. All identified bugs were addressed and resolved. The application is now stable and ready for deployment, meeting all the specified project requirements and learning outcomes.


