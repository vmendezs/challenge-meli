📂 ¡Bienvenidos Challenge Datapipeline! 📂

Aquí, en esta sección de mi repositorio, encontrarás:

🐍 Codigo con la solución: Codigo python "build_dataset.py" con la solución del reto.

🗂️ Resultado de la solución: Dentro de "dataset.csv", se encuentran los items obtenidos de la api correspondiente.

📜 Cabe aclarar unos puntos sobre la solución:
1. El resultado de la solución no cumple con la cantidad requerida de registros (+/- 5mil) dadas las condiciones de la API.
2. Del punto anterior, se debe aclarar que el límite de la paginación es de 50 items por cada página y el valor máximo del offset es 1000; por tal razón, la cantidad máxima de items que puede obtener el datapipeline es de 1000 items aproximadamente. Esto sucede porque el offset debe ser fijado en saltos que le permitan no repetir items por paginación, de forma que, el offset salta 50 items por iteración y al tener un máximo valor 1000, no se puede obtener más información.
3. A pesar de estas limitaciones, el código esta diseñado para que funcione con los mismos campos pero limitaciones diferentes. En ese sentido, si la configuración de la api cambiara y el límite por paginación fuera más alto, el valor máximo del offset fuera más alto o incluyendo otro tipo de variables como "next_page" dentro de la api, se podría evaluar una nueva forma de alcanzar la cantidad de datos requerida.
