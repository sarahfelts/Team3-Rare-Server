## Project Title:
Rare Server

## Motivation: 
Our client, Rare Publishing, needs a new application built for their readers. Currently, readers can submit new articles through the mail and once month Rare sends out a Zine of articles that the publishers liked the most. They've finally decided that the internet is not a fad and want a new way for readers view posts.

The finished application will give users the ability to submit, update and comment on posts. The posts will also be organized by tags and categories making it easier for the reader to find the posts they are searching for.

The previous dev team was able to complete the client and server side portions of login and register. It is up to you to complete the remaining tickets. It is also up to you to decide how many of those tickets you will complete in the first sprint.

## Tech/Framework Used:
- Python
- Django
- SQL

## ERD:
![Rare Server ERD](assets/rare-server-erd.png "Rare Server ERD")

## Postman Tests:
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/29856352-f0660fd9-e4b2-4547-8593-f29f83a67757?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D29856352-f0660fd9-e4b2-4547-8593-f29f83a67757%26entityType%3Dcollection%26workspaceId%3Da17a84ad-b447-438b-8887-52ae3c3fc5db)

## Installation:
1. Run `pipenv shell` to start the virtual environmentss
1. Run `pipenv install` to install the dependencies
1. Create a `db.sqlite3` file
1. Add a connection to the database file
1. Run the commands in the `loaddata.sql` file to create the tables in the database

## Contributions: 
- Jay Lhomme - Added ability to do full CRUD for Posts
- Frank Campos - Added ability to do full CRUD for Comments
- Jesse Ramirez - Added ability to do full CRUD For Users