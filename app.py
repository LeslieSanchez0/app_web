from flask import Flask, render_template

#Para crear el objeto
app = Flask(__name__)  

# Decorador para la ruta principal
@app.route('/')
def home():
    return render_template('index.html') # Renderiza el archivo index.html

if __name__ == '__main__':
    # Ejecutar la aplicación en modo de depuración
    app.run(debug=True)  # Cambia el puerto si es necesario

