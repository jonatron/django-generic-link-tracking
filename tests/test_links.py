from .models import Foo
from generic_links.models import GenericLink

import pytest
import time


@pytest.mark.django_db
def test_no_relation_link_creation():
    gl = GenericLink()
    gl.where = 'here'
    gl.url = 'http://www.google.com'
    gl.save()

    assert gl.get_link() == '/glc/B/'
    assert gl.click_count == 0


@pytest.mark.django_db
def test_relation_link_creation():
    foo = Foo()
    foo.bar = 'bat'
    foo.save()

    gl = GenericLink()
    gl.where = 'here'
    gl.url = 'http://www.google.com'
    gl.content_object = foo
    gl.save()

    assert gl.get_link() == '/glc/B/'
    assert gl.click_count == 0
    assert gl.content_object.bar == 'bat'


@pytest.mark.django_db
def test_link_click(client):
    gl = GenericLink()
    gl.where = 'here'
    gl.url = 'http://www.google.com'
    gl.save()

    assert gl.click_count == 0
    client.get(gl.get_link())
    assert gl.click_count == 1


# This test relies on randomness to pass :/
@pytest.mark.django_db
def test_rotation(client):
    gl = GenericLink()
    gl.where = 'here'
    gl.url = 'http://www.google.com'
    gl.save()

    gl2 = GenericLink()
    gl2.where = 'there'
    gl2.url = 'http://www.ask.com'  # jeeves!
    gl2.save()

    gl3 = GenericLink()
    gl3.where = 'there'
    gl3.url = 'http://www.bing.com'  # someone somewhere uses it, presumably
    gl3.rotate = "%s,%s" % (gl.id, gl2.id)
    gl3.save()

    response_urls = []
    for x in range(10):
        resp = client.get(gl3.get_link())
        response_urls.append(resp['location'])

    unique_urls = set(response_urls)
    assert len(unique_urls) > 1
