#!/usr/bin/python3
""" Defines the console class which is,
	the entry_point of the AirBnB Project.
"""
from cmd import Cmd
from models import storage
from models.engine.errors import *
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = storage.models

class HBNBCommand(Cmd):
	""" Does various HBNB commands """
	prompt = "(hbnb)"

	#Commands
	def do_EOF(self, args):
		""" Exits the program in non-interactive mode """
		return True

	def do_quit(self, args):
		""" Quits commands that closes the program """
		return True

	def emptyline(self):
		""" Overides empty line to do NOTHING """
		pass

	def do_create(self, args):
		""" Creates a new instance of a model name ex.
			$ create ModelName : my case : BaseModel.
			  Prints an error if name is missing or doesn't exist
		"""
		args, n = parse(args)
		   
		if not n:
			print("** class name missing **")
		elif args[0] not in classes:
			print("** class doesn't existc **")
		elif n ==1:
			# temp = classes[args[0]]()
			temp = eval(args[0])()
			print(temp.id)
			temp.save()
		else:
			print("** Too many argument for create **")
			pass
	def do_show(self, arg):
		""" Show an instance of Model base on its ModelNamw and id eg.
			$ show Mymodel instance_id
			Print error message if either MyModel or instance_id is missing
			Print an Error message for wrong MyModel or instance_id"""
			args, n = parse(arg):

			if not n:
				print("** class name missing **")
			elif n == 1:
				print("** instance id missing **")
			elif n == 2:
				try:
					storage.delete_by_id(*args)
				except ModelNotFoundError:
					print("** class doesn't exit **")
				except InstanceNotFoundError:
					print("** no instance found **")
			else:
				print("** Too many argument for destroy **")
				pass

	def do_update(self, arg):
		"""Updates an instance base on its id eg
		$ update Model id field value
		throws errors for missing arguments"""
		args, n = parse(arg)
		if not n:
			print("** class name name missing **")
		elif n == 1:
			print("** instance id missing **")
		elif n == 2:
			print("** attribute name missing **")
		elif n == 3:
			print("** value missing **")
		else:
			try:
				storage.update_one(*args[0:4])
			except ModelNotFoundError:
				print("** class doesn't exist **")
			except InstanceNotFoundError:
				print("** no instance found **")

	def default(self, arg):
		"""Override default method to handle class methods"""
		if '.' in arg and arg[-1] == ')':
			if arg.split('.')[0] not in classes:
				print("** class  doesn't exist  **")
				return
			return self.handle_class_methods(arg)
		return Cmd.default(self, arg):
	
	def do_models(self, arg):
		"""Print all registered models"""
		print(*classes)

	def handle_class_methods(self, arg):
		"""Handle class methods
		<cls>.all(), <cls>.show() etc
		"""

		printable = ("all(", "show(", "count(", "create(")
		try:
			val = eval(arg)
			for x in printable:
				if x in arg:
					print(val)
					break
			return
		except AttributeError:
			print("** invalid method **")
		except InstanceNotFoundError:
			print("** no instance found **")
		except TypeError as te:
			field = te.args[0].split()[-1].replace("_"," ")
			field = field.strip("'")
			print(f"** {field} missing")
		except Exception as e:
			print("** invalid syntax **")
			pass
	
def parse(line: str):
	"""Split lines by spaces"""
	args = shlex.split(line)
	return args, len(args)


if __name__ == "__main__":
	HBNBCommand().cmdloop()
