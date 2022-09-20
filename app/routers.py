from fastapi import APIRouter

router = APIRouter()


@router.get("/test")
def test_default(): # noqa : D103
    return "Hello world"


@router.get("/test/{test_id}")
def test_route(test_id: int): # noqa : D103
    return "Hello world № " + str(test_id)


@router.get("/")
def test_query(name: str): # noqa : D103
    return "Hello " + name
