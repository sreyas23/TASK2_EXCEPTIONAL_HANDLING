* I built this small FastAPI project to practice how to structure an API cleanly and how to handle errors at the controller level before the request reaches the service layer. The API works with an in-memory list of books and supports adding books, listing them, and generating book details.

* I tested the API using simple curl requests to make sure all the responses work the way they should. Here’s what I verified:

1) Listing books returned 200 OK and showed the existing books.

2) Adding a new book returned 201 Created and added it successfully.

3) Trying to add the same book again returned 409 Conflict, which means the duplication logic works.

4) Sending a request with an empty or missing title returned 400 Bad Request.

5) Getting book details returned 200 OK with the summary content.

These tests helped confirm that my exception handling in the controller is working correctly and different conditions return the correct HTTP status codes.

**TEST**

<img width="1468" height="841" alt="Screenshot 2025-11-13 at 12 00 01 AM" src="https://github.com/user-attachments/assets/a06b91e2-4593-4cc1-8a1c-ad64940ae2a5" />
