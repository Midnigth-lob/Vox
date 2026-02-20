#!/usr/bin/env python3
"""
VALIDADOR COMPLETO AUTOMÁTICO DE VOX LANGUAGE
Verifica que todas las traducciones sean correctas sin test manual
"""

import re
import sys
from typing import Dict, List, Set, Tuple
from transpiler_final import LuaDSLTranspiler

class VoxValidator:
    """Validador automático completo de traducciones Vox"""
    
    def __init__(self):
        self.transpiler = LuaDSLTranspiler()
        self.errors = []
        self.warnings = []
        self.passed_tests = []
        
        # 🔥 TABLA COMPLETA DE BUILTINS ESPERADOS
        self.expected_builtins = {
            # Math functions
            'math.piso': 'math.floor',
            'math.techo': 'math.ceil',
            'math.absoluto': 'math.abs',
            'math.maximo': 'math.max',
            'math.minimo': 'math.min',
            'math.redondear': 'math.round',
            'math.potencia': 'math.pow',
            'math.raiz': 'math.sqrt',
            
            # Task functions
            'tarea_espera': 'task.wait',
            'tarea_spawn': 'task.spawn',
            'tarea_delay': 'task.delay',
            'tarea_defer': 'task.defer',
            
            # Tween functions
            'info_tween': 'TweenInfo.new',
            'servicio_tween': 'TweenService',
            
            # Enums
            'estilo_suavizado.Quad': 'Enum.EasingStyle.Quad',
            'estilo_suavizado.Sine': 'Enum.EasingStyle.Sine',
            'direccion_suavizado.In': 'Enum.EasingDirection.In',
            'direccion_suavizado.Out': 'Enum.EasingDirection.Out',
            
            # Services
            'obtener_servicio': 'game:GetService',
            'esperar_hijo': 'WaitForChild',
            'encontrar_hijo': 'FindFirstChild',
            
            # Properties
            '.texto': '.Text',
            '.color_texto': '.TextColor3',
            '.escalado_texto': '.TextScaled',
            '.nombre': '.Name',
            '.padre': '.Parent',
            '.tamano': '.Size',
            '.posicion': '.Position'
        }
        
        # 🔥 ESTRUCTURAS CRÍTICAS ESPERADAS
        self.expected_structures = {
            'sino si': 'elseif',
            'funcion': 'function',
            'si': 'if',
            'entonces': 'then',
            'fin': 'end',
            'mientras': 'while',
            'hacer': 'do',
            'para': 'for',
            'retornar': 'return',
            'local': 'local',
            'y': 'and',
            'o': 'or',
            'no': 'not',
            'verdadero': 'true',
            'falso': 'false',
            'imprimir': 'print'
        }
        
    def validate_translation(self, vox_code: str, expected_lua: str, test_name: str) -> bool:
        """Valida una traducción específica"""
        try:
            # Transpilar código Vox
            generated_lua = self.transpiler._process_code_semantic(vox_code)
            
            # Limpiar ambos códigos para comparación
            generated_clean = self._clean_code(generated_lua)
            expected_clean = self._clean_code(expected_lua)
            
            if generated_clean == expected_clean:
                self.passed_tests.append(f"✅ {test_name}: Traducción correcta")
                return True
            else:
                self.errors.append(f"❌ {test_name}: Traducción incorrecta")
                self.errors.append(f"   Esperado: {expected_clean}")
                self.errors.append(f"   Generado: {generated_clean}")
                return False
                
        except Exception as e:
            self.errors.append(f"❌ {test_name}: Error en transpilación: {e}")
            return False
    
    def _clean_code(self, code: str) -> str:
        """Limpia código para comparación"""
        # Eliminar espacios extra y saltos de línea
        code = re.sub(r'\s+', ' ', code)
        code = code.strip()
        return code
    
    def run_comprehensive_validation(self) -> bool:
        """Ejecuta validación completa automática"""
        print("🚀 Iniciando Validación Completa Automática de Vox...")
        print("=" * 60)
        
        all_passed = True
        
        # 🔥 TEST 1: MATH FUNCTIONS
        print("📊 Validando Math Functions...")
        math_tests = [
            ('math.piso(4.7)', 'math.floor(4.7)', 'math.piso → math.floor'),
            ('math.techo(4.2)', 'math.ceil(4.2)', 'math.techo → math.ceil'),
            ('math.absoluto(-5)', 'math.abs(-5)', 'math.absoluto → math.abs'),
            ('math.maximo(10, 20)', 'math.max(10, 20)', 'math.maximo → math.max'),
            ('math.minimo(10, 20)', 'math.min(10, 20)', 'math.minimo → math.min')
        ]
        
        for vox, expected, name in math_tests:
            if not self.validate_translation(vox, expected, name):
                all_passed = False
        
        # 🔥 TEST 2: TASK FUNCTIONS
        print("⚡ Validando Task Functions...")
        task_tests = [
            ('tarea_espera(0.1)', 'task.wait(0.1)', 'tarea_espera → task.wait'),
            ('tarea_spawn(function() end)', 'task.spawn(function() end)', 'tarea_spawn → task.spawn'),
            ('tarea_delay(1, function() end)', 'task.delay(1, function() end)', 'tarea_delay → task.delay')
        ]
        
        for vox, expected, name in task_tests:
            if not self.validate_translation(vox, expected, name):
                all_passed = False
        
        # 🔥 TEST 3: TWEEN Y ENUMS
        print("🎨 Validando Tween y Enums...")
        tween_tests = [
            ('info_tween(1, estilo_suavizado.Quad, direccion_suavizado.Out)', 
             'TweenInfo.new(1, Enum.EasingStyle.Quad, Enum.EasingDirection.Out)', 
             'info_tween + enums'),
            ('estilo_suavizado.Quad', 'Enum.EasingStyle.Quad', 'estilo_suavizado.Quad'),
            ('direccion_suavizado.Out', 'Enum.EasingDirection.Out', 'direccion_suavizado.Out')
        ]
        
        for vox, expected, name in tween_tests:
            if not self.validate_translation(vox, expected, name):
                all_passed = False
        
        # 🔥 TEST 4: ESTRUCTURAS DE CONTROL
        print("🔧 Validando Estructuras de Control...")
        control_tests = [
            ('si x > 5 entonces imprimir("alto") fin', 
             'if x > 5 then print("alto") end', 'if-then-end'),
            ('si x > 5 entonces imprimir("alto") sino si x > 3 entonces imprimir("medio") fin',
             'if x > 5 then print("alto") elseif x > 3 then print("medio") end', 'if-elseif-end'),
            ('mientras x < 10 hacer x = x + 1 fin',
             'while x < 10 do x = x + 1 end', 'while-do-end'),
            ('funcion test() retornar 42 fin',
             'function test() return 42 end', 'function-end')
        ]
        
        for vox, expected, name in control_tests:
            if not self.validate_translation(vox, expected, name):
                all_passed = False
        
        # 🔥 TEST 5: SERVICIOS Y PROPIEDADES
        print("🏗️ Validando Servicios y Propiedades...")
        service_tests = [
            ('local jugadores = obtener_servicio("jugadores")',
             'local jugadores = game:GetService("Players")', 'obtener_servicio'),
            ('objeto.texto = "hola"', 'objeto.Text = "hola"', 'propiedad texto'),
            ('objeto.color_texto = Color3.new(1,1,1)', 'objeto.TextColor3 = Color3.new(1,1,1)', 'propiedad color_texto'),
            ('hijo = objeto:esperar_hijo("Part")', 'hijo = objeto:WaitForChild("Part")', 'método esperar_hijo')
        ]
        
        for vox, expected, name in service_tests:
            if not self.validate_translation(vox, expected, name):
                all_passed = False
        
        # 🔥 TEST 6: CONSTRUCTORES
        print("🏭 Validando Constructores...")
        constructor_tests = [
            ('Color3_nuevo(1, 0, 0)', 'Color3.new(1, 0, 0)', 'Color3_nuevo'),
            ('Vector3_nuevo(0, 10, 0)', 'Vector3.new(0, 10, 0)', 'Vector3_nuevo'),
            ('UDim2_nuevo(0, 200, 0, 100)', 'UDim2.new(0, 200, 0, 100)', 'UDim2_nuevo'),
            ('instancia_nueva("Part")', 'Instance.new("Part")', 'instancia_nueva')
        ]
        
        for vox, expected, name in constructor_tests:
            if not self.validate_translation(vox, expected, name):
                all_passed = False
        
        # 🔥 TEST 7: VALIDACIÓN DE ARIDAD
        print("🔢 Validando Aridad...")
        try:
            # Esto debe generar error
            self.transpiler._process_code_semantic('Color3_nuevo(1, 0, 0, 0.5)')
            self.errors.append("❌ Color3_nuevo con 4 parámetros no generó error")
            all_passed = False
        except Exception:
            self.passed_tests.append("✅ Color3_nuevo con 4 parámetros generó error correctamente")
        
        # 📊 RESULTADOS FINALES
        print("\n" + "=" * 60)
        print("📊 RESULTADOS DE VALIDACIÓN COMPLETA")
        print("=" * 60)
        
        for test in self.passed_tests:
            print(test)
        
        if self.errors:
            print("\n❌ ERRORES ENCONTRADOS:")
            for error in self.errors:
                print(error)
        
        if self.warnings:
            print("\n⚠️ ADVERTENCIAS:")
            for warning in self.warnings:
                print(warning)
        
        print(f"\n📈 RESUMEN:")
        print(f"✅ Tests pasados: {len(self.passed_tests)}")
        print(f"❌ Errores: {len(self.errors)}")
        print(f"⚠️ Advertencias: {len(self.warnings)}")
        
        if all_passed:
            print("\n🎉 ¡VALIDACIÓN COMPLETA EXITOSA! Vox Language funciona perfectamente.")
        else:
            print("\n🚨 Se encontraron errores. Revisar la lista above.")
        
        return all_passed

def main():
    """Función principal"""
    validator = VoxValidator()
    success = validator.run_comprehensive_validation()
    
    if success:
        print("\n🏆 Vox Language está listo para producción!")
        sys.exit(0)
    else:
        print("\n🔧 Se necesitan correcciones antes de producción.")
        sys.exit(1)

if __name__ == "__main__":
    main()
