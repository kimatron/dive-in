| Test Case Description                    | Expected Outcome                                 | Test Passed |
|-----------------------------------------|---------------------------------------------------|--------------|
| **Post Model**                          |                                                   |              |
| Test creating a new post                | Verify that a new post can created successfully   | yes          |
 Test creating a post with a duplicate title | Ensure the system prevents the creation of a post with a duplicate title | yes |
| Test setting post status as "Published" | Confirm that the status of a post can be set to "Published" successfully | yes |
| Test setting post status as "Draft"     | Confirm that status of a post can be set to "Draft" successfully | yes |
| Test creating a post without an author  | Ensure the system does not allow creating a post without specifying an author | yes |
| **Comment Model**                       |                                                    |              |
| Test creating a new comment              | Verify that a comment can be added to a post successfully | yes        |
| Test approving a comment                | Confirm that a comment can be approved successfully | yes      |
| Test creating a comment without a  | Ensure the system does not allow creating a comment without specifying a post | yes |
| **About Model**                         |                                                    |             |
| Test creating a new about section       | Verify that the about section can be created successfully | yes      |
| **Category Model**                      |                                                   |               |
| Test creating a new category             | Verify that a category can be created successfully | yes         |
| **Tag Model**                           |                                                   |               |
| Test creating a new tag                  | Verify that a tag can be created successfully | yes            |
| **Subscriber Model**                    |                                                   |                |
| Test subscribing with a valid email      | Confirm that a user can subscribe with a valid email address | yes     |
| Test unsubscribing a subscriber         | Verify that a subscriber can be unsubscribed | yes               |
| Test creating a subscriber without an email | Ensure the system does not allow creating a subscriber without specifying an email address | yes |
| **FeaturedPost Model**                  |                                                   |              |
| Test featuring a post                   | Verify that a post can be set as a featured post successfully | yes       |
| Test unaturing a post                   | Verify that a featured post can be unfeatured successfully | yes       |
