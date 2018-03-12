import falcon
from falcon import testing
import msgpack
import pytest

from pricesearch import ProductResource


@pytest.fixture
def client():
    return testing.TestClient(ProductResource)


# pytest will inject the object returned by the "client" function
# as an additional parameter.
def test_list_images(client):
    id = {
        'id': '3400052'
    }

    response = client.simulate_get('/product/{id}')
    result_doc = msgpack.unpackb(response.content, encoding='utf-8')
    assert result_doc == doc
    assert response.status == falcon.HTTP_OK
