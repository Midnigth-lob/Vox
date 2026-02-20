# Vox Language - Documentación Completa

## 📋 Tabla de Contenidos

1. [¿Qué es Vox?](#qué-es-vox)
2. [Instalación](#instalación)
3. [Comandos Disponibles](#comandos-disponibles)
4. [Estructura del Proyecto](#estructura-del-proyecto)
5. [Sintaxis del Lenguaje](#sintaxis-del-lenguaje)
6. [Ejemplos Prácticos](#ejemplos-prácticos)
7. [Configuración](#configuración)
8. [Transpilador](#transpilador)
9. [Extension VS Code](#extension-vs-code)
10. [Preguntas Frecuentes](#preguntas-frecuentes)

---

## 🚀 ¿Qué es Vox?

**Vox Language** es un DSL (Domain Specific Language) de Lua en español diseñado específicamente para el desarrollo de juegos en Roblox. Permite escribir código Roblox utilizando palabras clave en español, making it más accesible para desarrolladores hispanohablantes.

### Características Principales:
- ✅ **Sintaxis en español**: Palabras clave en español para mayor claridad
- ✅ **Transpilación automática**: Convierte código Vox a Lua estándar de Roblox
- ✅ **Análisis semántico avanzado**: Detección de errores en tiempo real
- ✅ **Integración con VS Code**: Extension completa con autocompletado
- ✅ **Optimización de código**: Mejoras automáticas de rendimiento
- ✅ **Validación sintáctica**: Errores detectados antes de ejecutar

---

## 📦 Instalación

### Opción 1: Extension de VS Code (Recomendada)

1. Abre VS Code
2. Ve a la sección de Extensiones (Ctrl+Shift+X)
3. Busca "Vox Language - Professional DSL"
4. Haz clic en "Instalar"

### Opción 2: Manual

1. Clona este repositorio:
```bash
git clone https://github.com/vox-studio/vox-language.git
cd vox-language
```

2. Instala dependencias:
```bash
npm install
```

3. Compila la extensión:
```bash
npm run compile
```

4. Empaqueta la extensión:
```bash
npm run package
```

---

## 🎯 Comandos Disponibles

### Comandos de VS Code

| Comando | Atajo | Descripción |
|---------|-------|-------------|
| `Transpilar Archivo Vox` | `Ctrl+Shift+T` | Convierte archivo .vox a .lua |
| `Validar Archivo Vox` | `Ctrl+Shift+V` | Verifica errores sintácticos |
| `Alternar Análisis Semántico` | `Ctrl+Shift+S` | Activa/desactiva análisis avanzado |
| `Mostrar Ayuda de Vox` | - | Muestra información de ayuda |
| `Abrir Documentación` | - | Abre esta documentación |
| `Crear Nuevo Proyecto Vox` | - | Inicia nuevo proyecto |

### Comandos de Terminal

#### build_vox.py - Compilador Principal
```bash
# Uso básico
python build_vox.py archivo.vox

# Con opciones avanzadas
python build_vox.py archivo.vox --output salida.lua --optimizar 3 --minificar --estadisticas
```

**Opciones disponibles:**
- `--output, -o`: Especificar archivo de salida
- `--optimizar [0-3]`: Nivel de optimización (0=ninguna, 3=máxima)
- `--minificar`: Reducir tamaño del archivo
- `--estadisticas`: Mostrar estadísticas de compilación

#### transpiler_final.py - Transpilador Avanzado
```bash
# Transpilar archivo individual
python transpiler_final.py entrada.vox salida.lua

# Transpilar directorio completo
python transpiler_final.py --directorio ./src --salida ./build
```

---

## 🏗️ Estructura del Proyecto

```
Vox/
├── 📁 src/                    # Código fuente de la extensión
│   ├── 📁 compiler/          # Compilador principal
│   ├── 📁 lexer/             # Analizador léxico
│   ├── 📁 parser/            # Analizador sintáctico
│   ├── 📁 semantic/          # Análisis semántico
│   ├── 📁 generator/         # Generador de código
│   └── 📄 extension.ts       # Extensión VS Code
├── 📁 examples/              # Ejemplos de código
├── 📁 tests/                 # Tests unitarios
├── 📁 docs/                  # Documentación adicional
├── 📁 snippets/              # Snippets para VS Code
├── 📁 syntaxes/              # Definición de sintaxis
├── 📄 build_vox.py          # Script de build principal
├── 📄 transpiler_final.py   # Transpilador avanzado
├── 📄 package.json          # Configuración de extensión
└── 📄 *.vox                 # Archivos de ejemplo
```

---

## 📝 Sintaxis del Lenguaje

### Palabras Clave Principales

| Español | Inglés (Lua) | Descripción |
|---------|--------------|-------------|
| `funcion` | `function` | Define una función |
| `fin` | `end` | Finaliza un bloque |
| `si` | `if` | Condición if |
| `entonces` | `then` | Then de condición |
| `sino` | `else` | Else de condición |
| `mientras` | `while` | Bucle while |
| `hacer` | `do` | Do de bucle |
| `para` | `for` | Bucle for |
| `en` | `in` | In de bucle |
| `retornar` | `return` | Retorna valor |
| `local` | `local` | Variable local |
| `y` | `and` | Operador AND |
| `o` | `or` | Operador OR |
| `no` | `not` | Operador NOT |
| `verdadero` | `true` | Boolean true |
| `falso` | `false` | Boolean false |
| `imprimir` | `print` | Imprime en consola |
| `esperar` | `wait` | Espera tiempo |
| `tipo` | `type` | Tipo de dato |
| `pares` | `pairs` | Itera pares clave-valor |
| `ipares` | `ipairs` | Itera arrays indexados |
| `nulo` | `nil` | Valor nulo |
| `romper` | `break` | Rompe bucle |
| `continuar` | `continue` | Continúa bucle |

### Funciones Roblox en Español

| Español | Roblox API | Descripción |
|---------|------------|-------------|
| `obtener_servicio()` | `game:GetService()` | Obtiene servicio de Roblox |
| `instancia_nueva()` | `Instance.new()` | Crea nueva instancia |
| `juego` | `game` | Objeto game principal |
| `esperar()` | `wait()` | Espera tiempo |
| `tick()` | `tick()` | Tiempo actual |
| `time()` | `time()` | Tiempo del juego |

### Servicios Roblox

**⚠️ IMPORTANTE: Los servicios en Vox funcionan EXACTAMENTE como en Roblox Lua**

Los servicios se traducen directamente a sus equivalentes de Roblox API sin modificaciones:

| Español | Roblox Service | Descripción |
|---------|----------------|-------------|
| `espacio_trabajo` | `Workspace` | Espacio de trabajo 3D |
| `jugadores` | `Players` | Servicio de jugadores |
| `luz` | `Lighting` | Servicio de iluminación |
| `sonido` | `SoundService` | Servicio de audio |
| `replicacion` | `ReplicatedStorage` | Almacenamiento replicado |
| `servidor_script` | `ServerScriptService` | Scripts de servidor |
| `servidor_almacen` | `ServerStorage` | Almacenamiento de servidor |
| `tienda_datos` | `DataStoreService` | Servicio de almacenamiento |
| `servicio_tween` | `TweenService` | Servicio de animaciones |
| `servicio_http` | `HttpService` | Servicio HTTP |
| `servicio_mensajes` | `MessagingService` | Servicio de mensajería |
| `servicio_teletransporte` | `TeleportService` | Servicio de teletransporte |
| `servicio_chat` | `Chat` | Servicio de chat |
| `servicio_gui` | `GuiService` | Servicio de GUI |
| `servicio_entrada` | `UserInputService` | Servicio de entrada |
| `servicio_context` | `ContextActionService` | Servicio de contexto |
| `servicio_fisica` | `PhysicsService` | Servicio de física |
| `servicio_carga` | `ContentProvider` | Servicio de contenido |

#### Uso de Servicios

```vox
-- En Vox - Se traduce exactamente a Roblox API
local jugadores = obtener_servicio("jugadores")
local espacio_trabajo = obtener_servicio("espacio_trabajo")
local tienda_datos = obtener_servicio("tienda_datos")

-- Se convierte a:
local jugadores = game:GetService("Players")
local espacio_trabajo = game:GetService("Workspace")
local tienda_datos = game:GetService("DataStoreService")
```

**✅ Compatible al 100% con Roblox Studio**

### Instancias Comunes

| Español | Roblox Instance | Descripción |
|---------|-----------------|-------------|
| `parte` | `Part` | Parte básica 3D |
| `malla_parte` | `MeshPart` | Parte con malla |
| `modelo` | `Model` | Modelo 3D |
| `script` | `Script` | Script de servidor |
| `script_local` | `LocalScript` | Script de cliente |
| `script_modulo` | `ModuleScript` | Módulo reutilizable |
| `texto_cadena` | `StringValue` | Valor de texto |
| `numero_valor` | `NumberValue` | Valor numérico |
| `booleano_valor` | `BoolValue` | Valor booleano |
| `objeto_valor` | `ObjectValue` | Valor de objeto |
| `marco_valor` | `CFrameValue` | Valor CFrame |
| `vector3_valor` | `Vector3Value` | Valor Vector3 |
| `color3_valor` | `Color3Value` | Valor Color3 |
| `ladrillo_color_valor` | `BrickColorValue` | Valor BrickColor |
| `entero_valor` | `IntValue` | Valor entero |
| `doble_valor` | `DoubleValue` | Valor doble |

### UI Elements

| Español | Roblox GUI | Descripción |
|---------|------------|-------------|
| `marco` | `Frame` | Marco contenedor |
| `etiqueta_texto` | `TextLabel` | Etiqueta de texto |
| `boton_texto` | `TextButton` | Botón con texto |
| `boton_imagen` | `ImageButton` | Botón con imagen |
| `marco_desplazamiento` | `ScrollingFrame` | Marco con scroll |
| `caja_texto` | `TextBox` | Caja de texto |
| `marco_video` | `VideoFrame` | Marco de video |

### Propiedades y Métodos

| Español | Roblox Property | Descripción |
|---------|-----------------|-------------|
| `nombre` | `Name` | Nombre del objeto |
| `padre` | `Parent` | Objeto padre |
| `tamano` | `Size` | Tamaño del objeto |
| `posicion` | `Position` | Posición del objeto |
| `color_fondo` | `BackgroundColor3` | Color de fondo |
| `texto` | `Text` | Texto del objeto |
| `color_texto` | `TextColor3` | Color del texto |
| `transparencia_fondo` | `BackgroundTransparency` | Transparencia de fondo |
| `escalado_texto` | `TextScaled` | Escalado de texto |
| `visible` | `Visible` | Visibilidad |
| `anclado` | `Anchored` | Si está anclado |
| `transparencia` | `Transparency` | Transparencia |
| `color` | `Color3` | Color |
| `material` | `Material` | Material |
| `reflejo` | `Reflectance` | Reflectancia |

### Propiedades de Humanoid

| Español | Roblox Property | Descripción |
|---------|-----------------|-------------|
| `humanoide` | `Humanoid` | Componente humanoid |
| `parte_primaria` | `PrimaryPart` | Parte primaria |
| `salud` | `Health` | Salud actual |
| `salud_maxima` | `MaxHealth` | Salud máxima |
| `velocidad_caminar` | `WalkSpeed` | Velocidad de caminar |
| `poder_salto` | `JumpPower` | Poder de salto |

### Constructores y Tipos

| Español | Roblox Constructor | Descripción |
|---------|-------------------|-------------|
| `UDim2_nuevo` | `UDim2.new()` | Crea UDim2 |
| `Vector3_nuevo` | `Vector3.new()` | Crea Vector3 |
| `Color3_nuevo` | `Color3.new()` | Crea Color3 |
| `CFrame_nuevo` | `CFrame.new()` | Crea CFrame |
| `secuencia_color` | `ColorSequence.new()` | Crea secuencia de color |
| `secuencia_numero` | `NumberSequence.new()` | Crea secuencia de números |

### Enums

| Español | Roblox Enum | Descripción |
|---------|-------------|-------------|
| `direccion_suavizado` | `Enum.EasingDirection` | Dirección de suavizado |
| `estilo_suavizado` | `Enum.EasingStyle` | Estilo de suavizado |
| `eje` | `Enum.Axis` | Ejes coordenados |
| `tipo_normal` | `Enum.NormalId` | Tipos de normales |
| `forma_material` | `Enum.FormFactor` | Formas de material |
| `tipo_parte` | `Enum.PartType` | Tipos de partes |

### Funciones de Task (Roblox)

| Español | Roblox Function | Descripción |
|---------|-----------------|-------------|
| `task_spawn` | `task.spawn()` | Ejecuta función asíncrona |
| `task_delay` | `task.delay()` | Retrasa ejecución |
| `task_wait` | `task.wait()` | Espera con task |
| `task_synchronize` | `task.synchronize()` | Sincroniza ejecución |
| `task_desynchronize` | `task.desynchronize()` | Desincroniza ejecución |
| `task_defer` | `task.defer()` | Difiere ejecución |

### Funciones de Manejo de Errores

| Español | Roblox Function | Descripción |
|---------|-----------------|-------------|
| `pcall` | `pcall()` | Llamada protegida |
| `xpcall` | `xpcall()` | Llamada protegida con handler |

### Funciones de DataStore (Seguras)

| Español | Función Wrapper | Descripción |
|---------|-----------------|-------------|
| `cargar_datos` | `GetAsync()` | Carga datos del datastore |
| `guardar_datos` | `SetAsync()` | Guarda datos en datastore |
| `incrementar_datos` | `IncrementAsync()` | Incrementa valor en datastore |

---

## 💡 Ejemplos Prácticos

### Ejemplo 1: Hola Mundo

```vox
-- Hola Mundo en Vox
imprimir("¡Hola Mundo desde Vox!")

-- Crear parte simple
local parte = crear_parte()
parte.establecer_nombre = "HolaMundo"
parte.establecer_posicion = crear_vector3(0, 10, 0)
parte.establecer_color = crear_color_bloque("rojo_brillante")
```

### Ejemplo 2: Función Básica

```vox
funcion saludar(nombre)
    local mensaje = "¡Hola, " .. nombre .. "!"
    imprimir(mensaje)
fin

-- Llamar función
saludar("Mundo")
```

### Ejemplo 3: Sistema de Partes y Colores

```vox
-- Crear sistema de partes con diferentes colores
funcion crear_sistema_partes()
    -- Crear parte principal
    local parte = instancia_nueva("Part")
    parte.nombre = "PartePrincipal"
    parte.tamano = Vector3_nuevo(4, 1, 4)
    parte.posicion = Vector3_nuevo(0, 5, 0)
    parte.color = Color3_nuevo(1, 0, 0) -- Rojo
    parte.material = Enum.Material.Neon
    parte.anclado = verdadero
    parte.padre = espacio_trabajo
    
    -- Crear partes secundarias
    para i = 1, 5 hacer
        local subparte = instancia_nueva("Part")
        subparte.nombre = "SubParte" .. i
        subparte.tamano = Vector3_nuevo(2, 1, 2)
        subparte.posicion = Vector3_nuevo(i * 3, 5, 0)
        subparte.color = Color3_nuevo(0, i/5, 1-i/5) -- Gradiente
        subparte.padre = espacio_trabajo
    fin
fin

-- Llamar función
crear_sistema_partes()
```

### Ejemplo 4: Interfaz de Usuario

```vox
-- Crear interfaz de usuario básica
funcion crear_interfaz_jugador(jugador)
    -- ScreenGui principal
    local screen_gui = instancia_nueva("ScreenGui")
    screen_gui.nombre = "InterfazJuego"
    screen_gui.padre = jugador:WaitForChild("PlayerGui")
    
    -- Marco principal
    local marco = instancia_nueva("Frame")
    marco.nombre = "MarcoPrincipal"
    marco.tamano = UDim2_nuevo(0, 200, 0, 100)
    marco.posicion = UDim2_nuevo(0, 10, 0, 10)
    marco.color_fondo = Color3_nuevo(0.2, 0.2, 0.2)
    marco.padre = screen_gui
    
    -- Etiqueta de texto
    local etiqueta = instancia_nueva("TextLabel")
    etiqueta.nombre = "EtiquetaSaludo"
    etiqueta.tamano = UDim2_nuevo(1, 0, 0, 30)
    etiqueta.posicion = UDim2_nuevo(0, 0, 0, 10)
    etiqueta.texto = "¡Bienvenido a Vox!"
    etiqueta.color_texto = Color3_nuevo(1, 1, 1)
    etiqueta.escalado_texto = verdadero
    etiqueta.padre = marco
    
    -- Botón
    local boton = instancia_nueva("TextButton")
    boton.nombre = "BotonAccion"
    boton.tamano = UDim2_nuevo(0, 150, 0, 40)
    boton.posicion = UDim2_nuevo(0, 25, 0, 50)
    boton.texto = "Clic Aquí"
    boton.color_fondo = Color3_nuevo(0, 0.5, 1)
    boton.padre = marco
    
    -- Evento del botón
    boton.MouseButton1Click:Connect(funcion()
        imprimir("¡Botón presionado!")
        etiqueta.texto = "¡Gracias por clickear!"
    fin)
fin

-- Conectar a jugador
jugadores.PlayerAdded:Connect(funcion(jugador)
    crear_interfaz_jugador(jugador)
fin)
```

### Ejemplo 5: Sistema de Datos con DataStore

```vox
-- Sistema de guardado de datos seguro
local tienda_datos = obtener_servicio("DataStoreService"):GetDataStore("JugadorDatos")

funcion guardar_estadisticas_jugador(jugador)
    local datos_jugador = {
        puntos = jugador.leaderstats.Puntos.Value,
        nivel = jugador:FindFirstChild("Nivel") y jugador.Nivel.Value o 1,
        experiencia = jugador:FindFirstChild("Experiencia") y jugador.Experiencia.Value o 0,
        ultima_conexion = tick()
    }
    
    local exito, error_msg = pcall(funcion()
        guardar_datos(tienda_datos, tostring(jugador.UserId), datos_jugador)
    fin)
    
    si exito entonces
        imprimir("Datos guardados para " .. jugador.Name)
    sino
        advertir("Error guardando datos: " .. tostring(error_msg))
    fin
fin

funcion cargar_estadisticas_jugador(jugador)
    local exito, datos = pcall(funcion()
        retornar cargar_datos(tienda_datos, tostring(jugador.UserId))
    fin)
    
    si exito y datos entonces
        -- Crear leaderstats si no existe
        local leaderstats = instancia_nueva("Folder")
        leaderstats.nombre = "leaderstats"
        leaderstats.padre = jugador
        
        -- Restaurar puntos
        local puntos = instancia_nueva("IntValue")
        puntos.nombre = "Puntos"
        puntos.Value = datos.puntos o 0
        puntos.padre = leaderstats
        
        -- Restaurar nivel
        local nivel = instancia_nueva("IntValue")
        nivel.nombre = "Nivel"
        nivel.Value = datos.nivel o 1
        nivel.padre = jugador
        
        imprimir("Datos cargados para " .. jugador.Name)
    sino
        imprimir("No se encontraron datos para " .. jugador.Name)
    fin
fin
```

### Ejemplo 6: Sistema de Tareas Asíncronas

```vox
-- Sistema de tareas con task functions
funcion ejecutar_tareas_asincronas()
    -- Tarea 1: Retrasada
    task_delay(2, funcion()
        imprimir("Tarea 1 ejecutada después de 2 segundos")
    fin)
    
    -- Tarea 2: Inmediata asíncrona
    task_spawn(funcion()
        esperar(1)
        imprimir("Tarea 2 ejecutada después de 1 segundo")
    fin)
    
    -- Tarea 3: Sincronizada
    task_synchronize()
    imprimir("Tarea 3 sincronizada")
    
    -- Tarea 4: Diferida
    task_defer(funcion()
        imprimir("Tarea 4 diferida al siguiente frame")
    fin)
fin

-- Bucle principal con task.wait
funcion bucle_principal_eficiente()
    mientras verdadero hacer
        task_wait(1/60) -- 60 FPS
        
        -- Lógica del juego aquí
        -- Esto es más eficiente que wait()
    fin
fin
```

### Ejemplo 7: Manejo Avanzado de Errores

```vox
-- Sistema robusto de manejo de errores
funcion operacion_segura(funcion_a_ejecutar, mensaje_error)
    local exito, resultado = pcall(funcion_a_ejecutar)
    
    si no exito entonces
        advertar("Error en operación: " .. mensaje_error)
        advertar("Detalles: " .. tostring(resultado))
        retornar nulo
    fin
    
    retornar resultado
fin

funcion ejemplo_uso_seguro()
    -- Operación segura 1: Crear instancia
    local parte = operacion_segura(funcion()
        retornar instancia_nueva("Part")
    fin, "No se pudo crear la parte")
    
    si parte entonces
        parte.nombre = "ParteSegura"
        parte.padre = espacio_trabajo
    fin
    
    -- Operación segura 2: Acceder a servicio
    local datos = operacion_segura(funcion()
        retornar obtener_servicio("DataStoreService"):GetDataStore("DatosSeguros")
    fin, "No se pudo acceder a DataStore")
    
    -- Operación segura 3: Operación matemática
    local resultado = operacion_segura(funcion()
        local a = 10
        local b = 0
        retornar a / b -- Esto causará error
    fin, "División por cero")
    
    si resultado entonces
        imprimir("Resultado: " .. resultado)
    sino
        imprimir("Operación fallida como se esperaba")
    fin
fin
```

### Ejemplo 8: Sistema de Animaciones y Tween

```vox
-- Sistema de animaciones con TweenService
local tween_service = obtener_servicio("TweenService")

funcion crear_animacion_suave(objeto, destino, duracion)
    local info = TweenInfo_nuevo(
        duracion,
        Enum.EasingStyle.Quad,
        Enum.EasingDirection.InOut,
        0, -- repeatCount
        falso, -- reverses
        0 -- delayTime
    )
    
    local tween = tween_service:Create(objeto, info, destino)
    tween:Play()
    
    retornar tween
end

funcion ejemplo_animaciones()
    -- Crear parte para animar
    local parte = instancia_nueva("Part")
    parte.nombre = "ParteAnimada"
    parte.tamano = Vector3_nuevo(2, 2, 2)
    parte.posicion = Vector3_nuevo(0, 10, 0)
    parte.color = Color3_nuevo(1, 0, 0)
    parte.anclado = verdadero
    parte.padre = espacio_trabajo
    
    -- Animación de posición
    crear_animacion_suave(parte, {
        Position = Vector3_nuevo(0, 20, 0)
    }, 2)
    
    -- Animación de color
    task_delay(2, funcion()
        crear_animacion_suave(parte, {
            Color = Color3_nuevo(0, 1, 0)
        }, 1)
    fin)
    
    -- Animación de tamaño
    task_delay(3, funcion()
        crear_animacion_suave(parte, {
            Size = Vector3_nuevo(4, 4, 4)
        }, 1.5)
    fin)
fin
```

### Ejemplo 9: Sistema de Eventos y Comunicación

```vox
-- Sistema de eventos remotos para comunicación cliente-servidor
local replicacion = obtener_servicio("ReplicatedStorage")

-- Crear eventos remotos
local evento_mensaje = instancia_nueva("RemoteEvent")
evento_mensaje.nombre = "MensajeGlobal"
evento_mensaje.padre = replicacion

local evento_datos = instancia_nueva("RemoteFunction")
evento_datos.nombre = "ObtenerDatosJugador"
evento_datos.padre = replicacion

-- Función del servidor para manejar mensajes
funcion manejar_mensaje_global(jugador, mensaje)
    imprimir("Mensaje de " .. jugador.Name .. ": " .. mensaje)
    
    -- Enviar a todos los jugadores
    para _, otro_jugador en ipairs(jugadores:GetPlayers()) hacer
        evento_mensaje:FireClient(otro_jugador, jugador.Name .. ": " .. mensaje)
    fin
fin

-- Función para obtener datos del jugador
funcion obtener_datos_jugador(jugador)
    local datos = {
        nombre = jugador.Name,
        userId = jugador.UserId,
        equipo = jugador.Team y jugador.Team.Name o "Ninguno",
        rango = jugador:FindFirstChild("Rango") y jugador.Rango.Value o "Principiante"
    }
    
    retornar datos
fin

-- Conectar eventos
evento_mensaje.OnServerEvent:Connect(manejar_mensaje_global)
evento_datos.OnServerInvoke = obtener_datos_jugador
```

### Ejemplo 10: Sistema de Habilidades y Cooldowns

```vox
-- Sistema de habilidades con cooldowns
local Habilidades = {}

funcion Habilidades.nueva(nombre, cooldown_maximo, costo_energia)
    local self = {}
    
    self.nombre = nombre
    self.cooldown_maximo = cooldown_maximo
    self.costo_energia = costo_energia
    self.cooldown_actual = 0
    self.esta_activa = falso
    
    funcion self.puede_usar(jugador)
        -- Verificar cooldown
        si self.cooldown_actual > 0 entonces
            retornar falso, "En cooldown: " .. math.ceil(self.cooldown_actual) .. "s"
        fin
        
        -- Verificar energía
        local energia = jugador:FindFirstChild("Energia")
        si no energia o energia.Value < self.costo_energia entonces
            retornar falso, "Energía insuficiente"
        fin
        
        -- Verificar si está vivo
        local humanoid = jugador:FindFirstChildOfClass("Humanoid")
        si no humanoid o humanoid.Health <= 0 entonces
            retornar falso, "No estás vivo"
        fin
        
        retornar verdadero, "Lista para usar"
    fin
    
    funcion self.usar(jugador, callback)
        local puede_usar, razon = self:puede_usar(jugador)
        si no puede_usar entonces
            imprimir(razon)
            retornar falso
        fin
        
        -- Consumir energía
        local energia = jugador:FindFirstChild("Energia")
        si energia entonces
            energia.Value = energia.Value - self.costo_energia
        fin
        
        -- Iniciar cooldown
        self.cooldown_actual = self.cooldown_maximo
        self.esta_activa = verdadero
        
        -- Ejecutar callback
        si callback entonces
            callback(jugador)
        fin
        
        -- Iniciar cooldown
        task_spawn(funcion()
            mientras self.cooldown_actual > 0 hacer
                task_wait(0.1)
                self.cooldown_actual = self.cooldown_actual - 0.1
            fin
            self.esta_activa = falso
        fin)
        
        retornar verdadero
    fin
    
    funcion self.obtener_progreso_cooldown()
        si self.cooldown_maximo > 0 entonces
            retornar 1 - (self.cooldown_actual / self.cooldown_maximo)
        fin
        retornar 1
    fin
    
    retornar self
fin

-- Ejemplo de uso
local habilidad_dash = Habilidades.nueva("Dash", 5, 20)
local habilidad_escudo = Habilidades.nueva("Escudo", 10, 30)

funcion dash_rapido(jugador)
    local humanoid = jugador:FindFirstChildOfClass("Humanoid")
    si humanoid entonces
        local direccion = humanoid.MoveDirection
        si direccion.Magnitude > 0 entonces
            humanoid:Move(direccion * 50)
            imprimir("Dash ejecutado!")
        fin
    fin
fin

funcion activar_escudo(jugador)
    local escudo = instancia_nueva("ForceField")
    escudo.nombre = "EscudoTemporal"
    escudo.padre = jugador.Character
    
    task_delay(3, funcion()
        si escudo entonces
            escudo:Destroy()
            imprimir("Escudo desactivado")
        fin
    fin)
    
    imprimir("Escudo activado por 3 segundos!")
fin
```

### Ejemplo 11: Sistema de Inventario y Objetos

```vox
-- Sistema de inventario completo
local SistemaInventario = {}

funcion SistemaInventario.nueva(capacidad_maxima)
    local self = {}
    
    self.capacidad_maxima = capacidad_maxima or 20
    self.objetos = {}
    self.espacios_usados = 0
    
    funcion self.agregar_objeto(objeto_id, cantidad)
        cantidad = cantidad o 1
        
        -- Verificar capacidad
        si self.espacios_usados >= self.capacidad_maxima entonces
            retornar falso, "Inventario lleno"
        fin
        
        -- Verificar si ya existe el objeto
        si self.objetos[objeto_id] entonces
            self.objetos[objeto_id].cantidad = self.objetos[objeto_id].cantidad + cantidad
        sino
            self.objetos[objeto_id] = {
                id = objeto_id,
                cantidad = cantidad,
                rareza = "comun"
            }
            self.espacios_usados = self.espacios_usados + 1
        fin
        
        retornar verdadero, "Objeto agregado"
    fin
    
    funcion self.remover_objeto(objeto_id, cantidad)
        cantidad = cantidad o 1
        
        si no self.objetos[objeto_id] entonces
            retornar falso, "Objeto no encontrado"
        fin
        
        local objeto = self.objetos[objeto_id]
        
        si objeto.cantidad <= cantidad entonces
            self.objetos[objeto_id] = nulo
            self.espacios_usados = self.espacios_usados - 1
            retornar verdadero, "Objeto eliminado completamente"
        sino
            objeto.cantidad = objeto.cantidad - cantidad
            retornar verdadero, "Se removieron " .. cantidad .. " unidades"
        fin
    fin
    
    funcion self.obtener_cantidad(objeto_id)
        si self.objetos[objeto_id] entonces
            retornar self.objetos[objeto_id].cantidad
        fin
        retornar 0
    fin
    
    funcion self.esta_vacio()
        retornar self.espacios_usados == 0
    fin
    
    funcion self.esta_lleno()
        retornar self.espacios_usados >= self.capacidad_maxima
    fin
    
    funcion self.obtener_lista_objetos()
        local lista = {}
        para id, objeto en pares(self.objetos) hacer
            tabla.insert(lista, {
                id = objeto.id,
                cantidad = objeto.cantidad,
                rareza = objeto.rareza
            })
        fin
        retornar lista
    fin
    
    funcion self.vaciar()
        self.objetos = {}
        self.espacios_usados = 0
    fin
    
    retornar self
fin

-- Ejemplo de uso del inventario
local inventario_jugador = SistemaInventario.nueva(15)

-- Agregar objetos
inventario_jugador:agregar_objeto("espada_madera", 1)
inventario_jugador:agregar_objeto("pocion_vida", 5)
inventario_jugador:agregar_objeto("moneda_oro", 100)

funcion mostrar_inventario(jugador)
    local objetos = inventario_jugador:obtener_lista_objetos()
    
    imprimir("=== INVENTARIO DE " .. jugador.Name:upper() .. " ===")
    imprimir("Espacios usados: " .. inventario_jugador.espacios_usados .. "/" .. inventario_jugador.capacidad_maxima)
    
    para _, objeto en ipairs(objetos) hacer
        imprimir("- " .. objeto.id .. " x" .. objeto.cantidad .. " [" .. objeto.rareza .. "]")
    fin
    
    si #objetos == 0 entonces
        imprimir("Inventario vacío")
    fin
end
```

### Ejemplo 12: Sistema de Partículas y Efectos Visuales

```vox
-- Sistema avanzado de partículas y efectos
local SistemaEfectos = {}

funcion SistemaEfectos.crear_explosion(posicion, tamano, color)
    local explosion = instancia_nueva("Explosion")
    explosion.Position = posicion
    explosion.BlastRadius = tamano o 10
    explosion.BlastPressure = 500000
    explosion.ExplosionType = Enum.ExplosionType.NoCraters
    
    si color entonces
        explosion.Visible = verdadero
    fin
    
    explosion.Parent = espacio_trabajo
    retornar explosion
fin

funcion SistemaEfectos.crear_chispa(posicion, cantidad, duracion)
    para i = 1, cantidad hacer
        task_spawn(funcion()
            local chispa = instancia_nueva("ParticleEmitter")
            chispa.Parent = workspace.Terrain
            
            -- Configurar partícula
            chispa.Color = ColorSequence_nuevo(Color3_nuevo(1, 0.5, 0))
            chispa.Transparency = NumberSequence_nuevo({
                NumberSequenceKeypoint_nuevo(0, 0),
                NumberSequenceKeypoint_nuevo(1, 1)
            })
            chispa.Size = NumberSequence_nuevo(1, 0)
            chispa.Lifetime = NumberRange_nuevo(0.1, 0.5)
            chispa.Rate = 100
            chispa.Speed = NumberRange_nuevo(5, 15)
            chispa.Acceleration = Vector3_nuevo(0, -10, 0)
            
            -- Posicionar y limpiar
            local attachment = instancia_nueva("Attachment")
            attachment.Position = posicion
            attachment.Parent = workspace.Terrain
            chispa.Parent = attachment
            
            task_delay(duracion, funcion()
                attachment:Destroy()
            fin)
        fin)
    fin
fin

funcion SistemaEfectos.crear_trail(objeto, color, duracion)
    local trail = instancia_nueva("Trail")
    trail.Color = ColorSequence_nuevo(color o Color3_nuevo(1, 1, 1))
    trail.Transparency = NumberSequence_nuevo({
        NumberSequenceKeypoint_nuevo(0, 0),
        NumberSequenceKeypoint_nuevo(1, 1)
    })
    trail.Lifetime = duracion o 0.5
    trail.MinLength = 0.1
    trail.MaxLength = 5
    
    -- Attachment para inicio y fin
    local attachment0 = instancia_nueva("Attachment")
    local attachment1 = instancia_nueva("Attachment")
    
    attachment0.Name = "TrailStart"
    attachment1.Name = "TrailEnd"
    
    attachment0.Parent = objeto
    attachment1.Parent = objeto
    
    trail.Attachment0 = attachment0
    trail.Attachment1 = attachment1
    trail.Parent = objeto
    
    retornar trail
end

funcion SistemaEfectos.crear_onda_choque(posicion, radio_maximo, duracion)
    local onda = instancia_nueva("Part")
    onda.Shape = Enum.PartType.Ball
    onda.Size = Vector3_nuevo(0.1, 0.1, 0.1)
    onda.Position = posicion
    onda.Color = Color3_nuevo(0, 1, 1)
    onda.Material = Enum.Material.Neon
    onda.Anchored = verdadero
    onda.CanCollide = falso
    onda.Transparency = 0.3
    onda.Parent = espacio_trabajo
    
    -- Animar onda
    local info_animacion = TweenInfo_nuevo(
        duracion,
        Enum.EasingStyle.Out,
        Enum.EasingDirection.Out,
        0,
        falso,
        0
    )
    
    local animacion = game:GetService("TweenService"):Create(onda, info_animacion, {
        Size = Vector3_nuevo(radio_maximo * 2, radio_maximo * 2, radio_maximo * 2),
        Transparency = 1
    })
    
    animacion:Play()
    animacion.Completed:Connect(funcion()
        onda:Destroy()
    fin)
    
    retornar onda
fin

-- Ejemplo de uso combinado
funcion demostrar_sistema_efectos()
    local posicion_central = Vector3_nuevo(0, 10, 0)
    
    -- Crear explosión principal
    SistemaEfectos.crear_explosion(posicion_central, 15, Color3_nuevo(1, 0, 0))
    
    -- Crear chispas alrededor
    para i = 1, 8 hacer
        local angulo = (i - 1) * (math.pi * 2 / 8)
        local offset = Vector3_nuevo(
            math.cos(angulo) * 5,
            0,
            math.sin(angulo) * 5
        )
        SistemaEfectos.crear_chispa(posicion_central + offset, 20, 2)
    fin
    
    -- Crear onda de choque
    SistemaEfectos.crear_onda_choque(posicion_central, 20, 1.5)
    
    -- Crear parte con trail
    local parte_movil = instancia_nueva("Part")
    parte_movil.Size = Vector3_nuevo(2, 2, 2)
    parte_movil.Position = posicion_central
    parte_movil.Color = Color3_nuevo(1, 0, 0)
    parte_movil.Anchored = falso
    parte_movil.Parent = espacio_trabajo
    
    -- Agregar trail
    SistemaEfectos.crear_trail(parte_movil, Color3_nuevo(1, 0.5, 0))
    
    -- Mover parte en círculo
    task_spawn(funcion()
        para i = 1, 360 hacer
            local angulo = math.rad(i)
            local nueva_posicion = posicion_central + Vector3_nuevo(
                math.cos(angulo) * 10,
                math.sin(angulo * 2) * 3,
                math.sin(angulo) * 10
            )
            parte_movil.Position = nueva_posicion
            task_wait(0.016) -- ~60 FPS
        fin
    fin)
end
```

---

## ⚙️ Configuración

### Configuración de VS Code

Puedes configurar Vox a través de la configuración de VS Code:

1. Abre configuración (Ctrl+,)
2. Busca "Vox Language"
3. Ajusta las siguientes opciones:

| Opción | Valor por Defecto | Descripción |
|--------|-------------------|-------------|
| `vox.transpilerPath` | `""` | Ruta al transpilador personalizado |
| `vox.autoTranspile` | `true` | Transpilar automáticamente al guardar |
| `vox.enableSemanticAnalysis` | `true` | Habilitar análisis semántico |
| `vox.showValidationErrors` | `true` | Mostrar errores en tiempo real |
| `vox.autoSaveLua` | `true` | Guardar automáticamente archivo Lua |
| `vox.outputDirectory` | `"./"` | Directorio de salida para archivos Lua |

### Configuración del Transpilador

El archivo `transpiler_final.py` se puede configurar modificando:

```python
# Nivel de optimización (0-3)
optimization_level = 2

# Palabras prohibidas personalizadas
forbidden_words = ['os.exit', 'game:Shutdown']

# Servicios Roblox permitidos
allowed_services = [
    'Workspace', 'Lighting', 'ReplicatedStorage', 
    'ServerScriptService', 'Players'
]
```

---

## 🔧 Transpilador

### ¿Cómo funciona el transpilador?

1. **Análisis Léxico**: Convierte el código en tokens
2. **Análisis Sintáctico**: Verifica estructura gramatical
3. **Análisis Semántico**: Detecta errores lógicos
4. **Generación de Código**: Produce Lua estándar compatible con Roblox

### Filosofía de Transpilación

**🎯 OBJETIVO: Vox genera código Lua 100% funcional en Roblox Studio**

El transpilador sigue estos principios:

- ✅ **Compatibilidad total** con Roblox API
- ✅ **Servicios traducidos** exactamente como en Roblox
- ✅ **Mantenimiento de estructura** y lógica original
- ✅ **Sin abstracciones** que rompan la funcionalidad
- ✅ **Código generado** listo para producción

### Usar el Transpilador

#### Método 1: Línea de Comandos

```bash
# Transpilar archivo simple
python transpiler_final.py input.vox output.lua

# Con opciones
python transpiler_final.py input.vox output.lua --optimizar 3 --verbose

# Transpilar directorio
python transpiler_final.py --directorio ./src --salida ./build
```

#### Método 2: Integrado en VS Code

La extensión transpila automáticamente cuando:
- Guardas un archivo .vox (si `autoTranspile` está activado)
- Usas el comando `Transpilar Archivo Vox`
- Presionas `Ctrl+Shift+T`

### Ejemplo de Transpilación Real

**Código Vox:**
```vox
local jugadores = obtener_servicio("jugadores")
local parte = instancia_nueva("Part")
parte.nombre = "MiParte"
parte.posicion = Vector3_nuevo(0, 10, 0)
parte.padre = espacio_trabajo
```

**Código Lua Generado:**
```lua
local jugadores = game:GetService("Players")
local parte = Instance.new("Part")
parte.Name = "MiParte"
parte.Position = Vector3.new(0, 10, 0)
parte.Parent = workspace
```

### Optimizaciones Aplicadas

El transpilador aplica automáticamente:

- ✅ **Traducción semántica** de servicios y propiedades
- ✅ **Optimización de variables** no usadas
- ✅ **Simplificación de expresiones**
- ✅ **Validación de seguridad** con palabras prohibidas
- ✅ **Mantenimiento de compatibilidad** con Roblox

**🔒 SEGURIDAD: El transpilador filtra palabras peligrosas mientras mantiene funcionalidad**

---

## 🎨 Extension VS Code

### Características de la Extensión

#### 🎯 Autocompletado Inteligente
- Palabras clave del lenguaje
- Servicios de Roblox
- Instancias comunes
- Métodos y propiedades

#### 🔍 Resaltado de Sintaxis
- Colores personalizados para Vox
- Diferenciación de tipos
- Resaltado de errores

#### ⚡ Detección de Errores
- Errores sintácticos en tiempo real
- Advertencias semánticas
- Sugerencias de corrección

#### 🛠️ Herramientas Integradas
- Transpilador con un clic
- Validador de código
- Explorador de proyectos

### Snippets Disponibles

Escribe los siguientes atajos y presiona Tab:

| Atajo | Código Generado |
|-------|-----------------|
| `func` | `funcion ... fin` |
| `si` | `si ... entonces ... fin` |
| `mientras` | `mientras ... hacer ... fin` |
| `para` | `para ... en ... hacer ... fin` |
| `servicio` | `local ... = obtener_servicio("...")` |

---

## ❓ Preguntas Frecuentes

### ¿Puedo mezclar código Lua y Vox?
Sí, puedes incluir código Lua estándar dentro de archivos Vox. El transpilador solo traducirá las palabras clave en español manteniendo el resto del código intacto.

### ¿Vox es compatible con todos los scripts de Roblox?
**✅ SÍ, 100% COMPATIBLE**. Vox genera código Lua exactamente como lo escribirías en Roblox Studio. Los servicios, propiedades y métodos se traducen directamente a sus equivalentes de Roblox API sin modificaciones.

### ¿El código generado funciona en Roblox Studio?
**✅ SÍ, FUNCIONA PERFECTAMENTE**. El código Lua generado por Vox es idéntico al que escribirías manualmente para Roblox. Puedes copiar y pegar directamente en Roblox Studio.

### ¿Cómo puedo depurar código Vox?
1. Transpila a Lua usando `Ctrl+Shift+T`
2. Revisa el archivo .lua generado (es código Lua estándar)
3. Usa las herramientas de depuración estándar de Roblox Studio

### ¿Los servicios funcionan igual que en Roblox?
**✅ EXACTAMENTE IGUALES**. `obtener_servicio("jugadores")` se convierte a `game:GetService("Players")` sin ninguna modificación. Mantenemos la compatibilidad total.

### ¿Puedo crear mis propias palabras clave?
Actualmente no, pero estamos trabajando en un sistema de macros para permitir extensiones personalizadas.

### ¿Vox rompe alguna funcionalidad de Roblox?
**❌ NO**. Vox está diseñado para NO romper ninguna funcionalidad. El transpilador mantiene la estructura y lógica original, solo traduce el lenguaje.

### ¿El código es más lento que Lua nativo?
**❌ NO**. El código generado es exactamente el mismo que escribirías en Lua, por lo que no hay pérdida de rendimiento.

### ¿Vox afecta el rendimiento?
No, Vox se transpila a Lua estándar antes de ejecutarse, por lo que el rendimiento es idéntico al código Lua nativo.

---

## 📚 Recursos Adicionales

### Enlaces Útiles
- [Repositorio Oficial](https://github.com/vox-studio/vox-language)
- [Marketplace de VS Code](https://marketplace.visualstudio.com/items?itemName=vox-studio.vox-language)
- [Reportar Issues](https://github.com/vox-studio/vox-language/issues)

### Comunidad
- [Discord Oficial](https://discord.gg/vox-language)
- [Foro de Discusión](https://github.com/vox-studio/vox-language/discussions)
- [Wiki del Proyecto](https://github.com/vox-studio/vox-language/wiki)

### Tutoriales
- [Tutorial Básico](docs/tutorial-basico.md)
- [Guía de FPS](docs/guia-fps.md)
- [ Mejores Prácticas](docs/mejores-practicas.md)

---

## 🎯 Garantía de Compatibilidad

### ✅ PROMESA DE VOX: 100% COMPATIBLE CON ROBLOX

**Vox Language está diseñado con un principio fundamental: no romper nunca la funcionalidad de Roblox.**

#### ¿Qué significa esto?

- 🔄 **Traducción directa**: `obtener_servicio("jugadores")` → `game:GetService("Players")`
- 🏗️ **Misma estructura**: El código generado mantiene la lógica original
- ⚡ **Sin pérdida de rendimiento**: El resultado es Lua estándar
- 🛡️ **Sin abstracciones peligrosas**: No se modifica el comportamiento de Roblox API
- 🎮 **Listo para producción**: Funciona directamente en Roblox Studio

#### Ejemplo Real:

```vox
-- Código Vox (español)
local jugadores = obtener_servicio("jugadores")
local parte = instancia_nueva("Part")
parte.nombre = "Test"
parte.posicion = Vector3_nuevo(0, 10, 0)
parte.padre = espacio_trabajo
```

```lua
-- Código Lua generado (Roblox API)
local jugadores = game:GetService("Players")
local parte = Instance.new("Part")
parte.Name = "Test"
parte.Position = Vector3.new(0, 10, 0)
parte.Parent = workspace
```

**🔥 RESULTADO: Código idéntico al que escribirías manualmente**

---

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT. Ver archivo [LICENSE](LICENSE) para más detalles.

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Por favor:

1. Fork el repositorio
2. Crea una rama (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -am 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Crea un Pull Request

---

**¡Gracias por usar Vox Language! 🚀**

*Desarrollado con ❤️ por Vox Studio*
