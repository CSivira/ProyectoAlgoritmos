# Importaciones necesarias
import sys

from Constantes import operators_

from Constantes import options_

from ExpressionTree import ExpressionTree

from Stack import Stack

def main():
	""" Metodo principal que ejecuta el algoritmo

	Parameters
	----------
	Nada

	Return
	------
	Nada

	Side Effect
	-----------
	Inicia la ejecucion del algoritmo
	"""

	# Recibimos los datos suministrados
	option = sys.argv[1]
	exp = sys.argv[2]

	# Creamos un arreglo con los caracteres suministrados
	exp = exp.split()

	# Si la expresion suministrada tiene menos de 3 elementos, entonces no
	# es valida
	if len(exp) < 3:
		print("This is not a valid expresion")
		sys.exit()

	# Verificamos si la opcion suministrada es valida
	if check_options(option):

		# Cosntruimos el arbol binario de las operaciones binarias
		result = ""
		root = tree_constructor(exp)

		# Verificamos si tenemos que trasnformar o evaluar la expresion
		# suministrada
		if option != "-eval":

			# Obtenemos la trasnformacion deseada
			result = tree_path(root, option)

		else:

			# Obtenemos el resultado de evaluar la expresion
			result = solve(root)

	else:

		# Terminamos la ejecucion si la opcion no es valida
		print("the argument " + option + " is not valid")
		sys.exit()

	# Mostramos la salida estandar solicitada
	print(result)


def check_operator(operator: str) -> (bool):
	""" Metodo que verifica si un operador dado es valido

	Parameters
	----------
	operator : string
		Contiene un operador que debe ser verificado como valido

	Returns
	-------
	bool
		Indica si el string suministrado es valido o no

  	Side Effect
  	-----------
  	El booleano indica si el string suministrado es valido o no

	"""
	state = False

	# Verificamos si existe una coincidencia con los operadores (+, -, *, /)
	for k in operators_:

		if operator == k:
			state = True

	return state


def check_operand(operand: str) -> (bool):
	""" Metodo que verifica si un operando dado es valido

	Parameters
	----------
	operand : string
		Contiene un operando que debe ser verificado como valido

	Returns
	-------
	bool
		Indica si el string suministrado es valido o no

	Side Effect
	-----------
	El booleano indica si el string suministrado es valido o no

	"""
	try:

		# Verificamos si el operando suministrado puede ser convertido a
		# flotante
		float(operand)
		return True

	except ValueError:

		return False


def check_options(option: str) -> (bool):
	""" Metodo que verifica si una opcion dada es valida

	Parameters
	----------
	option : string
		Contiene una opcionque debe ser verificada como valida

	Return
	------
	bool
		Indica si elstring suministrado es valido o no

	Side Effect
	-----------
	El booleano indica si el string suministrado es valido o no

	"""
	state = False

	# Verificamos si existen coincidencias con las opciones ("-inorder",
	# "-preorder", "-postorder", "-eval")
	for k in options_:

		if option == k:
			state = True

	return state


def solve(node: ExpressionTree) -> (ExpressionTree):
	""" Metodo que recorre un arbol binario de operaciones binarias con el
	objetivo de resolver su contenido respentando la presedencia de los
	operadores

    Parameters
    ----------
    node : ExpresionTree
        Objeto raiz del arbol binario de operaciones binarias

    Return
    ------
    ExpresionTree
        Se retorna la llamada del metodo de la clase ExpresionTree solve

    Side Effect
    -----------
    Se realiza la llamada del metodo de la clase ExpresionTree solve

    """
    # Si el objetos ExpresionTree no tiene contenido, entonces no es una
    # expresion valida para trabajar
	if node is None:
		print('Invalid expresion')
		sys.exit()

	# Creamos un objeto ExpresionTree vacio
	result = ExpressionTree("", None, None)

	# Verificamos si el arbol tiene operadores o operandos en los hijos
	# izquierda o derecha
	if check_operator(node.left.expr) and check_operator(node.right.expr):

		# Se asigna a result un ExpresionTree que tiene como contenido la
		# solucion de evaluar sus hijos izquierda y derecha
		result = ExpressionTree(node.expr, solve(node.left), solve(node.right))

	elif check_operator(node.left.expr) and check_operand(node.right.expr):

		result = ExpressionTree(node.expr, solve(node.left), node.right)

	elif check_operator(node.right.expr) and check_operand(node.left.expr):

		result = ExpressionTree(node.expr, node.left, solve(node.right))

	elif check_operand(node.left.expr) and  check_operand(node.right.expr):

		result = ExpressionTree(node.expr, node.left, node.right)

	# Se retorna el nodo raiz que contiene el resultado de evaluar toda la
	#expresion
	return result.evaluate()


def tree_constructor(expresion: [str]) -> (ExpressionTree):
	""" Metodo que construye un arbol binario con las operaciones binarias
	suministradas

	Parameters
	----------
	expresion : string array
		Contiene cada uno de los elementos de la expresion suministrada. Su
		tipo de dato es string

	Return
	------
	ExpresionTree
		Contiene al elemento raiz del arbol binario. Su tipo de dato es
		ExpresionTree. Si la expresion suministrada es invalida, entonces
		se retornara None

	Side Effect
	-----------
	La variable root contiene al elemento raiz del arbol binaro. Si la
	expresion es invalida, contiene None

	"""
	# Cremaos una lista con un tamaño suficiente
	stack_tree = Stack(len(expresion))

	# Recorremos cada uno de los elementos de la expresion
	for i in expresion:

		# Verificamos si el elemento es un operador, operando o un dato
		#invalido
		if check_operand(i):

			# Insertamos un ExpresionTree del operando en la lista stack_tree
			operand = ExpressionTree(i, None, None)
			stack_tree.push(operand)

		elif check_operator(i):

			# Verificamos si hay al menos dos elementos que se puedan
			# extraer de la lista
			if stack_tree.top_ > 0:

				# Extraemos los dos ultimos elmentos de la lista y creamos
				# un ExpresionTree con el opedaror como padre y los operandos
				# como hijos. Insertamos el objeto en la lista stack_tree
				operand2 = stack_tree.pop()
				operand1 = stack_tree.pop()
				operator = ExpressionTree(i, operand1, operand2)
				stack_tree.push(operator)

			else:

				# Salimos de ejecucion si faltan operadores
				print("missing operators")
				sys.exit()

		else:

			# Salimos de ejecucion si algun elemento de la expresion no es
			# valido
			print('The element: '+ i + ' is not a number or valid operand')
			sys.exit()

	# Extraemos el ultimo elemeto de la lista
	root = stack_tree.pop()

	# Verificamos si la lista no esta vacia para terminar la ejecucion
	if stack_tree.top_ != -1:

		print("There are operands without operators")
		stack_tree.push(root)
		sys.exit()

	# Retornamos el objeto raiz del arbol binario
	return root


def tree_path(node: ExpressionTree, print_mode: str) -> (str):
	""" Metodo que recorre el arbol binario de operaciones binarias de forma
	recursiva. Construye una trasnformacion de la expresion suministrada en
	el formato pedido

	Parameters
	----------
	node : ExpresionTree
		Contiene el elemento raiz del arbol binario de operaciones binarias.
		Tambien puede contener None
	print_mode : string
		Indica que tipo de trasnformacion ha de realizarse a la expresion
		suministrada. Los valores posibles son: "-preorder" , "-inorder" ,
		"-postorder"

	Return
	------
	string
		Cadena que contiene la trasnformacion de la expresion suminstrada
		mediante el metodo indicado. Este valor se obtiene mediante la
		llamada de la funcion de la clase ExpresionTree : printPreOrder,
		printInOrder, printPostOrder

	Side Effect
	-----------
	Se realiza la llamada de alguno de estos metodos de la clase
	ExpresionTree: printPreOrder, printInOrder, printPostOrder

	"""
	# Si el objetos ExpresionTree no tiene contenido, entonces no es una
	# expresion valida para trabajar
	if node is None:
		print('Invalid expresion')
		sys.exit()

	# Creamos un objeto ExpresionTree vacio
	result = ExpressionTree("", None, None)

	# Verificamos si el arbol tiene operadores o operandos en los hijos
	# izquierda o derecha
	if check_operator(node.left.expr) and check_operator(node.right.expr):
		
		# Se asigna a result un ExpresionTree que tiene como contenido la
		# solucion de llamar al metodo indicado por print_mode sus hijos
		# izquierda y derecha.
		result = ExpressionTree(node.expr, tree_path(node.left, print_mode), tree_path(node.right, print_mode))

	elif check_operator(node.left.expr) and check_operand(node.right.expr):

		result = ExpressionTree(node.expr, tree_path(node.left, print_mode), node.right)

	elif check_operator(node.right.expr) and check_operand(node.left.expr):

		result = ExpressionTree(node.expr, node.left, tree_path(node.right, print_mode))

	elif check_operand(node.left.expr) and  check_operand(node.right.expr):

		result = ExpressionTree(node.expr, node.left, node.right)

	# Se retorna una salida según la transformacion indicada por print_mode
	if print_mode == "-preorder":

		return result.printPreOrder()

	if print_mode == "-inorder":

		return result.printInOrder()

	if print_mode == "-postorder":

		return result.printPostOrder()

main()
