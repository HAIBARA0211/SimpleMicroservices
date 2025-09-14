from fastapi import APIRouter, HTTPException
from models.address import Address
from uuid import UUID

router = APIRouter(prefix="/addresses", tags=["addresses"])
_addresses: dict[UUID, Address] = {}

@router.get("", response_model=list[Address])
def list_addresses():
    return list(_addresses.values())

@router.post("", response_model=Address, status_code=201)
def create_address(a: Address):
    if a.id in _addresses:
        raise HTTPException(400, "ID exists")
    _addresses[a.id] = a
    return a

@router.get("/{id}", response_model=Address)
def get_address(id: UUID):
    if id not in _addresses:
        raise HTTPException(404, "Not found")
    return _addresses[id]

@router.put("/{id}", response_model=Address)
def update_address(id: UUID, a: Address):
    if id != a.id:
        raise HTTPException(400, "ID mismatch")
    if id not in _addresses:
        raise HTTPException(404, "Not found")
    _addresses[id] = a
    return a

@router.delete("/{id}", response_model=dict)
def delete_address(id: UUID):
    if id not in _addresses:
        raise HTTPException(404, "Not found")
    _addresses.pop(id)
    return {"ok": True}
