import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from students.models import Student, Course
from model_bakery import baker


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_course(courses_factory, client):
    course = courses_factory(name='programming')
    response = client.get(reverse('courses-detail', args=[course.id]))

    assert response.status_code == 200
    assert response.data['id'] == course.id
    assert response.data['name'] == course.name


@pytest.mark.django_db
def test_cours_list(client, courses_factory):
    courses = courses_factory(_quantity=20)
    response = client.get('/courses/')

    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)


@pytest.mark.django_db
def test_filter_course_id(client, courses_factory):
    courses = courses_factory(_quantity=20)
    course_id_filter = courses[0].id
    response = client.get(f'/courses/?id={course_id_filter}')

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]['id'] == course_id_filter


@pytest.mark.django_db
def test_filter_course_name(client, courses_factory):
    courses = courses_factory(_quantity=20)
    course_name_filter = courses[0].name
    response = client.get(f'/courses/?name={course_name_filter}')

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]['name'] == course_name_filter


@pytest.mark.django_db
def test_create_course(client):
    response = client.post('/courses/', data={'name': 'programming'})

    assert response.status_code == 201


@pytest.mark.django_db
def test_update_course(client):
    response1 = client.post('/courses/', data={'name': 'programming'})
    assert response1.status_code == 201

    course_id = response1.data['id']

    response2 = client.patch(reverse('courses-detail', args=[course_id]),
                             data={'name': 'programming update'})
    assert response2.status_code == 200


@pytest.mark.django_db
def test_delete_course(client):
    response1 = client.post('/courses/', data={'name': 'programming'})
    assert response1.status_code == 201

    courses_id = response1.data['id']

    response2 = client.delete(reverse('courses-detail', args=[courses_id]))
    assert response2.status_code == 204


