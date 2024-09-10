from django.db import models

# Tabla TBL_GENERO
class Genero(models.Model):
    tipo = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'TBL_GENERO'

# Tabla TBL_PERSONAS
class Persona(models.Model):
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=150, null=True)
    apellido = models.CharField(max_length=150, null=True)
    fecha_nacimiento = models.DateField(null=True)

    class Meta:
        db_table = 'TBL_PERSONAS'

# Tabla TBL_USUARIOS
class Usuario(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    user = models.CharField(max_length=75, unique=True)
    correo = models.EmailField(max_length=100, unique=True)
    contrasena = models.CharField(max_length=100)
    fecha_registro = models.DateField()

    class Meta:
        db_table = 'TBL_USUARIOS'

# Tabla TBL_DIRECTORES
class Director(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, primary_key=True)
    peliculas_dirigidas = models.IntegerField(null=True)

    class Meta:
        db_table = 'TBL_DIRECTORES'

# Tabla TBL_ACTORES
class Actor(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, primary_key=True)
    peliculas_actuadas = models.IntegerField(null=True)

    class Meta:
        db_table = 'TBL_ACTORES'

# Tabla TBL_PELICULAS
class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    anio_estreno = models.CharField(max_length=4, null=True)  # Ajuste en la longitud para un año de 4 dígitos
    duracion = models.CharField(max_length=45)
    clasificacion = models.CharField(max_length=45, null=True)
    trama = models.TextField(null=True)  # Usar TextField para descripciones largas

    class Meta:
        db_table = 'TBL_PELICULAS'

# Tabla TBL_GENERO_PELICULA
class GeneroPelicula(models.Model):
    tipo = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'TBL_GENERO_PELICULA'

# Tabla TBL_GENERO_X_PELICULA (Relacion Muchos a Muchos)
class PeliculaGenero(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    genero_pelicula = models.ForeignKey(GeneroPelicula, on_delete=models.CASCADE)

    class Meta:
        db_table = 'TBL_GENERO_X_PELICULA'
        unique_together = ('pelicula', 'genero_pelicula')

# Tabla TBL_PELICULAS_HAS_DIRECTORES (Relacion Muchos a Muchos)
class DirectorPelicula(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    class Meta:
        db_table = 'TBL_PELICULAS_HAS_DIRECTORES'
        unique_together = ('pelicula', 'director')

# Tabla TBL_PELICULAS_HAS_ACTORES (Relacion Muchos a Muchos)
class ActorPelicula(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)

    class Meta:
        db_table = 'TBL_PELICULAS_HAS_ACTORES'
        unique_together = ('pelicula', 'actor')

# Tabla TBL_COMENTARIOS
class Comentario(models.Model):
    descripcion = models.TextField(null=True)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_creado = models.DateField()

    class Meta:
        db_table = 'TBL_COMENTARIOS'

# Tabla TBL_RESENIAS
class Resenia(models.Model):
    calificacion = models.IntegerField()
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        db_table = 'TBL_RESENIAS'
        unique_together = ('pelicula', 'usuario')

# Tabla TBL_FAVORITOS
class Favorito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)

    class Meta:
        db_table = 'TBL_FAVORITOS'
        unique_together = ('usuario', 'pelicula')

# Tabla TBL_VISTAS
class Vista(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)

    class Meta:
        db_table = 'TBL_VISTAS'
        unique_together = ('usuario', 'pelicula')

# Tabla TBL_SEGUIDO (Relacion Muchos a Muchos)
class Seguido(models.Model):
    usuario_seguidor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='seguidores')
    usuario_seguido = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='seguidos')

    class Meta:
        db_table = 'TBL_SEGUIDO'
        unique_together = ('usuario_seguidor', 'usuario_seguido')

# Tabla TBL_DESEADAS
class Deseada(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)

    class Meta:
        db_table = 'TBL_DESEADAS'
        unique_together = ('usuario', 'pelicula')
