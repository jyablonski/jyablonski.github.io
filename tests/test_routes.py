def test_index_returns_200(client):
    """Test that the home page loads successfully."""
    response = client.get("/")
    assert response.status_code == 200


def test_posts_returns_200(client):
    """Test that the posts page loads successfully."""
    response = client.get("/posts/")
    assert response.status_code == 200


def test_projects_returns_200(client):
    """Test that the projects page loads successfully."""
    response = client.get("/projects/")
    assert response.status_code == 200


def test_resume_returns_200(client):
    """Test that the resume page loads successfully."""
    response = client.get("/resume/")
    assert response.status_code == 200


def test_404_for_nonexistent_page(client):
    """Test that non-existent pages return 404."""
    response = client.get("/this-page-does-not-exist/")
    assert response.status_code == 404


def test_index_contains_expected_content(client):
    """Test that the home page contains expected elements."""
    response = client.get("/")
    html = response.data.decode("utf-8")
    # Check that we get valid HTML back
    assert "<html" in html.lower() or "<!doctype" in html.lower()


def test_projects_contains_project_data(client):
    """Test that projects page loads project data from JSON."""
    response = client.get("/projects/")
    html = response.data.decode("utf-8")
    # Projects page should contain links to GitHub repos
    assert "github.com" in html.lower() or "project" in html.lower()
