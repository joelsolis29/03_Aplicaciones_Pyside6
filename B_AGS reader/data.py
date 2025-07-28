import csv
import pandas as pd

class AGS:
    lines = []
    file_path = None

    def _read_lines(self):
        with open(self.file_path, encoding="utf-8") as f:
            reader = csv.reader(f)
            self.lines = [row for row in reader if row]

    def read_group(self, group_name,df_to_return="all"):
        self._read_lines()
        unit, dtype, data = [], [], []
        in_group = False
        headings = []  # Para almacenar los encabezados

        for line in self.lines:
            # Si la línea está vacía, se omite
            if not line:
                continue

            parts = [p.strip().strip('"') for p in line]

            # Verificamos que haya al menos dos elementos en la línea
            if len(parts) < 2:
                continue

            if parts[0] == "GROUP" and parts[1] == group_name:
                in_group = True
                continue
            elif parts[0] == "GROUP" and in_group:  # hemos salido del grupo
                break

            if parts[0] == "HEADING":  # Encontramos la línea HEADING
                headings = parts[1:]  # Usamos los elementos después de "HEADING" como encabezados
            elif in_group:
                if parts[0] == "UNIT":
                    unit = parts[1:]
                elif parts[0] == "TYPE":
                    dtype = parts[1:]
                elif parts[0] == "DATA":
                    data.append(parts[1:])
                else:  # Si no se pasa un valor válido, devolvemos todos
                    return df_unit, df_type, df_data
                
        # Si no encontramos datos o tipos, lanzamos un error
        if not dtype or not data:
            raise ValueError(f"Grupo '{group_name}' no encontrado o incompleto.")
        
        if not headings:
            raise ValueError(f"No se encontró la línea 'HEADING' en el archivo.")

        # Usamos el encabezado de 'HEADING' para los 3 DataFrames
        df_unit = pd.DataFrame([unit], columns=headings)
        df_type = pd.DataFrame([dtype], columns=headings)
        df_data = pd.DataFrame(data, columns=headings)

        # Devolver solo el DataFrame solicitado
        if df_to_return == "unit":
            return df_unit
        elif df_to_return == "type":
            return df_type
        elif df_to_return == "data":
            return df_data
        
    def get_group(self):
        self._read_lines()
        groups = []

        for line in self.lines:
            parts = [p.strip().strip('"') for p in line]
            if len(parts) >= 2 and parts[0] == "GROUP":
                groups.append(parts[1])

        return groups