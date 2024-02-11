#!/usr/bin/python3
"""
Defines city model and
inherits from BaseModel
"""

from models.base_model import BaseModel

class City(BaseModel):
	# City Model

	# Attributes
	state_id: str = ''
	name: str= ''
