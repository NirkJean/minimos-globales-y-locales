import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Título de la aplicación
st.title("Solución Interactiva de Ejercicios de Optimización")

# Ejercicio general donde el usuario ingresa la función
st.header("Ejercicio: Ingrese su propia función para analizarla")

# Entrada de la función por parte del usuario
user_function = st.text_input("Introduce la función (por ejemplo, x**2 - 4*x + 5):")

# Verificar que el usuario haya ingresado una función
if user_function:
    try:
        # Crear una variable simbólica 'x'
        x = sp.symbols('x')

        # Convertir la cadena a una expresión simbólica
        f = sp.sympify(user_function)

        # Derivar la función
        f_prime = sp.diff(f, x)
        f_double_prime = sp.diff(f_prime, x)

        # Mostrar la función original y sus derivadas
        st.write(f"Función original: {f}")
        st.write(f"Primera derivada: {f_prime}")
        st.write(f"Segunda derivada: {f_double_prime}")

        # Entrada de valor para evaluar en x
        x_input = st.number_input("Introduce el valor de x:", min_value=-10.0, max_value=10.0, value=0.0)

        # Evaluar la función y sus derivadas en el punto x_input
        f_at_x = f.subs(x, x_input)
        f_prime_at_x = f_prime.subs(x, x_input)
        f_double_prime_at_x = f_double_prime.subs(x, x_input)

        # Mostrar resultados
        st.write(f"f({x_input}) = {f_at_x}")
        st.write(f"f'({x_input}) = {f_prime_at_x}")
        st.write(f"f''({x_input}) = {f_double_prime_at_x}")

        # Verificar si es un mínimo o máximo
        if f_prime_at_x == 0:  # Solo si la derivada es cero, podemos proceder a evaluar el tipo de mínimo
            if f_double_prime_at_x > 0:
                st.write(f"El punto x = {x_input} es un **mínimo local**.")
                st.write("Como la función es cuadrática o tiene una curvatura positiva (f'' > 0), es un mínimo local.")
            elif f_double_prime_at_x < 0:
                st.write(f"El punto x = {x_input} es un **máximo local**.")
                st.write("Como la función tiene una curvatura negativa (f'' < 0), es un máximo local.")
            else:
                st.write(f"El punto x = {x_input} es un **punto de inflexión**.")
                st.write("Dado que la segunda derivada es cero, la curvatura es plana en este punto.")
        else:
            st.write(f"El punto x = {x_input} no es un **punto crítico** ya que f'({x_input}) ≠ 0.")
            st.write("Esto significa que no podemos clasificarlo como un mínimo o máximo local.")

        # Graficar la función
        st.write("### Gráfico de la función ingresada")
        # Convertir la función a una función numérica para graficarla
        f_lambda = sp.lambdify(x, f, 'numpy')
        x_vals = np.linspace(-10, 10, 400)
        y_vals = f_lambda(x_vals)

        # Graficar
        plt.plot(x_vals, y_vals, label=f'{user_function}')
        plt.scatter(x_input, f_at_x, color='red', zorder=5)
        plt.text(x_input, f_at_x + 0.5, f'Valor en x = {x_input}', horizontalalignment='center')
        plt.title(f"Gráfico de {user_function}")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)
        plt.legend()
        st.pyplot(plt)

    except Exception as e:
        st.error(f"Hubo un error al procesar la función: {e}")


# Ejercicio 2: Función f(x) = |x| o cualquier función con parámetros
st.header("Ejercicio 2: Dibuja la función \( f(x) = |x| \) o ingresa tu propia función y determina si tiene un mínimo global o local en \( x = 0 \)")

# Entrada de la función por parte del usuario
user_function = st.text_input("Introduce la función (por ejemplo, abs(x) o x**2 - 4*x + 5):")

# Verificar que el usuario haya ingresado una función
if user_function:
    try:
        # Crear una variable simbólica 'x'
        x = sp.symbols('x')

        # Convertir la cadena a una expresión simbólica
        f = sp.sympify(user_function)

        # Mostrar la función original
        st.write(f"Función original: {f}")

        # Evaluar la función en x = 0
        f_at_0 = f.subs(x, 0)

        # Verificar si x = 0 es un mínimo global
        if isinstance(f, sp.Abs):  # Caso específico de f(x) = |x|
            st.write(f"f(x) = |x| es una función que siempre tiene valores mayores o iguales a 0.")
            st.write(f"f(0) = {f_at_0}, y para cualquier otro valor de x, f(x) > 0.")
            st.write(f"Por lo tanto, \( x = 0 \) es un **mínimo global** para esta función.")
        else:
            # Verificar que la función tenga un mínimo global en x = 0 para otras funciones
            # Generalmente f(0) debe ser el mínimo si la función es siempre no negativa
            f_vals = [f.subs(x, i) for i in np.linspace(-10, 10, 400) if i != 0]  # Evaluar para otros x
            if f_at_0 <= min(f_vals):
                st.write(f"Para cualquier otro valor de \( x \), f(x) > {f_at_0}. Por lo tanto, \( x = 0 \) es un **mínimo global**.")
            else:
                st.write(f"Para la función ingresada, no podemos afirmar que \( x = 0 \) sea un mínimo global en todo su dominio.")

        # Graficar la función
        st.write("### Gráfico de la función ingresada")
        # Convertir la función a una función numérica para graficarla
        f_lambda = sp.lambdify(x, f, 'numpy')
        x_vals = np.linspace(-10, 10, 400)
        y_vals = f_lambda(x_vals)

        # Graficar
        plt.plot(x_vals, y_vals, label=f'{user_function}')
        plt.scatter(0, f_at_0, color='red', zorder=5)
        plt.text(0, f_at_0 + 0.5, f'Valor en x = 0', horizontalalignment='center')
        plt.title(f"Gráfico de {user_function}")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)
        plt.legend()
        st.pyplot(plt)

    except Exception as e:
        st.error(f"Hubo un error al procesar la función: {e}")


# Ejercicio 3: Teorema de Weierstrass para función en un intervalo
st.header("Ejercicio 3: Utilizando el Teorema de Weierstrass, explica por qué una función tiene un mínimo global en un intervalo")

# Entrada de la función por parte del usuario
user_function = st.text_input("Introduce la función (por ejemplo, sin(x), x**2 - 4*x + 5):")

# Entrada para el intervalo [a, b]
interval_start = st.number_input("Introduce el inicio del intervalo (a):", value=0.0)
interval_end = st.number_input("Introduce el fin del intervalo (b):", value=np.pi)

# Verificar que el usuario haya ingresado una función y que el intervalo sea válido
if user_function and interval_start < interval_end:
    try:
        # Crear una variable simbólica 'x'
        x = sp.symbols('x')

        # Convertir la cadena de texto a una expresión simbólica
        f = sp.sympify(user_function)

        # Mostrar la función original
        st.write(f"Función original: {f}")

        # Verificar si la función es continua en el intervalo
        # Evaluar la función en los extremos del intervalo y en el medio
        f_at_a = f.subs(x, interval_start)
        f_at_b = f.subs(x, interval_end)
        f_at_half = f.subs(x, (interval_start + interval_end) / 2)

        # Mostrar las evaluaciones de la función
        st.write(f"f({interval_start}) = {f_at_a}")
        st.write(f"f({interval_end}) = {f_at_b}")
        st.write(f"f({(interval_start + interval_end) / 2}) = {f_at_half}")

        # Aplicar el teorema de Weierstrass
        st.write("**Teorema del Valor Extremo de Weierstrass**: Si una función es continua en un conjunto cerrado y acotado, entonces alcanza un máximo y un mínimo global en ese conjunto.")
        st.write(f"La función f(x) = {user_function} es continua en el intervalo cerrado y acotado \( [{interval_start}, {interval_end}] \), por lo que debe alcanzar un mínimo global y un máximo global en este intervalo.")

        # Verificar el mínimo y máximo global
        min_value = min(f_at_a, f_at_b, f_at_half)
        max_value = max(f_at_a, f_at_b, f_at_half)

        # Determinar el mínimo global
        if min_value == f_at_a:
            st.write(f"El mínimo global de la función en el intervalo [{interval_start}, {interval_end}] es f({interval_start}) = {f_at_a} .")
        elif min_value == f_at_b:
            st.write(f"El mínimo global de la función en el intervalo [{interval_start}, {interval_end}] es f({interval_end}) = {f_at_b} .")
        else:
            st.write(f"El mínimo global de la función en el intervalo [{interval_start}, {interval_end}] es f({(interval_start + interval_end) / 2}) = {f_at_half} .")

        # Graficar la función
        st.write("### Gráfico de la función en el intervalo dado")
        # Convertir la función a una función numérica para graficarla
        f_lambda = sp.lambdify(x, f, 'numpy')
        x_vals = np.linspace(interval_start, interval_end, 400)
        y_vals = f_lambda(x_vals)

        # Graficar
        plt.plot(x_vals, y_vals, label=f'{user_function}')
        plt.scatter([interval_start, interval_end, (interval_start + interval_end) / 2], [f_at_a, f_at_b, f_at_half], color='red', zorder=5)
        plt.text(interval_start, f_at_a, f'f({interval_start}) = {f_at_a}', horizontalalignment='center', verticalalignment='bottom')
        plt.text(interval_end, f_at_b, f'f({interval_end}) = {f_at_b}', horizontalalignment='center', verticalalignment='top')
        plt.text((interval_start + interval_end) / 2, f_at_half, f'f(mid) = {f_at_half}', horizontalalignment='center', verticalalignment='bottom')

        plt.title(f"Gráfico de {user_function} en el intervalo [{interval_start}, {interval_end}]")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)
        plt.legend()
        st.pyplot(plt)

    except Exception as e:
        st.error(f"Hubo un error al procesar la función: {e}")


# Ejercicio 4: Mínimo global de f(x, y) = x² + y² con la restricción x² + y² ≤ 1
st.header("Ejercicio 4: Considera f(x, y) = x^2 + y^2 con x^2 + y^2 <= 1.  ¿Dónde se encuentra el mínimo global?")

# Entrada de los valores de x y y
x_input = st.number_input("Introduce el valor de x:", min_value=-1.0, max_value=1.0, value=0.0)
y_input = st.number_input("Introduce el valor de y:", min_value=-1.0, max_value=1.0, value=0.0)

# Función f(x, y) = x² + y²
def f(x, y):
    return x**2 + y**2

# Evaluar la función f(x, y) en el punto ingresado
f_at_point = f(x_input, y_input)

# Mostrar los resultados
st.write(f"f(x, y) = x² + y²")
st.write(f"f({x_input}, {y_input}) = {f_at_point}")

# Determinar el mínimo global
f_min = f(0, 0)  # El mínimo global está en (0, 0)
if f_at_point == f_min:
    st.write(f"El punto (x, y) = (0, 0)es el **mínimo global** con valor f(0, 0) = 0 .")
else:
    st.write(f"El valor mínimo global de la función es f(0, 0) = 0, que ocurre en el centro del dominio (x, y) = (0, 0).")

# Graficar la función y la restricción x² + y² ≤ 1
st.write("### Gráfico de la función f(x, y) = x^2 + y^2 en el dominio x^2 + y^2 <= 1 ")

# Generar puntos para graficar el círculo de la restricción
theta = np.linspace(0, 2*np.pi, 400)
x_circle = np.cos(theta)
y_circle = np.sin(theta)

# Graficar el círculo con la restricción
plt.plot(x_circle, y_circle, label=r'$x^2 + y^2 = 1$', color="blue")
plt.fill(x_circle, y_circle, color="lightblue", alpha=0.5)

plt.scatter(x_input, y_input, color="red", zorder=5)
plt.text(x_input, y_input + 0.05, f"f({x_input}, {y_input}) = {f_at_point}", horizontalalignment='center')

# Marcar el mínimo global (0, 0)
plt.scatter(0, 0, color="green", zorder=5)
plt.text(0, 0.05, "Mínimo global (0, 0)", horizontalalignment='center')

plt.title(r"$f(x, y) = x^2 + y^2$")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.grid(True)
plt.legend()
st.pyplot(plt)


# Ejercicio 5: Mínimo global no único
st.header("Ejercicio 5: Diseña un ejemplo donde un mínimo global no sea único")

# Entrada de la función por parte del usuario
user_function = st.text_input("Introduce la función (por ejemplo, cos(x), x**2 - 4*x + 5):", "cos(x)")

# Entrada para el intervalo [a, b] con claves únicas
interval_start = st.number_input("Introduce el inicio del intervalo (a):", value=0.0, key="start_value")
interval_end = st.number_input("Introduce el fin del intervalo (b):", value=2*np.pi, key="end_value")

# Verificar que el usuario haya ingresado una función y que el intervalo sea válido
if user_function and interval_start < interval_end:
    try:
        # Crear una variable simbólica 'x'
        x = sp.symbols('x')

        # Convertir la cadena de texto a una expresión simbólica
        f = sp.sympify(user_function)

        # Mostrar la función original
        st.write(f"Función original: {f}")

        # Evaluar la función en los puntos del intervalo [a, b]
        f_at_a = f.subs(x, interval_start)
        f_at_b = f.subs(x, interval_end)
        f_at_pi = f.subs(x, np.pi)
        
        # Mostrar las evaluaciones de la función
        st.write(f"f({interval_start}) = {f_at_a}")
        st.write(f"f({interval_end}) = {f_at_b}")
        st.write(f"f(π) = {f_at_pi}")

        # Aplicar el análisis del mínimo global no único
        if f_at_pi == f_at_b == f_at_a:
            st.write(f"El mínimo global de la función es \( {f_at_a} \) y ocurre en \( x = 0, x = \pi, x = 2\pi \), por lo que no es único.")
        else:
            st.write(f"El mínimo global de la función ocurre en \( x = \pi \) y \( x = 2\pi \), ambos con valor \( f(\pi) = f(2\pi) = -1 \), por lo que el mínimo global no es único.")

        # Graficar la función
        st.write("### Gráfico de la función en el intervalo dado")
        # Convertir la función a una función numérica para graficarla
        f_lambda = sp.lambdify(x, f, 'numpy')
        x_vals = np.linspace(interval_start, interval_end, 400)
        y_vals = f_lambda(x_vals)

        # Graficar
        plt.plot(x_vals, y_vals, label=f'{user_function}')
        plt.scatter([np.pi, 2*np.pi], [-1, -1], color='red', zorder=5)
        plt.text(np.pi, -1.2, f'f(π) = -1', horizontalalignment='center')
        plt.text(2*np.pi, -1.2, f'f(2π) = -1', horizontalalignment='center')
        plt.title(f"Gráfico de {user_function} en el intervalo [{interval_start}, {interval_end}]")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.axhline(0, color='black',linewidth=1)
        plt.axvline(0, color='black',linewidth=1)
        plt.grid(True)
        plt.legend()
        st.pyplot(plt)

    except Exception as e:
        st.error(f"Hubo un error al procesar la función: {e}")

