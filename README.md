# Blog API

This project is a Blog API built with FastAPI. It provides endpoints for creating, reading, updating, and deleting blog posts. The API follows the OpenAPI 3.1 specification.

### Features
- Create a new blog post
- Retrieve all blog posts
- Retrieve a specific blog post by ID
- Update an existing blog post
- Delete a blog post by ID
Endpoints

### Rootes
*GET /*: Root endpoint to check if the API is running.
Blog Operations
*GET /api/v0/all_blog:* Retrieve all blog posts.
*GET /api/v0/blog/{str_id}:* Retrieve a specific blog post by its ID.
*POST /api/v0/create_post:* Create a new blog post.
*DELETE /api/v0/del_blog/{str_id}:* Delete a blog post by its ID.
*PUT /api/v0/update_blog/{str_id}:* Update an existing blog post by its ID.

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/BlogApi.git 


cd BlogApi
```

## Usage

```python
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install the dependencies:
pip install -r requirements.txt

# Run the application:'
py src/run.py

```
### Schemas
BlogBase
Defines the basic structure of a blog post.

### Usage
Once the server is running, you can access the API documentation at
- http://127.0.0.1:8000/docs 
- http://127.0.0.1:8000/redoc.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License
