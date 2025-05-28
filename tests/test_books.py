def test_post_book(client):
    response = client.post("/books", json={
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "genre": "Ficção"
    })
    assert response.status_code == 201
    assert b"Livro adicionado com sucesso" in response.data


def test_get_books(client):
    # Primeiro adiciona um livro
    client.post("/books", json={
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "genre": "Ficção"
    })
    # Depois testa a listagem
    response = client.get("/books")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["title"] == "1984"


def test_get_single_book(client):
    post = client.post("/books", json={
        "title": "Brave New World",
        "author": "Aldous Huxley",
        "year": 1932,
        "genre": "Ficção"
    })
    book_id = post.get_json()["message"]  # ou capture ID se retornar o objeto
    response = client.get("/books/1")
    assert response.status_code == 200
    assert response.get_json()["author"] == "Aldous Huxley"


def test_update_book(client):
    client.post("/books", json={
        "title": "Old Title",
        "author": "Author",
        "year": 2000,
        "genre": "Drama"
    })

    response = client.put("/books/1", json={"title": "New Title"})
    assert response.status_code == 200
    assert b"Livro atualizado com sucesso" in response.data

    updated = client.get("/books/1")
    assert updated.get_json()["title"] == "New Title"


def test_delete_book(client):
    client.post("/books", json={
        "title": "To Delete",
        "author": "Someone",
        "year": 2001,
        "genre": "Mistério"
    })
    response = client.delete("/books/1")
    assert response.status_code == 200
    assert b"Livro removido com sucesso" in response.data

    # Verifica se sumiu
    response = client.get("/books/1")
    assert response.status_code == 404