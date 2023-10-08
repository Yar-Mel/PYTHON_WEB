from datetime import date
import unittest
from unittest.mock import MagicMock
from sqlalchemy.orm import Session
from fastapi import HTTPException

from src.db.models import Contact, User
from schemas import ContactRequest
from src.repository.contacts import (
    create_contact,
    get_contact,
    get_contacts,
    update_contact,
    delete_contact,
    search_contacts,
    upcoming_birthdays,
)


class TestContacts(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.session = MagicMock(spec=Session)
        self.current_user = User(id=1)

    def tearDown(self):
        self.session.reset_mock()

    # ------------------------------------------------------------------------------------------------------------------
    async def test_create_contact(self):
        body = ContactRequest(
            first_name="Neville",
            last_name="Chamberlain",
            email="chamberlain@example.net",
            phone_number="+380981234567",
            birthday=date(1874, 11, 30),
        )
        self.session.query.return_value.filter.return_value.first.return_value = None
        result = await create_contact(
            contact=body, db=self.session, current_user=self.current_user
        )
        self.assertEqual(result.first_name, body.first_name)
        self.assertEqual(result.last_name, body.last_name)
        self.assertEqual(result.email, body.email)
        self.assertEqual(result.phone_number, body.phone_number)
        self.assertEqual(result.birthday, body.birthday)
        self.assertTrue(hasattr(result, "id"))

        self.session.query.return_value.filter.return_value.first.return_value = (
            Contact(phone_number=body.phone_number)
        )
        with self.assertRaises(HTTPException) as context:
            await create_contact(
                contact=body, db=self.session, current_user=self.current_user
            )
        self.assertEqual(context.exception.status_code, 400)
        self.assertEqual(context.exception.detail, "Phone number already exists")

    # ------------------------------------------------------------------------------------------------------------------
    async def test_get_contact(self):
        contact_id = 1
        contact = Contact(id=contact_id, user_id=self.current_user.id)
        self.session.query.return_value.filter.return_value.first.return_value = contact
        result = await get_contact(
            contact_id=contact_id, db=self.session, current_user=self.current_user
        )
        self.assertEqual(result, contact)

        self.session.query.return_value.filter.return_value.first.return_value = None
        with self.assertRaises(HTTPException) as context:
            await get_contact(
                contact_id=contact_id, db=self.session, current_user=self.current_user
            )
        self.assertEqual(context.exception.status_code, 404)
        self.assertEqual(context.exception.detail, "Contact not found")

    # ------------------------------------------------------------------------------------------------------------------
    async def test_get_contacts(self):
        body_1 = ContactRequest(
            first_name="Winston",
            last_name="Churchill",
            email="churchill@example.net",
            phone_number="111",
            birthday=date(1874, 11, 30),
        )
        body_2 = ContactRequest(
            first_name="Oswald",
            last_name="Mosley",
            email="mosley@example.net",
            phone_number="222",
            birthday=date(1896, 12, 3),
        )
        await create_contact(
            contact=body_1, db=self.session, current_user=self.current_user
        )
        await create_contact(
            contact=body_2, db=self.session, current_user=self.current_user
        )

        result = await get_contacts(
            0, 2, db=self.session, current_user=self.current_user
        )
        self.assertEqual(len(result), 1)

    # ------------------------------------------------------------------------------------------------------------------
    async def test_update_contact(self):
        contact_id = 1
        contact = Contact(id=contact_id, user_id=self.current_user.id)
        updated_contact_data = ContactRequest(
            first_name="Updated",
            last_name="Contact",
            email="updated@example.com",
            phone_number="+380981234561",
            birthday=date(2000, 1, 1),
        )
        self.session.query.return_value.filter.return_value.first.return_value = contact
        result = await update_contact(
            contact_id=contact_id,
            updated_contact=updated_contact_data,
            db=self.session,
            current_user=self.current_user,
        )
        self.assertEqual(result.first_name, updated_contact_data.first_name)
        self.assertEqual(result.last_name, updated_contact_data.last_name)
        self.assertEqual(result.email, updated_contact_data.email)
        self.assertEqual(result.phone_number, updated_contact_data.phone_number)
        self.assertEqual(result.birthday, updated_contact_data.birthday)

        self.session.query.return_value.filter.return_value.first.return_value = None
        with self.assertRaises(HTTPException) as context:
            await update_contact(
                contact_id=contact_id,
                updated_contact=updated_contact_data,
                db=self.session,
                current_user=self.current_user,
            )
        self.assertEqual(context.exception.status_code, 404)
        self.assertEqual(context.exception.detail, "Contact not found")

    # ------------------------------------------------------------------------------------------------------------------
    async def test_delete_contact(self):
        contact_id = 1
        contact = Contact(id=contact_id, user_id=self.current_user.id)
        self.session.query.return_value.filter.return_value.first.return_value = contact
        result = await delete_contact(
            contact_id=contact_id, db=self.session, current_user=self.current_user
        )
        self.assertEqual(result, contact)

        self.session.query.return_value.filter.return_value.first.return_value = None
        with self.assertRaises(HTTPException) as context:
            await delete_contact(
                contact_id=contact_id, db=self.session, current_user=self.current_user
            )
        self.assertEqual(context.exception.status_code, 404)
        self.assertEqual(context.exception.detail, "Contact not found")

    # ------------------------------------------------------------------------------------------------------------------
    async def test_search_contacts(self):
        query = "test_user"
        contacts = [
            Contact(id=i, user_id=self.current_user.id, first_name=f"test_user {i}")
            for i in range(1, 6)
        ]
        self.session.query.return_value.filter.return_value.offset.return_value.limit.return_value.all.return_value = (
            contacts
        )
        result = await search_contacts(
            q=query, skip=0, limit=5, db=self.session, current_user=self.current_user
        )
        self.assertEqual(result, contacts)

    # ------------------------------------------------------------------------------------------------------------------
    async def test_upcoming_birthdays(self):
        upcoming_birthdays_contacts = [
            Contact(id=i, user_id=self.current_user.id) for i in range(1, 6)
        ]
        self.session.query.return_value.filter.return_value.params.return_value.all.return_value = (
            upcoming_birthdays_contacts
        )
        result = await upcoming_birthdays(
            db=self.session, current_user=self.current_user
        )
        self.assertEqual(result, upcoming_birthdays_contacts)


if __name__ == "__main__":
    unittest.main()
