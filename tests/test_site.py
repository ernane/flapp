from flask import url_for


def test_get_home(client):
    response = client.get(url_for("site.home"))
    assert response.status_code == 200
    assert b"Home Page" in response.data
    assert response.mimetype == "text/html"


def test_get_index(client):
    response = client.get(url_for("site.index"))
    assert response.status_code == 200
    assert b"Index Page" in response.data
    assert response.mimetype == "text/html"


def test_request_returns_404(client):
    assert client.get("/not_found").status_code == 404
