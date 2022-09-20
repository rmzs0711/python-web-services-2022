from fastapi import APIRouter

from app.contracts import Guest

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


@router.post("/guests/")
def test_query(guest: Guest): # noqa : D103
    if guest.social_rating < 50:
        return "access denied"
    else:
        return "(^._.^) ---- meow "
