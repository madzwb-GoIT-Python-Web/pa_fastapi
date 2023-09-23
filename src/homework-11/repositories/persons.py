import database.schema as db

from datetime import date
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import func, and_
from schema import Person, PersonContacts#, Persons



async def create(datas: Person, session: Session) -> Person:
    datas = db.Person(**dict(datas))
    session.add(datas)
    session.commit()
    session.refresh(datas)
    return datas

async def reads(skip: int, limit: int, session: Session) -> List[Person]:
    persons:List[Person] = []
    result = session.query(db.Person).offset(skip).limit(limit).all()
    for r in result:
        person = Person.model_validate(r)
        persons.append(person)
    return persons

async def read(pid: int, session: Session) -> Person:
    return session.query(db.Person).filter(db.Person.id == pid).first()

async def reads_persons_by_birthday(days: int, session: Session) -> List[PersonContacts]:
    result = session.query(db.Person)\
                .join(db.Person.contacts)\
                .filter(func.days_to_birthday(db.Person.born_date, date.today()) <= days).all()
    persons:List[PersonContacts] = []
    for r in result:
        person = PersonContacts.model_validate(r)
        persons.append(person)
    return persons

async def reads_persons(first_name: str, last_name: str, session: Session) -> List[PersonContacts]:
    if first_name and last_name:
        result = session.query(db.Person)\
                    .join(db.Person.contacts)\
                    .filter(
                        and_(
                            db.Person.first_name.like('%' + first_name + '%'),
                            db.Person.last_name.like('%' + last_name + '%')
                        )
                    ).all()
    elif first_name:
        result = session.query(db.Person)\
                    .join(db.Person.contacts)\
                    .filter(db.Person.first_name.like('%' + first_name + '%'))\
                    .all()
    elif last_name:
        result = session.query(db.Person)\
                    .join(db.Person.contacts)\
                    .filter(db.Person.last_name.like('%' + first_name + '%'))\
                    .all()
    else:
        result = session.query(db.Person)\
                    .join(db.Person.contacts)
    persons:List[PersonContacts] = []
    for r in result:
        person = PersonContacts.model_validate(r)
        persons.append(person)
    return persons

async def reads_contacts(value: str, session: Session) -> List[PersonContacts]:
    result = session.query(db.Person).join(db.Person.contacts).filter(db.Contact.value.like('%' + value + '%')).all()
    contacts = []
    for r in result:
        contact = PersonContacts.model_validate(r)
        contacts.append(contact)
    return contacts

async def read_contacts(pid: int, session: Session) -> PersonContacts:
    result = session.query(db.Person).join(db.Person.contacts).filter(db.Person.id == pid).first()
    contacts = PersonContacts.model_validate(result)
    return contacts

async def update(pid: int, datas: Person, session: Session) -> Person | None:
    _datas = session.query(db.Person).filter(db.Person.id == pid).first()
    if _datas:
        _datas.first_name   = datas.first_name
        _datas.last_name    = datas.last_name
        _datas.born_date    = datas.born_date
        session.commit()
    return datas

async def delete(pid: int, session: Session)  -> Person | None:
    datas = session.query(db.Person).filter(db.Person.id == pid).first()
    if datas:
        session.delete(datas)
        session.commit()
    return datas