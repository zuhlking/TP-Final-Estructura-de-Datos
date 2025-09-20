# Desarrollo de proyecto – Entrega 1
## 1. Objetivo del Proyecto

El trabajo consiste en modelar un Cliente de Correo Electrónico en Python, aplicando Programación Orientada a Objetos y las estructuras de datos vistas en la cursada.
**El Cliente de Correo Electrónico permitirá:**

- Gestionar usuarios registrados o registrar nuevos usuarios en un servidor de correo.
- Enviar y recibir mensajes entre usuarios.
- Organizar mensajes en carpetas (Bandeja de entrada, Enviados, Papelera, etc.).
- Listar mensajes y aplicar operaciones básicas (leer, borrar, mover).

## 2. Modelado de clases, encapsulamiento y uso de estructuras de datos.

**Clases Principales**
### Clase Usuario

**Atributos:**

- _id (int, único por usuario, puede generarse automáticamente)
- _nombre (str)
- _email (str, único, usado como identificador principal)
- _password (str, aunque mas adelante se debería encriptar)
- _carpetas (dict con nombre → Carpeta, ejemplo: "Inbox", "Enviados", "Spam")

**Métodos:**

- verificar_password(password) → retorna True/False según coincida
- recibir_mensaje(mensaje) → guarda en carpeta "Inbox"
- enviar_mensaje(destinatario, asunto, cuerpo, servidor) → solicita al servidor enviar el mensaje
- crear_carpeta(nombre) → agrega una nueva carpeta
- listar_carpetas() → devuelve lista de nombres de carpetas

### Clase Mensaje

**Atributos:**

- _remitente (Usuario)
- _destinatario (Usuario)
- _asunto (str)
- _cuerpo (str)
- _leido (bool, por defecto False)

**Métodos:**

- marcar_leido()
- __str__() → representación del mensaje

### Clase Carpeta

**Atributos:**

- _nombre (str)
- _mensajes (list de Mensaje)

**Métodos:**

- agregar_mensaje(mensaje)
- eliminar_mensaje(mensaje)
- listar_mensajes()

### Clase ServidorCorreo

**Atributos:**

- _usuarios (dict email → Usuario)

**Métodos:**

- registrar_usuario(id_usuario, nombre, email, password) → crea un usuario nuevo (si el email no existe)
- autenticar_usuario(email, password) → retorna el objeto Usuario si las credenciales son correctas
- enviar_mensaje(remitente, destinatario, asunto, cuerpo) → genera un objeto Mensaje, lo agrega al Inbox del destinatario y a Enviados del remitente
- listar_usuarios() → devuelve todos los usuarios registrados

## 3. Estructuras de Datos a Utilizar

- Diccionario (dict): para mapear usuarios por su email en el servidor.
- Listas (list): para almacenar mensajes en cada carpeta.
- Encapsulamiento: todos los atributos serán privados (_atributo) y se accederá mediante propiedades y métodos.

## 4. Justificación de Diseño

Para el trabajo usamos Clases en Python que representan las partes principales de un sistema de correo electrónico. Esto nos permite organizar el código y trabajar con objetos.

- ServidorCorreo: funciona como intermediario. Cuando un usuario envía un mensaje, el servidor se encarga de entregarlo al destinatario correcto. 
- Usuario: cada usuario tiene un email y una contraseña para identificarse. Además, dispone de sus propias carpetas (por ejemplo, Inbox y Enviados)
- Mensaje: es el objeto que viaja de un usuario a otro. Su contenido (remitente, destinatario, asunto y cuerpo) no cambia una vez creado, pero sí puede modificarse su estado, como por ejemplo marcarlo como leído o no leído.
- Carpeta: permite almacenar mensajes dentro de cada usuario. Así se mantiene separado lo que está en la bandeja de entrada, en enviados u otras carpetas que el usuario quiera crear.

**Estructuras de datos a utilizar:**

- Usamos un diccionario (dict) para guardar a los usuarios en el servidor, ya que permite buscarlos rápidamente por su clave.
- Usamos una lista (list) para manejar los mensajes dentro de una carpeta, ya que es una estructura simple y flexible para almacenar colecciones en orden.


```mermaid
flowchart TD

    A([Inicio]) --> B[Registrar usuario]
    B -->|Éxito| C[Autenticar usuario]
    B -->|Email ya registrado| B2[Error y volver]

    C -->|Credenciales válidas| D[Usuario autenticado]
    C -->|Credenciales inválidas| C2[Error de autenticación]

    D --> E[Acción: Enviar Mensaje]
    D --> F[Acción: Recibir Mensaje]
    D --> G[Acción: Listar Carpetas]

    E --> H[ServidorCorreo verifica usuarios]
    H -->|Usuarios válidos| I[Crear Mensaje]
    I --> J[Agregar a Inbox del destinatario]
    I --> K[Agregar a Enviados del remitente]
    J --> L[Confirmar envío]
    K --> L

    F --> M[Guardar en Inbox del usuario]
    M --> L

    G --> N[Listar carpetas del usuario]
    N --> L

    L --> O([Fin])