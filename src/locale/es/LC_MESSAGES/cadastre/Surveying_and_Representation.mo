��          �               �  �   �  �   �  �   *  t   �  j   h     �  T   �  U   7  T   �  S   �  �   6  �   �  }   B     �     �     �  
   �  +   �  7   "  7   Z  �   �  �   	  n   �	     
     $
     A
  �   G
  �  �
  �   R  �     �   �  �   �  �   8     �  h   �  X   =  [   �  ^   �  �   Q  �   �  �   h     �                 0   *  7   [  7   �  �   �  �   l  �        �     �  
   �  �   �   **Boundary Point** is a specialized class of *LA_Point* which stores points that define a boundary. Boundary is an instance of *LA_BoundaryFaceString* class and its specializations. **Boundary** is a specialization of the *LA_CadenaCarasLindero* class to store boundaries that define plots. Two boundaries must not cross or overlap. **Control Point** is a specialized class of *LA_Point* which represents points belonging to the local network, used in cadastre operation for surveying physical information of the territorial objects. **Survey Point** is a specialized class of *LA_Point* which represents a building, right of way or auxiliary vertex. Add a Comma Separated Values file (CSV), choosing the delimiter and fields that contain point coordinates. Boundary Point Choose this option if you want to create a **Boundary** using QGIS digitizing tools. Choose this option to load points to **Boundary Points** layer from *LADM_COL* model. Choose this option to load points to **Control Points** layer from *LADM_COL* model. Choose this option to load points to **Survey Points** layer from *LADM_COL* model. Choose this option to open a window that allows you to import data from a source layer into the *LADM_COL* **puntolevantamiento** layer. Choose this option to open a window that allows you to import data from a source layer into the *LADM_COL* **puntolindero** layer. Choose this option to open a window that allows you to import data from a source table into the *LADM_COL* **lindero** table. Control Point Create Boundary Create Point Digitizing From a CSV file with the required structure From another QGIS Layer/table (setting a field mapping) From another QGIS layer/table (setting a field mapping) If the field structure of input and target layers differs, you can set a field mapping to define field transformations and correspondence. If the field structure of input and target tables differs, you can set a field mapping to define field transformations and correspondence. If you need to merge or explodes boundaries you can use the *merge* and *explode* buttons on Toolbar LADM_COL. Survey Point Surveying and Representation TODO! You can fill point bfs topology table using the button *Fill Point BFS* on Toolbar LADM_COL which makes automatic and faster this job. Project-Id-Version: LADM_COL Assistant
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2018-07-27 12:31-0500
PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE
Last-Translator: FULL NAME <EMAIL@ADDRESS>
Language: es
Language-Team: es <LL@li.org>
Plural-Forms: nplurals=2; plural=(n != 1)
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
Generated-By: Babel 2.6.0
 **Punto Lindero** es una clase especializada de *LA_Punto* que almacena puntos que definen un lindero. Lindero es una instancia de la clase *LA_BoundaryFaceString* y sus especializaciones. **Lindero** es una clase especializada de *LA_CadenaCarasLindero* que permite registrar los linderos. Dos linderos no pueden cruzarse ni superponerse. **Punto de Control** es una clase especializada de *LA_Punto* que representa puntos de la densificación de la red local, que se utiliza en la operación catastral para el levantamiento de información fisica de los objetos territoriales. **Punto Levantamiento** es una clase especializada de *LA_Punto* que representa la posición horizontal de un vértice de construcción, servidumbre o auxiliares. Agrega un archivo de valores separados por coma (CSV), seleccionando el delimitador y los campos que contienen las coordenadas de los puntos. Punto lindero Elige esta opción si deseas agregar un **Lindero** usando las herramientas de digitalización de QGIS.  Elige esta opción para cargar puntos a la capa **Punto Lindero** del modelo *LADM_COL*. Elige esta opción para cargar puntos a la capa **Punto de Control** del modelo *LADM_COL*. Elige esta opción para cargar puntos a la capa **Punto Levantamiento** del modelo *LADM_COL*. Elige esta opción para abrir una ventana que te permite importar datos desde una tabla fuente hacia la tabla **lindero** de *LADM_COL*. Elige esta opción para abrir una ventana que te permite importar datos desde una tabla fuente hacia la tabla **puntolindero** de *LADM_COL*. Elige esta opción para abrir una ventana que te permite importar datos desde una tabla fuente hacia la tabla **lindero** de *LADM_COL*. Punto de Control Crear Lindero Crear Punto Digitalizando Desde un archivo CSV con la estructura requerida Desde otra capa de QGIS (definiendo un mapeo de campos) Desde otra capa de QGIS (definiendo un mapeo de campos) Si la estructura de campos de las tablas de entrada y salida difiere, puedes definir un mapeo para transformar campos y establecer correspondencias entre ellos. Si la estructura de campos de las tablas de entrada y salida difiere, puedes definir un mapeo para transformar campos y establecer correspondencias entre ellos. Si necesitas unir o partir por segmentos los linderos, puedes utilizar los botones *Unir* y *Partir por segmento* en la barra de herramientas de LADM-COL. Punto Levantamiento Topografía y Representación POR HACER! Puedes llenar la tabla de topología PuntoCCL usando el botón *Llenar PuntosCCL* en barra de herramientas de LADM_COL que hace más rápido y de forma automática este trabajo. 