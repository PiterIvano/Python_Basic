import os

os.system("color 0a")
#verificar si es linux o windows
def limpiar():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
limpiar()
#Colocamos el logo del programa

#aqui definimos informacion de contacto 
def info_contacto():
    print("""           ACERCA DEL CREADOR DE ESTE PROGRAMA\n\n 
        CREADOR DE ESTE PROGRAMA: JOEL ANAYA 
        ACTUALIZACIONES: PITER
        """)

while True:
    input("Presiona cualquier tecla para continuar")
    limpiar()
    print("""\n
    |---------------------------------------------|
    |------------APRENDIENDO PYTHON---------------|
    |---------------------------------------------|\n
    \n""")


    print("""[!] GLOSARIO
    1. Que es python?
    2. Estructura de datos
    3. Números en python 
    4. Operaciomes matemáticas simples
    5. Operaciones matemáticas avanzadas
    6. Variables
    7. Cadenas de texto (String-Str)
    8. Listas
    9. Diccionarios
    10. Tuplas
    11. Sets
    12. Booleanos
    13. Encadenando comparadores de operación
    14. Condicionales if, elif y else
    15. Ciclos For
    16. Ciclos While
    17. Usando While y Else
    18. Palabras clave utiles (Extra)
    19. Operadores Utiles (Extra)
    20. Comprehension de listas
    21. Funciones
    22. Expresiones Lambda, Mapas y Filtros
    23. Programación orientada a objetos
    24. Modulos y paquetes en python
    25. __name___ y '__main__'
    26. Manejo de errores y excepciones
    27. ACERCA DEL CREADOR DE ESTE PROGRAMA 
    \n
    ELIGE EL TEMA QUE QUIERAS!!\n""")
    opcion = input("Elige el número con el tema que quieres trabajar\n--->")
    limpiar()

    #OPCIONES DEL 1
    if opcion =="1":
        print("""                    QUE ES PYTHON?\n 
        Python es un lenguaje de programación multiparadigma en el\ncual puedes desarrollar todo tipo de programa que quieras,\npuedes desarrollar paginas web, interfaces graficas,\nhacking etico y muchas cosas mas,si te interesa el tema\nquedate aquí y sigue navegando en el programa,hay muchos\ntemas!!  
        \n """)
        
    if opcion =="2":
        print("""                       ESTRUCTURA DE DATOS\n\n 
        NOMBRE                 TIPO          DESCRIPCION\n 
        Enteros                Int           3 500 50000\n   
        Decimales              Float         2.5 6.76 56.856\n 
        Cadena de texto        Str          'Hola','Joel', '20.000' \n       
        Listas                 List          [10,'Hola',200.4]\n   
        Diccionarios           Dic           {'Palabra':'significado                                     ',clave:'valor'}\n   
        Tuplas                 Tup           orden inmutable(10,'Hola',200,4)\n   
        Sets                   Set           Coleccion de objetos no ordenados{'a','b'}\n 
        Booleanos              Bool          True o False\n\n """)
         


    if opcion =="3":
        print("""                          NUMEROS EN PYTHON\n 
        Enteros-(Int)\n 
        a=4+4 
        print(a) 
        resultado: 8\n 
        Tambien lo podemos imprimir así:\n 
        print(4+4) 
        resultado: 8\n\n 
        Decimales-(Float)\n 
        b=4.5+4.56 
        print(b) 
        resultado: 9.05999... 
        \n """)
         
    if opcion =="4":
        print("""                 Operaciones matemáticas simples\n".upper())
            Podemos hacer restas, sumas, multiplicacion y division de la siguiente manera:\n 
            RESTAS (-)\n 
            a=4-4 
            print(a) 
            resultado: 0\n\n 
            SUMAS (+)\n 
            b=5+5 
            print(b) 
            resultado: 10\n\n 
            MULTIPLICACION (*)\n 
            c=2*2 
            print(c) 
            resultado: 4\n\n 
            DIVISION (/)\n 
            d=4/2 
            print(d) 
            resultado: 2\n\n""")
         

    if opcion=="5":
        print("""               OPERACIONES MATEMATICAS AVANZADAS 
            MODULUS\n 
            Modulus lo que hace es retornar la sobra de la division, ver si el numero es divisible, o si es par o impar para\nello utilizamos este signo(%)\n 
            RESTO O SOBRA\n 
            a=7%4 
            print(a) 
            resultado: 3\n 
            DIVISIBLE\n 
            a=50%5 
            print(a) 
            resultado: 0\n 
            PAR\n 
            a=23%1 
            print(a) 
            resultado: 0 ←par\n\n 
            IMPAR\n 
            a=23%2 
            print(a) 
            resultado: 1 ←impar\n\n\n 
            POTENCIA\n 
            La potencia de cada numero, lo que hace es que eleva o \nmultiplica 2 veces el numero que queremos multiplicar, para ello utilizamos dos veces el signo de multiplicar(**) 
            p=20**2 
            print(p) 
            resultado: 400\n 
            p2=10**2 
            print(p2) 
            resultado: 100\n 
            Tambien podemos hacer operaciones mas complejas a esto se le conoce como Betmas usando los signos de operaciones\nmatematicas de la siguiente manera:\n 
            BETMAS\n 
            a=2+10*10+4 
            print(a) 
            resultado: 106\n\n 
            a=(2+10)*(10+4) 
            print(a) 
            resultado: 168\n\n""") 
         
            
    if opcion =="6":
        print("""                     VARIABLES 
        Acabamos de trabajar con numeros,pero es dificil saber que\nrepresentan estos numeros si no les asignamos una variable.\n 
        Seria bueno asignar a estos tipos de datos un nombre para\npoder reconocerlos.\n\n 
        Por ejemplo:\n\n 
        Mis_casas=2\n 
        Reglas para nombrar variables:\n 
        []Se considera buena practica usar nombres en minúsculas.\n 
        [] Evita usar palabras con significado especial como\n'list' o 'Str'.\n\n 
        Python usa nomenclatura dinámica\n 
        []Esto significa que puedes re-asignar variables a otros\ntipos de datos.\n 
        []Esto hace python bastante flexible al momento de asignar\nvariables\n 
        mis_casas = 2\n 
        mis_casas = ['casa1','casa2'\n 
        Esto es correcto en python!!\n """)
         
        
    if opcion =="7":
        print("""                    CADENAS DE TEXTO  \n 
        Las cadenas de texto son secuencias de caracter,\nusan sintaxis con comillas simples o comillas dobles\n 
        [] 'Hola'\n 
        []  caracter = 'cadena de texto con muchos caracteres'\n 
        Debido a que las cadenas de texto son secuencias ordenadas\nsignifica que podemos usar indexado y slicing para agarrar\nsub-secciones de una cadena.\n 
        Notacion de indexado: [], asignado despues de la cadena\n 
        Imdexado: Permite agarrar un caracter singular de una cadena de texto.\n 
        Slicing: Permite agarrar una subseccion de multiples\ncaracteres, un 'slice' de una cadena.\n 
        Tiene la siguiente sintaxis:\n 
        [start:stop:step]→[0:4:2]\n 
        Start: Es un indice numerico para el slice iniciar.\n 
        Stop: Es el numero donde paramos el slice.\n 
        Step: Son los pasos que damos.\n\n 
        Indexado:\n 
        micadena=('Hola Mundo') 
        print(micadena[2] 
        resultado: l \n\n 
        Slicing:\n 
        micadena = 'Hola Mundo'\n 
        print(micadena[0:4] 
        resultado: Hola\n\n """)
         
        
    if opcion =="8":
        print("""                              LISTAS \n 
            Las listas son secuencias ordenadas que guardan una variedad de tipos de datos 
            Usan [] braquets y comas para separar objetos en una lista:\n 
            [1,2,3,4,5]\n 
            Las listas soportan indexados y slicing\n 
            Puedes tener listas adentro de listas y pueden guardar\nmetodos que pueden ser llamados.\n 
            milista=[1,2,3] 
            print(milista) 
            resultado: [1,2,3]\n\n """)
         

    if opcion =="9":
        print("""                          DICCIONARIOS\n  
            [] Son mapeos desordenados para guaradar objetos\n 
            [] Previamente vimos como las listas guardan objetos en una secuencia ordenada\n 
            [] Los diccionarios utilizan orden basado en par\nclave/valor.\n 
            [] Los diccionarios usan llaves abiertas y cerradas {} y dos puntos : para simbolizar las llaves y su valor asociado.\n\n 
            Cuando deberiamos escoger una lista o un diccionario?\n 
            [] Diccionarios: Objetos retornados por llave\n 
            [] Desordenado y no se guarda, bueno para cuando no\nsabes donde se encuentra algo\n 
            Listas: Objetos retornados por locación\n 
            [] Puede ser Indexado o Slicing\n\n 
            mi_diccionario = {'llave1':'valor1','llave2':'valor2'} 
            print(mi_diccionario) 
            resultado: {'llave1':'valor1','llave2':'valor2'}\n\n 
            mi_diccionario = {'llave1':'valor1','llave2':'valor2'} 
            print(mi_diccionario['llave1']) 
            resultado: valor1\n\n """)
         
    
    if opcion =="10":
        print("""                        TUPLAS\n 
        Las tuplas son similares a las listas.Sin embargo, tienen\nuna diferencia (inmutabilidad)\n 
        Una vez que un elemento se encuentra en una tupla, este no\npuede ser re-asignado.\n 
        Las tuplas usan parentesis: (1,2,3)\n 
        t=('a','a','b') 
        t[0]='Nuevo' 
        print(t)\n 
        Esto dará un error ya que las tuplas no se pueden re-asignar\n """)
         
        
    if opcion =="11":
        print("""                            SETS\n 
        Los sets son una coleccion unica y deaordenada de elementos.\n 
        Solamente puede haber UNA representacion del mismo objeto.\n\n 
        miset = set() 
        miset.add (1) 
        miset.add (2) 
        print(miset) 
        resultado: {1,2}\n """)
         
        
    if opcion =="12":
        print("""                       BOOLEANOS\n 
        Los booleanos son valores que permiten declarar verdadero o falso.\n 
        Son muy importantes cuando quieres hacer logicas.\n 
        print(2>3) 
        False\n 
        print(2<3) 
        True\n 
        print(2==3) 
        False\n 
        print(2>=2) 
        True\n\n 
        COMPARADORES DE OPERACION\n 
        == comparacion (a==b) Falso\n 
        <> Mayor o menor (2>3) Falso, (2<3) Verdadero\n 
        >= Mayor o igual a (2>=2) Verdadero, (2>=3) Falso\n 
        <= Menor o igual a (1<=2) Verdadero, (2<=1) Falso\n 
        != No son iguales (a!=b) Verdadero, (a!=a) Falso\n\n """)
         
        
    if opcion =="13":
        print("""        ENCADENANDO COMPARADORES DE OPERACION\n 
        Podemos usar operadores logicos para combinar comparaciones:\n 
        [] And\n 
        [] Or\n 
        [] Not\n 
        1<2 and 2<3 
        True\n 
        'y'=='y' or 3==3 
        True\n 
        300>6000 
        False\n 
        not 300>6000 
        True\n\n """)
         
        
    if opcion =="14":
        print("""            CONDICIONALES IF, ELIF, ELSE\n 
        Usamos las declaraciones para controlar el flujo de nuestro programa\n 
        Usualmente solo queremos que ciero código sea ejecutado\ncuando una condicion particular ocurra.\n 
        Por ejemplo, if mi perro tiene hambre aplicar logica),\nelse (aplicar logica si mi perro no tiene hambre)\n 
        Para controlar este flujo de logica usamos palabras clave:\n 
        [] if\n 
        [] elif\n 
        [] else\n 
        \n 
        COMO DECLARAMOS ESTAS CONDICIONES?\n\n 
        Sintaxis de una condicion (if)\n 
        if alguna_conficion:\n\n 
        Sintaxis de una declaracion (if/else)\n 
        if alguna_condicion: 
            ejecutamos codigo\n 
        if opcion == "": 
        aplicar algo mas\n\n 
        Sintaxis de una declaracion elif\n 
        if alguna_condicion: 
            ejecutamos codigo\n 
        elif alguna_otra_condicion: 
                    algo distinto\n 
        if opcion == "": 
        hacer algo mas\n\n 
        Ejemplo:\n 
        aprendiendo = True 
        if aprendiendo == True: 
            print('Estamos aprendiendo')\n 
        if opcion == "": 
        print('No estamos aprendiendo') 
        resultado: Estamos aprendiendo\n 
        si fuera false, el resultado seria No estamos aprendiendo\n\n """)
         
        
    if opcion =="15":
        print("""                        CICLOS FOR\n 
        Varios objetos en python son 'iterables', significa que podemos iterar sobre cada elemento en el objeto\n 
        Podemos iterar a travez de una lista o todos los caracteres en una cadena de texto\n 
        Podemos usar ciclos, For para ejecutar un bloque de codigo en cada iteracion\n 
        Sintaxis para un ciclo for:\n 
        lista_iterable = [1,2,3] 
        for nombre_item in lista_iterable: 
                print(nombre_item)\n\n 
        Ejemplo:\n 
        milista=[1,2,3,4,5,6,7,8,9,10] 
        for num in milista: 
            print(num) 
        resultado: \n 
        1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n\n 
        milista=[1,2,3,4,5,6,7,8,9,10] 
        for num in milista: 
            print('hola') 
        resultado: \n 
        hola\nhola\nhola\nhola\nhola\nhola\nhola\nhola\nhola\nhola\n\n """)
         
        
    if opcion =="16":
        print("""                    CICLOS WHILE\n\n 
        Los ciclos while van a continuar ejecutando un bloque\nde codigo. While (mientras) una condicion siga siendo\nverdadera\n\n 
        Sintaxis para ciclo while:\n 
        while condicion_booleana: 
                hacer algo\n\n 
        Puedes combinar con if opcion == "":\n 
        while condicion_booleana: 
                hacer algo 
        if opcion == "": 
        hacer algo distinto\n\n 
        Ejemplo:\n 
        x=0 
        while x < 5: 
            print(f'El valor actual de x es{x}') 
        x= x+1 
        resultado: El valor de x es 0\nEl valor de x es 1\nEl valor de x es 2\nEl valor de x es 3\nEl valor de x es 4\nEl valor de x es 5\n\n """)
         
        
    if opcion == "17":
        print("""                USANDO WHILE Y ELSE\n\n 
        x = 0 
        while x < 5: 
            print(f'El valor actual de x es {x}')\n 
        if opcion == "": 
        print('El ciclo terminó!!) 
        resultado: El valor de x es 0\nEl valor de x es 1\nEl valor de x es 2\nEl valor de x es 3\nEl valor de x es 4\nEl valor de x es 5\nEl ciclo terminó!!\n\n """)
         
        
    if opcion =="18":
        print("""                 PALABRAS CLAVE UTILES (EXTRA)\n\n 
        pass: Sirve para pasar de un problema o para saltar\nel problema\n 
        Ejemplo:\n 
        x=[1,2,3] 
        for item in x: 
            #comentario 
        print('Fin del programa')\n 
        ESTO DARÁ UN ERROR\n\n 
        x=[1,2,3] 
        for item in x: 
            #comentario 
            pass 
        print('Fin del programa') 
        Fin del programa\n\n 
        continue: Se usa para saltar letras o palabras\n\nEjemplo:\n 
        x=Python 
        for letra in x: 
            if letra =='y': 
                continue 
            print('letra') 
        resultado: Pthon\n\n 
        break: Se usa para parar o romper las cadenas o el bloque de codigo donde quieras que se detenga\n\nEjemplo:\n 
        x='Python' 
        for letra in x: 
            if letra =='t': 
                    break 
            print(letra) 
        resultado: Py\n 
        Como ves se detiene en la letra t\n\n """)
         
        
    if opcion =="19":
        print("""                   OPERADORES UTILES (EXTRA)\n\n 
        range: Sirve para colocar un rango a los numeros o palabras que queramos\n 
        Ejemplo:\n 
        for num in range(10): 
                print('num') 
        resultado: \n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n 
        El numero 10 no se muestra ya que python lo cuenta desde el numero cero, si queremos que aparesca el numero 10 tenemos\nque escribir en range el numero 11.\n\n 
        input: Sirve para las entradas que ingrese el usuario.\n 
        Ejemplo:\n 
        resultado = input('Escribe un numero aquí') 
        print(resultado) 
        resultado:\n Escribe un numero aquí\n 
        Como ves te aparecerá para que escribas un numero o texto y esto es lo que aparece despues\n 
        Escribe un numero aquí 10 
        10\n\n """)
         
        
    if opcion =="20":
        print("""                COMPREHENSION DE LISTAS\n\n 
        Manera unica de crear una lista de python rapidamente\n 
        Si te encuentras usando un ciclo for con .append() para\ncrear una lista, puedes usar una comprehension de lista en\nsu lugar\n\n 
        Con metodo .append()\n 
        mi_cadena = 'hola' 
        mi_lista = [] 
        for letras in mi_cadena: 
            mi_lista.append(letras) 
        print(mi_lista) 
        resultado:\n['h','o','l','a']\n\n 
        Con metodo comprehension de listas:\n\n 
        mi_lista = [x for x in range(0,11)] 
        print(mi_lista) 
        resultado:\n 
        [1,2,3,4,5,6,7,8,9,10]\n 
        Mucho mas rapido!!\n\n """)
         
        
    if opcion =="21":
        print("""                            FUNCIONES\n\n 
        Las funciones sirven para crear codigo limpio,ordenado y\nrepetible es muy importante para nosotros ser efectivos\nprogramando\n 
        Las funciones son un gran salto en tu carrera como\nprogramador python.\n 
        Esto significa que los problemas se pondran mas dificiles!\n\n 
        Sintaxis de funciones:\n 
        Crear funciones requiere de una sintaxis especial, empezamos con def.\n 
        veamos una funcion:\n 
        def nombre_de_funcion(nombre): 
        #corremos codigo 
                print('Las funciones retornan algo' + nombre\n\n 
        Tipicamente usamos la palabra clave return para retornar el valor de una funcion\n 
        Funcion de suma:\n 
        def suma(num1,num2): 
            return num1+num2\n\n 
        Ejemplo:\n\n 
        def decir_hola(): 
            print('Hola') 
            print('Como') 
            print('Estas') 
        decir_hola()\n 
        resultado:\n\nHola\nComo\nEstas\n\n """)
         
        
    if opcion =="22":
        print("""          EXPRESIONES LAMBDA,MAPAS Y FILTROS\n\n 
    Mapas: La funcion de mapa es muy utiñ cuando quieres llenar una funcion con una lidta de datos.\n 
    Ejemplo:\n 
    numeros = [1,2,3,4,5] 
    def raiz_cuadrada(num): 
                    resultado = num**2 
                    print(resultado) 
                    return resultado\n 
    for lista in map(raiz_cuadrada,numeros): 
                print(lista)\n 
    resultado:\n\n1\n4\n9\n16\n25\n\n 
    Filtros: Esta funcion nos ayuda a hacer filtros\n 
    Ejemplo:\n 
    numeros pares:\n 
    numeros = [1,2,3,4,5,6,7] 
    def chequear_numeros_pares(num): 
            return num % 2 == 0 
    for pares in filter(chequear_numeros_pares,numeros): 
    print(pares)\n 
    resultado:\n 
    2\n4\n6\n\n 
    Lambda: La funcion lambda se utiliza para hacer mas\nfunciones o cuando utilizamos mas funciones\n 
    Ejemplo:\n 
    raiz_cuadrada = lambda num: num**2 
    print(raiz_cuadrada(5))\n 
    resultado:\n25\n\n """)
     
    
    if opcion =="23":
        print("""            PROGRAMACION ORIENTADA A OBJETOS\n\n 
    [] Permite a los programadores crear sus propios objetos que tienen metodos y atributos.\n 
    [] Podemos llamar distintos metodos que se encuentran en una clase.\n 
    Veamos un ejemplo:\n 
    Sintaxis para metodos (class)\n 
    class nombre_clase(): 
            def __init__(self,param1,param2): 
                    self.param1 = param1 
                    self.param2 = param2 
            def otra_funcion(self): 
                    #accion 
                    print(self.param1)\n\n 
    Ejemplo:\n 
    class Perro(): 
        def __init__(self,raza,nombre,puntos): 
        self.raza = raza 
        self.nombre = nombre 
        self.puntos = puntos 
    huskie = Perro(raza='Huskie',nombre='Max',puntos=False\n\n 
    HERENCIA Y POLIMORFISMO:\n 
    class Animal(): 
        def __init__(self): 
            print('ANIMAL CRADO')\n 
        def quien_soy(self): 
            print('soy un animal')\n 
        def  comer(self): 
            print('estoy comiendo')\n\n 
        class Perro(Animal): 
            def __init__(self): 
                Animal.__init__(self): 
                    print('Perro Creado') 
            def quien_soy(self): 
                print('Soy un perro') 
    mi.Perro = Perro() 
    miperro.quien_soy()\n 
    resultado:\n 
    ANIMAL CREADO\nPerro Creado\nSoy un perro\n\n """)
         
    
    if opcion =="24":
        print("""              MODULOS Y PAQUETES\n\n 
        Modulos: Son simples archivos .py que llamamos desde otro\narchivo.\n 
        Paquetes: Son una coleccion de modulos\n 
        Crearemos nuestro propio modulo\n 
        De la clase pasada hablamos de las clases sobre el animal,\nperro lo importamos de la siguiente manera:\n 
        from clases import Animal,Perro\n 
        miPerro = Perro() 
        miPerro.quien_soy()\n 
        resultado:\nANIMAL CREADO\nPerro Creado\nSoy un perro\n\n """)
         
        
    if opcion =="25":
        print("""               __NAME___ Y '__MAIN__'\n\n 
        Cuando corremos codigo avanzado descargado del internet\nmuchas veces vemos esta linea de codigo en la parte de\nabajo.\n\n 
        if __name__=='__main___':\n 
        Cuando importamos un modulo queremos saber si las funciones usadas estan siendo usadas como import o si estas en el\narchivo original del archivo .py del modulo.\n\n 
        Exploremos esto en codigo para entenderlo mejor!:\n\n 
        Archivo uno.py\n 
        def funcion(): 
            print('funcion() en UNO.py') 
        print('Nivel Top en UNO.py')\n 
        if __name__=='__main__': 
            print('UNO.py está siendo corrido Directamente!!\n 
        if opcion == "": 
        print('UNO.py esta siendo importado!!\n\n 
        resultado:\nNivel Top en UNO.py\nUNO.py está siendo corrido directamente!!\n\n 
        Archivo dos.py\n\n 
        import uno\n 
        print('Nivel Top en Dos.py')\n 
        uno.funcion() 
        if __name__=='__main__': 
            print('Dos.py está siendo corrido directamente!!')\n 
        if opcion == "": 
        print('UNO.py está siendo importado!')\n\n 
        resultado:\n 
        Nivel Top en UNo.py\n 
        UNO.py está siendo importado!\n 
        Nivel Top en Dos.py\n 
        funcion() en UNO.py\n 
        Dos.py está siendo corrido directamente!!\n\n """)
         
    
    if opcion =="26":
        print("""               MANEJO DE ERRORES Y EXCEPCIONES\n\n 
        Podemos usar manejo de errores para poder planear posibles\ncasos de uso donde ocurra un error.\n 
        Usamos palabras claves:\n 
        Try: Esto bloquea el codigo de ser corrido.\n 
        Except: Bloque de codigo es ejecutado en caso de haber un\nerror en el bloque Try.\n 
        Finally: bloque de codigo ejecutado finalmente sin importar el error.\n\n 
        Ejemplos:\n 
        try: 
        resultado: = 10+'10'\n 
        except: 
        print('Parece que hay un error, escribe correctamente las variables')\n 
        resultado:\nParece que hay un erro, escribe correctamente las variables.\n\n """)
         
        
    if opcion=="27":
        info_contacto()
         

    if opcion == "":
        print("El tema que intentas buscar no se encuentra en el glosario!!\n\n")