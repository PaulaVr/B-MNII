#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#Biblioteca realizada por:
    #Borrás Bonilla, Esteban.
    #Cintado Puerta, Manuel.
    #Cores Hermoso, Juan Luis.
    #Valverde Romero, Paula.



import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import time as tm
import pandas as pd
from inspect import getsourcelines
from scipy.integrate import quad
from scipy.integrate import odeint

################################################## CLASE GLOBAL ############################################################

class Base_Global:
    """
    Clase con las funciones globales que usaremos en todas las clases.
    """

    def Funcion(self): 
        """
        Define la función que usaremos en los métodos.
        """
        aux = 1
        
        while aux == 1:
            
            # Nos aseguramos de que introduce un número válido.
            try:
                
                # Pedimos la función.
                h = input('Introduce la función, con variable x: ')
                print('\n')
                
                # Guardamos la cadena con la funci
                
                # Creamos la variable x como simbolo.
                x = sp.symbols('x')
                
                # Convertimos la cadena a función.
                f = sp.lambdify(x, h, "numpy")
                
                # Comprobamos que la función está bien introducida, si no al evaluarla dará error.
                f(9)
                
                # Salimos del bucle.
                aux = 0
                
                # Devolvemos la función.
                return f
                 
            # En caso de que el valor no sea válido, establece una rutina para volver a intentar o cancelar.
            except:

                r = input('La función introducida no es válida, ¿Desea volver a intentarlo? S/N: ')
                print('\n')
                  
                  
                if r.upper() == 'S':
                     
                    # Volvemos al bucle.
                    aux = 1
                    
                else:
                
                    
                    # Salimos de la función.
                    print("Operación cancelada.")
                    print('\n')
                    return None
                    
    def Tolerancia(self):
        """
        Define la tolerancia, que es pedida por teclado.
        """
        
        aux = 1
        
        while aux == 1:
            
            # Comprobamos que da un número válido.
            try:
                
                # Pedimos el número y lo convertimos a flotante.
                tol = float(input('Introduce la tolerancia, en decimales: '))
                print('\n')
                
                # Salimos del bucle.
                aux = 0
                
                # Comprobamos que la tolerancia está en el intervalo (0, 1).
                if tol < 0 or tol > 1:
                    
                    r1 = input('El valor introducido no es válido, ¿Desea volver a intentarlo? S/N: ')
                    print('\n')
                        
                    if r1.upper() == 'S':
                            
                        # Volvemos al bucle
                        aux = 1
                        
                    else:
                            
                        print("Operación cancelada.")
                        print('\n')
                        return
                
                # Sólo se almacenará el valor de la nueva tolerancia si todo está en orden.
                else:
                    
                    self.tol = tol
                    return
            
            # En caso de que el valor no sea válido, establece una rutina para volver a intentar o cancelar.
            except:
                
                r2 = input('El valor introducido no es válido, ¿Desea volver a intentarlo? S/N: ')
                print('\n')
                    
                if r2.upper() == 'S':
                      
                    # Volvemos al bucle.
                    aux = 1
                        
                else:
                        
                    # Salimos de la función.    
                    print("Operación cancelada.")
                    print('\n')
                    return
                
                
    def MaxIteraciones(self):
        """
        Define el número máximo de iteraciones, que se pide por teclado.
        """
        
        aux = 1
        
        while aux == 1:
            
            # Nos aseguramos de que introduce un número válido.
            try:
                
                # Pedimos el número y lo convertimos en entero.
                mIt = int(input('Introduce el máximo de iteraciones: '))
                print('\n')
                
                # Salimos del bucle.
                aux = 0
                
                #Si mIt es un entero negativo, establece rutina para volver a intentar o cancelar
                if (mIt <= 0):
                    
                    r1 = input('El valor introducido no es válido, ¿Desea volver a intentarlo? S/N: ')
                    print('\n')
                        
                    if r1.upper() == 'S':
                            
                        # Volvemos al bucle
                        aux = 1
                            
                    else:
                            
                        print("Operación cancelada.")
                        print('\n')
                        return
                
                # Sólo se almacenará el valor del nuevo máximo de iteraciones si todo está en orden.
                else:
                    
                    self.mIt = mIt
                    return
                    
            # En caso de que el valor no sea válido, establece una rutina para volver a intentar o cancelar.
            except:

                r2 = input('El valor introducido no es válido, ¿Desea volver a intentarlo? S/N: ')
                print('\n')
                    
                if r2.upper() == 'S':
                      
                    # Volvemos al bucle.    
                    aux = 1
                    
                else:
                        
                    # Salimos de la función.    
                    print("Operación cancelada.")
                    print('\n')
                    return
      
    
    def Intervalo(self):
        """
        Define los extremos de los intervalos, que son pedidos por teclado.
        """
        
        # Guardamos el límite inferior del intervalo actual por si se interrumpe la rutina al pedir el límite superior.
        old_a = self.a
        
        aux1 = 1
        
        while aux1 == 1:
            
            # Comprobamos que da un número válido.
            try:
                
                # Pedimos el número y lo convertimos a flotante.
                a = float(input('Introduce el límite inferior del intervalo: '))
                
                # Guardamos su valor.
                self.a = a
                
                # Salimos del bucle.
                aux1 = 0
                                
            # En caso de que el valor no sea válido, establece una rutina para volver a intentar o cancelar.
            except:
                           
                r1 = input('El límite inferior es incorrecto, ¿Desea volver a intentarlo? S/N: ')
                print('\n')
                        
                if r1.upper() == 'S':
                        
                    # Volvemos al bucle
                    aux1 = 1
                        
                else:
                          
                    # Salimos de la función.
                    print("Operación cancelada.")
                    print('\n')
                    return
                
                
        aux2 = 1
        
        while aux2 == 1:
            
            # Mismo proceso para el límite superior
            try:
                
                b = float(input('Introduce el límite superior del intervalo: '))
                print('\n')
                
                aux2 = 0
                
                # El límite superior no puede ser menor o igual que el límite inferior
                if (b <= a):
                    
                    r2 = input('El límite superior es incorrecto, ¿Desea volver a intentandolo?: S/N: ')
                    print('\n')
                    
                    if r2.upper() == 'S':
                           
                        # Volvemos al bucle.
                        aux2 = 1
                            
                    else:
                            
                        # Definimos a como su antiguo valor.    
                        self.a = old_a
                        
                        # Salimos de la función.
                        print("Operación cancelada.")
                        print('\n')
                        return
                    
                # Sólo se guardarán los nuevos límites del intervalo si son correctos
                else:
                    
                    # Guardamos el valor de b y salimos de la función.
                    self.b = b
                    return
                    
            except:
                
                        
                r3 = input('El límite superior es incorrecto, ¿Desea volver a intentarlo? S/N: ')
                print('\n')
                        
                if r3.upper() == 'S':
                        
                    # Volvemos al bucle.    
                    aux2 = 1
                        
                else:
                          
                    # Volvemos a definir a como su antiguo valor.
                    self.a = old_a
                    
                    # Salimos de la función.
                    print("Operación cancelada.")
                    print('\n')
                    return
                
            
    def ValorInicial(self):
        """
        Define el valor inicial, que se pide por teclado.
        """
        
        aux = 1
        
        while aux == 1:
            
            # Nos aseguramos de que introduce un número válido.
            try:
                
                # Pedimos el número y lo convertimos en entero.
                x0 = float(input('Introduce el valor inicial: '))
                print('\n')
                
                return x0
                
                # Salimos del bucle.
                aux = 0
                 
            # En caso de que el valor no sea válido, establece una rutina para volver a intentar o cancelar.
            except:

                r1 = input('El valor introducido no es válido, ¿Desea volver a intentarlo? S/N: ')
                print('\n')
                    
                if r1.upper() == 'S':
                      
                    # Volvemos al bucle.
                    aux = 1
                    
                else:
                       
                    # Salimos de la función.
                    print("Operación cancelada.")
                    print('\n')
                    return None
                
            
    def ValoresIniciales(self):
        """
        Define los valores iniciales, que son pedidos por teclado.
        """
        
        aux1 = 1
        
        while aux1 == 1:
            
            # Comprobamos que da un número válido.
            try:
                
                # Pedimos el número y lo convertimos a flotante.
                x1 = float(input('Introduce el primer valor inicial: '))
                x2 = float(input('Introduce el segundo valor inicial: '))
                print('\n')
                
                # Salimos del bucle.
                aux1 = 0
                
                return x1, x2
                                
            # En caso de que el valor no sea válido, establece una rutina para volver a intentar o cancelar.
            except:
                           
                r1 = input('El valor es incorrecto, ¿Desea volver a intentarlo? S/N: ')
                print('\n')
                        
                if r1.upper() == 'S':
                        
                    # Volvemos al bucle
                    aux1 = 1
                        
                else:
                           
                    # Salimos de la función.
                    print("Operación cancelada.")
                    print('\n')
                    return None, None
                    
    def Funcion_a_cadena(self):
        """
        Convierte una función en cadena de caracteres.
        """
        # Con la primera posición del array de getsourcelines sacamos la definición de la función y la convertimos a str.
        cf = str(getsourcelines(self.f)[0])
        
        # Comprobamos si la función ha sido creada con lambda.
        if cf.find('lambda') != -1:
        
            # Guardamos la posición donde se encuentra el caracter ':', después de este caracter empezará la expresión.
            p1 = cf.find(':')
            
            # Guardamos la posición donde acabará la expresión de la función.
            p2 = cf.find('\\n')
            
            # La expresión será:
            exp = cf[p1+1:p2]
            
            # Comprobamos si ha sido definida con np. o numpy.:
            s1 = str.replace(exp, 'np.', '')
            s2 = str.replace(s1, 'numpy.', '') 
            
            # Devolvemos la expresión.
            return s2
            
        # Comprobamos si la función ha sido creada con lambdify.    
        elif cf.find('lambdifygenerated') != -1:
        
            # Separamos la cadena por el caracter ',' y nos quedamos con la segunda posición.
            cf1 = cf.split(',')[1]
            
            # Guardamos la posición donde está el caracter '(', después de este comenzará la expresión.
            p1 = cf1.find('(')
            
            # Guardamos la posición donde terminará la expresión.
            p2 = cf1.find('\\n')
            
            # La expresión total es:
            exp = cf1[p1+1:p2-1]
            
            # Comprobamos si ha sido definida con np. o numpy.:
            s1 = str.replace(exp, 'np.', '')
            s2 = str.replace(s1, 'numpy.', '') 
            
            # Devolvemos la expresión.
            return s2
            
        else:
        
            # Separamos la cadena por el caracter ',' y nos quedamos con la segunda posición.
            cf1 = cf.split(',')[1]
            
            # Guardamos la posición donde están los caracteres 'return', después de estos comenzará la expresión.
            p1 = cf1.find('return')
            
            # Guardamos la posición donde terminará la expresión.
            p2 = cf1.find('\\n')
            
            # La expresión es:
            exp = cf1[p1 + 6:p2]
            
            # Comprobamos si ha sido definida con np. o numpy.:
            s1 = str.replace(exp, 'np.', '')
            s2 = str.replace(s1, 'numpy.', '') 
            
            # Devolvemos la expresión.
            return s2
    
#################################################### CLASE TEMA 1 ########################################################   

class Base_BuscaRaices(Base_Global):
    """
    Clase con las funciones generales que usaremos en la clase BuscaRaices.
    """
    
    def AuxAjustes(self,opcion):
        """
        Traduce las opciones de True o False
        """
        if opcion == True:
            cad = 'Si'
        else:
            cad = 'No'
        return(cad)
    
    def Ajustes(self):
        """
        Muestra un menu de ajustes para cambiar las configuraciones de BuscaRaices
        """
        Op = [self.raiz,self.ite,self.tim,self.er,self.verb]
        cont = True
        while cont == True:
            cont2 = True
            cad = []
            #Traducimos las opciones para crear el menu de ajustes.
            for i in Op:
                cad.append(self.AuxAjustes(opcion = i))
            #Creamos el menu de ajustes.
            try:
                print('\nAjustes Tema 1:\n')
                print('\t1. Devolver raíz: ',cad[0])
                print('\n\t2. Devolver iteraciones: ',cad[1])
                print('\n\t3. Devolver tiempo: ',cad[2])
                print('\n\t4. Devolver error del método:' ,cad[3])
                print('\n\t5. Mostrar informacion de las iteraciones:' ,cad[4])
                #Pedimos al usuario que introduzca una o varias opciones que desee cambiar y creamos una lista con dichas opciones.
                sel = input('\nSelecciona que opciones deseas cambiar o pulse 0 para acabar:\t')
                sel = sel.split(',')
                #Cambiamos las opciones seleccionadas 
                for j in sel:
                    fallo = j #Esta variable la usamos para mostrar un mensaje de error si la opcion introducida no es valida.
                    k = int(j) - 1
                    if k == -1:
                        cont = False
                    else:
                        if Op[k] == True:
                            Op[k] = False
                        else:
                            Op[k] = True
            except:
                print('\nLa opcion ',fallo,' no es valida')
                while cont2 == True:
                    aux = input('\n¿Desea continuar?\t1. Si\t2. No\t')
                    try:
                        aux = int(aux)
                        if aux == 1:
                            cont2 = False
                        elif aux == 2:
                            cont = False
                            cont2 = False
                        else:
                            print('Opción no valida')
                    except:
                        if aux.upper() == 'SI' or aux.upper() == 'YES' or aux.upper() == 'S' or aux.upper() == 'Y':
                            cont2 = False
                        elif aux.upper() == 'NO' or aux.upper() == 'N':
                            cont = False
                            cont2 = False
                        else:
                            print('Opción no valida')
        #Cambiamos las variables gobales de los ajustes.
        [self.raiz,self.ite,self.tim,self.er,self.verb] = Op
        cad = []
        #Traducimos los ajustes realizados.
        for i in Op:
            cad.append(self.AuxAjustes(i))
        #Mostramos como han quedado los ajustes al terminar y salimos de la función.
        print('\nAjustes Tema 1: \n')
        print('\t1. Devolver raiz:',cad[0])
        print('\n\t2. Devolver iteraciones:',cad[1])
        print('\n\t3. Devolver tiempo:',cad[2])
        print('\n\t4. Devolver error del método:' ,cad[3])
        print('\n\t5. Mostrar informacion de las iteraciones:' ,cad[4])
        
        return
        
    def Derivada(self):
        """
        Calcula la derivada de f.
        """
        try: 
            # Convertimos la función a cadena de caracteres.
            f = self.Funcion_a_cadena()
        
            # Definimos x como variable simbolica.
            x = sp.symbols('x')
            
            # Calculamos la derivada de la expresión.
            df = sp.diff(f, x)
            
            # Convertimos esta expresión, que es de tipo str, a función de numpy.
            df = sp.lambdify(x, df, "numpy")
            return df 
            
        except:
            
            print('No ha definido previamente la derivada de la función:')
            df = self.Funcion()
            return df

    def Bolzano(self):
        """
        Comprueba que se cumple la hipótesis del Teorema de Bolzano.
        
        Args:
            f: Función.
            
        Return:
            1: en caso de éxito ó 
            mensaje de error.
        """
        
        # En caso de no haber cambio de signo devolvemos un mensaje de error.
        if self.f(self.a) * self.f(self.b) >= 0:
            
            return(print('No es posible aplicar el método, compruebe previamente las hipótesis.'))
        
        # En caso de éxito devolverá 1.
        else:
            
            return 1
    
                    
    def Multiplicidad(self):
        aux = 1
        
        while aux == 1:
            
            # Nos aseguramos de que se introduce una primera inicialización válida.
            try:
                
                m = int(input('Introduce la multiplicidad de la raíz: '))
                print('\n')
                
                aux = 0
                
                self.m = m
                
                # Si la multiplicidad no es un natural mayor que uno, se vuelve a solicitar la introducción de m.
                if m <= 1:
                    
                    r1 = input('La multiplicidad debe ser un natural mayor que 1, ¿Desea volver a intentarlo? S/N: ')
                        
                    if r1.upper() == 'S':
                            
                        # Volvemos al bucle
                        aux1 = 1
                            
                    else:
                            
                        print("Cálculo cancelado.")
                        print('\n')
                        return
                    
                                
            # Si la primera inicialización es incorrecta, se establece rutina para volver a intentar o cancelar.
            except:
                
                        
                r2 = input('La multiplicidad debe ser un natural mayor que 1, ¿Desea volver a intentarlo? S/N: ')
                print('\n')
                        
                if r2.upper() == 'S':
                        
                    aux1 = 1
                        
                else:
                            
                    print("Cálculo cancelado.")
                    return

    def Tiempo(self, s):
        """
        Devuelve el tiempo que tarda en ejecutarse el método.
        
        Agr:
            s: Método del que desea saber el tiempo de ejecución.
            
        """
    
        # Guardamos las antiguas opciones para devolver en los métodos.
        old_raiz, old_verb, old_er, old_ite = self.raiz, self.verb, self.er, self.ite
        
        # Asignamos que devuelva solo la raíz.
        self.raiz, self.verb, self.tim, self.ite, self.er = True, False, False, False, False
        
        # Comprobamos el tiempo antes de hacer los calculos.
        start = tm.time()
            
        # Llamamos a la función 1000 veces.
        for i in range(1000):
            s()
                
        # Dejamos las opciones como estaban.
        self.raiz, self.verb, self.er, self.ite, self.tim = old_raiz, old_verb, old_er, old_ite, True
            
        # Devolvemos el tiempo el promedio de tiempo que tarda en ejecutarse la función.
        return (tm.time() - start)/1000
            
    def Error(self, s):
        """
        Devuelve la diferencia en valor absoluto entre la raíz calculada mediante el método elegido y la raíz dada por Python.
        
        Agr:
            s: Método elegido.
            
        """
    
        # Guardamos las antiguas opciones para devolver en los métodos.
        old_raiz, old_verb, old_tim, old_ite = self.raiz, self.verb, self.tim, self.ite
        
        # Asignamos que devuelva solo la raíz.
        self.raiz, self.verb, self.tim, self.ite, self.er = True, False, False, False, False
       
        # Calculamos la raíz del método elegido y la raíz dada por Python.
        raiz_s = s()
        raiz_p = self.Raiz_Python()
        
        # Dejamos las opciones como estaban.
        self.raiz, self.verb, self.tim, self.ite, self.er = old_raiz, old_verb, old_tim, old_ite, True
        
        # Devolvemos el error.
        return abs(raiz_s - raiz_p)
        
  
class BuscaRaices(Base_BuscaRaices):

    """
    Clase para la busqueda de las raíces de funciones de una variable.
    """
    
    def __init__(self, f = None, df = None, a = None, b = None, x0 = None, x1 = None, x2 = None, x = None, m = None, mIt = 100, tol = 1.e-12, raiz = True, ite = False,  tim = False, er = False, verb = False):
        """
        Inicializa las variables objeto para la busqueda de raíces de funciones de una variable.
        
        Args:
            f: Función.
            df: Derivada de la función.
            a, b: Límites del intervalo, None por defecto.
            x0: Valor inicial, para Newton, None por defecto.
            x1, x2: Valores iniciales para Secante, None por defecto.
            x: Valor inicial para Punto fijo, None por defecto.
            m: Multiplicidad del método de Newton Multiple, None por defecto
            mIt: Máximo de iteraciones, 100 por defecto.
            tol: Tolerancia, 1.e-12 por defecto.
            raiz: Variable para devolver o no la raiz del método, True por defecto.
            ite: Variable para devolver o no el número de iteraciones que realiza el método, False por defecto.
            tim: Variable para devolver o no el tiempo de ejecución del método, False por defecto.
            er: Variable para devolver o no la diferencia entre la raiz calcula por Python y la raíz dada por el método elegido, False por defecto.
            verb: Variable para imprimir o no por pantalla cada iteracción que realiza el método, False por defecto.
            
        Return:
            Mensaje de error si fallan los argumentos.
        """
        
        #Definimos los datos.
        self.f = f
        self.df = df
        
        # Primera comprobación de que los datos pueden ser incorrectos.
        if mIt <= 0 or tol < 0 or tol > 1:
            
            print("Error en los datos de entrada.")
            
        else:
            
            # Se guardarán los datos en caso de que los tipos sean los adecuados.
            try:
            
                self.mIt = int(mIt)
                self.tol = float(tol)
                
            except:
                
                print("Error en los datos de entrada.")
        
        # Comprobamos si se han introducido los límites del intervalo.
        if a == None and b == None:
            self.a = a
            self.b = b
            
        else:
            
            # Se guardarán los datos en caso de que los tipos sean los adecuados.
            try:
                
                self.a = float(a)
                self.b = float(b)
                
            except:
                print("Error en los datos de entrada.")
              
        # Comprobamos si ha introducido el valor inicial para Newton.
        if x0 == None:
            self.x0 = x0
            
        else:
            
            # Se guardarán los datos en caso de que los tipos sean los adecuados.
            try:
                
                self.x0 = float(x0)

            except:
                
                print("Error en los datos de entrada.")
                
        # Comprobamos si ha introducido el valor inicial para Punto fijo.
        if x == None:
            self.x = x
            
        else:
            
            # Se guardarán los datos en caso de que los tipos sean los adecuados.
            try:
                
                self.x = float(x)

            except:
                
                print("Error en los datos de entrada.")
                
        # Comprobamos que la multiplicidadintroducida es valida.
        if m == None:
            self.m = m
            
        else:
            
            # Se guardarán los datos en caso de que los tipos sean los adecuados.
            try:
                
                self.m = int(m)

            except:
                
                print("Error en los datos de entrada.")
 
        # Comprobamos si se han introducido los valores iniciales del método de la Secante.
        if x1 == None and x2 == None:
            self.x1 = x1
            self.x2 = x2
            
        else:
            
            # Se guardarán los datos en caso de que los tipos sean los adecuados.
            try:
                
                self.x1 = float(x1)
                self.x2 = float(x2)
                
            except:
                
                print("Error en los datos de entrada.") 
      
        # Comprobamos que las variables son válidas.
        if type(raiz) == bool and type(ite) == bool and type(tim) == bool and type(er) == bool and type(verb) == bool:
        
            self.raiz = raiz
            self.ite = ite
            self.tim = tim
            self.er = er
            self.verb = verb
            
        else: 
        
            return(print('Error en los datos de entrada'))
      

    def Biseccion(self):
        """
        Calcula una raíz de f(x) = 0 en (a, b) mediante el método de bisección.
        
        Parámetros previamente definidos:
            f: Función.
            a, b: Extremos del intervalo.
            tol: Tolerancia.
            mIt: Número máximo de iteraciones.
        
        Return:
            Según las opciones selecionadas puede devolver:
            x: Raíz calculada.
            it: Número de iteraciones realizadas.
            tim: Tiempo de ejecución del programa.
            er: Diferencia entre la raíz del método y la raíz dada por Python.
            
        """
        # Comprobamos si hay un error.
        try:
        
            # Definimos una lista donde guardaremos los resultados y una variable auxiliar.
            lista = []
            aux = 0
            
            # Comprobamos que los parámetros han sido definidos previamente, si no los definimos.
            if self.a == None or self.b == None:
                print('No ha definido previamente el intervalo:')
                self.Intervalo()
                
            if self.a == None or self.b == None:
                return
                
            if self.f == None:
                print('No ha definido previamente la función:')
                self.f = self.Funcion()
                
            if self.f == None:
                return
            
            # Creamos las variables auxiliares.
            a = self.a
            b = self.b
            f = self.f
            
            # Comprobamos la hipótesis del Teorema de Bolzano.
            if self.Bolzano() != 1:
                return
               
            # Realizar iteraciones.
            k = 0
            
            while k < self.mIt  and b-a > self.tol:
            
                # Calculamos el punto medio.
                c = (a + b)/2
            
                # Comprobamos si hemos encontrado la raíz.
                if abs(f(c)) < self.tol :
                    break
                
                # Calculamos el nuevo subintervalo e iteramos.
                if f(c) * f(a) < 0:
                    b = c
                
                else: 
                    a = c
                    
                # Si lo ha elegido devolvemos los resultados obtenidos en todas las iteraciones realizadas.    
                if self.verb == True:
                    print('k: ',k)
                    print('a_k: ', a)
                    print('b_k: ', b)
                    print('c_k: ', c)
                    print('f(a_k): ', f(a))
                    print('f(b_k): ', f(b))
                    print('f(c_k): ', f(c))
                    print('----------------------------------------')
                    
                
                # Pasamos a la siguiente iteración
                k += 1
            
            # Si lo ha elegido guardamos en la lista de devolución la raíz.
            if self.raiz == True:
                lista = lista + [c]
                aux += 1
            
            # Si lo ha elegido guardamos en la lista de devolución el número de iteraciones realizadas.
            if self.ite == True:
                lista = lista + [k]
                aux += 1
            
            # Si lo ha elegido guardamos en la lista de devolución el tiempo de ejecución.
            if self.tim == True:
                tim = self.Tiempo(self.Biseccion)
                lista = lista + [tim]
                aux += 1
                
            # Si lo ha elegido guardamos en la lista de devolución la diferencia entre la raíz y la raíz calculada por Python.    
            if self.er == True:
                er = self.Error(self.Biseccion)
                lista = lista + [er]
                aux += 1
                
            # Comprobamos cuantos parámetros se han guardado en la lista de devolución.
            # Si no se ha guardado ninguno devolvemos un mensaje.
            if aux == 0:
                return(print('Ha seleccionado no devolver nada, vuelva a Ajustes.'))
             
            # Si solo se ha guardado una variable devolvemos este valor.
            elif aux == 1:
                return lista[0]
                
            # En caso contrario devolvemos la tupla con todas las variables elegidas.
            else:
                return tuple(lista)
        
        # Si no se han definido los datos o no se han comprobado las hipótesis habrá un error y devolverá un mensaje.
        except:
            print('Puede no tener raíz, compruebe las hipótesis o defina previamente los datos.')
            
            
    def PuntoFijo(self):
        """
        Calcula un punto fijo de f partiendo de x0, que se pide por teclado.
        
        Parámetros previamente definidos:
            f: Función.
            a, b: Extremos del intervalo.
            tol: Tolerancia.
            mIt: Número máximo de iteraciones.
        
        Return:
            Según las opciones selecionadas puede devolver:
            x: Punto fijo.
            it: Número de iteraciones realizadas.
            tim: Tiempo de ejecución del programa.
        """   
        # Comprobamos si hay errores.
        try:
        
            # Definimos una lista donde guardaremos los resultados y una variable auxiliar.
            lista = []
            aux = 0
            
            # Comprobamos que los parámetros han sido definidos previamente, si no los definimos.
            if self.x == None:
                print('No ha definido previamente el valor inicial:')
                self.x = self.ValorInicial()
                
            if self.x == None:
                return
                
            if self.f == None:
                print('No ha definido previamente la función:')
                self.f = self.Funcion()
                
            if self.f == None:
                return
            
            # Creamos las variables auxiliares.
            x0 = self.x
            f = self.f
        
            # Nos aseguramos que entre en el bucle.
            error = self.tol
        
            k = 0
            while k < self.mIt and error >= self.tol:
            
                # Método de aproximaciones sucesivas.
                x = f(x0)
            
                # Preparamos la siguiente iteración.
                error = abs(x - x0)
                x0 = x
                
                # Si lo ha elegido devolvemos los resultados obtenidos en todas las iteraciones realizadas. 
                if self.verb == True:
                    print('k: ',k)
                    print('a_k: ', a)
                    print('x_k: ', c)
                    print('f(a_k): ', f(a))
                    print('Error: ', error)
                    print('----------------------------------------')
                
                
                k += 1
                
            # Si llegamos al máximo de iteraciones devolvemos un error.
            if k == self.mIt: 
                return(print('Error de convergencia.'))
            
            # Si lo ha elegido guardamos en la lista de devolución el punto fijo.
            if self.raiz == True:
                lista = lista + [x]
                aux += 1
            
            # Si lo ha elegido guardamos en la lista de devolución el número de iteraciones realizadas.
            if self.ite == True:
                lista = lista + [k]
                aux += 1
            
            # Si lo ha elegido guardamos en la lista de devolución el tiempo de ejecución.
            if self.tim == True:
                tim = self.Tiempo(self.PuntoFijo)
                lista = lista + [tim]
                aux += 1
                
            # Comprobamos cuantos parámetros se han guardado en la lista de devolución.
            # Si no se ha guardado ninguno devolvemos un mensaje.
            if aux == 0:
                return(print('Ha seleccionado no devolver nada, vuelva a Ajustes.'))
             
            # Si solo se ha guardado una variable devolvemos este valor.
            elif aux == 1:
                return lista[0]
                
            # En caso contrario devolvemos la tupla con todas las variables elegidas.
            else:
                return tuple(lista)
        
        # Si no se han definido los datos habrá un error y devolveremos un mesaje, en otra caso si no existe punto fijo de esta función.
        except:
            print("Puede no tener punto fijo, compruebe las hipótesis o defina previamente los datos.")
            
    
    def Newton(self):
        """
        Calcula una raíz de f partiendo de x0, mediante el método de Newton.
        
        Parámetros previamente definidos:
            f: Función
            x0: Valor inicial.
            tol: Tolerancia.
            mIt: Número máximo de iteraciones.
       
        Return:
            Según las opciones selecionadas puede devolver:
            x: Raíz calculada.
            it: Número de iteraciones realizadas.
            tim: Tiempo de ejecución del programa.
            er: Diferencia entre la raíz del método y la raíz dada por Python.
        """
        # Comprobamos si hay algún error.
        try:
        
            # Definimos una lista donde guardaremos los resultados y una variable auxiliar.
            lista = []
            aux = 0
            
            # Comprobamos que los parámetros han sido definidos previamente, si no los definimos.
            if self.x0 == None:
                print('No ha definido previamente el valor inicial:')
                self.x0 = self.ValorInicial()
                
            if self.x0 == None:
                return
                
            if self.f == None:
                print('No ha definido previamente la función:')
                self.f = self.Funcion()
                
            if self.f == None:
                return
                
            if self.df == None:
                self.df = self.Derivada()
                
            if self.df == None:
                return
            
            # Creamos las variables auxiliares.
            x0 = self.x0
            f = self.f
            df = self.df
      
            k = 0
        
            # Nos aseguramos de que entra en el bucle.
            error = self.tol
        
            while k < self.mIt and error >= self.tol:
            
                # Calculamos la aproximación de la raíz.
                x = x0 - f(x0)/df(x0)
            
                # Preparamos la siguiente iteración.
                error = abs(x - x0)
                x0 = x
                
                # Si lo ha elegido devolvemos los resultados obtenidos en todas las iteraciones realizadas. 
                if self.verb == True:
                    print('k: ',k)
                    print('x_k: ',x0)
                    print('f(x_k): ',f(x0))
                    print("f'(x_k): ",df(x0))
                    print('x_{k+1}: ',x)
                    print('Error: ',error)
                    print('----------------------------------------')
                
                k += 1
            
            # Si lo ha elegido guardamos en la lista de devolución la raíz.
            if self.raiz == True:
                lista = lista + [x]
                aux += 1
            
            # Si lo ha elegido guardamos en la lista de devolución el número de iteraciones realizadas.
            if self.ite == True:
                lista = lista + [k]
                aux += 1
            
            # Si lo ha elegido guardamos en la lista de devolución el tiempo de ejecución.
            if self.tim == True:
                tim = self.Tiempo(self.Newton)
                lista = lista + [tim]
                aux += 1
                
            # Si lo ha elegido guardamos en la lista de devolución la diferencia entre la raíz y la raíz calculada por Python.    
            if self.er == True:
                er = self.Error(self.Newton)
                lista = lista + [er]
                aux += 1
                
            # Comprobamos cuantos parámetros se han guardado en la lista de devolución.
            # Si no se ha guardado ninguno devolvemos un mensaje.
            if aux == 0:
                return(print('Ha seleccionado no devolver nada, vuelva a Ajustes.'))
             
            # Si solo se ha guardado una variable devolvemos este valor.
            elif aux == 1:
                return lista[0]
                
            # En caso contrario devolvemos la tupla con todas las variables elegidas.
            else:
                return tuple(lista)
        
        # Si no se han definido los datos o no se han comprobado las hipótesis habrá un error y devolveremos un mesaje.
        except:
            print('Puede no tener raíz, compruebe las hipótesis o defina previamente los datos.')
    
    
    
    def NewtonMultiple(self):
        """
        Calcula una raíz múltiple de f partiendo de x0, mediante el método de Newton.
        
        Parámetros previamente definidos:
            f: Función
            a, b: Extremos del intervalo.
            tol: Tolerancia.
            mIt: Número máximo de iteraciones.
            
        Return:
            Según las opciones selecionadas puede devolver:
            x: Raíz calculada.
            it: Número de iteraciones realizadas.
            tim: Tiempo de ejecución del programa.
            er: Diferencia entre la raíz del método y la raíz dada por Python.
        """
           
        # Comprobamos si hay algún error.
        try:
        
            # Definimos una lista donde guardaremos los resultados y una variable auxiliar.
            lista = []
            aux = 0
        
            # Comprobamos que los parámetros han sido definidos previamente, si no los definimos.
            if self.x0 == None:
                print('No ha definido previamente el valor inicial:')
                self.x0 = self.ValorInicial()
                
            if self.x0 == None:
                return
                
            if self.m == None:
                print('No ha definido previamente la multiplicidad:')
                self.Multiplicidad()
                
            if self.m == None:
                return
                
            if self.f == None:
                print('No ha definido previamente la función:')
                self.f = self.Funcion()
                
            if self.f == None:
                return
                
            if self.df == None:
                self.df = self.Derivada()
                
            if self.df == None:
                return
            
            # Creamos las variables auxiliares.
            x0 = self.x0
            m = self.m
            f = self.f
            df = self.df
            
            k = 0
        
            # Nos aseguramos de que entra en el bucle.
            error = self.tol
        
            while k < self.mIt and error >= self.tol:
            
                # Calculamos la aproximación de la raíz.
                x = x0 - m * (f(x0)/df(x0))
               
                #Al se raíz multiple si df(x)=0 se habria alcanzado la raíz.
                if df(x)==0 :
                    break
                    
                # Preparamos la siguiente iteración.    
                error = abs(x - x0)
                x0 = x
                
                # Si lo ha elegido devolvemos los resultados obtenidos en todas las iteraciones realizadas. 
                if self.verb == True:
                    print('k: ',k)
                    print('x_k: ',x0)
                    print('f(x_k): ',f(x0))
                    print("f'(x_k): ",df(x0))
                    print('x_{k+1}: ',x)
                    print('Error: ',error)
                    print('----------------------------------------')
                
                k += 1
            
            # Si lo ha elegido guardamos en la lista de devolución la raíz.
            if self.raiz == True:
                lista = lista + [x]
                aux += 1
            
            # Si lo ha elegido guardamos en la lista de devolución el número de iteraciones realizadas.
            if self.ite == True:
                lista = lista + [k]
                aux += 1
            
            # Si lo ha elegido guardamos en la lista de devolución el tiempo de ejecución.
            if self.tim == True:
                tim = self.Tiempo(self.NewtonMultiple)
                lista = lista + [tim]
                aux += 1
                
            # Si lo ha elegido guardamos en la lista de devolución la diferencia entre la raíz y la raíz calculada por Python.    
            if self.er == True:
                er = self.Error(self.NewtonMultiple)
                lista = lista + [er]
                aux += 1
                
            # Comprobamos cuantos parámetros se han guardado en la lista de devolución.
            # Si no se ha guardado ninguno devolvemos un mensaje.
            if aux == 0:
                return(print('Ha seleccionado no devolver nada, vuelva a Ajustes.'))
             
            # Si solo se ha guardado una variable devolvemos este valor.
            elif aux == 1:
                return lista[0]
                
            # En caso contrario devolvemos la tupla con todas las variables elegidas.
            else:
                return tuple(lista)
        
        # Si no se han definido los datos o no se han comprobado las hipótesis habrá un error y devolveremos un mesaje.
        except:
            print('Puede no tener raíz, compruebe las hipótesis o defina previamente los datos.')
    
    
    def Secante(self):
        """
        Calcula una raíz de f partiendo de x0 y x1, mediante el método de la secante.
        
        Parámetros previamente definidos:
            f: Función.
            x0, x1: Valores iniciales.
            tol: Tolerancia.
            mIt: Número máximo de iteraciones.
        
        Return:
            Según las opciones selecionadas puede devolver:
            x: Raíz calculada.
            it: Número de iteraciones realizadas.
            tim: Tiempo de ejecución del programa.
            er: Diferencia entre la raíz del método y la raíz dada por Python.
        """
        # Comprobamos si hay algún error.
        try:
        
            # Definimos una lista donde guardaremos los resultados y una variable auxiliar.
            lista = []
            aux = 0
        
            # Comprobamos que los parámetros han sido definidos previamente, si no los definimos.
            if self.x1 == None or self.x2 == None:
                print('No ha definido previamente los valores iniciales:')
                self.x1, self.x2 = self.ValoresIniciales()
                
            if self.x1 == None or self.x2 == None:
                return
                
            if self.f == None:
                print('No ha definido previamente la función:')
                self.f = self.Funcion()
                
            if self.f == None:
                return
            
            # Creamos las variables auxiliares.
            x1 = self.x1
            x2 = self.x2
            f = self.f
        
            k = 0
        
            # Nos aseguramos de que entra en el bucle.
            error = self.tol
        
            while k < self.mIt and error >= self.tol:
            
                # Calculamos la intersección.
                x = x2 - f(x2)*((x2 - x1)/(f(x2) - f(x1)))
            
                # Preparamos la siguiente iteración.
                error = abs(x - x2)
                x1 = x2
                x2 = x
                
                # Si lo ha elegido devolvemos los resultados obtenidos en todas las iteraciones realizadas. 
                if self.verb == True:
                    print('k: ',k)
                    print('x_{k-1}: ',x1)
                    print('x_k: ',x2)
                    print("f(x_{k-1}): ",f(x1))
                    print("f(x_k): ",f(x2))
                    print('x_{k+1}: ',x)
                    print('Error: ', error)
                    print('----------------------------------------')
                
                k += 1
            
            # Si lo ha elegido guardamos en la lista de devolución la raíz.
            if self.raiz == True:
                lista = lista + [x]
                aux += 1
            
            # Si lo ha elegido guardamos en la lista de devolución el número de iteraciones realizadas.
            if self.ite == True:
                lista = lista + [k]
                aux += 1
            
            # Si lo ha elegido guardamos en la lista de devolución el tiempo de ejecución.
            if self.tim == True:
                tim = self.Tiempo(self.Secante)
                lista = lista + [tim]
                aux += 1
                
            # Si lo ha elegido guardamos en la lista de devolución la diferencia entre la raíz y la raíz calculada por Python.    
            if self.er == True:
                er = self.Error(self.Secante)
                lista = lista + [er]
                aux += 1
                
            # Comprobamos cuantos parámetros se han guardado en la lista de devolución.
            # Si no se ha guardado ninguno devolvemos un mensaje.
            if aux == 0:
                return(print('Ha seleccionado no devolver nada, vuelva a Ajustes.'))
             
            # Si solo se ha guardado una variable devolvemos este valor.
            elif aux == 1:
                return lista[0]
                
            # En caso contrario devolvemos la tupla con todas las variables elegidas.
            else:
                return tuple(lista)
        
        # Si no se han definido los datos o no se han comprobado las hipótesis habrá un error y devolveremos un mesaje.
        except:
            print('Puede no tener raíz, compruebe las hipótesis o defina previamente los datos.')
    
    
    def RegulaFalsi(self):
        """
        Calcula una raíz de f en (a, b), mediante el método de Regula falsi.
        
        Parámetros previamente definidos:
            f: Función.
            a, b: Extremos del intervalo.
            tol: Tolerancia.
            mIt: Número máximo de iteraciones.
        
        Return:
            Según las opciones selecionadas puede devolver:
            x: Raíz calculada.
            it: Número de iteraciones realizadas.
            tim: Tiempo de ejecución del programa.
            er: Diferencia entre la raíz del método y la raíz dada por Python.
        """
        
        # Comprobamos si hay algún error.
        try:
        
            # Definimos una lista donde guardaremos los resultados y una variable auxiliar.
            lista = []
            aux = 0
            
            # Comprobamos que los parámetros han sido definidos previamente, si no los definimos.
            if self.a == None or self.b == None:
                print('No ha definido previamente el intervalo:')
                self.Intervalo()
                
            if self.a == None or self.b == None:
                return
                
            if self.f == None:
                print('No ha definido previamente la función:')
                self.f = self.Funcion()
                
            if self.f == None:
                return
            
            # Creamos las variables auxiliares para a y b.
            a = self.a
            b = self.b
            f = self.f
            
            # Comprobamos la hipótesis del Teorema de Bolzano.
            
            if self.Bolzano() != 1 :
                
                return
        
            k = 0
        
            while k < self.mIt  and b-a > self.tol:
            
                # Calculamos la intersección.
                c = ((f(b) * a) - (f(a) * b))/(f(b) - f(a))
                
                # Comprobamos si c esta en el intervalo de definición
                if c < a or c > b:
                    return(print('Error al aplicar el metodo compruebe las hipotesis'))
            
                # Comprobamos si hemos encontrado la raíz.
                if abs(f(c)) < self.tol :
                    break
                
                # Calculamos el nuevo subintervalo e iteramos.
                if f(c) * f(a) < 0:
                    b = c
                else: 
                    a = c
                
                # Si lo ha elegido devolvemos los resultados obtenidos en todas las iteraciones realizadas. 
                if self.verb == True:
                    print('k: ',k)
                    print('a_k: ', a)
                    print('b_k: ', b)
                    print('c_k: ', c)
                    print('f(a_k): ', f(a))
                    print('f(b_k): ', f(b))
                    print('f(c_k): ', f(c))
                    print('----------------------------------------')
                
                k += 1
            
            # Si lo ha elegido guardamos en la lista de devolución la raíz.
            if self.raiz == True:
                lista = lista + [c]
                aux += 1
            
            # Si lo ha elegido guardamos en la lista de devolución el número de iteraciones realizadas.
            if self.ite == True:
                lista = lista + [k]
                aux += 1
            
            # Si lo ha elegido guardamos en la lista de devolución el tiempo de ejecución.
            if self.tim == True:
                tim = self.Tiempo(self.RegulaFalsi)
                lista = lista + [tim]
                aux += 1
                
            # Si lo ha elegido guardamos en la lista de devolución la diferencia entre la raíz y la raíz calculada por Python.    
            if self.er == True:
                er = self.Error(self.RegulaFalsi)
                lista = lista + [er]
                aux += 1
                
            # Comprobamos cuantos parámetros se han guardado en la lista de devolución.
            # Si no se ha guardado ninguno devolvemos un mensaje.
            if aux == 0:
                return(print('Ha seleccionado no devolver nada, vuelva a Ajustes.'))
             
            # Si solo se ha guardado una variable devolvemos este valor.
            elif aux == 1:
                return lista[0]
                
            # En caso contrario devolvemos la tupla con todas las variables elegidas.
            else:
                return tuple(lista)
        
        # Si no se han definido los datos o no se han comprobado las hipotesis habrá un error y devolveremos un mesaje.
        except:
            print('Puede no tener raíz, compruebe las hipótesis o defina previamente los datos.')
             
    def Raiz_Python(self):
        """
        Calcula la raiz de la función a traves del módulo sympy de Python.
        Solo funcionará si se ha introducido una función definida como np. o numpy. o introducida por teclado.
        """
        
        # Comprobamos que los parámetros han sido definidos previamente, si no los definimos.
        if self.a == None or self.b == None:
            print('No ha definido previamente el intervalo:')
            self.Intervalo()
            
        if self.a == None or self.b == None:
                print('Método cancelado.')
                return
                
        if self.f == None:
            print('No ha definido previamente la función:')
            self.Funcion()
            
        if self.f == None:
                print('Método cancelado.')
                return
            
        # Creamos las variables auxiliares.
        a = self.a
        b = self.b
        
        # Pasamos la función a cadena de caracteres.
        g = self.Funcion_a_cadena()
        
        # Resolvemos la función mediante la expresión.
        aux = sp.solve(g)
        
        # Sacamos la forma numerica de las raíces y luego las tranformamos a complejo.
        sol = [complex(x.evalf()) for x in aux]
        
        # Creamos una lista.
        s = []
        
        # Comprobamos de que tipo son las raíces y las guardamos.
        # Comprobamos que la raíz esté en el intervalo.
        for i in range(len(sol)):
        
            # Nos quedamos con su parte real.
            s.append(sol[i].real)
                
            # Buscamos la raíz que esté en el intervalo.
            if s[i] < b and s[i] > a:
                return s[i]
            
        # Si no hay ninguna raíz contenida en el intervalo devolvemos un mensaje.
        return(print('No hay ninguna raíz en el intervalo dado.'))
    
#################################################### CLASE TEMA 2 ###################################################
    
class Base_Interpolacion(Base_Global):
    """
    Clase con las funciones generales que usaremos en la clase Interpolacion.
    """
    
    #sp.init_printing()
    
    def AuxAjustes(self, opcion):
        """
        Traduce las opciones de True o False
        """
        if opcion == True:
            cad = 'Si'
        else:
            cad = 'No'
        return(cad)
    
    def Ajustes(self):
        """
        Muestra un menu de ajustes para cambiar las configuraciones de BuscaRaices
        """
        Op = [self.expresion,self.tim]
        cont = True
        while cont == True:
            cont2 = True
            cad = []
            
            # Traducimos las opciones para crear el menu de ajustes.
            for i in Op:
                cad.append(self.AuxAjustes(opcion = i))
                
            # Creamos el menu de ajustes.
            try:
                print('\nAjustes Tema 2:\n')
                print('\t1. Devolver la expresión del polinomio de interpolación: ',cad[0])
                print('\n\t2. Devolver el tiempo: ',cad[1])
                
                # Pedimos al usuario que introduzca una o varias opciones que desee cambiar y creamos una lista con dichas opciones.
                sel = input('\nSelecciona que opciones deseas cambiar o pulse 0 para acabar:\t')
                sel = sel.split(',')
                
                # Cambiamos las opciones seleccionadas 
                for j in sel:
                    fallo = j # Esta variable la usamos para mostrar un mensaje de error si la opcion introducida no es valida.
                    k = int(j) - 1
                    if k == -1:
                        cont = False
                    else:
                        if Op[k] == True:
                            Op[k] = False
                        else:
                            Op[k] = True
            except:
                print('\nLa opcion ',fallo,' no es valida')
                while cont2 == True:
                    aux = input('\n¿Desea continuar?\t1. Si\t2. No\t')
                    try:
                        aux = int(aux)
                        if aux == 1:
                            cont2 = False
                        elif aux == 2:
                            cont = False
                            cont2 = False
                        else:
                            print('Opción no valida')
                    except:
                        if aux.upper() == 'SI' or aux.upper() == 'YES' or aux.upper() == 'S' or aux.upper() == 'Y':
                            cont2 = False
                        elif aux.upper() == 'NO' or aux.upper() == 'N':
                            cont = False
                            cont2 = False
                        else:
                            print('Opción no valida')
                            
        # Cambiamos las variables gobales de los ajustes.
        [self.expresion,self.tim] = Op
        cad = []
        
        # Traducimos los ajustes realizados.
        for i in Op:
            cad.append(self.AuxAjustes(i))
            
        # Mostramos como han quedado los ajustes al terminar y salimos de la función.
        print('\nAjustes Tema 2: \n')
        print('\t1. Devolver la expresión del polinomio de interpolación: ',cad[0])
        print('\n\t2. Devolver el tiempo: ',cad[1])
        
        return

    def Diferencias(self, i, j):
        """
        Calcula las diferencias acumuladas del interpolador de Newton
        
        arg:
            X = Conjunto de nodos
            Y = Conjunto de valores
            i = Posicion de los nodos y valores de la diferencia
            j = Posicion de los nodos y valores
        """
        
        # En caso de que i sea igual a j devuelve el valor del nodo x_i.
        if i == j:
            
            return(self.Y[i])
        
        # En caso contrario calcula la diferencia por recursividad.
        else:
            
            return (self.Diferencias(i+1, j) - self.Diferencias(i, j-1))/(self.X[j]-self.X[i])
    
                    

    def Tiempo(self, s):
        """
        Devuelve el tiempo que tarda en ejecutarse el método.
        
        Agr:
            s: Método del que desea saber el tiempo de ejecución.
            
        """
    
        # Guardamos las antiguas opciones para devolver en los métodos.
        old_expresion, old_tim = self.expresion, self.tim
        
        # Dejamos que solo muestre la expresion
        self.expresion, self.tim = True, False
        
        # Comprobamos el tiempo antes de hacer los calculos.
        start = tm.time()
            
        # Llamamos a la función 100 veces.
        for i in range(100):
            s()
                
        # Dejamos las opciones como estaban.
        self.expresion, self.tim = old_expresion, True
            
        # Devolvemos el tiempo el promedio de tiempo que tarda en ejecutarse la función.
        return (tm.time() - start)/100
    
    def Factorial(self, n):
        # Calculamos el factorial de un numero.
        factor = 1
        while n > 0:
            factor = factor*n
            n = n - 1
        return(factor)
    
    def Nodos(self):
        """
        Calcula los nodos de interpolación.
        
        arg:
            n: Grado del polinomio de interpolación deseado.
            a, b: Extremos del intervalo.
        """
        
        if self.a == None or self.b == None:
            print('Para crear los nodos necesitamos un intervalo.')
            self.Intervalo()
        
        if self.a == None or self.b == None:
            return
        
        if self.n == None:
            cont = True
            
            while cont == True:
                cont2 = True
                try:
                    n = int(input('Introduzca el numero de nodos deseados: '))
                    self.n = n
                    cont = False
                except:
                    print('Valor no valido')
                    
                    while cont2 == True:
                        cad = input('¿Desea continuar?\t 1. Si\t2. No')
                        try:
                            cad = int(cad)
                            if cad == 1:
                                cont2 = False
                                
                            elif cad == 2:
                                cont = False
                                cont2 = False
                                self.n = None
                            else:
                                print('Opcion no valida.')
                        except:
                            print('Opcion no valida introduzca el numero correspondiente a la opción deseada')
            

        
        if self.n == None:
            print('Operación cancelada')
            return
        
        a = self.a
        b = self.b 
        
        nodos = np.linspace(a, b, self.n)
        self.X = nodos
        
    def Valores(self):
        """
        Calcula el conjunto de valores que se usan para interpolar.
        
        arg:
            X: Nodos.
            f: Función que deseas interpolar.
        """
        if type(self.X) == type(None):
            print('Para crear valores es necesario los nodos')
            self.Nodos()
            
        if type(self.X) == type(None):
            return
            
        if self.f == None:
            print('Para crear valores es necesario una funcion')
            self.f = self.Funcion()
            
        if self.f == None:
            return
        
        Y = []
        for i in self.X:
            Y.append(self.f(i))
        
        self.Y = Y
    
class Interpolacion(Base_Interpolacion):

    """
    Clase para interpolacion de funciones de una variable.
    """
    
    def __init__(self, f = None, dnf = None, a = None, b = None, X = None, Y = None,n = None,expresion = True,  tim = False):
        """
        Inicializa las variables objeto para la busqueda de raíces de funciones de una variable.
        
        Args:
            f: Función, None por defecto.
            dnf: Derivada n-ésima de la función f, None por defecto.
            a, b: Límites del intervalo, None por defecto.
            X: Conjunto de nodos, None por defecto.
            Y: Conjunto de valores, None por defecto.
            n: Grado del polinomio de interpolación en caso de no tener X e Y, None por defecto
           expresion: Variable para devolver o no la expresion del polinomio de interpolacion, True por defecto.
            tim: Variable para devolver o no el tiempo de calculo del polinomio, False por defecto.
        Return:
            Mensaje de error si fallan los argumentos.
        """
        # Definimos los datos
        self.f = f
        self.dnf = dnf
        
        # Comprobamos si se han introducido los límites del intervalo.
        if a == None and b == None:
            self.a = a
            self.b = b
            
        else:
            
            # Se guardarán los datos en caso de que los tipos sean los adecuados.
            try:
                
                self.a = float(a)
                self.b = float(b)
                
            except:
                print("Error en los datos de entrada.")
                
        # Comprobamos si se han introducido Nodos y Valores.        
        if type(X) == type(None) and type(Y) == type(None):
            self.X = X
            self.Y = Y
        
        elif type(X) == type(np.array([])) and type(Y) == type(np.array([])):
            
            # Se guardan los datos en el caso de que los tipos sean adecuados y el rango de Nodos y Valores sea el mismo

            auxX = []
            auxY = []
            try:
                if len(X) != len(Y):
                    print('Error en los datos de entrada')
                else:    
                    for i in X:
                        auxX.append(float(i))
                    for j in Y:
                        auxY.append(float(j))
                    self.X = auxX
                    self.Y = auxY
            except:
                print('Error en los datos de entrada')
        else:
            print('Error en los datos de entrada')
        
        # Comprobamos si el usuario ha introducido grado de interpolación
        if n == None:
            
            # Si el usuario ha introducido nodos asignamos el rango de los nodos a n.
            try:
                self.n = len(self.X)
            except:
                self.n = n
            
        elif n != None and type(self.X) != type(None):
            # Se guarda el grado en el caso de que sean adecuados.
            try:
                n = int(n)
                if n == len(self.X):
                    self.n = n
                else:
                    print('Error en los datos de entrada')
            except:
                print('Error en los datos de entrada')
        
        else:
            # Se guarda en el caso de que sea adecuado.
            try:
                self.n = int(n)
            except:
                print('Error en los datos de entrada')
            
            
        # Define de manera global las variables de ajustes.
        if type(expresion) == bool and type(tim) == bool:
            self.expresion = expresion
            self.tim = tim
        
        else:
            print('Error de inicialización, las variables expresion y tim deben ser True o False')
            return
        

    def InterLagrange(self):
        """
        Calcula el polinomio de interpolación de Lagrange.
        
        Parámetros previamente definidos:
            X: Nodos.
            Y: Valores.
        Return:
            Según las opciones selecionadas puede devolver:
            expresion: La expresion del polinomio de interpolación.
            time: Tiempo que tarda en calcular el polinomio.
        """
        
        if type(self.X) == type(None):
            self.Nodos()
            
        if type(self.X) == type(None):
            return
            
        if type(self.Y) == type(None):
            self.Valores()
        
        if type(self.Y) == type(None):
            return        
        
        if self.f != None:
            for i in range(len(self.X)):
                if self.f(self.X[i]) != self.Y[i]:
                    print('Los valores dados no corresponden a valores de la función en los nodos')
                    return
        
        if self.a == None or self.b == None:
            self.a = self.X[0]
            self.b = self.X[-1]
        
        cont = True
        #Comprueba si el usuario a pedido que la funcion devuelva la expresion.
        if self.expresion == True:
            x = sp.symbols('x')
        else:
            while cont == True:
                cont2 = True
                try:
                    #Si el usuario no ha pedido que se devuelva la expresion le pide en que valor desea calcular el polinomio.
                    x = input('introduce el valor de x que desea calcular:\t')
                    x = float(x)
                    #Comprueba si el x seleccionado esta bien definido.
                    if x < self.a or x > self.b:
                        int('x')
                    else:
                        cont = False
                except:
                    print('El valor de x no es valido')
                    while cont2 == True:
                        cad = input('¿Desea continuar?\t1. Si\t2. No\t')
                        try:
                            cad = int(cad)
                            if cad != 1 and cad != 2:
                                print('Opcion no valida')
                            elif cad == 2:
                                return
                            else:
                                cont2 = False
                        except:
                            if cad.upper() == 'S' or cad.upper() == 'SI':
                                cont2 = False
                            elif cad.upper() == 'N' or cad.upper() == 'NO':
                                return
                            else:
                                print('Opcion no valida')
        
        #Calcula el polinomio de interpolación de Lagrange ya sea su expresión o el valor en el x seleccionado.
        l = len(self.X)
        sol = 0
        for i in range(l):
            inter = 1
            for j in range(l):
                if j == i:
                    inter = inter
                else:
                    inter = inter*(x-self.X[j])/(self.X[i]-self.X[j])
            sol = sol + self.Y[i]*inter
        lista = []
        lista.append(sp.expand(sol))
        

        #Si el usuario ha pedido que devuelva el tiempo lo calcula
        if self.tim == True:
            t = self.Tiempo(self.InterLagrange)
            lista.append(t)
        return(lista)

            
    def InterNewton(self):
        """
        Calcula el polinomio de interpolación de Newton.
        
        Parámetros previamente definidos:
            X: Nodos.
            Y: Valores.
        
        Return:
            Según las opciones selecionadas puede devolver:
            expresion: La expresion del polinomio de Newton.
            time: Tiempo de ejecución del programa.
        """  
        
        if type(self.X) == type(None):
            self.Nodos()
            
        if type(self.X) == type(None):
            return
        
        if type(self.Y) == type(None):
            self.Valores()
            
        if type(self.Y) == type(None):
            return
        
        if self.f != None:
            for i in range(len(self.X)):
                if self.f(self.X[i]) != self.Y[i]:
                    print('Los valores dados no corresponden a valores de la función en los nodos')
                    return            
            
        if self.a == None or self.b == None:
            self.a = self.X[0]
            self.b = self.X[-1]
            
        
        cont = True
        #Comprueba si el usuario a pedido que la funcion devuelva la expresion.
        if self.expresion == True:
            x = sp.symbols('x')
        else:
            while cont == True:
                cont2 = True
                try:
                    #Si el usuario no ha pedido que se devuelva la expresion le pide en que valor desea calcular el polinomio.
                    x = input('introduce el valor de x que desea calcular:\t')
                    x = float(x)
                    #Comprueba si el x seleccionado esta bien definido.
                    if x < self.a or x > self.b:
                        int('x')
                    else:
                        cont = False
                except:
                    print('El valor de x no es valido')
                    while cont2 == True:
                        cad = input('¿Desea continuar?\t1. Si\t2. No\t')
                        try:
                            cad = int(cad)
                            if cad != 1 and cad != 2:
                                print('Opcion no valida')
                            elif cad == 2:
                                return
                            else:
                                cont2 = False
                        except:
                            if cad.upper() == 'S' or cad.upper() == 'SI':
                                cont2 = False
                            elif cad.upper() == 'N' or cad.upper() == 'NO':
                                return
                            else:
                                print('Opcion no valida')  
        # Calcula el polinomio de interpolación de Newton ya sea su expresión o el valor en el x seleccionado.                        
        n = len(self.X)
        suma = self.Y[0]
        for i in range(1,n):
            producto = 1
            for j in range(i):
                producto = producto*(x - self.X[j])
            suma = suma + self.Diferencias(0,i)*producto
        lista = []
        lista.append(sp.expand(suma))
        

        #Si el usuario ha pedido que devuelva el tiempo lo calcula
        if self.tim == True:
            t = self.Tiempo(self.InterNewton)
            lista.append(t)
        return(lista)
    
    def SplineLineal(self):
        """
        Calcula el polinomio de interpolación mediante Spline Linal.
        
        Parámetros previamente definidos:
            X: Nodos.
            Y: Valores.
        Return:
            Según las opciones selecionadas puede devolver:
            expresion: Devuelve la expresión del Spline Lineal.
            time: Tiempo de ejecución del programa.
        """
        
        if type(self.X) == type(None):
            self.Nodos()
            
        if type(self.X) == type(None):
            return            
            
        if type(self.Y) == type(None):
            self.Valores()
            
        if type(self.Y) == type(None):
            return
            
        if self.f != None:
            for i in range(len(self.X)):
                if self.f(self.X[i]) != self.Y[i]:
                    print('Los valores dados no corresponden a valores de la función en los nodos')
                    return
        
        if self.a == None or self.b == None:
            self.a = self.X[0]
            self.b = self.X[-1]
        
        l = len(self.X)
        sol = 0
        cont = True
        # Si el usuario ha pedido que se devuelva la expresión, la calcula.
        if self.expresion == True:
            x = sp.symbols('x')
            lista = []
            for i in range(l-1):
                sol = self.Y[i] + (self.Y[i+1] - self.Y[i])*(x-self.X[i])/(self.X[i+1] - self.X[i])
                sol = sp.expand(sol)
                lista.append(sol)
            # Devuelve el tiempo en el caso de que el usuario lo haya pedido.
            if self.tim == True:
                t = self.Tiempo(self.SplineLineal)
                lista.append(t)
            return(lista)
        else:
            while cont == True:
                cont2 = True
                try:
                    #Si el usuario no ha pedido que se devuelva la expresion le pide en que valor desea calcular el polinomio.
                    x = input('introduce el valor de x que desea calcular:\t')
                    x = float(x)
                    #Comprueba si el x seleccionado esta bien definido.
                    if x < self.a or x > self.b:
                        int('x')
                    else:
                        cont = False
                except:
                    print('El valor de x no es valido')
                    while cont2 == True:
                        cad = input('¿Desea continuar?\t1. Si\t2. No\t')
                        try:
                            cad = int(cad)
                            if cad != 1 and cad != 2:
                                print('Opcion no valida')
                            elif cad == 2:
                                return
                            else:
                                cont2 = False
                        except:
                            if cad.upper() == 'S' or cad.upper() == 'SI':
                                cont2 = False
                            elif cad.upper() == 'N' or cad.upper() == 'NO':
                                return
                            else:
                                print('Opcion no valida')
            # Calcula el valor del polinomio de interpolación por Spline Lineal en el x seleccionado.                    
            for i in range(l-1):
                if x < self.X[i] or x > self.X[i+1]:
                    sol = [sol]
                else:
                    sol = [self.Y[i] + (self.Y[i+1] - self.Y[i])*(x-self.X[i])/(self.X[i+1] - self.X[i])]
                    if self.tim == True:
                        t = self.Tiempo(self.SplineLineal)
                        sol.append(t)
                    return(sol)
                
    def SplineCubico(self):
        """
        Calcula el polinomio de interpolación mediante Spline Cúbico.
        
        Parámetros previamente definidos:
            f: Función
            X: Nodos.
            Y: Valores.
            
        Return:
            Según las opciones selecionadas puede devolver:
            expresión: Devuelve la expresión del Spline Cúbico
            tim: Tiempo de ejecución del programa.
        """
        
        if type(self.X) == type(None):
            self.Nodos()
            
        if type(self.X) == type(None):
            return
            
        if type(self.Y) == type(None):
            self.Valores()
            
        if type(self.Y) == type(None):
            return
            
        if self.f != None:
            for i in range(len(self.X)):
                if self.f(self.X[i]) != self.Y[i]:
                    print('Los valores dados no corresponden a valores de la función en sus respectivos nodos')
                    return
        
        n = len(self.X)
        nec = n - 1
        lista = []
        
        # Creo las variables:
        x = sp.symbols('x')
        a = sp.symbols('a0:%d'%nec)
        b = sp.symbols('b0:%d'%nec)
        c = sp.symbols('c0:%d'%nec)
        d = sp.symbols('d0:%d'%nec)
    
        # Creo los polinomios:
        s = [a[i] + b[i] * (x - self.X[i]) + c[i] * (x-self.X[i])**2 + d[i] * (x - self.X[i])**3 for i in range (nec)]
    
        # Creamos las derivadas primeras:
        ds = [b[i] + 2 * c[i] * (x - self.X[i]) + 3 * d[i] * (x-self.X[i])**2 for i in range(nec)]
    
        # Creamos las derivadas segundas:
        dds = [2 * c[i] + 6 * d[i] * (x - self.X[i]) for i in range(nec)]
    
        # Vamos a crear las ecuaciones:
        # Interpolación:
        ec_interp = [s[i].subs(x, self.X[i]) - self.Y[i] for i in range(nec)] + [s[-1].subs(x, self.X[-1]) - self.Y[-1]]
    
        # Continuidad de s:
        ec_cont_s = [s[i].subs(x, self.X[i+1]) - s[i+1].subs(x, self.X[i+1]) for i in range(nec-1)]
    
        # Continuidad de ds:
        ec_cont_ds = [ds[i].subs(x, self.X[i+1]) - ds[i+1].subs(x, self.X[i+1]) for i in range(nec-1)]
    
        # Continuidad de dds:
        ec_cont_dds = [dds[i].subs(x, self.X[i+1]) - dds[i+1].subs(x, self.X[i+1]) for i in range(nec-1)]
    
       # Ecuación natural:
        ec_nat = [dds[0].subs(x,self.X[0]),dds[-1].subs(x,self.X[-1])]
    
        # Unimos todo:
        var = a + b+ c + d
        ec = ec_interp + ec_cont_s + ec_cont_ds + ec_cont_dds + ec_nat
    
        # Resolvemos el problema:
        sol = sp.solve(ec, var)
        
        lista = [s[i].subs(sol) for i in range(nec)]
        

        #Si el usuario ha pedido que devuelva el tiempo lo calcula
        if self.tim == True:
            t = self.Tiempo(self.SplineCubico)
            lista.append(t)
        return(lista)        

    def ErrorInter(self):
        """
        Devuelve la diferencia en valor absoluto entre la raíz calculada mediante el método elegido y la raíz dada por Python.
        
        Agr:
            f: Función a la cual se le ha aplicado el polinomio de interpolación.
            dnf: Derivada n-ésima de la función.
            X: Nodos.
            
        """
        # Comprobamos que esten definidos los datos necesarios.
        
        if type(self.X) == type(None):
            print('No se ha definido los nodos')
            self.Nodos()
            
        if type(self.X) == type(None):
            return

        if self.dnf == None:
            print('No es posible calcular el error defina la derivada n-ésima de la función en los datos de entrada')
            return
            
        
        # Calculamos el error.
        else:
            n = len(self.X)
            aux = np.linspace(self.X[0],self.X[-1],1000)
            # Calculamos el maximo en valor absoluto de la derivada n-ésima
            maximo = abs(self.dnf(self.X[0]))
            for i in aux:
                if abs(self.dnf(i)) > maximo:
                    maximo = abs(self.dnf(i))
            # Calcula la cota del error de interpolación.
            error = (maximo*(self.b-self.a)**(n))/self.Factorial(n)

        return(error)
####################################################### CLASE TEMA 3 ################################################## 
    
class Base_Cuadratura(Base_Global):
    
    
    def Cnuma(self):
        
        '''
        Permite defifinir el parámetro numa
        
        '''
        
        aux = 1
        
        while aux == 1:
            
            # Nos aseguramos de que introduce un número válido.
            try:
                
                # Pedimos el número de nodos y lo convertimos en entero.
                 
                    num = int(input('Introduce entre 1 y 5 el número de nodos para el que desea realizar la fórmula de cuadratura: '))
                    print('\n')
                
                    # Salimos del bucle.
                    aux = 0

                    #Si num no es uno de los valores previstos, establece rutina para volver a intentar o cancelar
                    if num < 1 or num > 5:

                        r1 = input('El valor introducido no es válido, ¿Desea volver a intentarlo? S/N: ')
                        print('\n')

                        if r1.upper() == 'S':

                            # Volvemos al bucle
                            aux = 1

                        else:

                            print("Operación cancelada.")
                            print('\n')
                            return
                    
                    #Asigno a numa el valor introducido por el usuario si todo se encuentra en orden.
                    self.numa = num
                    
            except:
                
                r1 = input('El valor introducido no es válido, ¿Desea volver a intentarlo? S/N: ')
                print('\n')

                if r1.upper() == 'S':

                    # Volvemos al bucle
                    aux = 1

                else:

                    print("Operación cancelada.")
                    print('\n')
                    return
                
    def Cnumb(self):
        
        '''
        Permite defifinir el parámetro numb
        
        '''
        
        aux = 1
        
        while aux == 1:
            
            # Nos aseguramos de que introduce un número válido.
            try:
                
                # Pedimos el número de nodos y lo convertimos en entero.
                 
                    num = int(input('Introduce entre 2 y 6 el número de nodos para el que desea realizar la fórmula de cuadratura: '))
                    print('\n')
                
                    # Salimos del bucle.
                    aux = 0

                    #Si num no es uno de los valores previstos, establece rutina para volver a intentar o cancelar
                    if num < 2 or num > 6:

                        r1 = input('El valor introducido no es válido, ¿Desea volver a intentarlo? S/N: ')
                        print('\n')

                        if r1.upper() == 'S':

                            # Volvemos al bucle
                            aux = 1

                        else:

                            print("Operación cancelada.")
                            print('\n')
                            return
                        
                    #Asigno a numb el valor introducido por el usuario si todo se encuentra en orden.
                    self.numb = num
                    
            except:
                
                r1 = input('El valor introducido no es válido, ¿Desea volver a intentarlo? S/N: ')
                print('\n')

                if r1.upper() == 'S':

                    # Volvemos al bucle
                    aux = 1

                else:

                    print("Operación cancelada.")
                    print('\n')
                    return
    
    
    
    
    
    def CNodos(self, formula = None):
        
        '''
        Realiza el cálculo de nodos para las fórmulas de cuadraturas abiertas y cerradas de Newton - Côtes.
        
        '''
            
            #Cálculo de nodos para cuadratura abierta
            
        if formula == 'abierta':
                        
            lista = []
            h = (self.b - self.a)/(self.numa + 2)
            i = 0

            while i != self.numa:

                i += 1
                lista = lista + [self.a + i*h]

            return lista
            
        #Cálculo de nodos para cuadratura cerrada.
                    
        if formula == 'cerrada':
                    
            lista = []
            h = (self.b - self.a)/(self.numb)
            i = 0

            while i != self.numb:

                lista = lista + [self.a + i*h]
                i += 1

            return lista
                    
        
        
    def NSub(self):
        
        '''
        Función para definir el número de subintervalos que se quiere utilizar en las fórmulas de cuadratura compuesta.
        
        '''
        
        aux1 = 1
        
        while aux1 == 1:
            
            # Comprobamos que da un número válido.
            try:
                
                # Pedimos el número y lo convertimos a flotante.
                
                N = int(input('Introduzca el número de subintervalos para el que desea realizar la fórmula de cuadratura compuesta: \n'))
                
                if N < 2 :
                    
                    r1 = input('N debe ser un entero mayor o igual a 2, ¿Desea volver a intentarlo? S/N: ')
                    print('\n')

                    if r1.upper() == 'S':

                        # Volvemos al bucle
                        aux1 = 1

                    else:

                        # Salimos de la función.
                        print("Operación cancelada.")
                        print('\n')
                        return
                    
                    
                
                # Guardamos su valor.
                self.N = N
                
                # Salimos del bucle.
                aux1 = 0
                                
            # En caso de que el valor no sea válido, establece una rutina para volver a intentar o cancelar.
            except:
                           
                r1 = input('N debe ser un entero mayor o igual a 2, ¿Desea volver a intentarlo? S/N: ')
                print('\n')
                        
                if r1.upper() == 'S':
                        
                    # Volvemos al bucle
                    aux1 = 1
                        
                else:
                          
                    # Salimos de la función.
                    print("Operación cancelada.")
                    print('\n')
                    return
        
            
    
    
    
    def TiempoC(self, s):
        """
        Devuelve el tiempo que tarda en ejecutarse el método.
        
        Agr:
            s: Método del que desea saber el tiempo de ejecución.
            
        """
    
        # Guardamos las antiguas opciones para devolver en los métodos.
        old_aprox, old_er = self.aprox, self.er
        
        # Asignamos que devuelva solo la aproximación.
        
        self.aprox,  self.tim, self.er = True, False, False
        
        # Comprobamos el tiempo antes de hacer los calculos.
        
        start = tm.time()
            
        # Llamamos a la función 1000 veces.
        for i in range(1000):
            s()
                
        # Dejamos las opciones como estaban.
        self.aprox, self.er, self.tim = old_aprox, old_er, True
            
        # Devolvemos el tiempo el promedio de tiempo que tarda en ejecutarse la función.
        return (tm.time() - start)/1000
            
    def ErrorC(self, s):
        """
        Devuelve la diferencia en valor absoluto entre la raíz calculada mediante el método elegido y la raíz dada por Python.
        
        Agr:
            s: Método elegido.
            
        """
    
        # Guardamos las antiguas opciones para devolver en los métodos.
        old_aprox, old_tim= self.aprox, self.tim
  
        # Asignamos que devuelva solo la aproximación.
        self.aprox, self.tim,self.er = True, False, False
       
        # Calculamos la aproximación del método elegido y la aproximación dada por Python.
        aprox_s = s()
        aprox_p = self.CPython()
        
        # Dejamos las opciones como estaban.
        self.aprox,self.tim, self.er = old_aprox, old_tim, True
        
        # Devolvemos el error.
        return abs(aprox_s - aprox_p)
    
    
    
class Cuadratura(Base_Cuadratura):
    
    def __init__ (self, f = None, a = None, b = None, aprox = True, tim = False, er = False, numa = None, numb = None, nodosa = None, nodosb = None, N = 100):
        
        """
        Inicializa las variables objeto para la busqueda de aproximaciones a la integral definida de una función dada.
        
        Args:
        
            f: Función, None por defecto.
            
            a, b: Límites del intervalo, None por defecto.
            
            aprox: Variable para devolver o no la aproximación del método, True por defecto.
            
            tim: Variable para devolver o no el tiempo de ejecución del método, False por defecto.
            
            er: Variable para devolver o no la diferencia entre la raiz calcula por Python y la raíz dada por el método elegido, 
            False por defecto.
            
            numa: Número de nodos entre 1 y 5 que se desea para calcular la aproximación de la integral por cuadratura abierta, None por defecto.
            
            numb: Número de nodos entre 2 y 6 que se desea para calcular la aproximación de la integral por cuadratura cerrada, None por defecto.
            
            N : Número de subintervalos en los que se dividirá el intervalo en las fórmulas de cuadratura compuesta. Por defecto 100.
            Debe de ser mayor o igual a 2.
            
        Return:
        
            Mensaje de error si fallan los argumentos.
            
        """
        
        # Definimos los datos :
        
        self.f = f
        
        # Primera comprobación de que los datos pueden ser incorrectos.
            
        #Comprobación para numa.
        if numa == None:
            
            self.numa = numa
        
        else:
            
            try:
                
                self.numa = int(numa)
                
                if numa < 1 or numa > 5:
                   
                    print('Error en los datos de entrada')
                    
            except:
                
                print('Error en los datos de entrada')
        
        #Comprobación para numb.        
        if numb == None:
            
            self.numb = numb
        
        else:
            
            try:
                
                self.numb = int(numb)
                
                if numa < 2 or numa > 6:
                   
                    print('Error en los datos de entrada')
                    
            except:
                
                print('Error en los datos de entrada')
        
        #Comprobación para N.
        if N == 100:
            
            self.N = N
        
        else:
            
            try:
                
                self.N = int(N)
                
                if N < 2 :
                   
                    print('Error en los datos de entrada')
                    
            except:
                
                print('Error en los datos de entrada')
        
        
        # Comprobamos si se han introducido los límites del intervalo.
        if a == None and b == None:
            self.a = a
            self.b = b
            
        else:
            
            # Se guardarán los datos en caso de que los tipos sean los adecuados.
            try:
                
                self.a = float(a)
                self.b = float(b)
                
            except:
                print("Error en los datos de entrada.")
               
        
        # Definimos variables globales:
        self.aprox = aprox
        self.tim = tim
        self.er = er
        self.nodosa = nodosa
        self.nodosb = nodosb
        
    # Fórmulas de cuadratura de tipo interpolatorio:
    
    def Ptomedio (self) :
        
        '''
        Calcula una aproximación a la integral definida de f en el intervalo [a, b] mediante la fórmula del punto medio.
        
        Parámetros previamente definidos:
            
            f: Función.
            a, b: Extremos del intervalo.
            
        Return:
            Según las opciones selecionadas puede devolver:
            x: Aproximación calculada.
            tim: Tiempo de ejecución del programa.
            er: Diferencia entre la aproximación del método y la aproximación dada por Python.
         
       ''' 
        
        aux = 0
        
        lista = []
        
        try:
            
            # Comprobamos que los parámetros han sido definidos previamente, si no los definimos.
            
            if self.a == None or self.b == None :
                
                print (' No se ha definido previamente el parámetro.\n')
                self.Intervalo()
                if self.a == None or self.b == None :
                    return
                
            if self.f == None:
                print('No ha definido previamente la función:')
                self.f = self.Funcion()
                if self.f == None:
                    return
                
            # Creamos las variables auxiliares.
            a = self.a
            b = self.b
            f = self.f
            
            
            # Se calcula la aproximación de la fórmula de cuadratura por el pto medio
            
            I0 = (b - a) * f((a + b) / 2)
            
            # Si lo ha elegido guardamos en la lista de devolución la aproximación.
            
            if self.aprox == True:
                lista = lista + [I0]
                aux += 1
            
            # Si lo ha elegido guardamos en la lista de devolución el tiempo de ejecución.
            if self.tim == True:
                tim = self.TiempoC(self.Ptomedio)
                lista = lista + [tim]
                aux += 1
            # Si lo ha elegido guardamos en la lista de devolución del error entre la sol de python y la del método usado.    
            if self.er == True:
                er = self.ErrorC(self.Ptomedio)
                lista = lista + [er]
                aux += 1 
                
            # Comprobamos cuantos parámetros se han guardado en la lista de devolución.
            # Si no se ha guardado ninguno devolvemos un mensaje.
            if aux == 0:
                return(print('No se ha seleccionado opción para devolver.'))
             
            # Si solo se ha guardado una variable devolvemos este valor.
            elif aux == 1:
                return lista[0]
                
            # En caso contrario devolvemos la tupla con todas las variables elegidas.
            else:
                return tuple(lista)
            
            
        except:
            
            print ('Los datos no han sido previamente definidos. Definalos e intentelo de nuevo.')
            return
        
    def Trapecio (self) :
        
        '''
        Calcula una aproximación a la integral definida de f en el intervalo [a, b] mediante la fórmula del trapecio.
        
        Parámetros previamente definidos:
            
            f: Función.
            a, b: Extremos del intervalo.
            
        Return:
            Según las opciones selecionadas puede devolver:
            x: Aproximación calculada.
            tim: Tiempo de ejecución del programa.
            er: Diferencia entre la aproximación del método y la aproximación dada por Python.
         
       ''' 
        
        aux = 0
        
        lista = []
        
        try:
            
            # Comprobamos que los parámetros han sido definidos previamente, si no los definimos.
            
            if self.a == None or self.b == None :
                
                print (' No se ha definido previamente el parámetro.\n')
                self.Intervalo()
                if self.a == None or self.b == None :
                    return
                
            if self.f == None:
                print('No ha definido previamente la función:')
                self.f = self.Funcion()
                if self.f == None:
                    return
                
            # Creamos las variables auxiliares.
            a = self.a
            b = self.b
            f = self.f
            
            
            # Se calcula la aproximación de la fórmula de cuadratura por la fórmula del trapecio.
            
            I1 = (b - a)/2 * (f(a) + f(b))
            
            # Si lo ha elegido guardamos en la lista de devolución la aproximación.
            
            if self.aprox == True:
                lista = lista + [I1]
                aux += 1
            
            # Si lo ha elegido guardamos en la lista de devolución el tiempo de ejecución.
            if self.tim == True:
                tim = self.TiempoC(self.Trapecio)
                lista = lista + [tim]
                aux += 1
            # Si lo ha elegido guardamos en la lista de devolución del error entre la sol de python y la del método usado.    
            if self.er == True:
                er = self.ErrorC(self.Trapecio)
                lista = lista + [er]
                aux += 1 
                
            # Comprobamos cuantos parámetros se han guardado en la lista de devolución.
            # Si no se ha guardado ninguno devolvemos un mensaje.
            if aux == 0:
                return(print('No se ha seleccionado opción para devolver.'))
             
            # Si solo se ha guardado una variable devolvemos este valor.
            elif aux == 1:
                return lista[0]
                
            # En caso contrario devolvemos la tupla con todas las variables elegidas.
            else:
                return tuple(lista)
            
            
        except:
            
            print ('Los datos no han sido previamente definidos. Definalos e intentelo de nuevo.')
            return
            
        
    def Simpson (self) :
        
        '''
        Calcula una aproximación a la integral definida de f en el intervalo [a, b] mediante la fórmula de Simpson.
        
        Parámetros previamente definidos:
            
            f: Función.
            a, b: Extremos del intervalo.
            
        Return:
            Según las opciones selecionadas puede devolver:
            x: Aproximación calculada.
            tim: Tiempo de ejecución del programa.
            er: Diferencia entre la aproximación del método y la aproximación dada por Python.
         
       ''' 
        
        aux = 0
        
        lista = []
        
        try:
            
            # Comprobamos que los parámetros han sido definidos previamente, si no los definimos, si no se define correctamente 
            #se cancela el metodo.
            
            if self.a == None or self.b == None :
                
                print (' No se ha definido previamente el parámetro.\n')
                self.Intervalo()
                if self.a == None or self.b == None :
                    return
                
            if self.f == None:
                print('No ha definido previamente la función:')
                self.f = self.Funcion()
                if self.f == None:
                    return
                
            # Creamos las variables auxiliares.
            a = self.a
            b = self.b
            f = self.f
            
            # Se calcula la aproximación de la fórmula de cuadratura por Simpson.
            
            I2 = (b - a)/6 * ( f(a) + 4 * f((a + b)/2) + f(b) )
            
            # Si lo ha elegido guardamos en la lista de devolución la aproximación.
            
            if self.aprox == True:
                lista = lista + [I2]
                aux += 1
            
            # Si lo ha elegido guardamos en la lista de devolución el tiempo de ejecución.
            if self.tim == True:
                tim = self.TiempoC(self.Simpson)
                lista = lista + [tim]
                aux += 1
            # Si lo ha elegido guardamos en la lista de devolución del error entre la sol de python y la del método usado.    
            if self.er == True:
                er = self.ErrorC(self.Simpson)
                lista = lista + [er]
                aux += 1 
                
            # Comprobamos cuantos parámetros se han guardado en la lista de devolución.
            # Si no se ha guardado ninguno devolvemos un mensaje.
            if aux == 0:
                return(print('No se ha seleccionado opción para devolver.'))
             
            # Si solo se ha guardado una variable devolvemos este valor.
            elif aux == 1:
                return lista[0]
                
            # En caso contrario devolvemos la tupla con todas las variables elegidas.
            else:
                return tuple(lista)
        except:
            
            print ('Los datos no han sido previamente definidos. Definalos e intentelo de nuevo.')
            return
    

    # Fórmulas de cuadratura de Newton - Côtes
    
    def CAbierta(self):
                
        '''
            Calcula una aproximación a la integral definida de f en el intervalo [a, b] mediante fórmulas de cuadratura abierta.

            Parámetros previamente definidos:

                f: Función.
                a, b: Extremos del intervalo.

            Return:
                Según las opciones selecionadas puede devolver en el siguiente orden:
                x: Aproximación calculada.
                tim: Tiempo de ejecución del programa.
                er: Diferencia entre la aproximación del método y la aproximación dada por Python.

        ''' 
        aux = 0
        
        lista = []
        
        try:
            
            # Comprobamos que los parámetros han sido definidos previamente, si no los definimos.

            if self.a == None or self.b == None :
                
                print (' No se ha definido previamente el parámetro.\n')
                self.Intervalo()
                if self.a == None or self.b == None :
                    return
                
            if self.f == None:
                print('No ha definido previamente la función:')
                self.f = self.Funcion()
                if self.f == None:
                    return

            if self.numa == None:

                print (' No se ha definido previamente el parámetro.\n')
                self.Cnuma()
                if self.numa == None:
                    return


            # Creamos las variables auxiliares.
            a = self.a
            b = self.b
            f = self.f


            # Se calcula la aproximación de la fórmula de cuadratura abierta según el número de nodos.

            self.nodosa = self.CNodos('abierta')

            h = (b-a)/(self.numa + 2) 

            if self.numa == 1:

                return self.Ptomedio()

            if self.numa == 2:

                Inum = 3/2 * h * (f(self.nodosa[0]) + f(self.nodosa[1]))

            if self.numa == 3:

                Inum = 4/3 * h * (2 * f(self.nodosa[0]) - f(self.nodosa[1]) + 2 * f(self.nodosa[2]))

            if self.numa == 4:

                Inum = 5/24 * h * (11 * f(self.nodosa[0]) + f(self.nodosa[1]) + f(self.nodosa[2]) + 11 * f(self.nodosa[3]))

            if self.numa == 5:

                Inum = 6/20 * h * (11 * f(self.nodosa[0]) - 14 * f(self.nodosa[1]) + 26 * f(self.nodosa[2]) - 14 * f(self.nodosa[3]) + 11 * f(self.nodosa[4]))


                #reseteo self.nodosa por si el usuario modificase self.numa:

            self.nodosa = None

                # Si lo ha elegido guardamos en la lista de devolución la aproximación.

            if self.aprox == True:
                lista = lista + [Inum]
                aux += 1

            # Si lo ha elegido guardamos en la lista de devolución el tiempo de ejecución.
            if self.tim == True:
                tim = self.TiempoC(self.CAbierta)
                lista = lista + [tim]
                aux += 1
            # Si lo ha elegido guardamos en la lista de devolución del error entre la sol de python y la del método usado.
            if self.er == True:
                er = self.ErrorC(self.CAbierta)
                lista = lista + [er]
                aux += 1 

            # Comprobamos cuantos parámetros se han guardado en la lista de devolución.
            # Si no se ha guardado ninguno devolvemos un mensaje.
            if aux == 0:
                return(print('No se ha seleccionado opción para devolver.'))

            # Si solo se ha guardado una variable devolvemos este valor.
            elif aux == 1:
                return lista[0]

                # En caso contrario devolvemos la tupla con todas las variables elegidas.
            else:
                return tuple(lista)
        except:

            print ('Los datos no han sido previamente definidos. Definalos e intentelo de nuevo.')
            return
        

    def CCerrada(self):
                
        '''
            Calcula una aproximación a la integral definida de f en el intervalo [a, b] mediante fórmulas de cuadratura cerrada.

            Parámetros previamente definidos:

                f: Función.
                a, b: Extremos del intervalo.

            Return:
                Según las opciones selecionadas puede devolver en el siguiente orden:
                x: Aproximación calculada.
                tim: Tiempo de ejecución del programa.
                er: Diferencia entre la aproximación del método y la aproximación dada por Python.

        ''' 
        aux = 0
        
        lista = []
        
        try:
            
            #Comprobamos que los parámetros han sido definidos previamente, si no los definimos.

            if self.a == None or self.b == None :
                
                print (' No se ha definido previamente el parámetro.\n')
                self.Intervalo()
                if self.a == None or self.b == None :
                    return
                
            if self.f == None:
                print('No ha definido previamente la función:')
                self.f = self.Funcion()
                if self.f == None:
                    return

            if self.numb == None:

                print (' No se ha definido previamente el parámetro.\n')
                self.Cnumb()
                if self.numb == None:
                    return

            # Creamos las variables auxiliares.
            a = self.a
            b = self.b
            f = self.f

            # Se calcula la aproximación de la fórmula de cuadratura abierta según el número de nodos.

            self.nodosb = self.CNodos('cerrada')

            h = (b-a)/(self.numb) 

            if self.numb == 2:

                return self.Trapecio()

            if self.numb == 3:

                return self.Simpson()

            if self.numb == 4:

                Inum = 3/8 * h * ( f(self.nodosb[0]) + 3 * f(self.nodosb[1]) + 3 * f(self.nodosb[2]) + f(self.nodosb[3]))

            if self.numb == 5:

                Inum = 2/45 * h * (7 * f(self.nodosb[0]) + 32 * f(self.nodosb[1]) + 12 * f(self.nodosb[2]) + 32 * f(self.nodosb[3]) + 7 * f(self.nodosb[4]))

            if self.numb == 6:

                Inum = 5/288 * h * (19 * f(self.nodosb[0]) + 75 * f(self.nodosb[1]) + 50 * f(self.nodosb[2]) + 50 * f(self.nodosb[3]) + 75 * f(self.nodosb[4]) + 19 * f(self.nodosb[5]))


            #reseteo self.nodosb por si el usuario modificase self.numb:

            self.nodosb = None

            # Si lo ha elegido guardamos en la lista de devolución la aproximación.

            if self.aprox == True:
                lista = lista + [Inum]
                aux += 1

            # Si lo ha elegido guardamos en la lista de devolución el tiempo de ejecución.
            if self.tim == True:
                tim = self.TiempoC(self.CCerrada)
                lista = lista + [tim]
                aux += 1
            # Si lo ha elegido guardamos en la lista de devolución del error entre la sol de python y la del método usado.
            if self.er == True:
                er = self.ErrorC(self.CCerrada)
                lista = lista + [er]
                aux += 1 

            # Comprobamos cuantos parámetros se han guardado en la lista de devolución.
            # Si no se ha guardado ninguno devolvemos un mensaje.
            if aux == 0:
                return(print('No se ha seleccionado opción para devolver.'))

            # Si solo se ha guardado una variable devolvemos este valor.
            elif aux == 1:
                return lista[0]

            # En caso contrario devolvemos la tupla con todas las variables elegidas.
            else:
                return tuple(lista)
        except:
            
            print ('Los datos no han sido previamente definidos. Definalos e intentelo de nuevo.')
            return
    
    
    # Fórmulas de cuadratura compuesta:
    
    def PtomedioComp(self):
        
        '''
        Aproxima a la integral de una función en un intervalo a partir de unos nodos e imagenes de los mismos, utilizando 
        la fórmula de cuadratura compuesta del punto medio.

        Parámetros previamente definidos:

            f: función a la que se quiere aproximar por cuadratura.

            a:extremo izquierdo del intervalo.

            b:extremo derecho del intervalo.

            N: Número de subintervalos en los que se aplicará la fórmula de cuadratura del pto medio.
        
        '''
        
        aux = 0
        
        lista = []
        
        
        try:
            
            # Comprobamos que los parámetros han sido definidos previamente, si no los definimos.
            
            if self.a == None or self.b == None :
                
                print (' No se ha definido previamente el parámetro.\n')
                self.Intervalo()
                if self.a == None or self.b == None :
                    return
                
            if self.f == None:
                print('No ha definido previamente la función:')
                self.f = self.Funcion()
                if self.f == None:
                    return
            
                
            # Creamos las variables auxiliares.
            a = self.a
            b = self.b
            f = self.f
            
            
            #Se divide el intervalo en subintervalos
            n_x = np.linspace(self.a, self.b, self.N*2+1) # [x0, x1, x2], [x2, x3, x4],..., [x2N-1, x2N, x2N+1] 
            
            #Se define la amplitud de los subintervalos y la imagen de los nodos.
            h = (self.b-self.a)/(self.N*2)
            fi = f(n_x)
            #nodos impares, corresponde a los ptos medios de los subintervalos.
            impares = fi[1::2]
            #Cálculo de la aproximación a la integral por cuadratura compuesta de pto medio.
            cc_compuesta = 2 * h * np.sum(impares)
    
            # Si lo ha elegido guardamos en la lista de devolución la aproximación.
            
            if self.aprox == True:
                lista = lista + [cc_compuesta]
                aux += 1
            
            # Si lo ha elegido guardamos en la lista de devolución el tiempo de ejecución.
            if self.tim == True:
                tim = self.TiempoC(self.PtomedioComp)
                lista = lista + [tim]
                aux += 1
            # Si lo ha elegido guardamos en la lista de devolución del error entre la sol de python y la del método usado.    
            if self.er == True:
                er = self.ErrorC(self.PtomedioComp)
                lista = lista + [er]
                aux += 1 
                
            # Comprobamos cuantos parámetros se han guardado en la lista de devolución.
            # Si no se ha guardado ninguno devolvemos un mensaje.
            if aux == 0:
                return(print('No se ha seleccionado opción para devolver.'))
             
            # Si solo se ha guardado una variable devolvemos este valor.
            elif aux == 1:
                return lista[0]
                
            # En caso contrario devolvemos la tupla con todas las variables elegidas.
            else:
                return tuple(lista)
        except:
            
            print ('Los datos no han sido previamente definidos. Definalos e intentelo de nuevo.')
            return
            
    
    def TrapecioComp(self):
        
        '''
        Aproxima a la integral de una función en un intervalo a partir de unos nodos e imagenes de los mismos, utilizando 
        la fórmula de cuadratura compuesta de los trapecios.

        Parámetros previamente definidos:

            f: función a la que se quiere aproximar por cuadratura.

            a:extremo izquierdo del intervalo.

            b:extremo derecho del intervalo.

            N: Número de subintervalos en los que se aplicará la fórmula de cuadratura de los trapecios.
        
        '''
        
        aux = 0
        
        lista = []
        
        
        try:
            
            # Comprobamos que los parámetros han sido definidos previamente, si no los definimos.

            if self.a == None or self.b == None :
                
                print (' No se ha definido previamente el parámetro.\n')
                self.Intervalo()
                if self.a == None or self.b == None :
                    return
                
            if self.f == None:
                print('No ha definido previamente la función:')
                self.f = self.Funcion()
                if self.f == None:
                    return

           # Creamos las variables auxiliares.
            a = self.a
            b = self.b
            f = self.f         


           #Se divide el intervalo en subintervalos
            n_x = np.linspace(self.a, self.b, self.N*2+1) # [x0, x1, x2], [x2, x3, x4],..., [x2N-1, x2N, x2N+1] 

            #Se define la amplitud de los subintervalos y la imagen de los nodos.
            h = (self.b-self.a)/(self.N*2)
            fi = f(n_x)
            #nodos pares e impares.
            pares   = fi[2:-1:2]
            impares = fi[1::2]
            #Cálculo de la aproximación a la integral por cuadratura compuesta del trapecio.

            cc_compuesta = h* (f(self.a)/2 + (np.sum(impares) + np.sum(pares))+ f(self.b)/2)

            # Si lo ha elegido guardamos en la lista de devolución la aproximación.

            if self.aprox == True:
                lista = lista + [cc_compuesta]
                aux += 1

                # Si lo ha elegido guardamos en la lista de devolución el tiempo de ejecución.
            if self.tim == True:
                tim = self.TiempoC(self.TrapecioComp)
                lista = lista + [tim]
                aux += 1

            if self.er == True:
                er = self.ErrorC(self.TrapecioComp)
                lista = lista + [er]
                aux += 1 

                # Comprobamos cuantos parámetros se han guardado en la lista de devolución.
                # Si no se ha guardado ninguno devolvemos un mensaje.
            if aux == 0:
                return(print('No se ha seleccionado opción para devolver.'))

                # Si solo se ha guardado una variable devolvemos este valor.
            elif aux == 1:
                return lista[0]

                # En caso contrario devolvemos la tupla con todas las variables elegidas.
            else:
                return tuple(lista)
        except:
            
            print ('Los datos no han sido previamente definidos. Definalos e intentelo de nuevo.')
            return
    
    
    def SimpsonComp(self):
        
        '''
        Aproxima a la integral de una función en un intervalo a partir de unos nodos e imagenes de los mismos, utilizando 
        la fórmula de cuadratura compuesta de Simpson.

        Parámetros previamente definidos:

            f: función a la que se quiere aproximar por cuadratura.

            a:extremo izquierdo del intervalo.

            b:extremo derecho del intervalo.

            N: Número de subintervalos en los que se aplicará la fórmula de cuadratura de Simpson Compuesta.
        
        '''
        
        aux = 0
        
        lista = []
        
        
        try:
            
            # Comprobamos que los parámetros han sido definidos previamente, si no los definimos.
            
            if self.a == None or self.b == None :
                
                print (' No se ha definido previamente el parámetro.\n')
                self.Intervalo()
                if self.a == None or self.b == None :
                    return
                
            if self.f == None:
                print('No ha definido previamente la función:')
                self.f = self.Funcion()
                if self.f == None:
                    return
            
                
            # Creamos las variables auxiliares.
            
            a = self.a
            b = self.b
            f = self.f
            
            #Se divide el intervalo en subintervalos
            n_x = np.linspace(self.a, self.b, self.N*2+1) # [x0, x1, x2], [x2, x3, x4],..., [x2N-1, x2N, x2N+1] 
            
            #Se define la amplitud de los subintervalos y la imagen de los nodos.
            h = (self.b-self.a)/(self.N*2)
            fi = f(n_x)
            #nodos pares e impares.
            pares   = fi[2:-1:2]
            impares = fi[1::2]
            #Cálculo de la aproximación a la integral por cuadratura compuesta de Simpson.
            
            cc_compuesta = h/3 * ( fi[0] + 4*np.sum(impares) + 2*np.sum(pares) + fi[-1] )
    
            # Si lo ha elegido guardamos en la lista de devolución la aproximación.
            
            if self.aprox == True:
                lista = lista + [cc_compuesta]
                aux += 1
            
            # Si lo ha elegido guardamos en la lista de devolución el tiempo de ejecución.
            if self.tim == True:
                tim = self.TiempoC(self.SimpsonComp)
                lista = lista + [tim]
                aux += 1
            # Si lo ha elegido guardamos en la lista de devolución del error entre la sol de python y la del método usado.    
            if self.er == True:
                er = self.ErrorC(self.SimpsonComp)
                lista = lista + [er]
                aux += 1 
                
            # Comprobamos cuantos parámetros se han guardado en la lista de devolución.
            # Si no se ha guardado ninguno devolvemos un mensaje.
            if aux == 0:
                return(print('No se ha seleccionado opción para devolver.'))
             
            # Si solo se ha guardado una variable devolvemos este valor.
            elif aux == 1:
                return lista[0]
                
            # En caso contrario devolvemos la tupla con todas las variables elegidas.
            else:
                return tuple(lista)
        except:
            
            print ('Los datos no han sido previamente definidos. Definalos e intentelo de nuevo.')
            return
    
    
    def CPython(self):
        
        """
        Calcula la aproximación integral a traves de la función quad del modulo scipy.integrate .
        """
        
        # Comprobamos que los parámetros han sido definidos previamente, si no los definimos.
        if self.a == None or self.b == None :
                
                print (' No se ha definido previamente el parámetro.\n')
                self.Intervalo()
                if self.a == None or self.b == None :
                    return
                
        if self.f == None :
            print('No ha definido previamente la función:')
            self.f = self.Funcion()
            if self.f == None:
                return
            
        # Creamos las variables auxiliares.
        a = self.a
        b = self.b
        f = self.f
        # Calculamos la aproximación dada por la función quad
        
        cpython = quad(f, a, b)
            
        return cpython[0]  
    
    
####################################################### CLASE TEMA 4 ##################################################  

class Base_EDO_PVI(Base_Global):
    
    def AuxAjustes(self,opcion):
        """
        Traduce las opciones de True o False.
        
        Return:
            cadena 'Sí' o 'No'
        """
        if opcion == True:
            cad = 'Si'
        else:
            cad = 'No'
        return(cad)
    
    def Ajustes(self):
        """
        Muestra un menu de ajustes para cambiar las configuraciones de EDO_PVI.
        """
        Op = [self.sol, self.tim, self.er, self.inf, self.lis, self.nod]
        cont = True
        while cont == True:
            cont2 = True
            cad = []
            # Traducimos las opciones para crear el menu de ajustes.
            for i in Op:
                cad.append(self.AuxAjustes(opcion = i))
            # Creamos el menu de ajustes.
            try:
                print('\nAjustes Tema 4:\n')
                print('\t1. Devolver las soluciones: ',cad[0])
                print('\n\t2. Devolver tiempo: ',cad[1])
                print('\n\t3. Devolver error del método:' ,cad[2])
                print('\n\t4. Devolver error del método en norma infinito:' ,cad[3])
                print('\n\t5. Devolver el soporte de puntos utilizados:',cad[4])
                print('\n\t6. Devolver información de cada nodo calculado:',cad[5])
    
                # Pedimos al usuario que introduzca una o varias opciones que desee cambiar y creamos una lista con dichas opciones.
                sel = input('\nSelecciona que opciones deseas cambiar o pulse 0 para acabar:\t')
                sel = sel.split(',')
                # Cambiamos las opciones seleccionadas 
                for j in sel:
                    fallo = j # Esta variable la usamos para mostrar un mensaje de error si la opcion introducida no es valida.
                    k = int(j) - 1
                    if k == -1:
                        cont = False
                    else:
                        if Op[k] == True:
                            Op[k] = False
                        else:
                            Op[k] = True
            except:
                print('\nLa opcion ',fallo,' no es valida')
                while cont2 == True:
                    aux = input('\n¿Desea continuar?\t1. Si\t2. No\t')
                    try:
                        aux = int(aux)
                        if aux == 1:
                            cont2 = False
                        elif aux == 2:
                            cont = False
                            cont2 = False
                        else:
                            print('Opción no valida')
                    except:
                        if aux.upper() == 'SI' or aux.upper() == 'YES' or aux.upper() == 'S' or aux.upper() == 'Y':
                            cont2 = False
                        elif aux.upper() == 'NO' or aux.upper() == 'N':
                            cont = False
                            cont2 = False
                        else:
                            print('Opción no valida')
        # Cambiamos las variables gobales de los ajustes.
        [self.sol, self.tim, self.er, self.inf, self.lis, self.nod] = Op
        cad = []
        # Traducimos los ajustes realizados.
        for i in Op:
            cad.append(self.AuxAjustes(i))
        # Mostramos como han quedado los ajustes al terminar y salimos de la función.
        print('\nAjustes Tema 4: \n')
        print('\t1. Devolver las soluciones:',cad[0])
        print('\n\t2. Devolver tiempo:',cad[1])
        print('\n\t3. Devolver error del método:' ,cad[2])
        print('\n\t4. Devolver error del método en norma infinito:' ,cad[3])
        print('\n\t5. Devolver el soporte de puntos utilizados:',cad[4])
        print('\n\t6. Devolver información de cada nodo calculado:',cad[5])
        
        return
    
    def Soporte_tamanio(self):
        """
        Establece el soporte de puntos que se utilizan en un método.
        
        Return:
            rango del bucle, soporte de puntos.
        """
        try:
            n = int(round((self.b - self.a)/self.h))
            support = np.linspace(self.a, self.b, n+1)
            
            return n, support
        except:
            print('Debe definir previamente los parámetros')
            return
        
    def Paso_de_tiempo(self):
        """
        Define o cambia el paso de tiempo que se usará en los métodos. Se pedirá por teclado.
        """
        aux = 1
        
        while aux == 1:
            
            # Nos aseguramos de que introduce un número válido.
            try:
                
                # Pedimos el número y lo convertimos en entero.
                h = float(input('Introduce el paso de tiempo: '))
                print('\n')
                
                # Salimos del bucle.
                aux = 0
                
                #Si h es un número negativo, establece rutina para volver a intentar o cancelar
                if (h <= 0):
                    
                    r1 = input('El valor introducido no es válido, ¿Desea volver a intentarlo? S/N: ')
                    print('\n')
                        
                    if r1.upper() == 'S':
                            
                        # Volvemos al bucle
                        aux = 1
                            
                    else:
                            
                        print("Operación cancelada.")
                        print('\n')
                        return
                
                # Sólo se almacenará el valor del paso de tiempo si todo está en orden.
                else:
                    
                    self.h = h
                    return
                    
            # En caso de que el valor no sea válido, establece una rutina para volver a intentar o cancelar.
            except:

                r2 = input('El valor introducido no es válido, ¿Desea volver a intentarlo? S/N: ')
                print('\n')
                    
                if r2.upper() == 'S':
                      
                    # Volvemos al bucle.    
                    aux = 1
                    
                else:
                        
                    # Salimos de la función.    
                    print("Operación cancelada.")
                    print('\n')
                    return
    
    def Funcion_dos_variables(self): 
        """
        Define o cambia la función que usaremos en los métodos.
        """
        aux = 1
        
        while aux == 1:
            
            # Nos aseguramos de que introduce un número válido.
            try:
                
                # Pedimos la función.
                h = input('Introduce la función, con variable t, y:  ')
                    
                # Creamos las variables como símbolo.
                x = sp.symbols('t')
                y = sp.symbols('y')
                
                # Convertimos la cadena a función.
                f = sp.lambdify([x, y], h, "numpy")
                    
                # Comprobamos que la función es válida, si no lo es al evaluarla dará error.
                f(1, 1)
                
                # Salimos del bucle.
                aux = 0
                    
                # Establecemos la función y salimos de la función.
                self.f = f
                return
                    
            # En caso de que el valor no sea válido, establece una rutina para volver a intentar o cancelar.
            except:

                r2 = input('La función no es válida, ¿Desea volver a intentarlo? S/N: ')
                  
                  
                if r2 == 's' or r2 == 'S':
                     
                    # Volvemos al bucle.
                    aux = 1
                    
                else:
                    
                    # Salimos de la función.
                    print("Operación cancelada.")
                    return
                
    def func(self, y, t):
        """
        Función que usaremos para la solución de python.
        
        Args:
            y, t
            
        Return:
            f(t,y)
        """
        try:
            
            if self.f == None:
                print('No se ha definido previamente la función.')
                self.Funcion_dos_variables(self)
                
            else:
                f = self.f
                return f(t, y)
            
        except:
            
            print('Error en los parámetros de entrada.')
            return
        
    def Tiempo(self, s):
        """
        Devuelve el tiempo que tarda en ejecutarse el método.
        
        Agr:
            s: Método del que desea saber el tiempo de ejecución.
            
        Return:
            Tiempo de ejecución.
            
        """
    
        # Guardamos las antiguas opciones para devolver en los métodos.
        old_sol, old_er, old_lis, old_nod, old_inf = self.sol, self.er, self.lis, self.nod, self.inf
        
        # Asignamos que devuelva solo la raíz.
        self.sol, self.tim, self.er, self.lis, self.nod, self.inf = True, False, False, False, False, False
        
        # Comprobamos el tiempo antes de hacer los calculos.
        start = tm.time()
            
        # Llamamos a la función 1000 veces.
        for i in range(1000):
            s()
                
        # Dejamos las opciones como estaban.
        self.sol, self.er, self. tim, self.lis, self.nod, self.inf = old_sol, old_er, True, old_lis, old_nod, old_inf
            
        # Devolvemos el tiempo el promedio de tiempo que tarda en ejecutarse la función.
        return (tm.time() - start)/1000
    
    def Error(self, s):
        """
        Devuelve la diferencia en valor absoluto entre la solución calculada mediante el método elegido y la solución dada por Python.
        
        Agr:
            s: Método elegido.
            
        Return:
            Error del método.
            
        """
    
        # Guardamos las antiguas opciones para devolver en los métodos.
        old_sol, old_tim, old_lis, old_nod, old_inf, old_er = self.sol, self.tim, self.lis, self.nod, self.inf, self.er
        
        # Asignamos que devuelva solo la raíz.
        self.sol, self.tim, self.er, self.lis, self.nod, self.inf = True, False, False, False, False, False
       
        # Calculamos la raíz del método elegido y la raíz dada por Python.
        sol_s = s()
        sol_p = self.Sol_Python()
        
        # Dejamos las opciones como estaban.
        self.sol, self.tim, self.er, self.lis, self.nod, self.inf = old_sol, old_tim, old_er, old_lis, old_nod, old_inf
       
        # Sacamos las soluciones de Python.
        sol_p_v = list(sol_p)
 
        # Sacamos los errores de cada función.
        e = [abs(sol_s[i] - sol_p_v[i]) for i in range(len(sol_s))]
        
        # Devolvemos el error.
        return e
    
class EDO_PVI(Base_EDO_PVI):
    
    def __init__(self, f = None, x0 = None, a = None, b = None, h = None, sol = True, er = False, inf = False, tim = False, lis = False, nod = False):
        """
        Inicializamos las variables que usaremos para resolver sistema de ecuaciones diferenciales de orden 2.
        
        Agr: 
            f: función del sistema de ecuaciones diferenciales, None por defecto.
            x0: Valor inicial de f, None por defecto.
            a, b: Extremos del intervalo de definción del PVI, en caso de no ser recibidos, None por defecto.
            h: Paso de tiempo, None por defecto.
            sol: Variable para devolver o no las soluciones del sistema, True por defecto.
            er: Variable para devolver o no la diferencia en valor absoluto entre las soluciones dadas por el método y las dadas por Python, False por defecto.
            inf: Variable para devolver o no la diferencia en valor absoluto entre las soluciones dadas por el método y las dadas por Python en norma infinito, False por defecto.
            tim: Variable para devolver o no el tiempo de ejecucion del método, False por defecto.
            lis: Variable para devolver o no el soporte de puntos utilizados, False por defecto.
            nod: Variable para mostrar o no por pantalla cada nodo calculado, False por defecto.
        
        Return:
            Mensaje de error si fallan los argumentos.
        """
        
        # Definimos los datos.
        self.f = f
        
        # Comprobamos si se ha introducido el valor inicial.
        if x0 == None:
            self.x0 = x0
            
        else:
            
            # Se guardará en caso de que el tipo sea adecuado.
            try:
                
                self.x0 = float(x0)
                
            except:
                
                print("Error en los datos de entrada.")
                
        # Comprobamos si se han introducido los límites del intervalo.
        if a == None and b == None:
            self.a = a
            self.b = b
            
        else:
            
            # Se guardarán los datos en caso de que los tipos sean los adecuados.
            try:
                
                self.a = float(a)
                self.b = float(b)
                
            except:
                print("Error en los datos de entrada.")
                
        # Comprobamos si se ha introducido el paso de tiempo:
        
        if h == None:
            self.h = h
            
        else:
            
            # Se guardará en caso de que sea un entero positivo:
            if h <= 0:
                print("Error en los datos de entrada.")
            
            else:
                try:
                    self.h = float(h)
                except:
                    print("Error en los datos de entrada.")
                
        # Comprobamos que las variables son válidas.
        if type(sol) == bool and type(tim) == bool and type(er) == bool and type(inf) == bool and type(lis) == bool and type(nod) == bool:
        
            self.sol = sol
            self.tim = tim
            self.er = er
            self.inf = inf
            self.lis = lis
            self.nod = nod
            
        else: 
        
            return(print('Error en los datos de entrada'))
        
    def Euler(self):
        """
        Resuelve un problema de valores iniciales mediante el método de Euler.
    
        Parámetros previamente definidos:
            f: Función que definela EDO.
            x0: Dato inicial.
            a, b: Intervalo.
            h: Paso de tiempo.
            
        Return:
            Según las opciones selecionadas puede devolver:
            x: Puntos que definen la función solución.
            tim: Tiempo de ejecución del programa.
            er: Diferencia entre los puntos dados por el méttodo y los dados por Python.
            inf: Diferencia entre los puntos dados por el método y los dados por Python en norma infinito).
            lis: Soporte de puntos utilizados
        """
        # Comprobamos si hay algún error.
        try:
            
            # Definimos una lista donde guardaremos los resultados y una variable auxiliar.
            lista = []
            aux = 0
            
            # Comprobamos que los parámetros han sido definidos, si no los definimos
            if self.f == None:
                print('No ha definido previamente la función.')
                self.Funcion_dos_variables()
                print('\n')
                
            if self.f == None:
                return
            
            if self.x0 == None:
                print('No ha definido previamente el valor inicial.')
                self.x0 = self.ValorInicial()
                print('\n')
                
            if self.x0 == None:
                return
                
            if self.a == None or self.b == None:
                print('No se ha definido previamente el intervalo.')
                self.Intervalo()
                print('\n')
                
            if self.a == None or self.b == None:
                return
            
            if self.h == None:
                print('No ha definido previamente el paso de tiempo.')
                self.Paso_de_tiempo()
                print('\n')
                
            if self.h == None:
                return
            
            # Creamos las variables auxiliares.
            f = self.f
            h = self.h
            yn = self.x0
            t_v = self.Soporte_tamanio()
            t = t_v[1]
            N = t_v[0]
            
            # Iniciamos la lista de soluciones con el valor inicial.
            sol = [yn]
    
            for i in range(N):
        
                # Calculamos la solución de Euler.
                tn = t[i]
                # Si lo ha elegido mostramos cada nodo calculado.
                if self.nod == True:
                    print('Nodo',i+1,':','(',tn,',',yn,')')
                    print('-------------------------------------------------')
                yn1 = yn + h*f(tn, yn)
                sol.append(yn1)
                yn = yn1
                
            # Mostramos el último nodo calculado en caso de que este se haya elegido:
            
            if self.nod == True:
                print('Nodo',N+1,':','(',t[N],',',yn,')')
                print('-------------------------------------------------')
        
            # Si lo ha elegido guardamos en la lista de devolución las soluciones.
            if self.sol == True:
                lista = lista + [sol]
                aux += 1
                
            # Si lo ha elegido guardamos en la lista de devolución la diferencia en valor absoluto entre la solución del método y la solución calculada por Python.    
            if self.er == True:
                er = self.Error(self.Euler)
                lista = lista + [er]
                aux += 1
                
            # Si lo ha elegido guardamos en la lista de devolución la diferencia entre la solución del método y la solución calculada por Python en norma infinito.    
            if self.inf == True:
                er = self.Error(self.Euler)
                err_inf = max(max(er))
                lista = lista + [err_inf]
                aux += 1
            
            # Si lo ha elegido guardamos en la lista de devolución el tiempo de ejecución.
            if self.tim == True:
                tim = self.Tiempo(self.Euler)
                lista = lista + [tim]
                aux += 1
                
            # Si lo ha elegido guardamos en la lista de devolución el soporte de puntos utilizados.
            if self.lis == True:
                lista = lista + [t]
                aux += 1
                
            # Comprobamos cuantos parámetros se han guardado en la lista de devolución.
            # Si no se ha guardado ninguno devolvemos un mensaje.
            if aux == 0:
                return(print('Ha seleccionado no devolver nada, vuelva a Ajustes.'))
                
            # En caso contrario devolvemos la tupla con todas las variables elegidas.
            else:
                return tuple(lista)
        
        # Si no se han definido los datos o no se han comprobado las hipotesis habrá un error y devolveremos un mesaje.
        except:
            print('Puede no tener solución, compruebe las hipótesis o defina previamente los datos.')
            
    def Euler_Cauchy(self):
        """
        Resuelve un problema de valores iniciales mediante el método de Euler-Cauchy.
    
        Parámetros previamente definidos:
            f: Función que definela EDO.
            x0: Dato inicial.
            a, b: Intervalo.
            h: Paso de tiempo.
            
        Return:
            Según las opciones selecionadas puede devolver:
            x: Puntos que definen la función solución.
            tim: Tiempo de ejecución del programa.
            er: Diferencia entre los puntos dados por el método y los dados por Python.
            inf: Diferencia entre los puntos dados por el método y los dados por Python en norma infinito).
            lis: Soporte de puntos utilizados
        """
        # Comprobamos si hay algún error.
        try:
            
            # Definimos una lista donde guardaremos los resultados y una variable auxiliar.
            lista = []
            aux = 0
            
            # Comprobamos que los parámetros han sido definidos, si no los definimos
            if self.f == None:
                print('No ha definido previamente la función.')
                self.Funcion_dos_variables()
                print('\n')
                
            if self.f == None:
                return
            
            if self.x0 == None:
                print('No ha definido previamente el valor inicial.')
                self.x0 = self.ValorInicial()
                print('\n')
                
            if self.x0 == None:
                return
                
            if self.a == None or self.b == None:
                print('No se ha definido previamente el intervalo.')
                self.Intervalo()
                print('\n')
                
            if self.a == None or self.b == None:
                return
            
            if self.h == None:
                print('No ha definido previamente el paso de tiempo.')
                self.Paso_de_tiempo()
                print('\n')
                
            if self.h == None:
                return
            
            # Creamos las variables auxiliares.
            f = self.f
            h = self.h
            yn = self.x0
            t_v = self.Soporte_tamanio()
            t = t_v[1]
            N = t_v[0]
            
            # Iniciamos la lista de soluciones con el valor inicial.
            sol = [yn]
    
            for i in range(N):
        
                # Calculamos la solución de Euler-Cauchy.
                tn = t[i]
                #Si lo ha elegido mostramos cada nodo calculado.
                if self.nod == True:
                    print('Nodo',i+1,':','(',tn,',',yn,')')
                    print('-------------------------------------------------')
                k1 = f(tn,yn)
                k2 = f(tn+h/2, yn+h/2*k1)
                yn1 = yn + h*k2
                sol.append(yn1)
                yn = yn1
                
            # Mostramos el último nodo calculado en caso de que este se haya elegido:
            
            if self.nod == True:
                print('Nodo',N+1,':','(',t[N],',',yn,')')
                print('-------------------------------------------------')
        
            # Si lo ha elegido guardamos en la lista de devolución las soluciones.
            if self.sol == True:
                lista = lista + [sol]
                aux += 1
                
            # Si lo ha elegido guardamos en la lista de devolución la diferencia en valor absoluto entre la solución del método y la solución calculada por Python.    
            if self.er == True:
                er = self.Error(self.Euler_Cauchy)
                lista = lista + [er]
                aux += 1
                
            # Si lo ha elegido guardamos en la lista de devolución la diferencia entre la solución del método y la solución calculada por Python en norma infinito.   
            if self.inf == True:
                er = self.Error(self.Euler_Cauchy)
                err_inf = max(max(er))
                lista = lista + [err_inf]
                aux += 1
            
            # Si lo ha elegido guardamos en la lista de devolución el tiempo de ejecución.
            if self.tim == True:
                tim = self.Tiempo(self.Euler_Cauchy)
                lista = lista + [tim]
                aux += 1
                
            # Si lo ha elegido guardamos en la lista de devolución el soporte de puntos utilizados.
            if self.lis == True:
                lista = lista + [t]
                aux += 1
                
            # Comprobamos cuantos parámetros se han guardado en la lista de devolución.
            # Si no se ha guardado ninguno devolvemos un mensaje.
            if aux == 0:
                return(print('Ha seleccionado no devolver nada, vuelva a Ajustes.'))
                
            # En caso contrario devolvemos la tupla con todas las variables elegidas.
            else:
                return tuple(lista)
        
        # Si no se han definido los datos o no se han comprobado las hipotesis habrá un error y devolveremos un mesaje.
        except:
            print('Puede no tener solución, compruebe las hipótesis o defina previamente los datos.')
            
    def Heunn(self):
        """
        Resuelve un problema de valores iniciales mediante el método de Heunn.
    
        Parámetros previamente definidos:
            f: Función que definela EDO.
            x0: Dato inicial.
            a, b: Intervalo.
            h: Paso de tiempo.
            
        Return:
            Según las opciones selecionadas puede devolver:
            x: Puntos que definen la función solución.
            tim: Tiempo de ejecución del programa.
            er: Diferencia entre los puntos dados por el méttodo y los dados por Python.
            inf: Diferencia entre los puntos dados por el método y los dados por Python en norma infinito).
            lis: Soporte de puntos utilizados
        """
        # Comprobamos si hay algún error.
        try:
            
            # Definimos una lista donde guardaremos los resultados y una variable auxiliar.
            lista = []
            aux = 0
            
            # Comprobamos que los parámetros han sido definidos, si no los definimos
            if self.f == None:
                print('No ha definido previamente la función.')
                self.Funcion_dos_variables()
                print('\n')
                
            if self.f == None:
                return
            
            if self.x0 == None:
                print('No ha definido previamente el valor inicial.')
                self.x0 = self.ValorInicial()
                print('\n')
                
            if self.x0 == None:
                return
                
            if self.a == None or self.b == None:
                print('No se ha definido previamente el intervalo.')
                self.Intervalo()
                print('\n')
                
            if self.a == None or self.b == None:
                return
            
            if self.h == None:
                print('No ha definido previamente el paso de tiempo.')
                self.Paso_de_tiempo()
                print('\n')
                
            if self.h == None:
                return
            
            # Creamos las variables auxiliares.
            f = self.f
            h = self.h
            yn = self.x0
            t_v = self.Soporte_tamanio()
            t = t_v[1]
            N = t_v[0]
            
            # Iniciamos la lista de soluciones con el valor inicial.
            sol = [yn]
    
            for i in range(N):
        
                # Calculamos la solución de Heunn.
                tn = t[i]
                # Si lo ha elegido mostramos cada nodo calculado.
                if self.nod == True:
                    print('Nodo',i+1,':','(',tn,',',yn,')')
                    print('-------------------------------------------------')
                t1 = t[i+1]
                k1 = yn + h*f(tn,yn)
                yn1 = yn + h*f(t1,k1)
                sol.append(yn1)
                yn = yn1
                
            # Mostramos el último nodo calculado en caso de que este se haya elegido:
            
            if self.nod == True:
                print('Nodo',N+1,':','(',t[N],',',yn,')')
                print('-------------------------------------------------')
        
            # Si lo ha elegido guardamos en la lista de devolución las soluciones.
            if self.sol == True:
                lista = lista + [sol]
                aux += 1
                
            # Si lo ha elegido guardamos en la lista de devolución la diferencia en valor absoluto entre la solución del método y la solución calculada por Python.    
            if self.er == True:
                er = self.Error(self.Heunn)
                lista = lista + [er]
                aux += 1
                
            # Si lo ha elegido guardamos en la lista de devolución la diferencia entre la solución del método y la solución calculada por Python en norma infinito..    
            if self.inf == True:
                er = self.Error(self.Heunn)
                err_inf = max(max(er))
                lista = lista + [err_inf]
                aux += 1
            
            # Si lo ha elegido guardamos en la lista de devolución el tiempo de ejecución.
            if self.tim == True:
                tim = self.Tiempo(self.Heunn)
                lista = lista + [tim]
                aux += 1
                
            # Si lo ha elegido guardamos en la lista de devolución el soporte de puntos utilizados.
            if self.lis == True:
                lista = lista + [t]
                aux += 1
                
            # Comprobamos cuantos parámetros se han guardado en la lista de devolución.
            # Si no se ha guardado ninguno devolvemos un mensaje.
            if aux == 0:
                return(print('Ha seleccionado no devolver nada, vuelva a Ajustes.'))
                
            # En caso contrario devolvemos la tupla con todas las variables elegidas.
            else:
                return tuple(lista)
        
        # Si no se han definido los datos o no se han comprobado las hipotesis habrá un error y devolveremos un mesaje.
        except:
            print('Puede no tener solución, compruebe las hipótesis o defina previamente los datos.')
            
    def Runge_Kutta(self):
        """
        Resuelve un problema de valores iniciales mediante el método de Runge_Kutta de orden 4.
    
        Parámetros previamente definidos:
            f: Función que definela EDO.
            x0: Dato inicial.
            a, b: Intervalo.
            h: Paso de tiempo.
            
      Return:
            Según las opciones selecionadas puede devolver:
            x: Puntos que definen la función solución.
            tim: Tiempo de ejecución del programa.
            er: Diferencia entre los puntos dados por el méttodo y los dados por Python.
            inf: Diferencia entre los puntos dados por el método y los dados por Python en norma infinito).
            lis: Soporte de puntos utilizados
        """
        # Comprobamos si hay algún error.
        try:
            
            # Definimos una lista donde guardaremos los resultados y una variable auxiliar.
            lista = []
            aux = 0
            
            # Comprobamos que los parámetros han sido definidos, si no los definimos
            if self.f == None:
                print('No ha definido previamente la función.')
                self.Funcion_dos_variables()
                print('\n')
                
            if self.f == None:
                return
            
            if self.x0 == None:
                print('No ha definido previamente el valor inicial.')
                self.x0 = self.ValorInicial()
                print('\n')
                
            if self.x0 == None:
                return
                
            if self.a == None or self.b == None:
                print('No se ha definido previamente el intervalo.')
                self.Intervalo()
                print('\n')
                
            if self.a == None or self.b == None:
                return
            
            if self.h == None:
                print('No ha definido previamente el paso de tiempo.')
                self.Paso_de_tiempo()
                print('\n')
                
            if self.h == None:
                return
            
            # Creamos las variables auxiliares.
            f = self.f
            h = self.h
            yn = self.x0
            t_v = self.Soporte_tamanio()
            t = t_v[1]
            N = t_v[0]
            
            # Iniciamos la lista de soluciones con el valor inicial.
            sol = [yn]
    
            for i in range(N):
        
                # Calculamos la solución de Runge_Kutta.
                tn = t[i]
                # Si lo ha elegido mostramos cada nodo calculado.
                if self.nod == True:
                    print('Nodo',i+1,':','(',tn,',',yn,')')
                    print('-------------------------------------------------')
                k1 = f(tn,yn)
                k2 = f(tn+h/2, yn + h/2 * k1)
                k3 = f(tn+h/2, yn + h/2 * k2)
                k4 = f(tn+h, yn + h * k3)
                yn1 = yn + h/6 * (k1 + 2*k2 + 2*k3 + k4)
                sol.append(yn1)
                yn = yn1
                
            # Mostramos el último nodo calculado en caso de que este se haya elegido:
            
            if self.nod == True:
                print('Nodo',N+1,':','(',t[N],',',yn,')')
                print('-------------------------------------------------')
        
            # Si lo ha elegido guardamos en la lista de devolución las soluciones.
            if self.sol == True:
                lista = lista + [sol]
                aux += 1
                
            # Si lo ha elegido guardamos en la lista de devolución la diferencia en valor absoluto entre la solución del método y la solución calculada por Python.    
            if self.er == True:
                er = self.Error(self.Runge_Kutta)
                lista = lista + [er]
                aux += 1
                
            # Si lo ha elegido guardamos en la lista de devolución la diferencia entre la solución del método y la solución calculada por Python en norma infinito..    
            if self.inf == True:
                er = self.Error(self.Runge_Kutta)
                err_inf = max(max(er))
                lista = lista + [err_inf]
                aux += 1
            
            # Si lo ha elegido guardamos en la lista de devolución el tiempo de ejecución.
            if self.tim == True:
                tim = self.Tiempo(self.Runge_Kutta)
                lista = lista + [tim]
                aux += 1
                
            # Si lo ha elegido guardamos en la lista de devolución el soporte de puntos utilizados.
            if self.lis == True:
                lista = lista + [t]
                aux += 1
                
            # Comprobamos cuantos parámetros se han guardado en la lista de devolución.
            # Si no se ha guardado ninguno devolvemos un mensaje.
            if aux == 0:
                return(print('Ha seleccionado no devolver nada, vuelva a Ajustes.'))
                
            # En caso contrario devolvemos la tupla con todas las variables elegidas.
            else:
                return tuple(lista)
        
        # Si no se han definido los datos o no se han comprobado las hipotesis habrá un error y devolveremos un mesaje.
        except:
            print('Puede no tener solución, compruebe las hipótesis o defina previamente los datos.')
            
    def Adams_Bashforth(self):
        """
        Resuelve un problema de valores iniciales mediante el método de Adams-Bashforth con inicialización de Euler-Cauchy.
    
        Parámetros previamente definidos:
            f: Función que definela EDO.
            x0: Dato inicial.
            a, b: Intervalo.
            h: Paso de tiempo.
            
        Return:
            Según las opciones selecionadas puede devolver:
            x: Puntos que definen la función solución.
            tim: Tiempo de ejecución del programa.
            er: Diferencia entre los puntos dados por el método y los dados por Python.
            inf: Diferencia entre los puntos dados por el método y los dados por Python en norma infinito).
            lis: Soporte de puntos utilizados
        """
        # Comprobamos si hay algún error.
        try:
            
            # Definimos una lista donde guardaremos los resultados y una variable auxiliar.
            lista = []
            aux = 0
            
            # Comprobamos que los parámetros han sido definidos, si no los definimos
            if self.f == None:
                print('No ha definido previamente la función.')
                self.Funcion_dos_variables()
                print('\n')
                
            if self.f == None:
                return
            
            if self.x0 == None:
                print('No ha definido previamente el valor inicial.')
                self.x0 = self.ValorInicial()
                print('\n')
                
            if self.x0 == None:
                return
                
            if self.a == None or self.b == None:
                print('No se ha definido previamente el intervalo.')
                self.Intervalo()
                print('\n')
                
            if self.a == None or self.b == None:
                return
            
            if self.h == None:
                print('No ha definido previamente el paso de tiempo.')
                self.Paso_de_tiempo()
                print('\n')
                
            if self.h == None:
                return
            
            # Creamos las variables auxiliares.
            f = self.f
            a = self.a
            h = self.h
            yn = self.x0
            t_v = self.Soporte_tamanio()
            t = t_v[1]
            N = t_v[0]
            
            # Iniciamos la lista de soluciones con el valor inicial.
            sol = [yn]
    
            for i in range(1):
        
                # Calculamos la inicialización de Euler-Cauchy.
                tn = t[i]
                
                #Si lo ha elegido mostramos cada nodo calculado.
                if self.nod == True:
                    print('Nodo',i+1,':','(',tn,',',yn,')')
                    print('-------------------------------------------------')
                
                k1 = yn + h/2 * f(tn, yn)
                yn = yn + h*f(tn + h/2, k1)
                sol.append(yn)
                
            y0 = sol[0]
            y1 = sol[1]
            f0 = f(a, y0)
            f1 = f(a + h, y1)
            
            for i in range(N-1):
                
                #Si lo ha elegido mostramos cada nodo calculado.
                if self.nod == True:
                    print('Nodo',i+2,':','(',t[i+1],',',yn,')')
                    print('-------------------------------------------------')
                
                # Calculamos la solución de Adams-Bashforth.
                yn = yn + h/2 * (3*f1 - f0)
                sol.append(yn)
                tn = t[i+2]
                f0 = f1
                f1 = f(tn, yn)
                
            # Mostramos el último nodo calculado en caso de que este se haya elegido:
            
            if self.nod == True:
                print('Nodo',N+1,':','(',t[N],',',yn,')')
                print('-------------------------------------------------')
            
            # Si lo ha elegido guardamos en la lista de devolución las soluciones.
            if self.sol == True:
                lista = lista + [sol]
                aux += 1
                
            # Si lo ha elegido guardamos en la lista de devolución la diferencia en valor absoluto entre la solución del método y la solución calculada por Python.    
            if self.er == True:
                er = self.Error(self.Adams_Bashforth)
                lista = lista + [er]
                aux += 1
                
            # Si lo ha elegido guardamos en la lista de devolución la diferencia entre la solución del método y la solución calculada por Python en norma infinito.   
            if self.inf == True:
                er = self.Error(self.Adams_Bashforth)
                err_inf = max(max(er))
                lista = lista + [err_inf]
                aux += 1
            
            # Si lo ha elegido guardamos en la lista de devolución el tiempo de ejecución.
            if self.tim == True:
                tim = self.Tiempo(self.Adams_Bashforth)
                lista = lista + [tim]
                aux += 1
                
            # Si lo ha elegido guardamos en la lista de devolución el soporte de puntos utilizados.
            if self.lis == True:
                lista = lista + [t]
                aux += 1
                
            # Comprobamos cuantos parámetros se han guardado en la lista de devolución.
            # Si no se ha guardado ninguno devolvemos un mensaje.
            if aux == 0:
                return(print('Ha seleccionado no devolver nada, vuelva a Ajustes.'))
                
            # En caso contrario devolvemos la tupla con todas las variables elegidas.
            else:
                return tuple(lista)
        
        # Si no se han definido los datos o no se han comprobado las hipotesis habrá un error y devolveremos un mesaje.
        except:
            print('Puede no tener solución, compruebe las hipótesis o defina previamente los datos.')
            
    def AB_AM(self):
        """
        Resuelve un problema de valores iniciales mediante el método de Adams-Bashforth pedictor y Adams-Moulton corrector con inicialización de Euler-Cauchy.
    
        Parámetros previamente definidos:
            f: Función que definela EDO.
            x0: Dato inicial.
            a, b: Intervalo.
            h: Paso de tiempo.
            
        Return:
            Según las opciones selecionadas puede devolver:
            x: Puntos que definen la función solución.
            tim: Tiempo de ejecución del programa.
            er: Diferencia entre los puntos dados por el método y los dados por Python.
            inf: Diferencia entre los puntos dados por el método y los dados por Python en norma infinito).
            lis: Soporte de puntos utilizados
        """
        # Comprobamos si hay algún error.
        try:
            
            # Definimos una lista donde guardaremos los resultados y una variable auxiliar.
            lista = []
            aux = 0
            
            # Comprobamos que los parámetros han sido definidos, si no los definimos
            if self.f == None:
                print('No ha definido previamente la función.')
                self.Funcion_dos_variables()
                print('\n')
                
            if self.f == None:
                return
            
            if self.x0 == None:
                print('No ha definido previamente el valor inicial.')
                self.x0 = self.ValorInicial()
                print('\n')
                
            if self.x0 == None:
                return
                
            if self.a == None or self.b == None:
                print('No se ha definido previamente el intervalo.')
                self.Intervalo()
                print('\n')
                
            if self.a == None or self.b == None:
                return
            
            if self.h == None:
                print('No ha definido previamente el paso de tiempo.')
                self.Paso_de_tiempo()
                print('\n')
                
            if self.h == None:
                return
            
            # Creamos las variables auxiliares.
            f = self.f
            a = self.a
            h = self.h
            yn = self.x0
            t_v = self.Soporte_tamanio()
            t = t_v[1]
            N = t_v[0]
            
            # Iniciamos la lista de soluciones con el valor inicial.
            sol = [yn]
    
            for i in range(1):
        
                # Calculamos la inicialización de Euler-Cauchy.
                tn = t[i]
                
                #Si lo ha elegido mostramos cada nodo calculado.
                if self.nod == True:
                    print('Nodo',i+1,':','(',tn,',',yn,')')
                    print('-------------------------------------------------')
                
                k1 = yn + h/2 * f(tn, yn)
                yn = yn + h*f(tn + h/2, k1)
                sol.append(yn)
                
            y0 = sol[0]
            y1 = sol[1]
            f0 = f(a, y0)
            f1 = f(a + h, y1)
            
            for i in range(N-1):
                
                #Si lo ha elegido mostramos cada nodo calculado.
                if self.nod == True:
                    print('Nodo',i+2,':','(',t[i+1],',',yn,')')
                    print('-------------------------------------------------')
                
                # Calculamos la solución de Adams-Bashforth (predictor) y Adams-Moulton(corrector).
                yn_pred = yn + h/2 * (3*f1 - f0)
                tn = t[i+2]
                fn = f(tn, yn_pred)
                yn = yn + h/12 * (5*fn + 8*f1 - f0)
                sol.append(yn)
                f0 = f1
                f1 = f(tn, yn)
                
            # Mostramos el último nodo calculado en caso de que este se haya elegido:
            
            if self.nod == True:
                print('Nodo',N+1,':','(',t[N],',',yn,')')
                print('-------------------------------------------------')
            
            # Si lo ha elegido guardamos en la lista de devolución las soluciones.
            if self.sol == True:
                lista = lista + [sol]
                aux += 1
                
            # Si lo ha elegido guardamos en la lista de devolución la diferencia en valor absoluto entre la solución del método y la solución calculada por Python.    
            if self.er == True:
                er = self.Error(self.AB_AM)
                lista = lista + [er]
                aux += 1
                
            # Si lo ha elegido guardamos en la lista de devolución la diferencia entre la solución del método y la solución calculada por Python en norma infinito.   
            if self.inf == True:
                er = self.Error(self.AB_AM)
                err_inf = max(max(er))
                lista = lista + [err_inf]
                aux += 1
            
            # Si lo ha elegido guardamos en la lista de devolución el tiempo de ejecución.
            if self.tim == True:
                tim = self.Tiempo(self.AB_AM)
                lista = lista + [tim]
                aux += 1
                
            # Si lo ha elegido guardamos en la lista de devolución el soporte de puntos utilizados.
            if self.lis == True:
                lista = lista + [t]
                aux += 1
                
            # Comprobamos cuantos parámetros se han guardado en la lista de devolución.
            # Si no se ha guardado ninguno devolvemos un mensaje.
            if aux == 0:
                return(print('Ha seleccionado no devolver nada, vuelva a Ajustes.'))
                
            # En caso contrario devolvemos la tupla con todas las variables elegidas.
            else:
                return tuple(lista)
        
        # Si no se han definido los datos o no se han comprobado las hipotesis habrá un error y devolveremos un mesaje.
        except:
            print('Puede no tener solución, compruebe las hipótesis o defina previamente los datos.')
        
    def Sol_Python(self):
        """
        Calculamos la solución dada por Python.
        """
        # Comprobamos si hay algún error.
        try:
            
            # Comprobamos que los parámetros han sido definidos previamente, si no los definimos.
            if self.f == None:
                print('No se ha definido previamente la función:')
                self.Funcion_dos_variables()
                print('\n')
                
            if self.f == None:
                return
            
            if self.x0 == None:
                print('No ha definido previamente el valor inicial:')
                self.x0 = self.ValorInicial()
                print('\n')
                
            if self.x0 == None:
                return
            
            if self.a == None or self.b == None:
                print('No se ha definido previamente el intervalo:')
                self.Intervalo()
                print('\n')
                
            if self.a == None or self.b == None:
                return
            
            if self.h == None:
                print('No ha definido previamente el paso de tiempo:')
                self.Paso_de_tiempo()
                print('\n')
                
            if self.h == None:
                return
        
            # Creamos las variables auxiliares.
            x0 = self.x0
            t_v = self.Soporte_tamanio()
            t = t_v[1]
        
            # Calculamos la solución dada por odeint.
            sol = odeint(self.func, x0, t)
        
            # Devolvemos la solución.
            return sol
        
        # Si no se han definido los datos o no se han comprobado las hipotesis habrá un error y devolveremos un mesaje.
        except:
            print('Puede no tener solución, compruebe las hipótesis o defina previamente los datos.')
                       
####################################################### CLASE TEMA 5 ##################################################    
    
class Base_EDO_Sistemas(Base_Global):
    
    def AuxAjustes(self,opcion):
        """
        Traduce las opciones de True o False
        """
        if opcion == True:
            cad = 'Si'
        else:
            cad = 'No'
        return(cad)
    
    def Ajustes(self):
        """
        Muestra un menu de ajustes para cambiar las configuraciones de BuscaRaices
        """
        Op = [self.sol, self.tim, self.er]
        cont = True
        while cont == True:
            cont2 = True
            cad = []
            #Traducimos las opciones para crear el menu de ajustes.
            for i in Op:
                cad.append(self.AuxAjustes(opcion = i))
            #Creamos el menu de ajustes.
            try:
                print('\nAjustes Tema 5:\n')
                print('\t1. Devolver las soluciones: ',cad[0])
                print('\n\t2. Devolver tiempo: ',cad[1])
                print('\n\t3. Devolver error del método:' ,cad[2])
    
                #Pedimos al usuario que introduzca una o varias opciones que desee cambiar y creamos una lista con dichas opciones.
                sel = input('\nSelecciona que opciones deseas cambiar o pulse 0 para acabar:\t')
                sel = sel.split(',')
                #Cambiamos las opciones seleccionadas 
                for j in sel:
                    fallo = j #Esta variable la usamos para mostrar un mensaje de error si la opcion introducida no es valida.
                    k = int(j) - 1
                    if k == -1:
                        cont = False
                    else:
                        if Op[k] == True:
                            Op[k] = False
                        else:
                            Op[k] = True
            except:
                print('\nLa opcion ',fallo,' no es valida')
                while cont2 == True:
                    aux = input('\n¿Desea continuar?\t1. Si\t2. No\t')
                    try:
                        aux = int(aux)
                        if aux == 1:
                            cont2 = False
                        elif aux == 2:
                            cont = False
                            cont2 = False
                        else:
                            print('Opción no valida')
                    except:
                        if aux.upper() == 'SI' or aux.upper() == 'YES' or aux.upper() == 'S' or aux.upper() == 'Y':
                            cont2 = False
                        elif aux.upper() == 'NO' or aux.upper() == 'N':
                            cont = False
                            cont2 = False
                        else:
                            print('Opción no valida')
        #Cambiamos las variables gobales de los ajustes.
        [self.sol, self.tim, self.er] = Op
        cad = []
        #Traducimos los ajustes realizados.
        for i in Op:
            cad.append(self.AuxAjustes(i))
        #Mostramos como han quedado los ajustes al terminar y salimos de la función.
        print('\nAjustes Tema 5: \n')
        print('\t1. Devolver las soluciones:',cad[0])
        print('\n\t2. Devolver tiempo:',cad[1])
        print('\n\t3. Devolver error del método:' ,cad[2])
        
        return
    
    def func(self, xy, t):
        """
        Define el sistema de ecuaciones de forma vectorial.
        """
        x, y = xy
        
        # Comprobamos que los parámetros han sido definidos, si no los definimos
        if self.f == None or self.g == None:
            print('No ha definido previamente las funciones.')
            self.f = self.Funcion_varias_variables()
            self.g = self.Funcion_varias_variables()
            
        if self.f == None or self.g ==  None:
            return
            
        # Creamos las variables auxiliares.
        f = self.f
        g = self.g
        
        return [f(t, x, y), g(t,x,y)]
    
    def Instantes(self):
        if self.a == None or self.b == None:
            print('Para crear la variable t necesitamos el intervalo.')
            self.Intervalo()
            
        if self.a == None or self.b == None:
            return
            
        a = self.a
        b = self.b
        
        t = np.linspace(a, b, 10)
        
        self.t = t
        
    def Funcion_varias_variables(self): 
        """
        Define la función que usaremos en los métodos.
        """
        aux = 1
        
        while aux == 1:
            
            # Nos aseguramos de que introduce un número válido.
            try:
                
                # Pedimos la función.
                h = input('Introduce la función, con variable t, x, y:  ')
                    
                # Creamos las variables como simbolo.
                x = sp.symbols('t')
                y = sp.symbols('x')
                z = sp.symbols('y')
                
                # Convertimos la cadena a función.
                f = sp.lambdify([x, y, z], h, "numpy")
                    
                # Comprobamos que la función es válida, si no lo es al evaluarla dará error.
                f(1, 1, 1)
                
                # Salimos del bucle.
                aux = 0
                    
                # Devolvemos la función.
                return f
                    
            # En caso de que el valor no sea válido, establece una rutina para volver a intentar o cancelar.
            except:

                r2 = input('La función no es válida, ¿Desea volver a intentarlo? S/N: ')
                  
                  
                if r2 == 's' or r2 == 'S':
                     
                    # Volvemos al bucle.
                    aux = 1
                    
                else:
                    
                    # Salimos de la función.
                    print("Operación cancelada.")
                    return
                
    def Tiempo(self, s):
        """
        Devuelve el tiempo que tarda en ejecutarse el método.
        
        Agr:
            s: Método del que desea saber el tiempo de ejecución.
            
        """
    
        # Guardamos las antiguas opciones para devolver en los métodos.
        old_sol, old_er = self.sol, self.er
        
        # Asignamos que devuelva solo la raíz.
        self.sol, self.tim, self.er = True, False, False
        
        # Comprobamos el tiempo antes de hacer los calculos.
        start = tm.time()
            
        # Llamamos a la función 1000 veces.
        for i in range(1000):
            s()
                
        # Dejamos las opciones como estaban.
        self.sol, self.er, self. tim = old_sol, old_er, True
            
        # Devolvemos el tiempo el promedio de tiempo que tarda en ejecutarse la función.
        return (tm.time() - start)/1000
                
    def Error(self, s):
        """
        Devuelve la diferencia en valor absoluto entre la solución calculada mediante el método elegido y la solución dada por Python.
        
        Agr:
            s: Método elegido.
            
        """
    
        # Guardamos las antiguas opciones para devolver en los métodos.
        old_sol, old_tim = self.sol, self.tim
        
        # Asignamos que devuelva solo la raíz.
        self.sol, self.tim, self.ite, self.er = True, False, False, False
       
        # Calculamos la raíz del método elegido y la raíz dada por Python.
        sol_s = s()
        sol_p = self.Sol_Python()
        
        # Dejamos las opciones como estaban.
        self.sol, self.tim, self.er = old_sol, old_tim, True
        
        # Sacamos las soluciones de cada función.
        sol_s_x = sol_s[0]
        sol_s_y = sol_s[1]
        
        sol_p_x = list(sol_p[0])
        sol_p_y = list(sol_p[1])
        
        # Sacamos los errores de cada función.
        eX = [abs(sol_s_x[i] - sol_p_x[i]) for i in range(len(sol_s_x))]
        eY = [abs(sol_s_y[i] - sol_p_y[i]) for i in range(len(sol_s_y))]
        
        # Devolvemos el error.
        return eX, eY
        
class EDO_Sistemas(Base_EDO_Sistemas):
    
    def __init__(self, f = None, g = None, x0 = None, y0 = None, t = None, a = None, b = None, sol = True, er = False, tim = False):
        """
        Inicializamos las variables que usaremos para resolver sistema de ecuaciones diferenciales de orden 2.
        
        Agr: 
            f: Primera función del sistema de ecuaciones diferenciales, None por defecto.
            g: Segunda función del sistema de ecuaciones diferenciales, None por defecto.
            x0: Valor inicial de f, None por defecto.
            y0: Valor inicial de g, None por defecto.
            t: Lista que define una partición de instantes para la variable independiente, None por defecto.
            a, b: Extromos del intervalo donde definir t, en caso de no ser recibida, None por defecto.
            sol: Variable para devolver o no las soluciones del sistema, True por defecto.
            er: Variable para devolver o no la diferencia en valor absoluto entre las soluciones dadas por el método y las dadas por Python, False por defecto.
            tim: Variable para devolver o no el tiempo de ejecucion del método, False por defecto.
        
        Return:
            Mensaje de error si fallan los argumentos.
        """
        
        # Definimos los datos.
        self.f = f
        self.g = g
        
        # Comprobamos si se ha introducido algo.
        if type(t) == type(None):
            self.t = t
        else:
            if type(t) == type(np.array([])):
                self.t = t
            else:
                return(print('Error en la entrada de datos.'))
        
        # Comprobamos si se han introducido los valores iniciales.
        if x0 == None and y0 == None:
            self.x0 = x0
            self.y0 = y0
            
        else:
            
            # Se guardarán los datos en caso de que los tipos sean los adecuados.
            try:
                
                self.x0 = float(x0)
                self.y0 = float(y0)
                
            except:
                
                print("Error en los datos de entrada.")
                
        # Comprobamos si se han introducido los límites del intervalo.
        if a == None and b == None:
            self.a = a
            self.b = b
            
        else:
            
            # Se guardarán los datos en caso de que los tipos sean los adecuados.
            try:
                
                self.a = float(a)
                self.b = float(b)
                
            except:
                print("Error en los datos de entrada.")
                
        # Comprobamos que las variables son válidas.
        if type(sol) == bool and type(tim) == bool and type(er) == bool:
        
            self.sol = sol
            self.tim = tim
            self.er = er
            
        else: 
        
            return(print('Error en los datos de entrada'))
                
    def Euler(self):
        """
        Resuelve un sistema de ecuaciones diferenciales mediante el método de Euler.
    
        Parámetros previamente definidos:
            f, g: Funciones que definen el sistema.
            x0, y0: Datos iniciales.
            t : Lista que define una partición de instantes para la variable independiente.
            
        Return:
            Según las opciones selecionadas puede devolver:
            x, y: Puntos que definen las funciones solución.
            tim: Tiempo de ejecución del programa.
            er: Diferencia entre los puntos dados por el méttodo y los dados por Python.
        """
        # Comprobamos si hay algún error.
        try:
            
            # Definimos una lista donde guardaremos los resultados y una variable auxiliar.
            lista = []
            aux = 0
            
            # Comprobamos que los parámetros han sido definidos, si no los definimos
            if self.f == None or self.g == None:
                print('No ha definido previamente las funciones.')
                self.f = self.Funcion_varias_variables()
                self.g = self.Funcion_varias_variables()
                print('\n')
            
            if self.f == None or self.g == None:
                return
            
            if self.x0 == None or self.y0 == None:
                print('No ha definido previamente los valores iniciales. ')
                self.x0, self.y0 = self.ValoresIniciales()
                print('\n')
                
            if self.x0 == None or self.y0 == None:
                return
            
            if type(self.t) == type(None):
                print('No ha definido previamente los instantes.')
                self.Instantes()
                print('\n')
                
            if type(self.t) == type(None):
                return
            
            # Creamos las variables auxiliares.
            f, g = self.f, self.g
            x0, y0 = self.x0, self.y0
            t = self.t
    
            # Sacamos el número de instantes salvo el inicial.
            n = len(t) - 1
    
            # Calculamos el valor de h.
            h = t[1]-t[0]
    
            # Iniciamos la lista de soluciones con los valores iniciales.
            x, y = [x0], [y0]
    
    
            for i in range(n):
        
                # Calculamos la solución de Euler para ambas funciones.
                x = x + [x[i] + h * f(t[i], x[i], y[i])]
                y = y + [y[i] + h * g(t[i], x[i], y[i])]
        
            # Si lo ha elegido guardamos en la lista de devolución las soluciones.
            if self.sol == True:
                lista = lista + [x, y]
                aux += 1
                
            # Si lo ha elegido guardamos en la lista de devolución la diferencia entre la raíz y la raíz calculada por Python.    
            if self.er == True:
                er = self.Error(self.Euler)
                lista = lista + [er]
                aux += 1
            
            # Si lo ha elegido guardamos en la lista de devolución el tiempo de ejecución.
            if self.tim == True:
                tim = self.Tiempo(self.Euler)
                lista = lista + [tim]
                aux += 1
                
            # Comprobamos cuantos parámetros se han guardado en la lista de devolución.
            # Si no se ha guardado ninguno devolvemos un mensaje.
            if aux == 0:
                return(print('Ha seleccionado no devolver nada, vuelva a Ajustes.'))
                
            # En caso contrario devolvemos la tupla con todas las variables elegidas.
            else:
                return tuple(lista)
        
        # Si no se han definido los datos o no se han comprobado las hipotesis habrá un error y devolveremos un mesaje.
        except:
            print('Puede no tener solución, compruebe las hipótesis o defina previamente los datos.')
    
    def Euler_Cauchy(self):
        """
        Resuelve un sistema de ecuaciones diferenciales mediante el método de Euler-Cauchy.
    
        Parámetros previamente definidos:
            f, g: Funciones que definen el sistema.
            x0, y0: Datos iniciales.
            t : Lista que define una partición de instantes para la variable independiente.
            
        Return:
            Según las opciones selecionadas puede devolver:
            x, y: Puntos que definen las funciones solución.
            tim: Tiempo de ejecución del programa.
            er: Diferencia entre los puntos dados por el méttodo y los dados por Python.
        """
        # Comprobamos si hay algún error.
        try:
            
            # Definimos una lista donde guardaremos los resultados y una variable auxiliar.
            lista = []
            aux = 0
            
            # Comprobamos que los parámetros han sido definidos, si no los definimos
            if self.f == None or self.g == None:
                print('No ha definido previamente las funciones.')
                self.f = self.Funcion_varias_variables()
                self.g = self.Funcion_varias_variables()
                print('\n')
                
            if self.f == None or self.g == None:
                return
            
            if self.x0 == None or self.y0 == None:
                print('No ha definido previamente los valores iniciales. ')
                self.x0, self.y0 = self.ValoresIniciales()
                print('\n')
                
            if self.x0 == None or self.y0 == None:
                return
            
            if type(self.t) == type(None):
                print('No ha definido previamente los instantes.')
                self.Instantes()
                print('\n')
                
            if type(self.t) == type(None):
                return
            
            # Creamos las variables auxiliares.
            f, g = self.f, self.g
            x0, y0 = self.x0, self.y0
            t = self.t
    
            # Sacamos el número de instantes salvo el inicial.
            n = len(t) - 1
    
            # Calculamos el valor de h.
            h = t[1]-t[0]
    
            # Iniciamos la lista de soluciones con los valores iniciales.
            x, y = [x0], [y0]
    
    
            for i in range(n):
        
                # Calculamos la solución de Euler-Cauchy para ambas funciones.
                x = x + [x[i] + h * f(t[i] + h/2, x[i] + h/2 * f(t[i], x[i], y[i]), y[i] + h/2 * g(t[i], x[i], y[i]))]
                y = y + [y[i] + h * g(t[i] + h/2, x[i] + h/2 * f(t[i], x[i], y[i]), y[i] + h/2 * g(t[i], x[i], y[i]))]
        
            # Si lo ha elegido guardamos en la lista de devolución las soluciones.
            if self.sol == True:
                lista = lista + [x, y]
                aux += 1
                
            # Si lo ha elegido guardamos en la lista de devolución la diferencia entre la raíz y la raíz calculada por Python.    
            if self.er == True:
                er = self.Error(self.Euler_Cauchy)
                lista = lista + [er]
                aux += 1
            
            # Si lo ha elegido guardamos en la lista de devolución el tiempo de ejecución.
            if self.tim == True:
                tim = self.Tiempo(self.Euler_Cauchy)
                lista = lista + [tim]
                aux += 1
                
            # Comprobamos cuantos parámetros se han guardado en la lista de devolución.
            # Si no se ha guardado ninguno devolvemos un mensaje.
            if aux == 0:
                return(print('Ha seleccionado no devolver nada, vuelva a Ajustes.'))
   
            # En caso contrario devolvemos la tupla con todas las variables elegidas.
            else:
                return tuple(lista)
        
        # Si no se han definido los datos o no se han comprobado las hipotesis habrá un error y devolveremos un mesaje.
        except:
            print('Puede no tener solución, compruebe las hipótesis o defina previamente los datos.')
    
    def Heunn(self):
        """
        Resuelve un sistema de ecuaciones diferenciales mediante el método de Heunn.
    
        Parámetros previamente definidos:
            f, g: Funciones que definen el sistema.
            x0, y0: Datos iniciales.
            t : Lista que define una partición de instantes para la variable independiente.
            
        Return:
            Según las opciones selecionadas puede devolver:
            x, y: Puntos que definen las funciones solución.
            tim: Tiempo de ejecución del programa.
            er: Diferencia entre los puntos dados por el méttodo y los dados por Python.
        """
        
        # Comprobamos si hay algún error.
        try:
            
            # Definimos una lista donde guardaremos los resultados y una variable auxiliar.
            lista = []
            aux = 0
        
            # Comprobamos que los parámetros han sido definidos, si no los definimos
            if self.f == None or self.g == None:
                print('No ha definido previamente las funciones.')
                self.f = self.Funcion_varias_variables()
                self.g = self.Funcion_varias_variables()
                print('\n')
            
            if self.f == None or self.g == None:
                return
            
            if self.x0 == None or self.y0 == None:
                print('No ha definido previamente los valores iniciales. ')
                self.x0, self.y0 = self.ValoresIniciales()
                print('\n')
                
            if self.x0 == None or self.y0 == None:
                return
            
            if type(self.t) == type(None):
                print('No ha definido previamente los instantes.')
                self.Instantes()
                print('\n')
                
            if type(self.t) == type(None):
                return
            
            # Creamos las variables auxiliares.
            f, g = self.f, self.g
            x0, y0 = self.x0, self.y0
            t = self.t
    
            # Sacamos el número de instantes salvo el inicial.
            n = len(t) - 1
    
            # Calculamos el valor de h.
            h = t[1]-t[0]
    
            # Iniciamos la lista de soluciones con los valores iniciales.
            x, y = [x0], [y0]
    
    
            for i in range(n):
            
                # Definimos variables auxiliares.
                f0 = f(t[i], x[i], y[i]) 
            
                # f en la etapa i+1.
                f1 = x[i] + h * f(t[i], x[i], y[i])
            
                g0 = g(t[i], x[i], y[i]) 
            
                # g en la etapa i+1.
                g1 = y[i] + h * g(t[i], x[i], y[i]) 
            
                # Calculamos la solución de Heunn para ambas funciones.
                x = x + [x[i] + h/2 * (f0 + f(t[i+1], f1, g1))]
                y = y + [y[i] + h/2 * (g0 + g(t[i+1], f1, g1))]
        
            # Si lo ha elegido guardamos en la lista de devolución las soluciones.
            if self.sol == True:
                lista = lista + [x, y]
                aux += 1
                
            # Si lo ha elegido guardamos en la lista de devolución la diferencia entre la raíz y la raíz calculada por Python.    
            if self.er == True:
                er = self.Error(self.Heunn)
                lista = lista + [er]
                aux += 1
            
            # Si lo ha elegido guardamos en la lista de devolución el tiempo de ejecución.
            if self.tim == True:
                tim = self.Tiempo(self.Heunn)
                lista = lista + [tim]
                aux += 1
                
            # Comprobamos cuantos parámetros se han guardado en la lista de devolución.
            # Si no se ha guardado ninguno devolvemos un mensaje.
            if aux == 0:
                return(print('Ha seleccionado no devolver nada, vuelva a Ajustes.'))
                
            # En caso contrario devolvemos la tupla con todas las variables elegidas.
            else:
                return tuple(lista)
        
        # Si no se han definido los datos o no se han comprobado las hipotesis habrá un error y devolveremos un mesaje.
        except:
            print('Puede no tener solución, compruebe las hipótesis o defina previamente los datos.')
    
    def Runge_Kutta(self):
        """
        Resuelve un sistema de ecuaciones diferenciales mediante el método de Runge-Kutta.
    
        Parámetros previamente definidos:
            f, g: Funciones que definen el sistema.
            x0, y0: Datos iniciales.
            t : Lista que define una partición de instantes para la variable independiente.
            
        Return:
            Según las opciones selecionadas puede devolver:
            x, y: Puntos que definen las funciones solución.
            tim: Tiempo de ejecución del programa.
            er: Diferencia entre los puntos dados por el méttodo y los dados por Python.
        """
        
        # Comprobamos si hay algún error.
        try: 
        
            # Definimos una lista donde guardaremos los resultados y una variable auxiliar.
            lista = []
            aux = 0
            
            # Comprobamos que los parámetros han sido definidos, si no los definimos
            if self.f == None or self.g == None:
                print('No ha definido previamente las funciones.')
                self.f = self.Funcion_varias_variables()
                self.g = self.Funcion_varias_variables()
                print('\n')
                
            if self.f == None or self.g == None:
                return
            
    
            if self.x0 == None or self.y0 == None:
                print('No ha definido previamente los valores iniciales. ')
                self.x0, self.y0 = self.ValoresIniciales()
                print('\n')
                
            if self.x0 == None or self.y0 == None:
                return
            
            if type(self.t) == type(None):
                print('No ha definido previamente los instantes.')
                self.Instantes()
                print('\n')
                
            if type(self.t) == type(None):
                return
            
            # Creamos las variables auxiliares.
            f, g = self.f, self.g
            x0, y0 = self.x0, self.y0
            t = self.t
    
            # Sacamos el número de instantes salvo el inicial.
            n = len(t) - 1
    
            # Calculamos el valor de h.
            h = t[1]-t[0]
    
            # Iniciamos la lista de soluciones con los valores iniciales.
            x, y = [x0], [y0]
    
    
            for i in range(n):
            
                # Definimos variables auxiliares.
                m1 = h * f(t[i], x[i], y[i])
                k1 = h * g(t[i], x[i], y[i])
            
                m2 = h * f(t[i] + h/2, x[i] + m1/2, y[i] + k1/2)
                k2 = h * g(t[i] + h/2, x[i] + m1/2, y[i] + k1/2)
            
                m3 = h * f(t[i] + h/2, x[i] + m2/2, y[i] + k2/2)
                k3 = h * g(t[i] + h/2, x[i] + m2/2, y[i] + k2/2)
            
                m4 = h * f(t[i] + h, x[i] + m3, y[i] + k3)
                k4 = h * g(t[i] + h, x[i] + m3, y[i] + k3)
            
                # Calculamos la solución de Runge-Kutta para ambas funciones.
                x = x + [x[i] + 1/6 * (m1 + 2 * m2 + 2 * m3 + m4)]
                y = y + [y[i] + 1/6 * (k1 + 2 * k2 + 2 * k3 + k4)]
        
            # Si lo ha elegido guardamos en la lista de devolución las soluciones.
            if self.sol == True:
                lista = lista + [x, y]
                aux += 1
                
            # Si lo ha elegido guardamos en la lista de devolución la diferencia entre la raíz y la raíz calculada por Python.    
            if self.er == True:
                er = self.Error(self.Runge_Kutta)
                lista = lista + [er]
                aux += 1
            
            # Si lo ha elegido guardamos en la lista de devolución el tiempo de ejecución.
            if self.tim == True:
                tim = self.Tiempo(self.Runge_Kutta)
                lista = lista + [tim]
                aux += 1
                
                
            # Comprobamos cuantos parámetros se han guardado en la lista de devolución.
            # Si no se ha guardado ninguno devolvemos un mensaje.
            if aux == 0:
                return(print('Ha seleccionado no devolver nada, vuelva a Ajustes.'))
   
            # En caso contrario devolvemos la tupla con todas las variables elegidas.
            else:
                return tuple(lista)
    
        # Si no se han definido los datos o no se han comprobado las hipotesis habrá un error y devolveremos un mesaje.
        except:
            print('Puede no tener solución, compruebe las hipótesis o defina previamente los datos.')
    
    def Sol_Python(self):
        """
        Calculamos la solución dada por Python.
        """
        # Comprobamos si hay algún error.
        try:
            
            # Comprobamos que los parámetros han sido definidos previamente, si no los definimos.
            if self.x0 == None or self.y0 == None:
                print('No ha definido previamente los valores iniciales. ')
                self.x0, self.y0 = self.ValoresIniciales()
                
            if self.x0 == None or self.y0 == None:
                return
            
            if type(self.t) == type(None):
                print('No ha definido previamente los instantes.')
                self.Instantes()
                
            if type(self.t) == type(None):
                return
        
            # Creamos las variables auxiliares.
            x0 = self.x0
            y0 = self.y0
            t = self.t
        
            # Calculamos la solución dada por odeint.
            sol = odeint(self.func, [x0, y0], t)
        
            # Sacamos las soluciones por separado.
            x = sol[:,0]
            y = sol[:,1]
        
            # Devolvemos las soluciones.
            return x, y
        
        # Si no se han definido los datos o no se han comprobado las hipotesis habrá un error y devolveremos un mesaje.
        except:
            print('Puede no tener solución, compruebe las hipótesis o defina previamente los datos.')
    