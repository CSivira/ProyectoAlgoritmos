class ExpressionTree:

    def __init__(self, expr, left=None, right=None):
        """ Metodo que inicializa los valores del tipo de dato ExpresionTree

        Parameters
        ----------
        self : ExpresionTree
            Se trabaja sobre el mismo objeto
        expr : string
            Contenido del ExpresionTree
        left : ExpresionTree
            Hijo izquierdo del objeto actual
        right : ExpresionTree
            Hijo derecho del objeto actual

        Return
        ------
        Nada

        Side Effect
        -----------
        Se inicializa un nuevo objeto de tipo ExpresionTree

        """
        self.expr = expr
        self.left = left
        self.right = right

    def __str__(self):
        """ Metodo de salida estandar para el tipo de dato ExpresionTree

        Parameters
        ----------
        self : ExpresionTree
            Se trabaja sobre el mismo objeto

        Return
        ------
        Salida estandar en formato string. Solo se muestra el contenido del objeto
        actual, es decir, el atributo expr

        Side Effect
        -----------
        Se muestra por la salida estandar el contenido del objeto actual

        """
        return "%s" % (str(self.expr))

    def printPreOrder(self):
        """ Metodo que transforma el contenido del objeto en la notacion prefija de
        operacion binaria

        Parameters
        ----------
        self : ExpresionTree
            Se trabaja sobre el mismo objeto

        Return
        ------
        Retorna la transformacion del contenido en la notacion prefija de la operacion binaria

        Side Effect
        -----------
        El contenido del objeto se retorna en notacion prefija de la operacion binaria

        """
        return "(%s %s %s)" % (str(self.expr), str(self.left), str(self.right))

    def printInOrder(self):
        """ Metodo que transforma el contenido del objeto en la notacion infija de operacion binaria

        Parameters
        ----------
        self : ExpresionTree
            Se trabaja sobre el mismo objeto

        Return
        ------
        Retorna la transformacion del contenido en la notacion infija de la operacion binaria

        Side Effect
        -----------
        El contenido del objeto se retorna en notacion infija de la operacion binaria

        """
        return "(%s %s %s)" % (str(self.left), str(self.expr), str(self.right))

    def printPostOrder(self):
        """ Metodo que transforma el contenido del objeto en la notacion sufija de operacion binaria

        Parameters
        ----------
        self : ExpresionTree
            Se trabaja sobre el mismo objeto

        Return
        ------
        Retorna la transformacion del contenido en la notacion sufija de la operacion binaria

        Side Effect
        -----------
        El contenido del objeto se retorna en notacion sufija de la operacion binaria

        """
        return "(%s %s %s)" % (str(self.left), str(self.right), str(self.expr))

    def evaluate(self):
        """ Metodo que resuelve una operacion binaria suministrada

        Parameters
        ----------
        self : ExpresionTree
            Se trabaja sobre el mismo objeto

        Return
        ------
        ExpresionTree
            Se guarda el resultado obtenido de realizar la operacion binaria con los
            datos suministrados en el atribuyo expr. Si la operacion es invalida,
            entonces retorna None

        Side Effect
        -----------
        La variable result contiene el ExpresionTree que guarda el resultado de
        realizar la operacion binaria con los datos suministrados

        """
        result = 0
        # Se verifica en cada guardia que tipo de operador se esta leyendo (+,-,*,/)
        if self.expr == "/":

            # Evitamos la division por cero mediante una guardia
            if float(self.right.expr) != 0:

                # Se resuelven las operaciones haciendo el contenido de los objetos hijos flotantes
                result = float(self.left.expr) / float(self.right.expr)

            else:

                print('''Can't divide by zero''')
                return None

        elif self.expr == "*":

            result = float(self.left.expr) * float(self.right.expr)

        elif self.expr == "-":

            result = float(self.left.expr) - float(self.right.expr)

        elif self.expr == "+":

            result = float(self.left.expr) + float(self.right.expr)

        solution = ExpressionTree(str(result), None, None)

        # Se retorna la solucion como un objeto ExpresionTree
        return solution
        