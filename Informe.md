#### CI2692 Proyecto 2
##### Autor: Carlos Sivira 15-11377

### Aplicación de Pilas y Árboles Binarios: Expresiones en Notación Polaca Inversa 
****
#### Resumen

El objetivo de este proyecto es la aplicación de dos estructuras de datos fundamentales, pilas y árboles binarios, para la evaluación de expresiones aritméticas en Notación Polaca Inversa (NPI). Adicionalmente se desea poder transformar expresiones desde su forma en NPI a su forma infija y su forma prefija.
****
#### Detalles de la implementación

El proyecto está compuesto por tres script : ExpressionTree.py, NPI.py y Stack.py. Además se tiene un script llamado Constantes.py que contiene los datos constantes a usar en la implementación.

**ExpresionTree.py**: Este script cuenta con una clase llamada ExpresionTree. Esta clase recibe en su constructor tres parámetros: expr (contenido del objeto), left (apuntador al hijo izquierdo del objeto) y right (apuntador al hijo derecho del objeto). La salida estándar de esta tipo de dato es el contenido del objeto, es decir, el atributo expr. La clase cuenta con tres métodos propios: printPreOrder (retorna el contenido del objeto, en string, de la forma prefija), printInOrder (retorna el contenido del objeto, en string, de la forma infija) y printPostOrder (retorna el contenido del objeto, en string, de la forma sufija). Finalmente, este objeto tiene un último método propio que se encarga de retornar la evaluación del contenido del objeto. Este método verifica que tipo de operador esta contenido en el atributo expr y guarda en una variable el resultado de evaluar la operacion con dicho operador; el resultado es guardado en una variable de tipo ExpresionTree con hijo izquierda y derecha nulos.

**NPI.py**: Primeramente, nos encontramos con el método main, que basicamente contiene las instrucciones de entradas de datos. Además determina que tipo de operación es solicitada para mostrar por la salida estandart el resultado conveniente. 

Si la operacion indicada es "-eval", se procede a la contrucción de un árbol binario con los tipos de datos ExpressionTree; esta operación la realiza el método tree_constructor que recibe un arreglo de strings. Este métoco recorre el arreglo verificando si cada elemento es un operador o un operando y luego, mediante el algoritmo de la notación polaca inversa y el uso de listas, construye cada ExpressionTree de la siguiente forma: Si es operando, crea un ExpressionTree con el operando y con hijos nulos; Si es operador, crea un ExpressionTree con el operador y siendo sus hijos los dos operadores anteriores al operando. Luego de construir el árbol binario, se procede a evaluar, recursivamente, el contenido de cada ExpresionTree dentro de árbol binario. Para hacerlo, se ejecuta el método solve, que recibe el objeto raíz del árbol binario; luego, mediante la implementación recursiva de solve, es llamado el método evaluate de la clase ExpressionTree para que retorne la evaluación de cada objeto dentro del árbol.

El método solve verifica los cuatro casos posibles para un nodo del árbol binario:

* Si ambos hijos del objeto actual son operadores, entonces se procede a crear una variable resultado, de tipo ExpressionTree, que contiene al objeto actual y como hijos tiene la llamada del método solve para cada hijo.

* Si solo un hijos del objeto actual es operador, y el otro es operando, se procede a crear una variable resultado, de tipo ExpressionTree, que contiene al objeto actual. Uno de sus hijos, el operador, es pasado con la llamada del método solve, mientas que para el otro hijo solo se pasa su apuntador. Aca se contemplan las dos conbinaciones posibles entre los hijos izquierda y derecha.

* Si ambos hijos del objeto actual son operandos, entonces se procede a crear una variable resultado, de tipo ExpressionTree, que contiene al objeto actual y como hijos tiene los apuntadores de cada hijo. Este sería el caso base de la recursión.

Si la operación indicada es "-preorder", "-inorder" o "-postorder" se procede nuevamente con la construccion del árbol binario. Posteriormente, se ejecuta, recursivamente, el método tree_path que recibe el objeto raíz del árbol binario. Este método funciona de manera análoga al método solve, su única diferencia radica en que el valor retornado es la llamada al método de la clase ExpressionTree correspondiente con la opcion solicitada. 

* Si la opción es "-preorder", entonces se llama al método printPreOrder que retorna la trasnformación de la expresión en su forma prefija.

* Si la opción es "-inorder", entonces se llama al método printInOrder que retorna la trasnformación de la expresión en su forma infija

* Si la opción es "-postorder", entonces se llama al método printPostOrder que retorna la trasnformación de la expresión en su forma sufija

Para verificar si un operador o una opción es valida, es decir, que son las indicadas para la implementación de proyecto, se usadon los métodos check_operator y check_option. Ambos métodos son una implementación del operador existencial y solo verifican si el string suministrado aparece dentro de los arreglos de contenido constante.

Para verificar si un operando era válido, se hace uso del método check_operand que verifica si un string dado puede ser convertido a un tipo de dato flotante. Si dicho valor no puede ser convertido, se retorna falso, caso contrario, se retorna verdadero.

**Stack.py**: Este script contiene la implementación de una pila básica. Como esta implementación fue utilizada en previos laboratorios, no nos detendremos a explicar su funcionamiento.

**Constantes.py**: Este “script” solo contiene dos variables cuyos valores no se verán alterados en la ejecución del resto de los algoritmos. La primera variable es operators_, contiene un arreglo de cuatro strings (“+”, “-”, “*”, “/”) que indican los operadores permitidos. La segunda variable es options_, contiene un arreglo de cuatro strings (“-preorder”, “-inorder”, “postorder”, “-eval”) que indican las operaciones válidas que el algoritmo puede realizar. Se decidió colocar las constantes en un script aparte para diferenciar su contenido del resto del algoritmo.
****
#### Conclusiones

La implementación del árbol binario de operaciones binarias se logró de manera exitosa, así como el proceso de evaluación y transformación del la expresión suministrada.

Por otra parte, el uso de pilas resulto bastante útil para la construcción del árbol binario, ya que, en este caso particular, permite mantener la precedencia de los operadores.

Al momento de realizar la evaluación y la transformación de la expresión, nos encontramos con que una implementación recursiva es la mejor manera de atacar el problema, primeramente porque en algoritmos anteriores recorremos los árboles de manera recursiva y segundo por que la naturaleza de la clase ExpressionTree no admite una solucion "sencilla" que no sea implementando una solución recursiva. 

