#!/usr/bin/env python3
"""
Transpilador DSL de Lua en español para Roblox - VERSIÓN SEMÁNTICA CORREGIDA
Convierte código Lua con palabras clave en español a Lua estándar para Roblox Studio
"""

import re
import sys
import os
from typing import Dict, List, Tuple, Optional
from enum import Enum


class DSLError(Exception):
    """Excepción personalizada para errores del transpilador DSL"""
    pass


class SemanticError(Exception):
    """Excepción personalizada para errores semánticos"""
    pass


class ErrorType(Enum):
    """Tipos de error del transpilador"""
    FORBIDDEN_WORD = "PALABRA_PROHIBIDA"
    SYNTAX_ERROR = "ERROR_SINTAXIS"
    FILE_ERROR = "ERROR_ARCHIVO"
    STRING_ERROR = "ERROR_STRING"


class LuaDSLTranspiler:
    """Transpilador principal de DSL a Lua Roblox con análisis semántico"""
    
    def __init__(self):
        """Inicializa el transpilador con diccionarios de traducción y palabras prohibidas"""
        
        # Diccionario principal de traducción español -> inglés
        self.translation_dict: Dict[str, str] = {
            # Estructuras de control
            'funcion': 'function',
            'fin': 'end',
            'si': 'if',
            'entonces': 'then',
            'sino': 'else',
            'sino_si': 'elseif',
            'mientras': 'while',
            'hacer': 'do',
            'para': 'for',
            'en': 'in',
            'retornar': 'return',
            'local': 'local',
            'y': 'and',
            'o': 'or',
            'no': 'not',
            'verdadero': 'true',
            'falso': 'false',
            'imprimir': 'print',
            'advertar': 'warn',
            'esperar': 'wait',
            'tick': 'tick',
            'time': 'time',
            'tipo': 'type',
            'pares': 'pairs',
            'ipares': 'ipairs',
            'nulo': 'nil',
            'romper': 'break',
            'continuar': 'continue',
            'repetir': 'repeat',
            'hasta': 'until',
            
            # Funciones seguras adicionales
            'pcall': 'pcall',
            'xpcall': 'xpcall',
            'task_spawn': 'task.spawn',
            'task_delay': 'task.delay',
            'task_wait': 'task.wait',
            'task_synchronize': 'task.synchronize',
            'task_desynchronize': 'task.desynchronize',
            'task_defer': 'task.defer',
            'cargar_datos': 'function(store, key) return store:GetAsync(key) end',
            'guardar_datos': 'function(store, key, value) return store:SetAsync(key, value) end',
            'incrementar_datos': 'function(store, key, delta) return store:IncrementAsync(key, delta) end',
            
            # Funciones de tarea y tiempo
            'tarea_espera': 'task.wait',
            'tarea_spawn': 'task.spawn',
            'tarea_delay': 'task.delay',
            'tarea_defer': 'task.defer',
            
            # Funciones de Tween y animación
            'servicio_tween': 'TweenService',
            'info_tween': 'TweenInfo.new',
            'estilo_suavizado': 'Enum.EasingStyle',
            'direccion_suavizado': 'Enum.EasingDirection',
            
            # Funciones de espera y tiempo
            'esperar_hijo': 'WaitForChild',
            'encontrar_hijo': 'FindFirstChild',
            
            # Roblox Services (seguros)
            'juego': 'game',
            'espacio_trabajo': 'Workspace',
            'jugadores': 'Players',
            'luz': 'Lighting',
            'sonido': 'SoundService',
            'replicacion': 'ReplicatedStorage',
            'servidor_script': 'ServerScriptService',
            'servidor_almacen': 'ServerStorage',
            'tienda_datos': 'DataStoreService',
            'servicio_tween': 'TweenService',
            'servicio_http': 'HttpService',
            'servicio_mensajes': 'MessagingService',
            'servicio_teletransporte': 'TeleportService',
            'servicio_chat': 'Chat',
            'servicio_gui': 'GuiService',
            'servicio_entrada': 'UserInputService',
            'servicio_context': 'ContextActionService',
            'servicio_sonido': 'SoundService',
            'servicio_fisica': 'PhysicsService',
            'servicio_carga': 'ContentProvider',
            'servicio_recursos': 'HttpService',
            
            # Instancias comunes
            'instancia_nueva': 'Instance.new',
            'parte': 'Part',
            'malla_parte': 'MeshPart',
            'parte_cuña': 'WedgePart',
            'parte_esquina': 'CornerWedgePart',
            'modelo': 'Model',
            'script': 'Script',
            'script_local': 'LocalScript',
            'script_modulo': 'ModuleScript',
            'texto_cadena': 'StringValue',
            'numero_valor': 'NumberValue',
            'booleano_valor': 'BoolValue',
            'objeto_valor': 'ObjectValue',
            'marco_valor': 'CFrameValue',
            'vector3_valor': 'Vector3Value',
            'color3_valor': 'Color3Value',
            'ladrillo_color_valor': 'BrickColorValue',
            'entero_valor': 'IntValue',
            'doble_valor': 'DoubleValue',
            'angulo_valor': 'NumberSequenceValue',
            'color_secuencia_valor': 'ColorSequenceValue',
            
            # UI Elements
            'marco': 'Frame',
            'etiqueta_texto': 'TextLabel',
            'boton_texto': 'TextButton',
            'boton_imagen': 'ImageButton',
            'marco_desplazamiento': 'ScrollingFrame',
            'caja_texto': 'TextBox',
            'marco_video': 'VideoFrame',
            'imagen': 'ImageLabel',
            'lista_desplazamiento': 'ScrollingFrame',
            'barra_desplazamiento': 'ScrollBar',
            'gui_pantalla': 'ScreenGui',
            'gui_billetera': 'BillboardGui',
            'gui_superficie': 'SurfaceGui',
            'gui_mapa': 'ViewportFrame',
            'caja_seleccion': 'SelectionBox',
            'caja_resalte': 'Highlight',
            
            # Propiedades básicas
            'nombre': 'Name',
            'padre': 'Parent',
            'tamano': 'Size',
            'posicion': 'Position',
            'color_fondo': 'BackgroundColor3',
            'texto': 'Text',
            'color_texto': 'TextColor3',
            'transparencia_fondo': 'BackgroundTransparency',
            'escalado_texto': 'TextScaled',
            'visible': 'Visible',
            'anclado': 'Anchored',
            'transparencia': 'Transparency',
            'color': 'Color3',
            'material': 'Material',
            'reflejo': 'Reflectance',
            'forma': 'Shape',
            'superficie': 'TopSurface',
            'superficie_inferior': 'BottomSurface',
            'frente': 'FrontSurface',
            'atras': 'BackSurface',
            'izquierda': 'LeftSurface',
            'derecha': 'RightSurface',
            'puede_colisionar': 'CanCollide',
            'masa': 'Mass',
            'densidad': 'Density',
            'friccion': 'Friction',
            'elasticidad': 'Elasticity',
            'resistencia_friction': 'FrictionWeight',
            'resistencia_elasticidad': 'ElasticityWeight',
            
            # Propiedades de Humanoid
            'humanoide': 'Humanoid',
            'parte_primaria': 'PrimaryPart',
            'salud': 'Health',
            'salud_maxima': 'MaxHealth',
            'velocidad_caminar': 'WalkSpeed',
            'poder_salto': 'JumpPower',
            'altura_salto': 'JumpHeight',
            'estado_movimiento': 'MoveState',
            'estado_sitio': 'Sit',
            'estado_saltando': 'Jump',
            'estado_cayendo': 'Freefall',
            'estado_aterrizando': 'Landed',
            'tipo_cuerpo': 'BodyType',
            'tipo_estado': 'BodyPartType',
            'escalado_altura': 'HipHeight',
            'ancho_hombros': 'ShoulderWidth',
            'profundidad_cabeza': 'HeadScale',
            'escalado_cuerpo': 'BodyDepthScale',
            'escalado_ancho': 'BodyWidthScale',
            'escalado_altura_cuerpo': 'BodyHeightScale',
            
            # Propiedades de UI
            'posicion_udim2': 'UDim2',
            'tamano_udim2': 'UDim2',
            'borde_pixel': 'BorderSizePixel',
            'radio_esquina': 'CornerRadius',
            'recorte': 'ClipsDescendants',
            'seleccionable': 'Selectable',
            'modo_seleccion': 'SelectionMode',
            'orden_z': 'ZIndex',
            'layout': 'LayoutOrder',
            'alineamiento': 'Alignment',
            'alineamiento_vertical': 'VerticalAlignment',
            'alineamiento_horizontal': 'HorizontalAlignment',
            'relleno': 'Padding',
            'espaciado': 'Spacing',
            'relleno_superior': 'PaddingTop',
            'relleno_inferior': 'PaddingBottom',
            'relleno_izquierdo': 'PaddingLeft',
            'relleno_derecho': 'PaddingRight',
            'fuente': 'Font',
            'tamano_fuente': 'FontSize',
            'peso_fuente': 'FontWeight',
            'estilo_fuente': 'FontStyle',
            'linea_texto': 'TextWrap',
            'ajuste_texto': 'TextWrapped',
            'texto_truncado': 'TextTruncate',
            'alineacion_texto': 'TextXAlignment',
            'alineacion_texto_vertical': 'TextYAlignment',
            'color_borde': 'BorderColor3',
            'transparencia_borde': 'BorderTransparency',
            
            # Tipos y constructores
            'UDim2_nuevo': 'UDim2.new',
            'Vector3_nuevo': 'Vector3.new',
            'Vector2_nuevo': 'Vector2.new',
            'Color3_nuevo': 'Color3.new',
            'CFrame_nuevo': 'CFrame.new',
            'CFrame_angulos': 'CFrame.Angles',
            'secuencia_color': 'ColorSequence.new',
            'secuencia_numero': 'NumberSequence.new',
            'punto_secuencia_numero': 'NumberSequenceKeypoint.new',
            'punto_secuencia_color': 'ColorSequenceKeypoint.new',
            'rango_numero': 'NumberRange.new',
            'rango_color': 'ColorRange.new',
            'ladrillo_color': 'BrickColor.new',
            'ladrillo_color_random': 'BrickColor.random',
            'ruido_perlin': 'math.noise',
            'aleatorio': 'math.random',
            'semilla_aleatoria': 'math.randomseed',
            'absoluto': 'math.abs',
            'techo': 'math.ceil',
            'piso': 'math.floor',
            'maximo': 'math.max',
            'minimo': 'math.min',
            'redondear': 'math.round',
            'potencia': 'math.pow',
            'raiz': 'math.sqrt',
            'grados_a_radianes': 'math.deg',
            'radianes_a_grados': 'math.rad',
            'pi': 'math.pi',
            'infinito': 'math.huge',
            'exp': 'math.exp',
            'log': 'math.log',
            'log10': 'math.log10',
            'sin': 'math.sin',
            'cos': 'math.cos',
            'tan': 'math.tan',
            'asin': 'math.asin',
            'acos': 'math.acos',
            'atan': 'math.atan',
            'atan2': 'math.atan2',
            'sinh': 'math.sinh',
            'cosh': 'math.cosh',
            'tanh': 'math.tanh',
            
            # Enums principales
            'direccion_suavizado': 'Enum.EasingDirection',
            'estilo_suavizado': 'Enum.EasingStyle',
            'eje': 'Enum.Axis',
            'tipo_normal': 'Enum.NormalId',
            'forma_material': 'Enum.FormFactor',
            'tipo_parte': 'Enum.PartType',
            'material': 'Enum.Material',
            'forma': 'Enum.Shape',
            'superficie_tipo': 'Enum.SurfaceType',
            'fuente': 'Enum.Font',
            'tamano_fuente': 'Enum.FontSize',
            'tipo_cuerpo': 'Enum.BodyPartType',
            'tipo_estado_humanoide': 'Enum.HumanoidStateType',
            'tipo_animacion': 'Enum.AnimationPriority',
            'tipo_interpolacion': 'Enum.InterpolationStyle',
            'direccion_interpolacion': 'Enum.InterpolationDirection',
            'tipo_mensaje': 'Enum.MessageType',
            'tipo_entrada': 'Enum.UserInputType',
            'estado_entrada': 'Enum.UserInputState',
            'tipo_gesto': 'Enum.PlayerGestureType',
            'tipo_animacion_r': 'Enum.AnimationStatus',
            'tipo_camara': 'Enum.CameraType',
            'modo_camara': 'Enum.CameraMode',
            'tipo_foco': 'Enum.FocusType',
            
            # Métodos comunes de objetos
            'obtener_servicio': 'GetService',
            'encontrar_hijo': 'FindFirstChild',
            'esperar_hijo': 'WaitForChild',
            'obtener_hijos': 'GetChildren',
            'obtener_descendientes': 'GetDescendants',
            'es_ancestro': 'IsAncestorOf',
            'es_descendiente': 'IsDescendantOf',
            'clonar': 'Clone',
            'destruir': 'Destroy',
            'conectar': 'Connect',
            'desconectar': 'Disconnect',
            'desconectar_todo': 'DisconnectAll',
            'esperar': 'Wait',
            'emitir': 'Emit',
            'jugar': 'Play',
            'pausar': 'Pause',
            'detener': 'Stop',
            'reanudar': 'Resume',
            'volumen': 'Volume',
            'tiempo_posicion': 'TimePosition',
            'duracion': 'TimeLength',
            'id_sonido': 'SoundId',
            'id_imagen': 'Image',
            'id_malla': 'MeshId',
            'id_textura': 'TextureID',
            'aplicar_impulso': 'ApplyImpulse',
            'aplicar_fuerza': 'ApplyForce',
            'aplicar_torque': 'ApplyTorque',
            'aplicar_velocidad_angular': 'ApplyAngularImpulse',
            'velocidad': 'Velocity',
            'velocidad_angular': 'AngularVelocity',
            'velocidad_maxima': 'MaxVelocity',
            'velocidad_rotacion': 'RotVelocity',
            'fuerza': 'Force',
            'torque': 'Torque',
            'densidad': 'Density',
            'masa': 'Mass',
            'centro_masas': 'CenterOfMass',
            
            # Métodos de Tween
            'crear_tween': 'Create',
            'info_tween': 'TweenInfo.new',
            'completado': 'Completed',
            'estado_tween': 'PlaybackState',
            'tiempo_reproduccion': 'TweenTime',
            'tiempo_actual': 'CurrentTime',
            
            # Métodos de Players
            'obtener_jugadores': 'GetPlayers',
            'jugador_local': 'LocalPlayer',
            'personaje': 'Character',
            'cargar_personaje': 'LoadCharacter',
            'quitar_personaje': 'RemoveCharacter',
            'distancia_de_camara': 'CameraMaxZoomDistance',
            'distancia_minima_camara': 'CameraMinZoomDistance',
            'modo_camara': 'CameraMode',
            'tipo_camara': 'CameraType',
            
            # Métodos de Humanoid
            'mover': 'Move',
            'saltar': 'Jump',
            'sentar': 'Sit',
            'levantar': 'Stand',
            'plataforma_elevada': 'PlatformStand',
            'requiere_plataforma_elevada': 'RequiresNeck',
            'salto_automatico': 'AutoJump',
            'tipo_movimiento': 'MoveDirection',
            'velocidad_movimiento': 'WalkSpeed',
            'poder_salto': 'JumpPower',
            'altura_salto': 'JumpHeight',
            'estado_actual': 'GetState',
            'cambiar_estado': 'ChangeState',
            
            # Métodos de UI
            'capturar_foco': 'CaptureFocus',
            'liberar_foco': 'ReleaseFocus',
            'perder_foco': 'FocusLost',
            'ganar_foco': 'Focused',
            'texto_cambiado': 'TextChanged',
            'texto_focalizado': 'Focused',
            'texto_perdido_foco': 'FocusLost',
            
            # Eventos comunes
            'conectado': 'Connected',
            'desconectado': 'Disconnected',
            'agregado': 'Added',
            'eliminado': 'Removed',
            'cambiado': 'Changed',
            'tocado': 'Touched',
            'tocar_terminado': 'TouchEnded',
            'presionado': 'Pressed',
            'liberado': 'Released',
            'movido': 'Moved',
            'clic_izquierdo': 'MouseButton1Down',
            'clic_izquierdo_soltado': 'MouseButton1Up',
            'clic_derecho': 'MouseButton2Down',
            'clic_derecho_soltado': 'MouseButton2Up',
            'clic_medio': 'MouseButton3Down',
            'clic_medio_soltado': 'MouseButton3Up',
            'rueda_mouse': 'MouseWheel',
            'mouse_movido': 'MouseMoved',
            'mouse_entro': 'MouseEnter',
            'mouse_salio': 'MouseLeave',
            'tecla_presionada': 'KeyDown',
            'tecla_liberada': 'KeyUp',
            'entrada_comenzo': 'InputBegan',
            'input_termino': 'InputEnded',
            'input_cambiado': 'InputChanged',
            
            # Propiedades de Part
            'posicion': 'Position',
            'tamano': 'Size',
            'color': 'Color3',
            'material': 'Material',
            'reflejo': 'Reflectance',
            'transparencia': 'Transparency',
            'anclado': 'Anchored',
            'puede_colisionar': 'CanCollide',
            'masa': 'Mass',
            'densidad': 'Density',
            'friccion': 'Friction',
            'elasticidad': 'Elasticity',
            'forma': 'Shape',
            'superficie': 'TopSurface',
            'superficie_inferior': 'BottomSurface',
            'frente': 'FrontSurface',
            'atras': 'BackSurface',
            'izquierda': 'LeftSurface',
            'derecha': 'RightSurface',
            
            # Propiedades de Light
            'tipo_luz': 'LightType',
            'brillo': 'Brightness',
            'color_luz': 'Color',
            'sombra': 'Shadows',
            'rango': 'Range',
            'angulo': 'Angle',
            'atenuacion': 'Falloff',
            'habilitado': 'Enabled',
            
            # Propiedades de Sound
            'id_sonido': 'SoundId',
            'volumen': 'Volume',
            'tiempo_posicion': 'TimePosition',
            'duracion': 'TimeLength',
            'pitch': 'Pitch',
            'loop': 'Looped',
            'jugando': 'Playing',
            'distancia_maxima': 'MaxDistance',
            'distancia_minima': 'MinDistance',
            'atenuacion_rolloff': 'RollOffMode',
            'efecto_sonido': 'SoundEffect',
            'reverb': 'ReverbSoundEffect',
            'eco': 'EchoSoundEffect',
            'distorsion': 'DistortionSoundEffect',
            'compresor': 'CompressorSoundEffect',
            
            # Propiedades de Mesh
            'id_malla': 'MeshId',
            'id_textura': 'TextureID',
            'escala_textura': 'TextureSize',
            'desplazamiento_vertice': 'VertexColor',
            'offset_malla': 'Offset',
            'escala_malla': 'Scale',
            
            # Funciones de tabla
            'insertar': 'table.insert',
            'remover': 'table.remove',
            'ordenar': 'table.sort',
            'concatenar': 'table.concat',
            'longitud': '#',
            'vaciar': 'table.clear',
            'encontrar': 'table.find',
            'copiar': 'table.copy',
            'fusionar': 'table.merge',
            'congelar': 'table.freeze',
            'esta_congelado': 'table.isfrozen',
            'empaquetar': 'table.pack',
            'desempaquetar': 'table.unpack',
            
            # Funciones de math (CORREGIDAS)
            'piso': 'math.floor',
            'techo': 'math.ceil',
            'absoluto': 'math.abs',
            'maximo': 'math.max',
            'minimo': 'math.min',
            'redondear': 'math.round',
            'potencia': 'math.pow',
            'raiz': 'math.sqrt',
            'grados_a_radianes': 'math.deg',
            'radianes_a_grados': 'math.rad',
            'aleatorio': 'math.random',
            'semilla_aleatoria': 'math.randomseed',
            'ruido_perlin': 'math.noise',
            'pi': 'math.pi',
            'infinito': 'math.huge',
            'exp': 'math.exp',
            'log': 'math.log',
            'log10': 'math.log10',
            'sin': 'math.sin',
            'cos': 'math.cos',
            'tan': 'math.tan',
            'asin': 'math.asin',
            'acos': 'math.acos',
            'atan': 'math.atan',
            'atan2': 'math.atan2',
            'sinh': 'math.sinh',
            'cosh': 'math.cosh',
            'tanh': 'math.tanh',
        }
        
        # Lista de palabras prohibidas (seguridad)
        self.forbidden_words: List[str] = [
            'loadstring', 'getfenv', 'setfenv', 'rawget', 'rawset', 
            'rawequal', 'newproxy', 'debug', 'collectgarbage',
            'dofile', 'require', 'package', 'module', 'coroutine',
            'PostAsync', 'RequestAsync'
        ]
        
        # Funciones seguras permitidas (actualizado para 1.2.6)
        self.safe_functions: List[str] = [
            'pcall', 'xpcall', 'task_spawn', 'task_delay', 'task_wait', 
            'task_synchronize', 'task_desynchronize', 'task_defer'
        ]
        
        # Funciones adicionales para DataStore (wrapper seguro)
        self.datastore_functions: Dict[str, str] = {
            'cargar_datos': 'function(store, key) return store:GetAsync(key) end',
            'guardar_datos': 'function(store, key, value) return store:SetAsync(key, value) end',
            'incrementar_datos': 'function(store, key, delta) return store:IncrementAsync(key, delta) end'
        }
        
        # Pre-compilar expresiones regulares
        self._compile_patterns()
    
    def _compile_patterns(self):
        """Pre-compila las expresiones regulares usadas en el transpilador"""
        
        # Patrón para detectar palabras clave completas (con límites de palabra)
        keyword_pattern = r'\b(' + '|'.join(map(re.escape, self.translation_dict.keys())) + r')\b'
        self.keyword_regex = re.compile(keyword_pattern, re.IGNORECASE)
    
    def translate_keyword(self, match: re.Match) -> str:
        """
        Traduce una palabra clave encontrada
        
        Args:
            match: Match de la expresión regular
            
        Returns:
            Palabra traducida
        """
        keyword = match.group(0)
        translated = self.translation_dict.get(keyword.lower(), keyword)
        
        # Si la traducción empieza con . o :, mantener el contexto
        if translated.startswith(('.', ':')):
            return translated
        else:
            return translated
    
    def transpile_content(self, content: str, filename: str = "") -> str:
        """
        Transpila el contenido de DSL a Lua estándar con análisis semántico real
        
        Args:
            content: Contenido DSL a transpilar
            filename: Nombre del archivo para mensajes de error
            
        Returns:
            Contenido transpilado a Lua
            
        Raises:
            DSLError: Si hay errores en el transpilado
        """
        # Verificar palabras prohibidas primero
        self.check_forbidden_words(content, filename)
        
        # Análisis semántico con múltiples pasadas
        result = self._semantic_transpile(content)
        
        return result
    
    def _semantic_transpile(self, content: str) -> str:
        """
        Realiza transpilación con análisis semántico en múltiples pasadas
        """
        lines = content.split('\n')
        transpiled_lines = []
        
        for line_num, line in enumerate(lines, 1):
            try:
                transpiled_line = self._transpile_line_semantic(line)
                transpiled_lines.append(transpiled_line)
            except Exception as e:
                raise DSLError(f"Error procesando línea {line_num}: {str(e)}")
        
        return '\n'.join(transpiled_lines)
    
    def _transpile_line_semantic(self, line: str) -> str:
        """
        Transpila línea con análisis semántico completo
        """
        if not line.strip():
            return line
        
        # Extraer strings para no procesar su contenido
        parts = self._extract_strings(line)
        result_parts = []
        
        for part in parts:
            if part['type'] == 'string':
                result_parts.append(part['content'])
            else:
                # Procesar código no-string con análisis semántico
                processed = self._process_code_semantic(part['content'])
                result_parts.append(processed)
        
        return ''.join(result_parts)
    
    def _extract_strings(self, line: str) -> List[Dict]:
        """
        Extrae strings y devuelve lista de partes con tipos
        """
        parts = []
        current_pos = 0
        in_string = False
        string_char = None
        string_start = 0
        
        i = 0
        while i < len(line):
            char = line[i]
            
            if not in_string and char in ['"', "'"]:
                in_string = True
                string_char = char
                string_start = i
                i += 1
            elif in_string and char == string_char:
                # Verificar que no esté escapado
                if i == 0 or line[i-1] != '\\':
                    # Agregar parte antes del string
                    if current_pos < string_start:
                        parts.append({
                            'type': 'code',
                            'content': line[current_pos:string_start]
                        })
                    
                    # Agregar el string
                    parts.append({
                        'type': 'string',
                        'content': line[string_start:i+1]
                    })
                    
                    in_string = False
                    string_char = None
                    current_pos = i + 1
                    i += 1
                else:
                    i += 1
            elif in_string:
                i += 1
            else:
                i += 1
        
        # Agregar parte final
        if current_pos < len(line):
            parts.append({
                'type': 'code',
                'content': line[current_pos:]
            })
        
        return parts
    
    def _process_code_semantic(self, code: str) -> str:
        """
        Procesa código con análisis semántico completo
        """
        if not code.strip():
            return code
        
        # 1. PRIMERO: Traducciones de servicios y funciones (más específicas)
        result = self._translate_services(code)
        
        # 2. Traducciones de métodos con : (dos puntos) - MÁS TEMPRANO
        result = self._translate_methods(result)
        
        # 3. Traducciones de constructores (.new)
        result = self._translate_constructors(result)
        
        # 4. Traducciones de propiedades
        result = self._translate_properties(result)
        
        # 5. Traducciones de enums
        result = self._translate_enums(result)
        
        # 6. ÚLTIMO: Traducciones básicas de palabras clave (menos específicas)
        result = self._translate_keywords(result)
        
        return result
    
    def _translate_keywords(self, code: str) -> str:
        """
        Traduce palabras clave básicas y funciones globales
        """
        # Palabras clave que necesitan coincidencia exacta
        keywords = ['funcion', 'fin', 'si', 'entonces', 'sino', 'mientras', 'hacer', 
                   'para', 'en', 'retornar', 'local', 'y', 'o', 'no', 'verdadero', 
                   'falso', 'imprimir', 'esperar', 'tick', 'time', 'tipo', 'pares', 
                   'ipares', 'nulo', 'romper', 'continuar', 'repetir', 'hasta']
        
        # PRIMERO: Manejar sino si -> elseif (caso especial)
        code = re.sub(r'\bsino\b\s+\bsi\b\s+\bentonces\b', 'elseif then', code)
        code = re.sub(r'\bsino\b\s+\bsi\b', 'elseif', code)
        
        # 🔥 CORRECCIÓN CRÍTICA: Funciones globales (tarea_espera → task.wait)
        global_functions = {
            'tarea_espera': 'task.wait',
            'tarea_spawn': 'task.spawn',
            'tarea_delay': 'task.delay',
            'tarea_defer': 'task.defer',
            'tarea_synchronize': 'task.synchronize',
            'tarea_desynchronize': 'task.desynchronize',
            'cargar_datos': 'function(store, key) return store:GetAsync(key) end',
            'guardar_datos': 'function(store, key, value) return store:SetAsync(key, value) end',
            'incrementar_datos': 'function(store, key, delta) return store:IncrementAsync(key, delta) end',
            'info_tween': 'TweenInfo.new',
            'esperar_hijo': 'WaitForChild',
            'encontrar_hijo': 'FindFirstChild',
            'obtener_hijos': 'GetChildren',
            'obtener_descendientes': 'GetDescendants',
            'es_ancestro': 'IsAncestorOf',
            'es_descendiente': 'IsDescendantOf',
            'clonar': 'Clone',
            'destruir': 'Destroy',
            'conectar': 'Connect',
            'desconectar': 'Disconnect',
            'desconectar_todo': 'DisconnectAll',
            'jugar': 'Play',
            'pausar': 'Pause',
            'detener': 'Stop',
            'reanudar': 'Resume',
            'emitir': 'Emit'
        }
        
        # Traducir funciones globales PRIMERO (antes que palabras clave)
        for spanish_func, english_func in global_functions.items():
            pattern = r'\b' + re.escape(spanish_func) + r'\b(?=\s*\()'
            code = re.sub(pattern, english_func, code)
        
        for keyword in keywords:
            if keyword in self.translation_dict:
                # Usar word boundaries para evitar reemplazos parciales
                pattern = r'\b' + re.escape(keyword) + r'\b'
                code = re.sub(pattern, self.translation_dict[keyword], code)
        
        return code
    
    def _translate_methods(self, code: str) -> str:
        """
        Traduce métodos con : (dos puntos) - VERSIÓN CORREGIDA
        """
        # 🔥 CORRECCIÓN CRÍTICA: Métodos con dos puntos
        method_mappings = {
            'clonar': 'Clone',
            'destruir': 'Destroy',
            'conectar': 'Connect',  # 🔥 CORREGIDO: Conectar → Connect
            'desconectar': 'Disconnect',
            'desconectar_todo': 'DisconnectAll',
            'esperar': 'Wait',
            'jugar': 'Play',
            'pausar': 'Pause',
            'detener': 'Stop',
            'reanudar': 'Resume',
            'emitir': 'Emit',
            'encontrar_hijo': 'FindFirstChild',
            'esperar_hijo': 'WaitForChild',
            'obtener_hijos': 'GetChildren',
            'obtener_descendientes': 'GetDescendants',
            'es_ancestro': 'IsAncestorOf',
            'es_descendiente': 'IsDescendantOf'
        }
        
        # 🔥 CORRECCIÓN CRÍTICA: Patrón mejorado para objeto:metodo() -> objeto:Metodo()
        for spanish_method, english_method in method_mappings.items():
            # Patrón que funciona con o sin espacios: objeto:metodo( o objeto: metodo(
            pattern = r':\s*' + re.escape(spanish_method) + r'\s*\('
            replacement = f':{english_method}('
            code = re.sub(pattern, replacement, code)
            
            # 🔥 CORRECCIÓN EXTRA: También manejar eventos .Evento:metodo(
            pattern2 = r'\.\w+:\s*' + re.escape(spanish_method) + r'\s*\('
            replacement2 = f':{english_method}('
            code = re.sub(pattern2, replacement2, code)
        
        return code
    
    def _translate_services(self, code: str) -> str:
        """
        Traduce servicios y llamadas a funciones - VERSIÓN CORREGIDA
        """
        # Mapeo directo de servicios
        service_mapping = {
            'jugadores': 'Players',
            'espacio_trabajo': 'Workspace',
            'luz': 'Lighting',
            'sonido': 'SoundService',
            'replicacion': 'ReplicatedStorage',
            'servidor_script': 'ServerScriptService',
            'servidor_almacen': 'ServerStorage',
            'servicio_almacen_inicio': 'StarterGui',
            'servicio_sonido': 'SoundService',
            'servicio_chat': 'Chat',
            'servicio_datos': 'DataStoreService',
            'servicio_ejecucion': 'RunService',
            'servicio_http': 'HttpService',
            'servicio_localizacion': 'LocalizationService',
            'servicio_prueba': 'TestService',
            'servicio_terminales': 'Teams',
            'servicio_basura': 'Debris',
            'tienda_datos': 'DataStoreService',
            'servicio_tween': 'TweenService',
            'UserInputService': 'UserInputService',
            'ContextActionService': 'ContextActionService'
        }
        
        # 🔥 CORRECCIÓN: Manejar obtener_servicio de forma limpia
        # obtener_servicio("servicio") -> game:GetService("Servicio")
        for spanish, english in service_mapping.items():
            # obtener_servicio("jugadores") -> game:GetService("Players")
            pattern = rf'obtener_servicio\(\s*"{spanish}"\s*\)'
            replacement = f'game:GetService("{english}")'
            code = re.sub(pattern, replacement, code)
        
        # Para obtener_servicio con variables: obtener_servicio(variable)
        code = re.sub(r'\bobtener_servicio\b', 'game:GetService', code)
        
        return code
    
    def _translate_constructors(self, code: str) -> str:
        """
        Traduce constructores .new a la forma correcta con validación de aridad mejorada
        """
        # 🔥 CORRECCIÓN CRÍTICA: Validación de aridad en Color3.new (máximo 3 parámetros)
        # Validar Color3.new con más de 3 parámetros
        color3_invalid_pattern = r'Color3\.new\(([^,]+,\s*[^,]+,\s*[^,]+,\s*[^)]+)\)'
        def validate_color3_arity(match):
            params = match.group(1).strip()
            raise SemanticError(f"Color3.new acepta máximo 3 parámetros (r, g, b), se encontraron 4 parámetros: {params}")
        
        code = re.sub(color3_invalid_pattern, validate_color3_arity, code)
        
        # Validar Color3_nuevo con más de 3 parámetros
        color3_nuevo_invalid_pattern = r'Color3_nuevo\(([^,]+,\s*[^,]+,\s*[^,]+,\s*[^)]+)\)'
        def validate_color3_nuevo_arity(match):
            params = match.group(1).strip()
            raise SemanticError(f"Color3_nuevo acepta máximo 3 parámetros (r, g, b), se encontraron 4 parámetros: {params}")
        
        code = re.sub(color3_nuevo_invalid_pattern, validate_color3_nuevo_arity, code)
        
        # Patrón para Constructor_nuevo(...) -> Constructor.new(...)
        constructor_pattern = r'(\w+)_nuevo\s*\('
        
        def replace_constructor(match):
            constructor_name = match.group(1)
            # Mapeo especial para algunos constructores
            if constructor_name == 'Color3':
                return 'Color3.new('
            elif constructor_name == 'Vector3':
                return 'Vector3.new('
            elif constructor_name == 'UDim2':
                return 'UDim2.new('
            elif constructor_name == 'CFrame':
                return 'CFrame.new('
            elif constructor_name == 'secuencia_color':
                return 'ColorSequence.new('
            elif constructor_name == 'secuencia_numero':
                return 'NumberSequence.new('
            else:
                return f'{constructor_name}.new('
        
        code = re.sub(constructor_pattern, replace_constructor, code)
        
        # instancia_nueva("Tipo") -> Instance.new("Tipo")
        code = re.sub(r'instancia_nueva\s*\(', 'Instance.new(', code)
        
        return code
    
    def _translate_properties(self, code: str) -> str:
        """
        Traduce propiedades de objetos y acceso a miembros
        """
        # Lista extendida de propiedades comunes
        properties = [
            'nombre', 'padre', 'tamano', 'posicion', 'color_fondo', 
            'texto', 'color_texto', 'transparencia_fondo', 'escalado_texto',
            'visible', 'anclado', 'transparencia', 'color', 'material',
            'reflejo', 'humanoide', 'parte_primaria', 'salud', 'salud_maxima',
            'velocidad_caminar', 'poder_salto', 'forma', 'superficie',
            'superficie_inferior', 'frente', 'atras', 'izquierda', 'derecha',
            'puede_colisionar', 'masa', 'densidad', 'friccion', 'elasticidad',
            'borde_pixel', 'radio_esquina', 'recorte', 'seleccionable',
            'orden_z', 'layout', 'alineamiento', 'alineamiento_vertical',
            'alineamiento_horizontal', 'relleno', 'espaciado', 'fuente',
            'tamano_fuente', 'linea_texto', 'ajuste_texto', 'texto_truncado',
            'alineacion_texto', 'alineacion_texto_vertical', 'color_borde',
            'transparencia_borde', 'fondo_transparente', 'rango', 'brillo',
            'angulo', 'atenuacion', 'habilitado', 'volumen', 'tiempo_posicion',
            'duracion', 'pitch', 'loop', 'jugando', 'distancia_maxima',
            'distancia_minima', 'id_sonido', 'id_imagen', 'id_malla', 'id_textura',
            'velocidad', 'velocidad_angular', 'velocidad_maxima', 'velocidad_rotacion',
            'fuerza', 'torque', 'centro_masas', 'tipo_luz', 'sombra',
            'atenuacion_rolloff', 'escala_textura', 'desplazamiento_vertice',
            'offset_malla', 'escala_malla'
        ]
        
        for prop in properties:
            if prop in self.translation_dict:
                # Simple reemplazo: .texto -> .Text
                pattern = r'\.' + re.escape(prop) + r'\b'
                replacement = '.' + self.translation_dict[prop]
                code = re.sub(pattern, replacement, code)
        
        # 🔥 CORRECCIÓN CRÍTICA: Math member access (math.piso → math.floor)
        math_mappings = {
            'piso': 'floor',
            'techo': 'ceil',
            'absoluto': 'abs',
            'maximo': 'max',
            'minimo': 'min',
            'redondear': 'round',
            'potencia': 'pow',
            'raiz': 'sqrt',
            'grados_a_radianes': 'deg',
            'radianes_a_grados': 'rad',
            'aleatorio': 'random',
            'semilla_aleatoria': 'randomseed',
            'ruido_perlin': 'noise',
            'pi': 'pi',
            'infinito': 'huge',
            'exp': 'exp',
            'log': 'log',
            'log10': 'log10',
            'sin': 'sin',
            'cos': 'cos',
            'tan': 'tan',
            'asin': 'asin',
            'acos': 'acos',
            'atan': 'atan',
            'atan2': 'atan2',
            'sinh': 'sinh',
            'cosh': 'cosh',
            'tanh': 'tanh'
        }
        
        for spanish_func, english_func in math_mappings.items():
            # math.piso → math.floor
            pattern = r'math\.' + re.escape(spanish_func) + r'\b'
            replacement = f'math.{english_func}'
            code = re.sub(pattern, replacement, code)
        
        return code
    
    def _translate_enums(self, code: str) -> str:
        """
        Traduce enums y valores especiales con mapeo de namespace
        """
        # 🔥 CORRECCIÓN CRÍTICA: Enums con namespace completo
        enum_mappings = {
            # Material enums
            'material_plastico': 'Enum.Material.Plastic',
            'metal': 'Enum.Material.Metal',
            'madera': 'Enum.Material.Wood',
            'cristal': 'Enum.Material.Glass',
            'neon': 'Enum.Material.Neon',
            
            # EasingStyle enums
            'estilo_suavizado.Linear': 'Enum.EasingStyle.Linear',
            'estilo_suavizado.Sine': 'Enum.EasingStyle.Sine',
            'estilo_suavizado.Back': 'Enum.EasingStyle.Back',
            'estilo_suavizado.Quad': 'Enum.EasingStyle.Quad',
            'estilo_suavizado.Quart': 'Enum.EasingStyle.Quart',
            'estilo_suavizado.Quint': 'Enum.EasingStyle.Quint',
            'estilo_suavizado.Expo': 'Enum.EasingStyle.Expo',
            'estilo_suavizado.Circular': 'Enum.EasingStyle.Circular',
            'estilo_suavizado.Elastic': 'Enum.EasingStyle.Elastic',
            'estilo_suavizado.Bounce': 'Enum.EasingStyle.Bounce',
            
            # EasingDirection enums
            'direccion_suavizado.In': 'Enum.EasingDirection.In',
            'direccion_suavizado.Out': 'Enum.EasingDirection.Out',
            'direccion_suavizado.InOut': 'Enum.EasingDirection.InOut',
            
            # PartType enums
            'tipo_parte.Ball': 'Enum.PartType.Ball',
            'tipo_parte.Block': 'Enum.PartType.Block',
            'tipo_parte.Cylinder': 'Enum.PartType.Cylinder',
            
            # SurfaceType enums
            'superficie_tipo.Smooth': 'Enum.SurfaceType.Smooth',
            'superficie_tipo.Glue': 'Enum.SurfaceType.Glue',
            
            # Font enums
            'fuente.Legacy': 'Enum.Font.Legacy',
            'fuente.SourceSans': 'Enum.Font.SourceSans',
            'fuente.SourceSansBold': 'Enum.Font.SourceSansBold',
            'fuente.SourceSansLight': 'Enum.Font.SourceSansLight',
            'fuente.SourceSansItalic': 'Enum.Font.SourceSansItalic',
            'fuente.SourceSansBoldItalic': 'Enum.Font.SourceSansBoldItalic',
            'fuente.Roboto': 'Enum.Font.Roboto',
            'fuente.RobotoMono': 'Enum.Font.RobotoMono',
            
            # HumanoidStateType enums
            'tipo_estado_humanoide.Running': 'Enum.HumanoidStateType.Running',
            'tipo_estado_humanoide.Jumping': 'Enum.HumanoidStateType.Jumping',
            'tipo_estado_humanoide.Freefall': 'Enum.HumanoidStateType.Freefall',
            'tipo_estado_humanoide.Landed': 'Enum.HumanoidStateType.Landed',
            'tipo_estado_humanoide.Swimming': 'Enum.HumanoidStateType.Swimming',
            'tipo_estado_humanoide.Sitting': 'Enum.HumanoidStateType.Sitting',
            'tipo_estado_humanoide.PlatformStanding': 'Enum.HumanoidStateType.PlatformStanding',
            'tipo_estado_humanoide.Dead': 'Enum.HumanoidStateType.Dead',
            
            # UserInputType enums
            'tipo_entrada.MouseButton1': 'Enum.UserInputType.MouseButton1',
            'tipo_entrada.MouseButton2': 'Enum.UserInputType.MouseButton2',
            'tipo_entrada.MouseButton3': 'Enum.UserInputType.MouseButton3',
            'tipo_entrada.Keyboard': 'Enum.UserInputType.Keyboard',
            'tipo_entrada.Touch': 'Enum.UserInputType.Touch',
            
            # UserInputState enums
            'estado_entrada.Begin': 'Enum.UserInputState.Begin',
            'estado_entrada.Change': 'Enum.UserInputState.Change',
            'estado_entrada.End': 'Enum.UserInputState.End',
            'estado_entrada.Cancel': 'Enum.UserInputState.Cancel'
        }
        
        # Reemplazar enums completos
        for spanish_enum, english_enum in enum_mappings.items():
            pattern = r'\b' + re.escape(spanish_enum) + r'\b'
            code = re.sub(pattern, english_enum, code)
        
        # 🔥 CORRECCIÓN CRÍTICA: Mapeo de enums simples (sin namespace)
        simple_enum_mappings = {
            'Linear': 'Enum.EasingStyle.Linear',
            'Sine': 'Enum.EasingStyle.Sine',
            'Back': 'Enum.EasingStyle.Back',
            'Quad': 'Enum.EasingStyle.Quad',
            'Quart': 'Enum.EasingStyle.Quart',
            'Quint': 'Enum.EasingStyle.Quint',
            'Expo': 'Enum.EasingStyle.Expo',
            'Circular': 'Enum.EasingStyle.Circular',
            'Elastic': 'Enum.EasingStyle.Elastic',
            'Bounce': 'Enum.EasingStyle.Bounce',
            'In': 'Enum.EasingDirection.In',
            'Out': 'Enum.EasingDirection.Out',
            'InOut': 'Enum.EasingDirection.InOut'
        }
        
        # Mapear enums después de punto (estilo_suavizado.Quad → Enum.EasingStyle.Quad)
        for simple_enum, full_enum in simple_enum_mappings.items():
            pattern = r'(?:estilo_suavizado|direccion_suavizado)\.(\b' + re.escape(simple_enum) + r'\b)'
            code = re.sub(pattern, full_enum, code)
        
        # Colores BrickColor (mantener funcionalidad existente)
        color_pattern = r'(\w+)_brillante'
        def replace_color(match):
            color_name = match.group(1)
            return f'BrickColor.new("Bright {color_name}")'
        
        code = re.sub(color_pattern, replace_color, code)
        
        return code
    
    def check_forbidden_words(self, content: str, filename: str = "") -> None:
        """
        Verifica que no haya palabras prohibidas en el contenido
        
        Args:
            content: Contenido a verificar
            filename: Nombre del archivo para mensajes de error
            
        Raises:
            DSLError: Si encuentra palabras prohibidas
        """
        lines = content.split('\n')
        for line_num, line in enumerate(lines, 1):
            for forbidden in self.forbidden_words:
                if forbidden.lower() in line.lower():
                    raise DSLError(
                        f"Palabra prohibida '{forbidden}' encontrada en línea {line_num} de {filename}",
                        ErrorType.FORBIDDEN_WORD
                    )


def main():
    """
    Función principal para ejecutar el transpilador desde línea de comandos
    """
    if len(sys.argv) != 3:
        print("Uso: python transpiler_final.py <archivo_entrada.vox> <archivo_salida.lua>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    try:
        # Verificar que el archivo de entrada exista
        if not os.path.exists(input_file):
            print(f"❌ Error: El archivo '{input_file}' no existe")
            sys.exit(1)
        
        # Crear transpilador y procesar
        transpiler = LuaDSLTranspiler()
        
        # Leer archivo de entrada
        with open(input_file, 'r', encoding='utf-8') as f:
            dsl_content = f.read()
        
        # Transpilar contenido
        lua_content = transpiler.transpile_content(dsl_content, input_file)
        
        # Escribir archivo de salida
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(lua_content)
        
        print(f"Transpilacion exitosa: {input_file} -> {output_file}")
        
    except DSLError as e:
        print(f"Error de DSL: {e}")
        sys.exit(2)
    except Exception as e:
        print(f"Error inesperado: {e}")
        sys.exit(3)


if __name__ == "__main__":
    main()

