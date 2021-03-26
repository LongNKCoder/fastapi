from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.base import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateEntitiesType = TypeVar("CreateEntitiesType", bound=BaseModel)
UpdateEntitiesType = TypeVar("UpdateEntitiesType", bound=BaseModel)


class BaseDAO(Generic[ModelType, CreateEntitiesType, UpdateEntitiesType]):
    def __init__(self, model: Type[ModelType]):
        """
        DAO object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `entities`: A Pydantic model (entities) class

        Every model want to interact with database need to inherit from this class

        Then you can override the function for specific goals
        """
        self.model = model

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        """Get a model by query an Id of object
        :param db: Session that connect to database
        :param id: Id use to query
        :action: Query and return an model if the object's id is exist else raise 404 status_code
        :rtype: ModelType
        """
        result = db.query(self.model).filter(self.model.id == id).first()
        if not result:
            raise HTTPException(status_code=404, detail=f"{self.model} not found")
        return result

    def get_list(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        """Get a list of models
        :param db: Session that connect to database
        :param skip: skip objects
        :param limit: limit objects appear
        :action: Query and return a list of model
        :rtype: ModelType
        """
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in: CreateEntitiesType) -> ModelType:
        """Add a model to databse
        :param db: Session that connect to database
        :param obj_in: Object want to add
        :action: Change input obj_in in to dictionary and make it a db's model
                 then add it into database and commit then refesh database
        :rtype: ModelType
        """
        obj_in_data = jsonable_encoder(obj_in)
        validate_data = obj_in.dict(exclude_unset=True)
        for field in obj_in_data:
            if validate_data.get(field) is None:
                raise HTTPException(status_code=422)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: Union[UpdateEntitiesType, Dict[str, Any]]
    ) -> ModelType:
        """Update a model to databse
        :param db: Session that connect to database
        :param obj_in: Object want to add
        :param db_obj: Object want to compare
        :action: Compare fields in 2 objects db_obj and obj_in
                 if obj_in's field has value. Update it.
        :rtype: ModelType
        """
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data and update_data.get(field, None) is not None:
                setattr(db_obj, field, update_data.get(field))
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, id: int) -> ModelType:
        """Delete a model by query an Id of object
        :param db: Session that connect to database
        :param id: Id use to delete
        :action: de;ete and return an model if the object's id is exist else raise 404 status_code
        :rtype: ModelType
        """
        obj = db.query(self.model).get(id)
        if not obj:
            raise HTTPException(status_code=404, detail=f"{self.model} not found")
        db.delete(obj)
        db.commit()
        return obj
