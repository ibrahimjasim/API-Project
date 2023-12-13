# Moments - API

## User stories
Welcome to Fotogram, your go-to social media app! Fotogram is a dynamic platform crafted to empower users to share the meaningful moments of their lives.
| Category  | User Action                               | Purpose                                      | API Feature                 |
|-----------|-------------------------------------------|----------------------------------------------|-----------------------------|
| Auth      | Register for an account                   | Have a personal profile with a picture        | dj-rest-auth                |
| Auth      | Register for an account                   | Create, like, and comment on posts           | Create post, Create comment, Create like |
| Auth      | Register for an account                   | Follow users                                 | Create follower             |
| Posts     | Visitor - View a list of posts            | Browse the most recent uploads                | List/Filter posts           |
| Posts     | Visitor - View an individual post         | See user feedback, i.e., likes and read comments | Retrieve post            |
| Posts     | Visitor - Search a list of posts          | Find a post by a specific artist or title    | List/Filter posts           |
| Posts     | Visitor - Scroll through a list of posts  | Browse the site more comfortably              | List/Filter posts           |
| Posts     | User - Edit and delete my post            | Correct or hide any mistakes                 | Update property, Destroy property |
| Posts     | User - Create a post                      | Share my moments with others                 | Create post                 |
| Posts     | User - View liked posts                   | Go back often to my favorite posts            | List/Filter posts           |
| Posts     | User - View followed users' posts         | Keep up with my favorite users' moments      | List/Filter posts           |
| Likes     | User - Like a post                        | Express my interest in someone's shared moment | Create like                |
| Likes     | User - Unlike a post                      | Express that my interest in someone's shared moment has faded away | Destroy like |
| Comments  | User - Create a comment                   | Share my thoughts on other people's content  | Create comment              |
| Comments  | User - Edit and delete my comment         | Correct or hide any mistakes                 | Update comment, Destroy comment |
| Profiles  | User - View a profile                     | See a user's recent posts, followers, following count data | Retrieve profile, List/Filter posts |
| Profiles  | User - Edit a profile                     | Update my profile information                 | Update profile              |
| Followers | User - Follow a profile                   | Express my interest in someone's content     | Create follower             |
| Followers | User - Unfollow a profile                 | Express that my interest in someone's content has faded away and remove their posts from my feed | Destroy follower |
| Events    | User - Create an event                    | Organize and share upcoming events           | Create event                |
| Events    | User - View upcoming events               | Stay informed about upcoming activities      | List/Filter events          |
| Contacts  | User - View my contacts                   | Access and manage my contact list            | List/Filter contacts        |
| Contacts  | User - Add a contact                      | Expand my network by adding new contacts     | Create contact              |
| Contacts  | User - Remove a contact                   | Manage my contact list                       | Destroy contact       


## Models and CRUD breakdown
| Model      | Endpoint            | Create | Retrieve | Update | Delete | Filter        | Text Search   |
|------------|---------------------|--------|----------|--------|--------|---------------|---------------|
| Users      | users/              | Yes    | Yes      | Yes    | No     | No            | No            |
|            | users/:id/           | Yes    | Yes      | Yes    | No     | No            | No            |
| Profiles   | profiles/           | Yes (signals) | Yes  | Yes    | No     | Following,    | Name          |
|            | profiles/:id/        | Yes (signals) | Yes  | Yes    | No     | Name          |               |
| Followers  | followers/          | Yes    | Yes      | No     | Yes    | No            | No            |
|            | followers/:id/       | Yes    | Yes      | No     | Yes    | No            | No            |
| Likes      | likes/              | Yes    | Yes      | No     | Yes    | No            | No            |
|            | likes/:id/           | Yes    | Yes      | No     | Yes    | No            | No            |
| Comments   | comments/           | Yes    | Yes      | Yes    | Yes    | Post          | No            |
|            | comments/:id/        | Yes    | Yes      | Yes    | Yes    | Post          | No            |
| Posts      | posts/               | Yes    | Yes      | Yes    | Yes    | Profile,      | Title         |
|            | posts/:id/           | Yes    | Yes      | Yes    | Yes    | Liked, Feed   | Title         |
| Events     | events/              | Yes    | Yes      | Yes    | Yes    | No            | Title         |
|            | events/:id/          | Yes    | Yes      | Yes    | Yes    | No            | Title         |
| Contacts   | contacts/            | Yes    | Yes      | Yes    | Yes    | No            | Name          |
|            | contacts/:id/        | Yes    | Yes      | Yes    | Yes    | No            | Name          |

## Database schema.
![Api Diagram - SqlDBM - Google Chrome 2023-12-13 13_29_45](https://github.com/ibrahimjasim/API-Project/assets/127301769/d8ee9018-3d57-483e-bf40-aa84beece261)


## Deployment steps
- set the following environment variables:
    - CLIENT_ORIGIN
    - CLOUDINARY_URL
    - DATABASE_URL
    - DISABLE_COLLECTSTATIC
    - SECRET_KEY
- installed the following libraries to handle database connection:
    - psycopg2
	- dj-database-url
- configured dj-rest-auth library for JWTs
- set allowed hosts
- configured CORS:
	- set allowed_origins
- set default renderer to JSON
- added Procfile with release and web commands
- gitignored the env&#46;py file
- generated requirements.txt
- deployed to Heroku

---

