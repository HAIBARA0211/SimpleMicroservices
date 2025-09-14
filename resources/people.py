from fastapi import APIRouter, HTTPException
from models.person import Person

router = APIRouter(prefix="/persons", tags=["persons"])
_people: dict[str, Person] = {}

@router.get("", response_model=list[Person])
def list_persons():
    return list(_people.values())

@router.post("", response_model=Person, status_code=201)
def create_person(p: Person):
    if p.uni in _people:
        raise HTTPException(400, "UNI exists")
    _people[p.uni] = p
    return p

@router.get("/{uni}", response_model=Person)
def get_person(uni: str):
    if uni not in _people:
        raise HTTPException(404, "Not found")
    return _people[uni]

@router.put("/{uni}", response_model=Person)
def update_person(uni: str, p: Person):
    if uni != p.uni:
        raise HTTPException(400, "UNI mismatch")
    if uni not in _people:
        raise HTTPException(404, "Not found")
    _people[uni] = p
    return p

@router.delete("/{uni}", response_model=dict)
def delete_person(uni: str):
    if uni not in _people:
        raise HTTPException(404, "Not found")
    _people.pop(uni)
    return {"ok": True}
