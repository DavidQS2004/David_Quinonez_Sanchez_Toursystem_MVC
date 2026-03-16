import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.geometry('800x400')
root.title("DESTINO SOÑADO S.A.")

# Crear el widget Notebook (pestañas)
notebook = ttk.Notebook(root)

# Crear los frames que irán dentro de las pestañas
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
tab4 = ttk.Frame(notebook)

# Añadir las pestañas al Notebook
notebook.add(tab1, text="Destino Soñado S.A.")
notebook.add(tab2, text="Paquetes Turisticos")
notebook.add(tab3, text="Gestion Guias")
notebook.add(tab4, text="Gestion Clientes")

# Empaquetar el Notebook para que se muestre en la ventana
notebook.pack(expand=True, fill="both")

# CONTENIDO DE LA PESTAÑA 1 (DESTINOS SOÑADOS S.A.)
# Título
titulo = tk.Label(tab1,
                  text="DESTINOS SOÑADOS S.A.",
                  font=("Arial", 16, "bold"),
                  fg="blue")
titulo.pack(pady=20)

# Frame para contener el formulario
form_frame = tk.Frame(tab1)
form_frame.pack(pady=20, anchor="w", padx=50)

# Fila 1: DestinyID
tk.Label(form_frame, text="IDDestino:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
DestinyID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
DestinyID.grid(row=1, column=1, sticky="w", pady=10)

# Fila 2: DestinyName
tk.Label(form_frame, text="Nombre del destino:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
DestinyName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
DestinyName.grid(row=2, column=1, sticky="w", pady=10)

# Fila 3: DestinyCountry
tk.Label(form_frame, text="País del destino:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
DestinyCountry = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
DestinyCountry.grid(row=3, column=1, sticky="w", pady=10)

# Fila 4: DestinyRegion
tk.Label(form_frame, text="Región del destino:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
DestinyRegion = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
DestinyRegion.grid(row=4, column=1, sticky="w", pady=10)

# Fila 5: DestinyGeographyCoordinates
tk.Label(form_frame, text="Coordinadas geográficas:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
DestinyGeographyCoordinates = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
DestinyGeographyCoordinates.grid(row=5, column=1, sticky="w", pady=10)

# Fila 6: DestinyType
tk.Label(form_frame, text="Tipo de destino:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
DestinyType = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
DestinyType.grid(row=6, column=1, sticky="w", pady=10)

#Fila 7: DestinyDescription
tk.Label(form_frame, text="Descripcion detallada:", font=("Arial", 12)).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
DestinyDescription = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
DestinyDescription.grid(row=7, column=1, sticky="w", pady=10)

#Fila 8: DestinyRecommended
tk.Label(form_frame, text="Temporadas recomendadas:", font=("Arial", 12)).grid(row=8, column=0, sticky="w", padx=(0, 10), pady=10)
DestinyRecommended = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
DestinyRecommended.grid(row=8, column=1, sticky="w", pady=10)

#Fila 9: DestinyPopularity
tk.Label(form_frame, text="Nivel de popularidad:", font=("Arial", 12)).grid(row=9, column=0, sticky="w", padx=(0, 10), pady=10)
DestinyPopularity = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
DestinyPopularity.grid(row=9, column=1, sticky="w", pady=10)

#Fila 10: DestinyRestrictions
tk.Label(form_frame, text="Restricciones conocidas:", font=("Arial", 12)).grid(row=10, column=0, sticky="w", padx=(0, 10), pady=10)
DestinyRestrictions = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
DestinyRestrictions.grid(row=10, column=1, sticky="w", pady=10)

#Fila 11: DestinyPhotography
tk.Label(form_frame, text="Fotografías del destino:", font=("Arial", 12)).grid(row=11, column=0, sticky="w", padx=(0, 10), pady=10)
DestinyPhotography = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
DestinyPhotography.grid(row=11, column=1, sticky="w", pady=10)


# Frame para botones
button_frame = tk.Frame(tab1)
button_frame.pack(pady=20)

# Botones de acción
btn_save = tk.Button(button_frame, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10)
btn_save.pack(side=tk.LEFT, padx=5)

btn_update = tk.Button(button_frame, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10)
btn_update.pack(side=tk.LEFT, padx=5)

btn_delete = tk.Button(button_frame, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10)
btn_delete.pack(side=tk.LEFT, padx=5)

btn_clear = tk.Button(button_frame, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10)
btn_clear.pack(side=tk.LEFT, padx=5)

# CONTENIDO DE LA PESTAÑA 2 (PAQUETES TURISTICOS)
titulo2 = tk.Label(tab2, text="PAQUETES TURÍSTICOS", font=("Arial", 16, "bold"), fg="green")
titulo2.pack(pady=20)

form_frame = tk.Frame(tab2)
form_frame.pack(pady=20, anchor="w", padx=50)

# Fila 1: PackageID
tk.Label(form_frame, text="IDPaquete:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
PackageID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
PackageID.grid(row=1, column=1, sticky="w", pady=10)

# Fila 2: PackageName
tk.Label(form_frame, text="Nombre comercial:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
PackageName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
PackageName.grid(row=2, column=1, sticky="w", pady=10)

# Fila 3: PackageDestiny
tk.Label(form_frame, text="Destinos incluidos:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
PackageDestiny = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
PackageDestiny.grid(row=3, column=1, sticky="w", pady=10)

# Fila 4: PackageDuration
tk.Label(form_frame, text="Duración Dias/Noches:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
PackageDuration = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
PackageDuration.grid(row=4, column=1, sticky="w", pady=10)

# Fila 5: PackageTransport
tk.Label(form_frame, text="Transporte:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
PackageTransport = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
PackageTransport.grid(row=5, column=1, sticky="w", pady=10)

# Fila 6: PackageAccommodation
tk.Label(form_frame, text="Categoria de alojamiento:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
PackageAccommodation = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
PackageAccommodation.grid(row=6, column=1, sticky="w", pady=10)

# Fila 7: PackageDiet
tk.Label(form_frame, text="Regimen alimenticio:", font=("Arial", 12)).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
PackageDiet = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
PackageDiet.grid(row=7, column=1, sticky="w", pady=10)

# Fila 8: PackageActivityIncluded
tk.Label(form_frame, text="Actividades incluidas:", font=("Arial", 12)).grid(row=8, column=0, sticky="w", padx=(0, 10), pady=10)
PackageActivityIncluded= tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
PackageActivityIncluded.grid(row=8, column=1, sticky="w", pady=10)

# Fila 9: PackageActivityOptional
tk.Label(form_frame, text="Actividades opcionales:", font=("Arial", 12)).grid(row=9, column=0, sticky="w", padx=(0, 10), pady=10)
PackageActivityOptional = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
PackageActivityOptional.grid(row=9, column=1, sticky="w", pady=10)

# Fila 10: PackagePrice
tk.Label(form_frame, text="Precio base:", font=("Arial", 12)).grid(row=10, column=0, sticky="w", padx=(0, 10), pady=10)
PackagePrice = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
PackagePrice.grid(row=10, column=1, sticky="w", pady=10)

# Fila 11: PackageSeasons
tk.Label(form_frame, text="Temporadas disponibles:", font=("Arial", 12)).grid(row=11, column=0, sticky="w", padx=(0, 10), pady=10)
PackageSeasons = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
PackageSeasons.grid(row=11, column=1, sticky="w", pady=10)

# Fila 12: PackageParticipants
tk.Label(form_frame, text="Minimo de participantes:", font=("Arial", 12)).grid(row=12, column=0, sticky="w", padx=(0, 10), pady=10)
PackageParticipants = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
PackageParticipants.grid(row=12, column=1, sticky="w", pady=10)

# Fila 13: PackageDifficulty
tk.Label(form_frame, text="Nivel de dificultad:", font=("Arial", 12)).grid(row=13, column=0, sticky="w", padx=(0, 10), pady=10)
PackageDifficulty = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
PackageDifficulty.grid(row=13, column=1, sticky="w", pady=10)

# Frame para botones
button_frame = tk.Frame(tab2)
button_frame.pack(pady=20)

# Botones de acción
btn_save = tk.Button(button_frame, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10)
btn_save.pack(side=tk.LEFT, padx=5)

btn_update = tk.Button(button_frame, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10)
btn_update.pack(side=tk.LEFT, padx=5)

btn_delete = tk.Button(button_frame, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10)
btn_delete.pack(side=tk.LEFT, padx=5)

btn_clear = tk.Button(button_frame, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10)
btn_clear.pack(side=tk.LEFT, padx=5)

# PESTAÑA 3 (GESTION GUIAS)
titulo3 = tk.Label(tab3, text="GESTION DE GUIAS TURISTICOS", font=("Arial", 16, "bold"), fg="red")
titulo3.pack(pady=20)

form_frame = tk.Frame(tab3)
form_frame.pack(pady=20, anchor="w", padx=50)

# FILA 1 :EMPLOYEE ID
tk.Label(form_frame, text="IDEmployee:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
EmployeeID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
EmployeeID.grid(row=1, column=1, sticky="w", pady=10)

# FILA 2: EmployeeName
tk.Label(form_frame, text="Nombres:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
EmployeeName= tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
EmployeeName.grid(row=2, column=1, sticky="w", pady=10)

#FILA 3: EmployeeSecondName
tk.Label(form_frame,text="Apellidos :", font=("Arial",12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
EmployeeSecondName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
EmployeeSecondName.grid(row=3, column=1, sticky="w", pady=10)

#FILA 4: EmployeeDocument
tk.Label(form_frame, text="Documento:", font=("Arial",12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
EmployeeDocument = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
EmployeeDocument.grid(row=4, column=1, sticky="w", pady=10)

#FILA 5: EmployeeNationality
tk.Label(form_frame, text="Nacionalidad:", font=("Arial", 12)).grid(row=5, column=0, sticky="w",padx=(0, 10), pady=10)
EmployeeNationtality=tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
EmployeeNationtality.grid(row=5, column=1, sticky="w", pady=10)

#FILA 6: EmployeeLanguages:
tk.Label(form_frame, text="Idiomas que habla:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
EmployeeLanguages=tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
EmployeeLanguages.grid(row=6, column=1, sticky="w", pady=10)

#FILA 7: EmployeeSpecialities
tk.Label(form_frame, text="Especialidades:", font=("Arial", 12)).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
EmployeeSpecialities=tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
EmployeeSpecialities.grid(row=7, column=1, sticky="w", pady=10)

#FILA 8: EmployeeDestiny
tk.Label(form_frame, text="Destinos que conoce:", font=("Arial", 12)).grid(row=8, column=0, sticky="w", padx=(0, 10), pady=10)
EmployeeDestiny=tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
EmployeeDestiny.grid(row=8, column=1, sticky="w", pady=10)

#FILA 9: EmployeeCertification
tk.Label(form_frame, text="Certificaciones", font=("Arial", 12)).grid(row=9, column=0, sticky="w", padx=(0, 10), pady=10)
EmployeeCertification=tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
EmployeeCertification.grid(row=9, column=1, sticky="w", pady=10)

#FILA 10: EmployeePerformance
tk.Label(form_frame, text="Evaluacion de desempeño:", font=("Arial", 12)).grid(row=10, column=0, sticky="w", padx=(0, 10), pady=10)
EmployeePerformance=tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
EmployeePerformance.grid(row=10, column=1, sticky="w", pady=10)

#FILA 11: EmployeeDisponibility
tk.Label(form_frame, text="Disponibilidad:", font=("Arial", 12)).grid(row=11, column=0, sticky="w", padx=(0, 10), pady=10)
EmployeeDisponibility=tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
EmployeeDisponibility.grid(row=11, column=1, sticky="w", pady=10)

# Frame para botones
button_frame = tk.Frame(tab3)
button_frame.pack(pady=20)

# Botones de acción
btn_save = tk.Button(button_frame, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10)
btn_save.pack(side=tk.LEFT, padx=5)

btn_update = tk.Button(button_frame, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10)
btn_update.pack(side=tk.LEFT, padx=5)

btn_delete = tk.Button(button_frame, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10)
btn_delete.pack(side=tk.LEFT, padx=5)

btn_clear = tk.Button(button_frame, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10)
btn_clear.pack(side=tk.LEFT, padx=5)


# CONTENIDO DE LA PESTAÑA 4 (GESTION CLIENTES)
# Título
titulo = tk.Label(tab4,
                  text="GESTION DE CLIENTES",
                  font=("Arial", 16, "bold"),
                  fg="grey")
titulo.pack(pady=20)

# Frame para contener el formulario
form_frame = tk.Frame(tab4)
form_frame.pack(pady=20, anchor="w", padx=50)

# Fila 1: ClientID
tk.Label(form_frame, text="IDCliente:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
ClientID= tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
ClientID.grid(row=1, column=1, sticky="w", pady=10)

# Fila 2: ClientType
tk.Label(form_frame, text="Tipo de cliente:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
ClientType= tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
ClientType.grid(row=2, column=1, sticky="w", pady=10)

# Fila 3: ClientName
tk.Label(form_frame, text="Nombres - Razon social:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
ClientName= tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
ClientName.grid(row=3, column=1, sticky="w", pady=10)

# Fila 4: ClientDocument
tk.Label(form_frame, text="Documento:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
ClientDocument= tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
ClientDocument.grid(row=4, column=1, sticky="w", pady=10)

# Fila 5: ClientNation
tk.Label(form_frame, text="Nacionalidad:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
ClientNation= tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
ClientNation.grid(row=5, column=1, sticky="w", pady=10)

# Fila 6: ClientAddress
tk.Label(form_frame, text="Direccion:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
ClientAddress= tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
ClientAddress.grid(row=6, column=1, sticky="w", pady=10)

# Fila 7: ClientTelephone
tk.Label(form_frame, text="Telefono:", font=("Arial", 12)).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
ClientTelephone= tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
ClientTelephone.grid(row=7, column=1, sticky="w", pady=10)

# Fila 8: ClientMail
tk.Label(form_frame, text="Correo electronico:", font=("Arial", 12)).grid(row=8, column=0, sticky="w", padx=(0, 10), pady=10)
ClientMail= tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
ClientMail.grid(row=8, column=1, sticky="w", pady=10)

# Fila 9: ClientPreferences
tk.Label(form_frame, text="Preferencias de viaje:", font=("Arial", 12)).grid(row=9, column=0, sticky="w", padx=(0, 10), pady=10)
ClientPreferences= tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
ClientPreferences.grid(row=9, column=1, sticky="w", pady=10)

# Fila 10: ClientHistory
tk.Label(form_frame, text="Historial de compras:", font=("Arial", 12)).grid(row=10, column=0, sticky="w", padx=(0, 10), pady=10)
ClientHistory= tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
ClientHistory.grid(row=10, column=1, sticky="w", pady=10)

# Fila 11: ClientProgram
tk.Label(form_frame, text="Programa de fidelizacion:", font=("Arial", 12)).grid(row=11, column=0, sticky="w", padx=(0, 10), pady=10)
ClientProgram= tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
ClientProgram.grid(row=11, column=1, sticky="w", pady=10)

# Frame para botones
button_frame = tk.Frame(tab4)
button_frame.pack(pady=20)

# Botones de acción
btn_save = tk.Button(button_frame, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10)
btn_save.pack(side=tk.LEFT, padx=5)

btn_update = tk.Button(button_frame, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10)
btn_update.pack(side=tk.LEFT, padx=5)

btn_delete = tk.Button(button_frame, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10)
btn_delete.pack(side=tk.LEFT, padx=5)

btn_clear = tk.Button(button_frame, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10)
btn_clear.pack(side=tk.LEFT, padx=5)


root.mainloop()