from sqlalchemy.orm import Session
from models.companies import Company

def create_company(db: Session, name: str, address: str, contact_email: str):
    db_company = Company(name=name, address=address, contact_email=contact_email)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

def get_company(db: Session, company_id: int):
    return db.query(Company).filter(Company.company_id == company_id).first()

def get_companies_by_name(db: Session, name: str, skip: int = 0):
    return db.query(Company).filter(Company.name.ilike(f"%{name}%")).all()

def update_company_info(db: Session, company_id: int, address: str, contact_email: str):
    db_company = db.query(Company).filter(Company.company_id == company_id).first()
    if db_company:
        db_company.address = address
        db_company.contact_email = contact_email
        db.commit()
        db.refresh(db_company)
        return db_company
    return None

def delete_company(db: Session, company_id: int):
    db_company = db.query(Company).filter(Company.company_id == company_id).first()
    if db_company:
        db.delete(db_company)
        db.commit()
        return db_company
    return None
